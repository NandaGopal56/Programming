import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt

x, y = datasets.make_regression(n_samples=100, n_features=1, noise=20, random_state=4)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1234)


class linearRegression:
    def __init__(self, lr=0.01, epochs=100000):
        self.lr = lr
        self.epochs = epochs
        self.weights = None
        self.bias = None

    def fit(self, x, y):
        #init parameters
        n_samples,n_features = x.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.epochs):
            y_predicted = np.dot(x,self.weights) + self.bias

            dw = (1/n_samples) * np.dot(x.T, (y_predicted-y))
            db = (1/n_samples) * np.sum(y_predicted-y)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self,x):
        y_predicted = np.dot(x,self.weights) + self.bias

        return y_predicted


regressor = linearRegression()
regressor.fit(x_train,y_train)
prdicted = regressor.predict(x_test)

def mse(y_true,y_predicted):
    return np.mean((y_true-y_predicted)**2)

print(mse(y_test,prdicted))
print(y_test)
print(prdicted)










'''
print(x_train)
print()
print(y_train)
print()
print(x_test)
print()
print(y_test)

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)


fig = plt.figure(figsize=(8,6))
plt.scatter(x,y,color='b',marker='o',s=30)
plt.show()
'''