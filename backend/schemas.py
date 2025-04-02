from pydantic import BaseModel

class PaymentRequest(BaseModel):
    name: str
    email: str
    phone: str
    amount: float

class PaymentResponse(BaseModel):
    id: int
    name: str
    email: str
    amount: float
    payment_id: str
    status: str