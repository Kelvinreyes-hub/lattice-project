import numpy as np
from itertools import product

q = 17
rng = np.random.default_rng(42)

n = 3
m = 6

best_score = float("inf")
best_secret = None
best_error = None


A = rng.integers(0, q, size=(m, n))
secret = rng.integers(-2, 3, size=n)
error = rng.integers(-1, 2, size=m)

b = (A @ secret + error) % q

clean_value = A @ secret
noisy = clean_value + error

for values in product(range(-2,3), repeat = n): 
    possible_secret = np.array(values)

    possible_error = (b - A @ possible_secret) % q
    centered_error = np.where(
        possible_error > q//2, 
        possible_error - q, 
        possible_error
    )
    score = np.linalg.norm(centered_error)

    if score < best_score: 
        best_score = score
        best_secret = possible_secret
        best_error = centered_error


print("\n    Toy LWE Attack Result    ")
print("Actual secret:", secret)
print("Recovered secret:", best_secret)
print("Recovered centered error:", best_error)
print("Smallest error score:", round(best_score, 2))

print( "Attack successful?", np.array_equal(secret, best_secret))
print("Guesses tested:", 5 ** n)



# print("Actual hidden secret:", secret)
# print("Recovered secret:", best_secret)
# print("Recovered error:", best_error)
# print("Smallest score:", best_score)

# print("Attack successful?",
#       np.array_equal(secret, best_secret))
