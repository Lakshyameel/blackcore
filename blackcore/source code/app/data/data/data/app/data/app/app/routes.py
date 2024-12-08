from flask import Response
import pandas as pd

@main.route('/download/<file_format>')
@login_required
def download_data(file_format):
    """
    Download commodity data in CSV or Excel format.
    """
    commodities = Commodity.query.all()
    data = pd.DataFrame(
        [(c.name, c.price, c.date) for c in commodities],
        columns=['Name', 'Price', 'Date']
    )

    if file_format == 'csv':
        response = Response(data.to_csv(index=False), mimetype='text/csv')
        response.headers['Content-Disposition'] = 'attachment; filename=commodity_data.csv'
        return response
    elif file_format == 'excel':
        output = pd.ExcelWriter('commodity_data.xlsx')
        data.to_excel(output, index=False, sheet_name='Commodities')
        output.save()

        response = Response(open('commodity_data.xlsx', 'rb').read(), mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response.headers['Content-Disposition'] = 'attachment; filename=commodity_data.xlsx'
        return response
    else:
        return "Invalid file format requested", 400
