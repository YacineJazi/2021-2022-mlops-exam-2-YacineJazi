# Exam MLOps Version 2

## Goal

Your goal is to write a custom FastAPI that connects to one of my Kubernetes services.
My service is a StorageService which is already deployed onto Kubernetes. You'll write an ImageScraper that will get an input path from Google and send it over to my Storage Service.

However, there are a few mistakes on the StorageService. Fix them in order to continue. You do not get the source code of the Storage Service. That one is secret, be creative!

Kubernetes contains a namespace `exam-2-segers-nathan` (with your own name ...) into a project called `exam-segers-nathan`. Don't change this.

## Steps
(You can use Check marks to see if you have done everything!)
- [ ] Clone the GitHub Classrooms Repository from this link. Which you already have done once you can read this text.
- [ ] Clone the GitHub repo onto your Virtual Machine, or your own laptop. Think about your Kubernetes deployments at least!
- [ ] Create a new FastAPI, and use this code as an inspiration.
- [ ] Make sure to fix the errors and set up communication to the FastAPI service by using an API_CONNECTION environment variable.
- [ ] Create a Docker image for the FastAPI scraper application. Use your GitHub Container Registry to push this. Give it a tag `mlops-exam-2-scraper:latest`.
- [ ] The FastAPI Storage service is already dockerized under a public Image: `ghcr.io/nathansegers/mlops-exam-2-fastapi:latest`.
- [ ] Notice that the Scraper still needs to communicate to the Storage in order to work. Fix the communication with Docker-compose during your development. The basic Docker-compose is already given.
- [ ] Onto the Rancher project, you work inside the Kubernetes namespace you have gotten.
- [ ] Make sure to deploy your own Scraper Service onto Kubernetes in a new Deployments and Services. Create Kubernetes YAML files for this, which you can then apply with KubeCTL.
- [ ] Setup the communication between the Scraper App and the Storage App in your Kubernetes namespace as well. Remember what to think about.
- [ ] In Kubernetes, you'll provide the necessary parameter input to the FastAPI frontend by using a **ConfigMap**. You do not need to create a Kubernetes YAML file for this, you can do it manually in Rancher.
- [ ] Automate the Docker build and push, and kubectl deployment with a GitHub action. The basic format is already given. Make sure the Action can be triggered manually but also on pushes to the **main** branch.
- [ ] Upload all your written and added files onto your GitHub Classrooms repository.

## Example code

Use this code for your scraper. Adapt where requested, make sure it works with FastAPI.

```python
image = requests.get(imagePath).content
files = {'file': (imagePath.split('/')[-1], image, 'image/jpeg')}

try:
    response = requests.post(f'<missing-api-connection>?type=IMAGE', files=files)
    return Response(response.text, 200)
except Exception as e:
    print(e)
    return Response('Something went wrong. Search the logs for the error.', 500)
```

## Hand IN?

- Create an Empty Word document to hand in the following screenshots:
- Take a screenshot of your working frontend.
- Take a screenshot of your Rancher namespace resources. Services, Deployments ... Everything I need to see.
- Take a screenshot of your finished GitHub Actions.
- In case you couldn't solve some things: Take note of all errors you have encountered and what you tried to do.
- Push all your changes to GitHub
- Create a ZIP file of your GitHub repository
- Upload the WORD document, together with the ZIP file onto Leho

After you have handed in everything on Leho, your access to the Rancher project will be removed, and you can leave the class. Send a message to let me know you've uploaded the document, so I can check it.

