from src.data_cleaning import load_data, clean_data
from src.analysis import (
    compute_kpis,
    top_bottom_products,
    category_analysis,
    size_analysis,
    time_analysis
)
from src.visualization import bar_chart, line_chart, plot_kpis


# LOAD DATA
df = load_data("data/pizza_sales.csv")
df = clean_data(df)

# KPI
kpis = compute_kpis(df)
plot_kpis(kpis)

# TOP/BOTTOM
top5_rev, bottom5_rev, top5_qty, bottom5_qty = top_bottom_products(df)

bar_chart(top5_rev, "Top 5 Pizzas by Revenue", "Pizza Name", "Revenue")
bar_chart(bottom5_rev, "Bottom 5 Pizzas by Revenue", "Pizza Name", "Revenue")

bar_chart(top5_qty, "Top 5 Pizzas by Quantity", "Pizza Name", "Quantity")
bar_chart(bottom5_qty, "Bottom 5 Pizzas by  Quantity", "Pizza Name", "Quantity")

# CATEGORY
category = category_analysis(df)
bar_chart(category, "Revenue by Pizzas Category", "Pizza Category", "Revenue")

# SIZE
size = size_analysis(df)
bar_chart(size, "Revenue by Pizzas Size", "Pizza Size", "Revenue")

# TIME
monthly, daily = time_analysis(df)

line_chart(monthly, "Monthly Trend")
line_chart(daily, "Daily Trend")