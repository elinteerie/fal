from pathlib import Path
from fastapi import HTTPException, HTTPException, File, UploadFile, FastAPI
from fastapi.responses import FileResponse
import shutil

app = FastAPI()

@app.post('/uploadfile')
async def upload_file(file: UploadFile = File(...)):
    with open(f"uploads/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": file.filename 
    }


@app.get('/downloadfile', response_class=FileResponse)
async def downloadf(filename: str):
    if not Path(f"uploads/{filename}").exists():
        raise HTTPException(status_code=404, detail=f"File {filename} not found"
                            )
    return FileResponse(path=f"uploads/{filename}", filename=filename)