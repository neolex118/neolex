import requests
import time
import random


API_URL = 'http://price-model:8000/api/prediction'  

fuel_types = ['Petrol','Diesel','CNG']
transmission = ['Automatic', 'Manual']
seller = ['Dealer', 'Individual']


for i in range(50):
    car_id = {"car_id":i}
    data = {
        "Car_Name": "ciaz",
        "Year": random.randint(2003,2018),
        "Present_Price": random.uniform(2,10),
        "Driven_kms": random.randint(5000,100000),
        "Fuel_Type": random.choice(fuel_types),
        "Selling_type": random.choice(seller),
        "Transmission": random.choice(transmission),
        "Owner": random.randint(0,3)
                }
    
    try:
        response = requests.post(API_URL, params=car_id, json=data)
        if response.status_code == 200:
            print(response.json())
        else:
            print(f"Ошибка {response.status_code}: {response.text}")
    except requests.RequestException as e:
        print(f"Ошибка запроса: {e}")

    time.sleep(random.randint(1, 5))



