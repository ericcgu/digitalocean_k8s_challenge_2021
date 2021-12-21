from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_helloworld():
    return {"message": "Hello World"}
