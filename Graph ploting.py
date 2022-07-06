import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y = [10, 30, 20, 50, 60, 35, 36, 15, 33]

plt.plot(x, y, marker="*", markersize= "10", linestyle= "--", color="blue", markerfacecolor='red')
plt.title('x axis vs y axis')
plt.xlabel('x axis')
plt.ylabel('y axis')

plt.show()