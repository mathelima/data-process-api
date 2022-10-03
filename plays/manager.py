import uuid

import dask.dataframe as dd
import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile

from fastapi import UploadFile


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
    The gap of the function is on the exportation to csv, consuming the most time."""
    try:
        tasks[task_id] = "Processing"
        path = save_upload_file_tmp(file)
        ddf = dd.read_csv(path)
        result = ddf.groupby(['Song', 'Date'])['Number of Plays'].sum().compute()
        result.to_csv(f"{task_id}.csv")
        tasks[task_id] = "Finished"
    except KeyError:
        tasks[task_id] = "Error"
