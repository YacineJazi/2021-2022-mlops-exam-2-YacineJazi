from typing import List
from fastapi import FastAPI, HTTPException
from fastapi import FastAPI, File, UploadFile
import Response
import uvicorn
import requests

app = FastAPI()

@app.get("/")
def start():
    return "Welcome to API"


#Extra => try catch with bad data
@app.post("/predict_movies", status_code=200)
def sendInput(imagePath):
    image = requests.get(imagePath).content
    files = {'file': (imagePath.split('/')[-1], image, 'image/jpeg')}

    try:
        response = requests.post(f'<missing-api-connection>?type=IMAGE', files=files)
        return Response(response.text, 200)
    except Exception as e:
        print(e)
        return Response('Something went wrong. Search the logs for the error.', 500)
    

# Run the script
if __name__ == "__main__":
    uvicorn.run(app)