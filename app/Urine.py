from fastapi import FastAPI, UploadFile, File
import shutil
import app.model as m

app = FastAPI()

@app.get("/index")
async def root():
    return {"message": "Hello"}

@app.post("app/upload_image/")
async def upload_image(file: UploadFile = File(...)):
    result = ""
    with open("app/saved_image/"+file.filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        class_name, percent = m.recognizaion(file.filename)
    if class_name == 0:
        result = "White"
        print(class_name)
    elif class_name == 1:
        print(class_name)
        result = "yellow"
    elif class_name == 2:
        print(class_name)
        result = "dark yellow"
    return {"percent": percent,
            "result": result}
