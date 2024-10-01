from fastapi import APIRouter, UploadFile, File, HTTPException
from machine_learning.scripts import data_treatment

router = APIRouter()

@router.post("/upload-pdf/")
async def upload_file(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="File must be a PDF file")
    
    text = data_treatment(file)