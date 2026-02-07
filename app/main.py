from fastapi import FastAPI

app = FastAPI(title="AI API Doc Generator")

@app.get("/")
def home():
    return {"message": "AI API Doc Generator is running"}
