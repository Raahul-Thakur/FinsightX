from neuralprophet import NeuralProphet
import pandas as pd

model = NeuralProphet()

def forecast(
    df: pd.DataFrame, 
    time_col: str = "ds", 
    value_col: str = "y", 
    periods: int = 30
) -> pd.DataFrame:
    df = df.rename(columns={time_col: "ds", value_col: "y"})
    model.fit(df, freq="D")
    future = model.make_future_dataframe(df, periods=periods)
    forecast_df = model.predict(future)
    return forecast_df[["ds", "yhat1"]]
