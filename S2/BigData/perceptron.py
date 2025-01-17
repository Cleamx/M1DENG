import matplotlib.pyplot as plt
import numpy as np

Data = np.loadtxt('DataIF.txt')
X = Data[:, :3]
LY = Data[:, 3]


def perceptron():
    continuer = True
    W = [0] * (X.shape[1])

    while continuer:
        continuer = False
        for i in range(X.shape[0]):
            FX = np.dot(W, X[i])
            if FX > 0:
                Y = 1
            else:
                Y = 0
            if LY[i] != Y:
                continuer = True
                W = W + (LY[i] - Y) * X[i]
    return W


W = perceptron()

absi = [0, 3]
ordo = [-(W[0] + W[1] * absi[0]) / W[2], -(W[0] + W[1] * absi[1]) / W[2]]
plt.plot(absi, ordo)
plt.scatter(Data[:, 1], Data[:, 2], c=Data[:, 3])
plt.show()
