import numpy as np
import matplotlib.pyplot as plt

def babai_2d(b1, b2, target): 
    projection = (np.dot(b2,b1) / np.dot(b1,b1)) * b1
    b2_star = b2 - projection
    z2 = round( np.dot(target, b2_star) / np.dot(b2_star, b2_star))

    remaining_target = target - z2 * b2
    z1 = round (
        np.dot(remaining_target, b1)/ np.dot(b1, b1)
    )
    est_point = z1 * b1 + z2 * b2
    return est_point, [z1, z2]


b1 = np.array([3,0])
b2 = np.array([1,2])
hidden_point = 2 * b1 - b2
error = np.array([.3, .4])
# error = np.array([1.6, 1.1])

target = hidden_point + error


points = []
distances = []
coefficients = []

for z1 in range(-3,4):
    for z2 in range(-3,4):
        point = (z1*b1) + (z2 * b2)
        points.append(point)
        coefficients.append([z1, z2])

points = np.array(points)
x_value = points[:, 0]
y_value = points[:, 1]



for point in points: 
    distance = np.linalg.norm(target - point)
    distances.append(distance)

#print(distances[:5])
closest_index = np.argmin(distances)
closest_point = points[closest_index]
closest_distance = distances[closest_index]
closest_coefficients = coefficients[closest_index]




plt.scatter(x_value, y_value)
plt.scatter(target[0], target[1], color= "black", marker = "x", s=100, label="target point")
plt.scatter(closest_point[0], closest_point[1], color="limegreen", s=120, label="closest lattice point")
plt.quiver(0,0, b1[0], b1[1], angles="xy", scale_units="xy", scale = 1, color = "red", label ="b1 = (3,0)")
plt.quiver(0,0,b2[0], b2[1], angles="xy", scale_units="xy", scale = 1, color = "blue", label = "b2 = (1,2)")

plt.plot([target[0], closest_point[0]], [target[1], closest_point[1]], linestyle= "--", color = "black")
plt.grid()
plt.axis("equal")
plt.xlabel("x-coordinate")
plt.ylabel("y-coordinate")
plt.title("2D Lattice")
plt.legend()
plt.show()






babai_point, babai_coefficients = babai_2d(b1, b2, target)

print("Brute-force point:", closest_point)
print("Babai point:", babai_point)
print("Babai coefficients:", babai_coefficients)

print("Do they match?",
      np.array_equal(closest_point, babai_point))




#print("closest coef", closest_coefficients )
# print("hidden point", hidden_point)
# print("error", error)
# # print("target", target)

# print("closest lattice", closest_point) 
# print("distance to target", closest_distance)
