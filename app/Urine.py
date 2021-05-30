from fastapi import FastAPI, UploadFile, File
import shutil
import model

app = FastAPI()

@app.get("/index")
async def root():
    return {"message": "Hello"}

@app.post("/upload_image/")
async def upload_image(file: UploadFile = File(...)):
    result = ""
    with open("saved_image/"+file.filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        class_name, percent = model.recognizaion(file.filename)
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
