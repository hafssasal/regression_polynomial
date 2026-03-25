import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

X = np.array([10,20,30,40,50,60,70]).reshape(-1,1)
y = np.array([100,180,250,300,320,310,290])

poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

def predict_production(x):
    val = poly.transform([[x]])
    return round(model.predict(val)[0],2)