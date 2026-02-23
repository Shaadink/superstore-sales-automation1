import numpy as np
from sklearn.linear_model import LinearRegression


def forecast_linear(monthly_sales, periods=3):
    monthly_sales = monthly_sales.reset_index(drop=True)
    monthly_sales['Time_Index'] = np.arange(len(monthly_sales))

    X = monthly_sales[['Time_Index']]
    y = monthly_sales['Sales']

    model = LinearRegression()
    model.fit(X, y)

    future_index = np.arange(len(monthly_sales),
                             len(monthly_sales) + periods).reshape(-1, 1)

    future_sales = model.predict(future_index)

    return future_sales
