from fastapi import FastAPI, UploadFile, File

from app.parser import extract_endpoints

app = FastAPI(title="AI API Doc Generator")

@app.get("/")
def home():
    return {"message": "AI API Doc Generator is running"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8")

    endpoints = extract_endpoints(text)

    return {
        "filename": file.filename,
        "endpoints": endpoints
    }