from fastapi import FastAPI
from backend.models import Grievance
from backend.agents import (
    classify_department,
    detect_priority,
    assign_sla,
    check_escalation
)

app = FastAPI(title="AI Grievance Resolution System")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/grievances")
def create_grievance(grievance: Grievance):
    department = classify_department(grievance.description)
    priority = detect_priority(grievance.description)
    sla_deadline = assign_sla(priority)
    escalated = check_escalation(sla_deadline)

    return {
        "message": "Grievance received",
        "department": department,
        "priority": priority,
        "sla_deadline": sla_deadline,
        "escalated": escalated,
        "status": "submitted"
    }
