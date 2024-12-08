from flask import jsonify
import pandas as pd
from data.analytics import plot_price_trends, interactive_trends_plot

@main.route('/dashboard')
@login_required
def dashboard():
    commodities = Commodity.query.all()
    data = pd.DataFrame(
        [(c.name, c.price, c.date) for c in commodities],
        columns=['Name', 'Price', 'Date']
    )
    fig = interactive_trends_plot(data)
    return render_template('dashboard.html', plot=fig.to_html(), data=commodities)

@main.route('/api/commodity_data', methods=['GET'])
def api_commodity_data():
    """
    API endpoint to fetch commodity data.
    """
    commodities = Commodity.query.all()
    data = [{"name": c.name, "price": c.price, "date": c.date} for c in commodities]
    return jsonify(data)
