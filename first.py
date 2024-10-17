#%%
import pandas as pd
OnlineRetail = pd.read_csv('/Users/manvendra/Desktop/python/project/new/OnlineRetail.csv', encoding='ISO-8859-1')
OnlineRetail.head()
# %%
OnlineRetail.info()
OnlineRetail.describe()
OnlineRetail.isnull().sum()
# %%
OnlineRetail.dropna(subset=['Description','CustomerID'],inplace=True)
# %%
OnlineRetail.isnull().sum()
# %%
OnlineRetail.duplicated().sum()
OnlineRetail.drop_duplicates(inplace=True)
# %%
OnlineRetail.describe()
# %%
import seaborn as sns
import matplotlib.pyplot as plt
sns.boxplot(x=OnlineRetail['UnitPrice'])
plt.show()
# %%  Total price of the products
OnlineRetail['TotalCost'] = OnlineRetail['Quantity']* OnlineRetail['UnitPrice']
print('Successfully Done')
# %% Sales in each country
salesBYcountry = OnlineRetail.groupby('Country')['TotalCost'].sum()
print(salesBYcountry)
# %%  Monthly COST -- GRAPH
OnlineRetail['InvoiceDate'] = pd.to_datetime(OnlineRetail['InvoiceDate'])
OnlineRetail.set_index('InvoiceDate', inplace=True)
OnlineRetail['TotalCost'].resample('M').sum().plot()
plt.title('Monthly Total Cost Over Time')
plt.ylabel('Total Cost')
plt.xlabel('Month')
plt.show()
# %%  Product -- SALES
top_products = OnlineRetail.groupby('Description')['TotalCost'].sum().nlargest(10)
top_products.plot(kind='bar')
plt.show()
# %%
#%% For the repeated customers 
customer_frequency =  OnlineRetail.groupby('CustomerID')['InvoiceNo'].nunique()
plt.hist(customer_frequency, bins=100)  
plt.title("Customer Frequency")  
plt.xlabel("Number of Purchases")  
plt.ylabel("Number of Customers")  
plt.show()
# %%