import numpy as np

class NeuralNetwork:
    def __init__(self,x,y):
        self.input=x
        self.weight1=np.random.rand(self.input.shape[1],4)
        self.weight2=np.random.rand(4,1)
        self.output=np.zeros(y.shape)

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input ,self.weight1))
        self.layer2 = sigmoid(np.dot(self.layer1 ,self.weight2))
        
    def backpropagation(self):
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))

        self.weights1 += d_weights1
        self.weights2 += d_weights2

        