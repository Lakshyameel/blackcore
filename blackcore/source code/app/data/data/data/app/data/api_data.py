from apscheduler.schedulers.background import BackgroundScheduler
import requests
from .models import Commodity, db

def fetch_and_store_data():
    url = "https://api.example.com/commodities"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for item in data:
            new_entry = Commodity(
                name=item['name'],
                price=item['price'],
                date=item['date']
            )
            db.session.add(new_entry)
        db.session.commit()

# Scheduler to fetch data every hour
scheduler = BackgroundScheduler()
scheduler.add_job(fetch_and_store_data, 'interval', hours=1)
scheduler.start()
