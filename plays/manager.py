import uuid
import dask.dataframe as dd
import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile
import time
from fastapi import UploadFile
import logging

logger = logging.getLogger('data-process-api')


def save_upload_file_tmp(upload_file: UploadFile) -> Path:
    """Function to save the uploaded file on a temp path"""
    try:
        suffix = Path(upload_file.filename).suffix
        with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(upload_file.file, tmp)
            tmp_path = Path(tmp.name)
    finally:
        upload_file.file.close()
    return tmp_path


def process_chunk_csv(file: UploadFile, task_id: uuid, tasks: list):
    """Function to process the csv uploaded using dask.
    Dask is a python library that uses pandas but with parallelism and scalability.
    It utilizes multiple CPU cores by internally chunking dataframe and process in parallel.
    Instead of computing first, Dask create a graph of tasks, allowing to store data larger than the memory.
    The groupby complexity is O(n) since the data is scanned per-row and aggregated in one pass.
    The gap of this function is on the exportation to csv, consuming the most time."""
    try:
        logger.debug(f"Starting task id {task_id}.")
        s_time = time.time()
        tasks[task_id] = "Processing"
        path = save_upload_file_tmp(file)
        ddf = dd.read_csv(path)
        result = ddf.groupby(['Song', 'Date'])['Number of Plays'].sum().compute()
        result.to_csv(f"{task_id}.csv")
        tasks[task_id] = "Finished"
        e_time = time.time()
        logger.debug(f"Task id {task_id} finished in {(e_time - s_time)} seconds.")
    except KeyError:
        tasks[task_id] = "Error"
        logger.error(f"Occurred an error processing task id {task_id}.")
