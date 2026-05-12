from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import shutil
import os
import uuid

from services.resume_parser import extract_resume_text
from services.jd_parser import parse_job_description
from services.keyword_extractor import extract_keywords
from services.ai_service import tailor_resume
from services.document_generator import create_docx

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
GENERATED_DIR = "generated"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(GENERATED_DIR, exist_ok=True)


@app.get("/")
def root():
    return {"message": "Resume Tailor API Running"}


@app.post("/generate-resume")
async def generate_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(None),
    job_url: str = Form(None)
):

    file_id = str(uuid.uuid4())

    file_path = f"{UPLOAD_DIR}/{file_id}_{resume.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)

    resume_text = extract_resume_text(file_path)

    jd_text = parse_job_description(job_description, job_url)

    keywords = extract_keywords(jd_text)

    tailored_resume = tailor_resume(
        resume_text,
        jd_text,
        keywords
    )

    output_file = f"{GENERATED_DIR}/{file_id}.docx"

    create_docx(tailored_resume, output_file)

    return {
        "message": "Resume generated successfully",
        "download_url": f"/download/{file_id}",
        "keywords": keywords
    }


@app.get("/download/{file_id}")
def download_resume(file_id: str):

    path = f"generated/{file_id}.docx"

    return FileResponse(
        path,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        filename="tailored_resume.docx"
    )