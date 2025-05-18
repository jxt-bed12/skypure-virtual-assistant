from supabase import create_client
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import os

app = FastAPI()

# Initialize Supabase client
supabase = create_client(
    os.environ.get("SUPABASE_URL"),
    os.environ.get("SUPABASE_KEY")
)

class CustomerCreate(BaseModel):
    name: str
    phone_number: str
    location: str
    language_preference: str

class InteractionCreate(BaseModel):
    customer_id: int
    query_type: str
    notes: Optional[str]

class FeedbackCreate(BaseModel):
    customer_id: int
    rating: int
    comments: Optional[str]

# Business Constants
BUSINESS_INFO = {
    "en": {
        "hours": "Monday to Friday, 7am–5pm",
        "location": "Kasoa Nyanyano Curve",
        "products": {
            "20g": {"price": 50, "currency": "cedis"},
            "50g": {"price": 65, "currency": "cedis"}
        }
    },
    "tw": {
        "hours": "Ɛdwoada kosi Fiada, anɔpa dɔn 7–ewimbra dɔn 5",
        "location": "Kasoa Nyanyano Curve",
        "products": {
            "20g": {"price": 50, "currency": "cedis"},
            "50g": {"price": 65, "currency": "cedis"}
        }
    }
}

@app.post("/customers")
async def create_customer(customer: CustomerCreate):
    try:
        response = supabase.table('customers').insert(customer.dict()).execute()
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/interactions")
async def create_interaction(interaction: InteractionCreate):
    try:
        response = supabase.table('interactions').insert(interaction.dict()).execute()
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/feedback")
async def create_feedback(feedback: FeedbackCreate):
    try:
        response = supabase.table('feedback').insert(feedback.dict()).execute()
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))