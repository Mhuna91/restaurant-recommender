from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is working"}

@app.post("/recommend")
def recommend():
    return {
        "recommendations": [
            "Restaurant A",
            "Restaurant B",
            "Restaurant C"
        ]
    }
