from fastapi import APIRouter, BackgroundTasks, UploadFile, Response, status, HTTPException
from fastapi.responses import FileResponse, StreamingResponse
from .manager import process_chunk_csv
import uuid

router = APIRouter()
tasks = {}


@router.post("/plays", status_code=202)
async def process_csv_plays(file: UploadFile, background_tasks: BackgroundTasks, response: Response):
    """Endpoint to schedule file to process. Input: CSV file upload. Output: ID of the processing task."""
    if not file.content_type:
        raise HTTPException(status_code=400, detail="Missing upload file.")
    elif file.content_type != 'text/csv':
        raise HTTPException(status_code=415, detail="Invalid type of file.")
    else:
        task_id = uuid.uuid4()
        background_tasks.add_task(process_chunk_csv, file, task_id, tasks)
        return {"task_id": task_id}


@router.get("/plays/{task_id}")
async def get_csv_processed(task_id: uuid.UUID, response: Response):
    """Endpoint to download the file processed. Input: ID of the processing task. Output: The resulting CSV if
    processing is done. """
    if task_id not in tasks.keys():
        raise HTTPException(status_code=404, detail="Task informed not found")
    if tasks[task_id] == "Processing":
        response.status_code = status.HTTP_202_ACCEPTED
        return {"message": "Task is being processed."}
    if tasks[task_id] == "Finished":
        return FileResponse(f"{task_id}.csv")
    if tasks[task_id] == "Error":
        raise HTTPException(status_code=500, detail="An error occurred while processing the file. Please verify if "
                                                    "the csv file is correct.")
