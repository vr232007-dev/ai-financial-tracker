from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ExpensePreview(BaseModel):
    amount: float
    category: str


@app.get("/")
def read_root():
    return {"message": "Financial Tracker API is running"}


@app.post("/preview-expense")
def preview_expense(expense: ExpensePreview):
    return {
        "received_amount": expense.amount,
        "received_category": expense.category,
        "note": "This is just a test endpoint — no database yet"
    }