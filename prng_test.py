# prng_test.py

import matplotlib.pyplot as plt
import seaborn as sns

class SimplePRNG:
    def __init__(self, seed=123456789):
        self.modulus = 2**32
        self.multiplier = 1103515245
        self.increment = 12345
        self.state = seed

    def next(self):
        self.state = (self.multiplier * self.state + self.increment) % self.modulus
        return self.state / self.modulus

# PRNG ব্যবহার করে 10000 সংখ্যা তৈরি
prng = SimplePRNG(seed=42)
data = [prng.next() for _ in range(10000)]

# Uniformity Plot
plt.figure(figsize=(8, 4))
sns.histplot(data, bins=50, kde=True, color='skyblue')
plt.title("Distribution (Uniformity)")
plt.xlabel("Generated Number")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# Dependency Plot
plt.figure(figsize=(6, 6))
plt.scatter(data[:-1], data[1:], s=1, alpha=0.5)
plt.title("Dependency Plot (Xi vs Xi+1)")
plt.xlabel("Xi")
plt.ylabel("Xi+1")
plt.grid(True)
plt.show()
