import numpy as np
import matplotlib.pyplot as plt


def lll_2d(b1, b2, delta=0.75):
    b1 = b1.copy()
    b2 = b2.copy()

    while True:
        
        mu = np.dot(b2, b1) / np.dot(b1, b1)
        b2 = b2 - round(mu) * b1

        
        mu = np.dot(b2, b1) / np.dot(b1, b1)
        b2_star = b2 - mu * b1

        left_side = np.dot(b2_star, b2_star)
        right_side = (delta - mu**2) * np.dot(b1, b1)

        if left_side >= right_side:
            return b1, b2

   
        b1, b2 = b2, b1


def babai_2d(b1, b2, target):
    mu = np.dot(b2, b1) / np.dot(b1, b1)
    b2_star = b2 - mu * b1

    z2 = round(np.dot(target, b2_star) / np.dot(b2_star, b2_star))

    remaining_target = target - z2 * b2
    z1 = round(np.dot(remaining_target, b1) / np.dot(b1, b1))

    return z1 * b1 + z2 * b2



b1 = np.array([4, 1])
b2 = np.array([7, 3])


final_b1, final_b2 = lll_2d(b1, b2)


lattice_points = []

for z1 in range(-5, 6):
    for z2 in range(-5, 6):
        point = z1 * b1 + z2 * b2
        lattice_points.append(point)

lattice_points = np.array(lattice_points)




hidden_point = 2 * b1 - 2 * b2
error = np.array([1.0, 1.0])
target = hidden_point + error


original_babai = babai_2d(b1, b2, target)
reduced_babai = babai_2d(final_b1, final_b2, target)

print("Original basis:", b1, b2)
print("LLL-reduced basis:", final_b1, final_b2)
print("Hidden lattice point:", hidden_point)
print("Target:", target)
print("Babai using original basis:", original_babai)
print("Babai using LLL basis:", reduced_babai)

plt.scatter(lattice_points[:, 0], lattice_points[:, 1],
            color="lightgray", s=25,
            label="lattice points")

plt.scatter(hidden_point[0], hidden_point[1],
            color="purple", marker="*", s=180,
            label="hidden lattice point")

plt.scatter(target[0], target[1],
            color="black", marker="x", s=120,
            label="target")

plt.scatter(original_babai[0], original_babai[1],
            color="red", s=100,
            label="Babai: original basis")

plt.scatter(reduced_babai[0], reduced_babai[1],
            color="limegreen", s=100,
            label="Babai: LLL basis")

plt.plot([target[0], original_babai[0]],
         [target[1], original_babai[1]],
         linestyle="--", color="red")

plt.plot([target[0], reduced_babai[0]],
         [target[1], reduced_babai[1]],
         linestyle="--", color="limegreen")

plt.grid()
plt.axis("equal")
plt.legend()
plt.title("Babai before and after LLL reduction")
plt.show()