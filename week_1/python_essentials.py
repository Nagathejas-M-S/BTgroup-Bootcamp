
# ============================================================
# 1. PYTHON BASICS
# ============================================================

# Comments
# This is a comment.

"""
This is a docstring explaining the file or a function.
"""

# import sys
# print("Python version:", sys.version)

# ============================================================
# 2. VARIABLES & DATA TYPES
# ============================================================

# x = 10          # int
# pi = 3.14       # float
# flag = True     # bool
# text = "Hello"  # str

# print(type(x), type(pi), type(flag), type(text))

# # None
# empty = None
# print(empty)

# # Type casting
# n = int("50")
# f = float("3.5")
# print(n, f)

# # Mutable vs Immutable
# a = 5
# print(id(a))
# a = a + 1
# print(id(a))   # new object

# lst = [1, 2]
# print(id(lst))
# lst.append(3)
# print(id(lst)) # same object


# ============================================================
# 3. OPERATORS
# ============================================================


# a = 10
# b = 3

# # Arithmetic
# print(a + b, a - b, a * b, a / b, a % b, a ** b)

# # Comparison
# print(a > b, a == b, a != b)

# # Logical
# print(True and False)
# print(True or False)
# print(not True)

# # Bitwise
# print(a & b, a | b, a ^ b, a << 1, a >> 1)

# # Assignment
# c = 5
# c += 2
# print(c)

# # Identity / Membership
# nums = [1, 2, 3]
# print(nums is nums)
# print(2 in nums)


# ============================================================
# 4. STRINGS
# ============================================================

# s = "Python Rocks!"

# print(s[0], s[-1])
# print(s[0:6])
# print(s[::2])

# # Methods
# msg = "  python is fun  "
# print(msg.strip())
# print(msg.upper())
# print(msg.replace("python", "coding"))

# # split & join
# words = msg.strip().split()
# print(words)
# print("_".join(words))

# # Formatting
# name = "user"

# # f-string
# print(f"Hello {name}")

# # .format
# print("Hello {}".format(name))

# # Raw string
# path = r"C:\Users\NewFolder"
# print(path)


# ============================================================
# 5. COLLECTIONS
# ============================================================

# # Array
# from array import array
# arr = array("i", [1, 2, 3])
# print(arr)

# # List
# lst = [10, 20, 30]
# lst.append(40)
# print(lst, lst[1:3])

# # List comprehension
# sq = [i*i for i in range(5)]
# print(sq)

# # Tuple
# t = (1, 2, 3)
# print(t)

# # Set
# st = {1, 2, 2, 3}
# st.add(4)
# print(st)

# # Dictionary
# d = {"a": 1, "b": 2}
# d["b"] = 20
# print(d)

# for key, value in d.items():
#     print(key, value)

# # Built-in functions
# nums = [5, 1, 9]
# print(len(nums), max(nums), min(nums), sum(nums), sorted(nums))


# ============================================================
# 6. CONTROL FLOW
# ============================================================

# val = 12

# if val < 10:
#     print("small")
# elif val < 20:
#     print("medium")
# else:
#     print("large")

# # for loop
# for i in [1, 2, 3]:
#     print(i)

# # while loop
# i = 0
# while i < 3:
#     print(i)
#     i += 1

# # break / continue / pass
# for i in range(5):
#     if i == 1:
#         continue
#     if i == 3:
#         break
#     if i == 2:
#         pass
#     print("i =", i)


# ============================================================
# 7. FUNCTIONS
# ============================================================


# def greet(user):
#     """Return greeting text"""
#     return f"Hello, {user}"

# print(greet("world"))

# # Positional & keyword arguments
# def add(a, b):
#     return a + b

# print(add(2, 3))
# print(add(a=5, b=10))

# # Default arguments
# def power(base, exp=2):
#     return base ** exp

# print(power(3))
# print(power(3, 3))

# # *args and **kwargs
# def show_all(*args, **kwargs):
#     print(args, kwargs)

# show_all(1, 2, 3, x=10, y=20)

# # Scope
# global_var = "outside"

# def outer():
#     x = "outer"

#     def inner():
#         nonlocal x
#         print(global_var)
#         x = "inner changed"
#     inner()
#     print(x)

# outer()

# count = 0

# def inc():
#     global count
#     count += 1

# inc()
# inc()
# print("count =", count)


# MAIN GUARD
# if __name__ == "__main__":
#     print("\n--- End of Examples ---")

