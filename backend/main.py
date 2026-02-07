from fastapi import FastAPI

app = FastAPI(title="AI Grievance Resolution System")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/grievances")
def create_grievance(grievance: dict):
    return {
        "message": "Grievance received",
        "data": grievance,
        "status": "submitted"
    }
