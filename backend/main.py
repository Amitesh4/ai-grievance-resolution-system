from fastapi import FastAPI
from backend.models import Grievance

app = FastAPI(title="AI Grievance Resolution System")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/grievances")
def create_grievance(grievance: Grievance):
    return {
        "message": "Grievance received",
        "data": grievance,
        "status": "submitted"
    }
