
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles


from models import ContactForm
import os

app = FastAPI()

IMAGE_DIRECTORY = "static/images"


# Define allowed origins
origins = [
    "http://localhost:8080"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["origins"],
    allow_credentials=True,
    allow_methods=["*"],  # List of allowed http methods
    allow_headers=["*"],
)

@app.get("/")
async def read_main():
    return {"message": "Home page"}


@app.get("/my_gallery")
async def read_gallery():
    images = []
    for image_name in os.listdir(IMAGE_DIRECTORY):
        image_path = os.path.join(IMAGE_DIRECTORY, image_name)
        if os.path.isfile(image_path):
            images.append(f"/static/images/{image_name}")

    return JSONResponse(content={"images": images})


@app.get("/about_me")
async def read_gallery():
    return {"message": f"About Me"}


@app.post("/contact_me")
async def submit_contact(contact_form: ContactForm):
    return {"message": f"Contact form submitted by {contact_form.name}"}


app.mount("/static", StaticFiles(directory="static"), name="static")

