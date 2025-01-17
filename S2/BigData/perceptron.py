import matplotlib.pyplot as plt



def perceptron():
    W = [0,0,0]
    LY = 1 * W[0] + X[0, i] * W[1] + X[1, i] * W[2]
    if LY > 0:
        Y = 1
    else:
        Y = 0
    for W in range(0, 3):
        W[0] = W[i] + (LY[i] - Y)
        W[1] = W[i] + (LY[i] - Y) * X[0, i]
        W[2] = W[i] + (LY[i] - Y) * X[1, i]


plt.scatter(X[0], X[1], c=Y)
plt.show()