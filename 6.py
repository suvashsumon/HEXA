# %%
import pandas as pd

# %%
df = pd.read_csv("dataset.csv")
df.head()

# %%
df['date'] = pd.to_datetime(df['date'])
df.head()

# %%
df.keys()

# %%
df = df.set_index("date")
df.head()

# %%
df.dropna()

# %%
df[:24].plot()

# %%
df['first_order'] = df - df.shift(12)

# %%
from statsmodels.tsa.stattools import adfuller



# %%
p_value = adfuller(df['value'].dropna())[1]
print(p_value)

# %%
p_value = adfuller(df['first_order'].dropna())[1]
print(p_value)

# %%
df['second_order'] = df['first_order'] - df['first_order'].shift(1)

# %%
p_value = adfuller(df['second_order'].dropna())[1]
print(p_value)

# %%
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib

# %%
plot_acf(df["value"], lags=10);

# %%
plot_pacf(df["value"], lags=10);

# %%
from statsmodels.tsa.arima.model import ARIMA

# %%
df = df.drop("first_order", axis=1)
df = df.drop("second_order", axis=1)
df.head()

# %%
p = 2
d = 2
q = 5
model = ARIMA(df, order=(p, d, q))

# %%
fittedmodel = model.fit()

# %%
forecast = fittedmodel.predict(start=len(df)-24, end=len(df)+24)

# %%
import matplotlib.pyplot as plt 

# %%
plt.plot(forecast)
plt.plot(df)
plt.show()

# %%
from statsmodels.tsa.statespace.sarimax import SARIMAX

# %%
model = SARIMAX(df, order=(p, d, q), seasonal_order=(p, d, q, 12))

# %%
fittedmodel = model.fit()

# %%
forecast = fittedmodel.predict(start=len(df)-24, end=len(df)+24)

# %%
plt.plot(forecast)
plt.plot(df[-50:])
plt.show()

# %%
from sklearn.metrics import mean_squared_error, mean_absolute_error

# %%
forecast = fittedmodel.predict(start=len(df)-24, end=len(df))

# %%
mse = mean_squared_error(forecast, df[-25:])

# %%
import numpy as np

# %%
print(f"MSE : {mse}")
print(f"RMSE : {np.sqrt(mse)}")

# %%
len(df)

# %%
df1 = df[:150]
len(df1)

# %%
df2 = df[150:]
len(df2)


