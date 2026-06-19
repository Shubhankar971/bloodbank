from sklearn.linear_model import LinearRegression
import numpy as np


days=np.array([1,2,3,4,5]).reshape(-1,1)

units=np.array([20,30,35,50,60])


model=LinearRegression()

model.fit(days,units)


future=model.predict([[6]])

print(
"Predicted Blood Demand:",
future
)
