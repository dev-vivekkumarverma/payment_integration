document.getElementById("donate-btn").addEventListener("click", async function () {
    console.log("Donate button clicked!"); // Debugging

    const name = document.getElementById("name").value;
    const amount = document.getElementById("amount").value;
    const email = document.getElementById("email").value;
    const phone = document.getElementById("phone").value;

    if (!name || !amount || !email || !phone) {
        alert("Please fill in all fields.");
        return;
    }

    // Update fetch URL to match Docker networking
    const response = await fetch("http://localhost:8000/create_payment/", {  
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, amount, email, phone }),
    });

    if (!response.ok) {
        alert("Failed to create order. Try again later.");
        return;
    }

    const order = await response.json();
    console.log("Order received:", order); // Debugging

    var options = {
        key: order.key, // Use env value
        amount: order.amount,
        currency: "INR",
        name: "XYZ Org",
        description: "Donation Payment",
        order_id: order.id,
        handler: function (response) {
            alert("Payment successful!");
            window.location.href = "/success"; // Redirect to success page
        },
        prefill: { name, email, contact: phone },
        theme: { color: "#3399cc" },
    };

    console.log("Opening Razorpay Checkout"); // Debugging
    var rzp = new Razorpay(options);
    rzp.open();
});
