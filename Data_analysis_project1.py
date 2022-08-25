import pandas as pd
from matplotlib import pyplot as plt


stock_df = pd.read_excel(r"C:\Users\dalty\PycharmProjects\pythonProject10\stock_prices.xltx")
plt.style.use("ggplot")
stock_df_index = stock_df.index
stock_df_cols = stock_df.columns
price_y = []
year_x = []
for year in range(50):
    year_x.append(stock_df["year"][year])
num = 49
for price in stock_df["avg_price"][49:103]:
    price_y.append(stock_df["avg_price"][num])
    num += 1
plt.style.use('ggplot')
df = pd.read_excel(r"C:\Users\dalty\Documents\Custom Office Templates\listings.xltx")
df_index = df.index
df_cols = df.columns
x_values = []
y_values = []
x1_values = []
y1_values = []
hotel_x = []
hotel_y = []
shared_x = []
shared_y = []
for i in range(len(df['room_type'])):
    if df['room_type'][i] == "Entire home/apt":
        y_values.append(int(df['price'][i]))
        x_values.append(df['room_type'][i])
    elif df['room_type'][i] == "Private room":
        y1_values.append(int(df['price'][i]))
        x1_values.append(df['room_type'][i])
    elif df['room_type'][i] == "Hotel room":
        hotel_y.append(int(df['price'][i]))
        hotel_x.append(df['room_type'][i])
    elif df['room_type'][i] == "Shared room":
        shared_y.append(int(df['price'][i]))
        shared_x.append(df['room_type'][i])
    else:
        pass
plt.bar(x_values, sorted(y_values), label='Entire Home')
plt.bar(x1_values, sorted(y1_values), label='Private Room')
plt.bar(hotel_x, sorted(hotel_y), color='#444444', label='Hotel Room')
plt.bar(shared_x, sorted(shared_y), label='Shared Room')
plt.xlabel('Room Types')
plt.ylabel('Price Range')
plt.title('Price Range per Room Type')
plt.legend()
plt.show()
price_y.remove(price_y[0])
plt.plot(year_x, price_y, marker=".")
plt.xlabel("Years")
plt.ylabel("Average Stock Prices")
plt.title("Average Walmart Stock Price Per Year")
plt.grid(True)
plt.show()
