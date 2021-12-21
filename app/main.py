from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_helloworld():
    return {"message": "Hello World"}

@app.get("/good_bye")
def get_goodbye():
    return {"message": "Good Bye"}