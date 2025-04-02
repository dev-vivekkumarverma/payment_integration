from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import razorpay
import os
from database import SessionLocal
from models import Payment
from schemas import PaymentRequest
from utils import send_email

router = APIRouter()
client = razorpay.Client(auth=(os.getenv("RAZORPAY_KEY"), os.getenv("RAZORPAY_SECRET")))
print("creds::",os.getenv("RAZORPAY_KEY"), os.getenv("RAZORPAY_SECRET"))
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create_payment/")
def create_payment(payment: PaymentRequest, db: Session = Depends(get_db)):
    try:
        order_data = {
            "amount": int(payment.amount * 100),  # Razorpay expects amount in paisa
            "currency": "INR",
            "payment_capture": "1" # For automatic handling of payment capture by razor pay
        }
        order = client.order.create(order_data)
        new_payment = Payment(
            name=payment.name,
            email=payment.email,
            phone=payment.phone,
            amount=payment.amount,
            payment_id=order['id'],
            status="pending"
        )
        db.add(new_payment)
        db.commit()
        db.refresh(new_payment)
        return {
                "id": order['id'],
                "amount": order["amount"],
                "currency": order["currency"],
                "key": os.getenv("RAZORPAY_KEY"),  # Send key to frontend
            }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/payment_success/")
def payment_success(payment_id: str, db: Session = Depends(get_db)):
    payment = db.query(Payment).filter(Payment.payment_id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    payment.status = "success"
    db.commit()
    email_body = f"""
        <h3>Thank you for helping XYZ Org with Rs. {payment.amount}</h3>
        <p>You are a kind human being. God Bless you.</p>
    """
    send_email(payment.email, "Thank You for Your Donation", email_body)
    return {"message": "Payment successful, thank you!"}



# import os
# from dotenv import load_dotenv
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import razorpay

# # Load environment variables
# load_dotenv()

# # Read Razorpay API keys from environment variables
# RAZORPAY_KEY_ID = os.getenv("RAZORPAY_KEY_ID")
# RAZORPAY_KEY_SECRET = os.getenv("RAZORPAY_KEY_SECRET")

# # Initialize Razorpay client
# client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))

# app = FastAPI()

# class OrderRequest(BaseModel):
#     name: str
#     amount: int
#     email: str
#     phone: str

# @app.post("/create-order")
# async def create_order(order: OrderRequest):
#     try:
#         amount_paise = order.amount * 100  # Convert amount to paise

#         data = {
#             "amount": amount_paise,
#             "currency": "INR",
#             "payment_capture": 1,  # Auto capture payment
#         }
        
#         payment = client.order.create(data)
#         return {
#             "id": payment["id"],
#             "amount": payment["amount"],
#             "currency": payment["currency"],
#             "key": RAZORPAY_KEY_ID,  # Send key to frontend
#         }
    
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))
