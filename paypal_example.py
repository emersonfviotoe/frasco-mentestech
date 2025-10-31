import paypalrestsdk

paypalrestsdk.configure({
    "mode": "sandbox",
    "client_id": "SEU_CLIENT_ID_SANDBOX",
    "client_secret": "SEU_CLIENT_SECRET_SANDBOX"
})

payment = paypalrestsdk.Payment({
    "intent": "sale",
    "payer": {
        "payment_method": "paypal"
    },
    "transactions": [{
        "amount": {
            "total": "10.00",
            "currency": "BRL"
        },
        "description": "Curso de teste"
    }],
    "redirect_urls": {
        "return_url": "http://localhost:5000/paypal/return",
        "cancel_url": "http://localhost:5000/paypal/cancel"
    }
})

if payment.create():
    print("Pagamento criado com sucesso!")
else:
    print(payment.error)
