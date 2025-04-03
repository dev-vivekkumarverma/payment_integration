# Payment Integration
---
# FastAPI Razorpay Donation System
---
## 📌 Project Overview
This project is a **donation system** built using **FastAPI, HTML, CSS, JavaScript, and Razorpay** for payment processing. It allows users to donate to an organization and processes the payment via Razorpay.

### Features:
- Collects **Name, Email, Phone Number, and Donation Amount** from users.
- Uses **Razorpay** to handle secure online payments.
- **FastAPI** backend to create orders and verify payments.
- **Dockerized setup** with Nginx as a reverse proxy.

---

## 🏗️ Project Structure
```
fastapi-razorpay-donation/
│── backend/
│   ├── main.py              # FastAPI application (handles payment)
│   ├── database.py          # SQLite3 database setup
│   ├── models.py            # ORM Models
│   ├── schemas.py           # Pydantic models
│   ├── services.py          # Razorpay integration
│   ├── utils.py             # Helper functions
│   ├── .env                 # Environment variables (to be created manually)
│   ├── requirements.txt     # Backend dependencies
│
│── frontend/
│   ├── index.html           # Main donation page
│   ├── donate.js            # Handles form submission and Razorpay checkout
│   ├── styles.css           # Styling
│   ├── nginx.conf           # Nginx configuration
│   ├── Dockerfile           # Dockerfile for frontend
│
│── docker-compose.yml       # Defines services (backend, frontend, nginx)
│── README.md                # Documentation
```

---

## 🛠️ Setup Instructions

### 1️⃣ Prerequisites
- **Docker & Docker Compose** installed
- **Razorpay Account** (for API keys)
- **Git** installed (optional but recommended)

### 2️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/fastapi-razorpay-donation.git
cd fastapi-razorpay-donation
```

### 3️⃣ Create and Configure the `.env` File
Inside the `backend/` directory, create a `.env` file with the following content:
```
DATABASE_URL=sqlite:///data/db.sqlite3
RAZORPAY_KEY=your_razorpay_key_here
RAZORPAY_SECRET=your_razorpay_secret_here
```
🔹 **Replace placeholders** with actual values.

---

## 🚀 Running the Project (Dockerized)
1️⃣ **Build & Run Containers**
```sh
docker-compose up --build
```
2️⃣ **Access the App**
- Open **`http://localhost`** in your browser.
- Click the **Donate** button.
- Complete the Razorpay checkout process.

---

## ⏹️ Stopping the Containers
To stop the running containers, use:
```sh
docker-compose down
```
This will shut down and remove all running containers.

---

## ✅ Expected Behavior
- Clicking **Donate** opens the Razorpay checkout.
- If **payment is successful**, user sees a thank-you message.
- If **payment fails**, an alert is shown prompting retry.

---

## ❓ Troubleshooting
- **If Razorpay modal doesn’t appear:**
  - Check browser console for errors.
  - Verify backend is running (`docker ps` should show `backend` container running).
- **If API requests fail:**
  - Ensure `nginx.conf` correctly proxies `/create-order` to `backend:8000`.

---

## 📧 Support
If you face any issues, feel free to open an issue in the repository.





*This is just for tech demonstration purpose

