import mercadopago
import os
from dotenv import load_dotenv
import json
# Agrega credenciales
load_dotenv()
sdk = mercadopago.SDK(os.getenv('PAY_TOKEN'))

# Crea un ítem en la preferencia
preference_data = {
    "items": [
        {
            "title": "Mi producto",
            "quantity": 1,
            "unit_price": 75.76,
        }
    ]
}

preference_response = sdk.preference().create(preference_data)
preference = preference_response["response"]
print(json.dumps(preference, indent=4))