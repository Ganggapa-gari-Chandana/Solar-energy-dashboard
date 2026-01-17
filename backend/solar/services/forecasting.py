import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from datetime import timedelta

def seven_day_forecast(data):

    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    df['day'] = df['date'].dt.day
    df['month'] = df['date'].dt.month

    X = df[['irradiance','temperature','day','month']]
    y = df['energy_generated']

    model = RandomForestRegressor()
    model.fit(X, y)

    last = df.iloc[-1]
    future = []

    for i in range(1, 8):
        future.append([
            last['irradiance'],
            last['temperature'],
            (last['day'] + i) % 30,
            last['month']
        ])

    preds = model.predict(future)

    result = []
    for i, val in enumerate(preds):
        result.append({
            "day": f"Day {i+1}",
            "energy": round(float(val), 2)
        })

    return result
