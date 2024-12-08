def send_price_alert(user_email, commodity_name, new_price):
    msg = Message(
        f"Price Alert: {commodity_name}",
        sender='your-email@example.com',
        recipients=[user_email]
    )
    msg.body = f"The price of {commodity_name} has changed to {new_price}. Check it now!"
    mail.send(msg)
