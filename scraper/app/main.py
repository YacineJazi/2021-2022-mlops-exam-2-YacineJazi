import uvicorn
from fastapi import FastAPI
import requests
import os
app = FastAPI()
API_CONNECTION = os.environ['API_CONNECTION']
#API_CONNECTION = "test"


@app.get("/")
def start():
    return "Welcome to API"


#Extra => try catch with bad data
@app.post("/predict_movies", status_code=200)
def sendInput(imagePath):
    image = requests.get(imagePath).content
    files = {'file': (imagePath.split('/')[-1], image, 'image/jpeg')}

    try:
        response = requests.post(f'{API_CONNECTION}?type=IMAGE', files=files)
        return Response(response.text, 200)
    except Exception as e:
        print(e)
        return Response('Something went wrong. Search the logs for the error.', 500)
    

class Response():
    text:str
    code:int

    def print(self):
        print(self.code+": " +self.text)

# Run the script
if __name__ == "__main__":
    uvicorn.run(app)