# Lattice Cryptography Learning Project

This project is a collection of small Python programs I built to learn the mathematical ideas behind lattice-based cryptography and post-quantum cryptography.


## Files

- `lattice_practice.py` — Creates a 2D lattice, finds the closest lattice point by checking nearby possibilities, and demonstrates Babai's nearest-plane algorithm.
- `lwe.py` — Builds a small Learning With Errors (LWE) problem using the formula:

  \[
  b = As + e \pmod q
  \]

  It then performs a brute-force search to recover the small hidden secret.

- `encryption.py` — Demonstrates toy one-bit LWE-style encryption and decryption.

- `lll_basics.py` — Demonstrates LLL basis reduction. It compares Babai's algorithm using an awkward original basis versus an LLL-reduced basis, showing how a better basis can improve the nearest-point estimate.

## Concepts practiced

- Vectors and integer combinations
- Two-dimensional lattices
- Euclidean distance and closest-vector problems
- Gram-Schmidt projection
- Babai's nearest-plane algorithm
- Learning With Errors (LWE)
- Modular arithmetic
- Small error vectors
- LLL lattice basis reduction
