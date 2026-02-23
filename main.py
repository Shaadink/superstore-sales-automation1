import os
import pandas as pd

from analysis import (
    clean_data,
    sales_over_time,
    category_analysis,
    region_analysis,
    segment_analysis
)

from model import forecast_linear


def main():
    # 1️ Load raw data
    df = pd.read_csv("data/Sample - Superstore.csv", encoding="latin1")

    # 2️ Clean data
    df = clean_data(df)

    # 3️ Perform analysis
    monthly = sales_over_time(df)
    category = category_analysis(df)
    region = region_analysis(df)
    segment = segment_analysis(df)

    # 4️ Run prediction
    forecast = forecast_linear(monthly)

    # 5️ Save outputs
    os.makedirs("output", exist_ok=True)

    df.to_csv("output/cleaned_data.csv", index=False)
    monthly.to_csv("output/monthly_sales.csv", index=False)
    category.to_csv("output/category_summary.csv", index=False)
    region.to_csv("output/region_summary.csv", index=False)
    segment.to_csv("output/segment_summary.csv", index=False)

    # Save forecast properly
    forecast_df = pd.DataFrame({
        "Forecast_Month_Index": range(len(monthly), len(monthly) + len(forecast)),
        "Predicted_Sales": forecast
    })
    forecast_df.to_csv("output/forecast.csv", index=False)

    print("✅ Pipeline completed successfully!")
    print("📁 Check the output folder.")


if __name__ == "__main__":
    main()