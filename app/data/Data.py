import os
USER_DATA = {
    1: {
        "name": "Ania Lin",
        "email": "Ania@outlook.com",
        "phone": "+16479056520",
        "scenePoints": 800,
        "scotiaAccount": "447430028888888"
    }

}

ORDERS = {
    1: {
        "inProgress": {
            "farmId": 1,
            "items": [
                {
                    "itemId": 1,
                    "name": "tomato",
                    "price": 4.5,
                    "unit": "kg"
                },
                {
                    "itemId": 2,
                    "name": "broccoli",
                    "price": 2.99,
                    "unit": "kg"
                },
                {
                    "itemId": 3,
                    "name": "green onions",
                    "price": 1.59,
                    "unit": "each"
                }
            ]
        }
    }
}

FARMS = {
    1: {
        "name": "Living Earth Farm",
        "raing": 4.8,
        "coord": (43.744270, -79.484365),
        "phone": 6475603939
    },
    2: {
        "name": "Black Creek Community Farm",
        "raing": 4.5,
        "coord": (43.774140, -79.521222),
        "phone": 4163936381
    },
    3: {
        "name": "Downey's Farm Market",
        "raing": 4.3,
        "coord": (43.785585, -79.848363),
        "phone": 9058382990
    },
    4: {
        "name": "John's Market",
        "coord": (43.785585, -79.848363),
        "phone": 9058382990
    },
    5: {
        "name": "Muddy Crops Ontario Farm Company",
        "raing": 4.7,
        "coord": (43.785585, -79.848363),
        "phone": 9058382990
    },
}

ITEM = [
    {
        "itemId": 1,
        "name": "tomato",
        "price": 4.5,
        "unit": "kg",
        "image": os.getenv("TOMATO")
    },
    {
        "itemId": 2,
        "name": "broccoli",
        "price": 2.99,
        "unit": "kg",
        "image": os.getenv("BROCCOLI")
    },
    {
        "itemId": 3,
        "name": "green onions",
        "price": 1.59,
        "unit": "each",
        "image": os.getenv("GREEN_ONION")
    },
    {
        "itemId": 4,
        "name": "milk",
        "price": 2.99,
        "unit": "kg",
        "image": os.getenv("MILK")
    },
]
