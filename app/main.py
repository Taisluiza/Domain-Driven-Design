from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI(
    title="Track Money",
    description="A simple application to track your finances.",
    version="0.1.0",
)

@app.get("/health")
async def health_check():
    return JSONResponse({"status": "ok"})

def main ():
    print ("Hello from track-money")


if __name__== "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
   