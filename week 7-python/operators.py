

# Declare initial values
a = 12
b = 5

# --- Arithmetic Operators ---
print("Arithmetic Operators:")
print("a =", a, ", b =", b)
print("a + b =", a + b)     # Addition
print("a - b =", a - b)     # Subtraction
print("a * b =", a * b)     # Multiplication
print("a / b =", a / b)     # Division (float)
print("a // b =", a // b)   # Floor division (integer result)
print("a % b =", a % b)     # Modulus (remainder)
print("a ** b =", a ** b)   # Exponentiation

# --- Assignment with Arithmetic ---
# Re-initialize 'a' to 12 before starting
a = 12

print("\nAssignment with Arithmetic Operators:")
a += b
print("a += b  →", a)  # a = a + b

a -= b
print("a -= b  →", a)  # a = a - b

a *= b
print("a *= b  →", a)  # a = a * b

a /= b
print("a /= b  →", a)  # a = a / b

a //= b
print("a //= b →", a)  # a = a // b

a %= b
print("a %= b  →", a)  # a = a % b

a **= b
print("a **= b →", a)  # a = a ** b
