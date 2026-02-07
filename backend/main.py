from fastapi import FastAPI
from backend.models import Grievance
from backend.agents import classify_department

app = FastAPI(title="AI Grievance Resolution System")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/grievances")
def create_grievance(grievance: Grievance):
    department = classify_department(grievance.description)

    return {
        "message": "Grievance received",
        "department": department,
        "status": "submitted"
    }
