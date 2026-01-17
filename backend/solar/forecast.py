import pandas as pd
from sklearn.linear_model import LinearRegression

def forecast_energy(data):
    df = pd.DataFrame(data)

    X = df[['irradiance', 'temperature']]
    y = df['energy_generated']

    model = LinearRegression()
    model.fit(X, y)

    future_input = [[800, 30]]  # example
    prediction = model.predict(future_input)

    return prediction[0]
