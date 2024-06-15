from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.membership import MembershipDetails
from models.gallery import Gallery
from models.trainers import Trainers
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/membership")
async def get_cards():
    cards = MembershipDetails.get_all()
    return {"memberships": [card.to_dict() for card in cards]}

@app.get("/gallery")
async def get_images():
    images = Gallery.get_all()
    return {"images": [image.to_dict() for image in images]}

@app.get("/trainers")
async def get_trainers():
    trainers = Trainers.get_all()
    return {"trainers": [trainer.to_dict() for trainer in trainers]}