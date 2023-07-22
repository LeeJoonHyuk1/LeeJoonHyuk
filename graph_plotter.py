import matplotlib.pyplot as plt

x=["A", "B", "C", "D", "E"] 
y=[2,3,4,5,6]

plt.bar(x,y)
plt.plot(x,y, Label="Line 1")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.legend()
plt.title("Demo")
plt.show()
