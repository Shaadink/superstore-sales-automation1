import pandas as pd

def clean_data(df):
    df = df.drop_duplicates()
    
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')
    
    df['Profit Margin (%)'] = (df['Profit'] / df['Sales']) * 100
    df['Profit Margin (%)'] = df['Profit Margin (%)'].fillna(0)
    
    return df



def sales_over_time(df):
    monthly = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum()
    monthly = monthly.reset_index()
    monthly.columns = ['Year-Month', 'Sales']
    return monthly


def category_analysis(df):
    result = df.groupby('Category')[['Sales', 'Profit']].sum().reset_index()
    result['Profit Margin %'] = (result['Profit'] / result['Sales']) * 100
    return result


def region_analysis(df):
    result = df.groupby('Region')[['Sales', 'Profit']].sum().reset_index()
    result['Profit Margin %'] = (result['Profit'] / result['Sales']) * 100
    return result


def segment_analysis(df):
    result = df.groupby('Segment')[['Sales', 'Profit']].sum().reset_index()
    result['Profit Margin %'] = (result['Profit'] / result['Sales']) * 100
    return result