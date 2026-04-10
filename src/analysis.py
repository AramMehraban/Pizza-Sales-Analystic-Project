import pandas as pd

def compute_kpis(df):

    Total_Revenue = df['total_price'].sum()
    Total_Orders = df['order_id'].nunique()
    Avg_Order_Value = df.groupby('order_id')['total_price'].sum().mean()
    Total_Pizzas = df['quantity'].sum()
    Avg_Pizza_per_Order = Total_Pizzas / Total_Orders

    return {
        "Revenue": Total_Revenue,
        "Orders": Total_Orders,
        "AOV": Avg_Order_Value,
        "Pizzas": Total_Pizzas,
        "Avg/Pizza": Avg_Pizza_per_Order
    }


def top_bottom_products(df):

    top5_rev = df.groupby('pizza_name')['total_price'].sum().sort_values(ascending=False).head(5)
    bottom5_rev = df.groupby('pizza_name')['total_price'].sum().sort_values().head(5)

    top5_qty = df.groupby('pizza_name')['quantity'].sum().sort_values(ascending=False).head(5)
    bottom5_qty = df.groupby('pizza_name')['quantity'].sum().sort_values().head(5)

    return top5_rev, bottom5_rev, top5_qty, bottom5_qty


def category_analysis(df):
    return df.groupby('pizza_category')['total_price'].sum()


def size_analysis(df):
    return df.groupby('pizza_size')['total_price'].sum()


def time_analysis(df):

    month_order = [
        "January","February","March","April","May","June",
        "July","August","September","October","November","December"
    ]

    day_order = [
        "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"
    ]

    monthly = df.groupby(df['order_date'].dt.month_name())['order_id'].nunique()
    monthly = monthly.reindex(month_order)

    daily = df.groupby(df['order_date'].dt.day_name())['order_id'].nunique()
    daily = daily.reindex(day_order)

    return monthly, daily