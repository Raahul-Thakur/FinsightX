from tools.forecast_tool import forecast
import pandas as pd

def analyze_macro_trends(df: pd.DataFrame) -> dict:
    forecast_df = forecast(df)
    latest = forecast_df.tail(1)
    return latest.to_dict(orient="records")[0]
