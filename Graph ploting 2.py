import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [1.2, 0.9, -0.3, 0.6, -1.0, -1.3, 1.5, 0.6, 0.2, -2.0]

plt.plot(x, y, marker="o", markersize= "10")
plt.title('x axis vs y axis')
plt.xlabel('x axis')
plt.ylabel('y axis')

plt.show()