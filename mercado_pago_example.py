import mercadopago

sdk = mercadopago.SDK("SEU_ACCESS_TOKEN_SANDBOX")

preference_data = {
    "items": [
        {
            "title": "Curso de Teste",
            "quantity": 1,
            "unit_price": 10.0
        }
    ]
}

preference = sdk.preference().create(preference_data)
print("Link de pagamento MercadoPago:", preference['response']['init_point'])
