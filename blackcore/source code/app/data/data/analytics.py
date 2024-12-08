import pandas as pd

def calculate_price_trends(data):
    data['price_diff'] = data['price'].diff()
    data['trend'] = data['price_diff'].apply(lambda x: 'Up' if x > 0 else 'Down')
    return data
