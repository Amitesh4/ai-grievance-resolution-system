from fastapi import FastAPI

app = FastAPI(title="AI Grievance Resolution System")


@app.get("/health")
def health_check():
    return {"status": "ok"}
