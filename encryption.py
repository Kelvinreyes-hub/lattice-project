import numpy as np
from itertools import product

q = 17
rng = np.random.default_rng(42)

n = 2
m = 4

best_score = float("inf")
best_secret = None
best_error = None


def keygen( q, n, m, rng):
    A = rng.integers(0, q, size=(m, n))
    secret = rng.integers(-2, 3, size=n)
    error = rng.integers(-1, 2, size=m)

    b = (A @ secret + error) % q
    return A, b, secret, error



def encrypt_bit(A, b, message, q, rng):
    r = rng.integers(0, 2, size=len(b))

    u = (A.T @ r) % q

    v = (
        b @ r + message * (q // 2)
    ) % q

    return u, v

def decrypt_bit(u, v, secret, q):
    phase = (v - secret @ u) % q

    if phase > q // 2:
        centered_phase = phase - q
    else:
        centered_phase = phase

    if abs(centered_phase) < q / 4:
        recovered_message = 0
    else:
        recovered_message = 1

    return recovered_message, phase, centered_phase

A, b, secret, error = keygen(q, n, m, rng)

for message in [0, 1]:
    u, v = encrypt_bit(A, b, message, q, rng)

    recovered_message, phase, centered_phase = decrypt_bit(
        u, v, secret, q
    )

    print("Original message:", message)
    print("Ciphertext:", (u, v))
    print("Recovered message:", recovered_message)
    print("Successful?", recovered_message == message)
    print()



