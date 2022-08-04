from fastapi import FastAPI
import time

app = FastAPI()


async def wait():
    time.sleep(10)
    print("compeleted")
    return


@app.get("/")
async def root():
    await wait()
    return {"message": "Hello World"}
