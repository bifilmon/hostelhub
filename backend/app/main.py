from fastapi import FastAPI

app = FastAPI(
    title="HostelHub API",
    description="Modern Hostel Management System",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "name": "HostelHub API",
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/bifil")
def human():
    return {
        "status": "Good boy"
    }