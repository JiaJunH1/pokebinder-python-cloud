from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
#from cardsearch import returnimages_given_name  # your function 
 # This is for all cards
from search151 import return151images_given_name
 # This if or 151 SPECIFIC
import uvicorn

app = FastAPI()

# Allow access from your iOS app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to your app’s domain
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/search")
def search_cards(q: str = Query(...)):
    #results = returnimages_given_name(q)
     # This is for all cards
    results = return151images_given_name(q)
     # This is for 151 SPECIFIC
    return {"images": results}

if __name__ == "__main__":
    uvicorn.run("server:app", port=8000, reload=True)
