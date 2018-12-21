x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []

for point in zip(labels,x_coord,y_coord,z_coord):
    points.append("{}: {} {} {}".format(*point))

for point in points:
    print(point)
'''
F: 23 677 4
J: 53 233 16
A: 2 405 -6
Q: -12 433 -42
Y: 95 905 3
B: 103 376 -6
W: 14 432 23
X: -5 445 -1
'''