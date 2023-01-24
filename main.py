from fastapi import FastAPI, UploadFile, File, Depends
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.security.api_key import APIKey
import auth
import os
from dotenv import load_dotenv
import uvicorn


env = load_dotenv()


app = FastAPI(
    title="File Uploader",
    description="Upload files to the server",
    version="1.0.0",
)

# static files
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.post("/upload")
async def upload_file(file: UploadFile = File(...), 
                      dir: str = None, name_of_file: 
                      str = None,
                      api_key: APIKey = Depends(auth.get_api_key)
                      ):

    dir_files = dir if dir else ""
    file_name = name_of_file if name_of_file else file.filename

    if not os.path.exists(f"static/{dir_files}"):
        os.makedirs(f"static/{dir_files}")

    with open(f"static/{dir_files}/{file_name}", "wb") as buffer:
        while chunk := await file.read(1024):
            buffer.write(chunk)

    return {"link": f"http://193.106.99.147:8083/static/{dir_files}/{file_name}"}


@app.get("/files")
async def get_files(dir: str = None,
                    file: str = None,
                    api_key: APIKey = Depends(auth.get_api_key)):
    dir_files = dir if dir else ""
    # if not exists
    if os.path.exists(f"static/{dir_files}"):
        files = [file for file in os.listdir(f"static/{dir_files}") if os.path.isfile(f"static/{dir_files}/{file}")]
        if file:
            files = [file1 for file1 in files if file.lower() in file1.lower()]
            return {"files": files}
    else:
        return {"error": "Directory not found"}

    return {"files": files}


@app.delete("/files/delete")
async def delete_file(file: str = None, dir: str = None,
                        api_key: APIKey = Depends
                        (auth.get_api_key)):
     
    if os.path.exists(f"static/{dir}/{file}"):
        os.remove(f"static/{dir}/{file}")
        return {"message": "File deleted"}
    
    return {"error": "File not found"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8083)
