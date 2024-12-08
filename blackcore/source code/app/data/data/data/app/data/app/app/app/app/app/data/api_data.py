def fetch_and_store_data():
    url = "https://api.example.com/commodities"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for item in data:
            existing = Commodity.query.filter_by(name=item['name']).first()
            if existing and existing.price != item['price']:
                send_price_alert("user@example.com", item['name'], item['price'])
            
            new_entry = Commodity(
                name=item['name'],
                price=item['price'],
                date=item['date']
            )
            db.session.add(new_entry)
        db.session.commit()
