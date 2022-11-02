

# 1. Library imports
import uvicorn
from fastapi import FastAPI,UploadFile,File
import model
import shutil

# 2. Create the app object
app = FastAPI()
# pickle_in = open("model.pkl","rb")
# ocrmodel=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    
    return {'message': 'Hello, World'}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile=File(...)):
    with open("img.jpg","wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    res=model.predict("img.jpg")
    return{"filename":res}
    



    


# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload