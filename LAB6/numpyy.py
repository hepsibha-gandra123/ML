# import numpy as np
# np.random.seed(1234)
# a = np.random.randint(low=1, high=10, size=(3, 4))
# b = np.random.randint(low=1, high=10, size=(3, 1))
# print(a)
# print(b)

# a = np.array([3, 11, 4, 5])
# b = np.array([5, 0, 3])
# A = a[:, np.newaxis]
# print(A)
# B = b[np.newaxis, :]
# print(B)
# print(A-B)

# arr = np.arange(start=1, stop=9)
# print(arr)
# arr = arr.reshape(2, 4)
# print(arr)
# print(arr.T)

# mask = arr == 8
# print(mask)

# bot = np.ones(shape=(3, 4))
# bot[[0, 2], [1, 2]] = np.nan
# print(bot)


# np.nan==np.nan-->false
# np.nan!=np.nan-->true
# np.isnan(np.nan)

# print(np.array([np.inf, -np.inf]))


# generator = rng = np.random.default_rng(123)
# arr = generator.integers(low=1, high=7, size=3)
# print(arr)

# generator = rng = np.random.default_rng(1236)
# arr = generator.choice(a=10, size=3, replace=False)
# print(arr)

# f = np.array([
#     [1, 2],
#     [3, 4],
#     [5, 6],
#     [7, 8],

#     [9, 10]

# ])
# generator = rng = np.random.default_rng(1236)
# arr = generator.permutation(f, axis=0)
# print(arr)


# generator = np.random.default_rng(seed=123)
# arr = generator.uniform(low=1.0, high=2.0, size=(2, 2))
# print(arr)

# generator = np.random.default_rng(seed=123)
# arr = generator.normal(loc=0.0, scale=1.0, size=(2, 2))
# print(arr)

# generator = np.random.default_rng(seed=123)
# arr = generator.binomial(n=10, p=0.25, size=(3, 2))
# print(arr)


import numpy as np
import pandas as pd
# 1.
# arr = np.array([[1, 2, 3],
#                 [4, 5, 6]])
# df = pd.DataFrame(arr, columns=["A", "B", "C"])
# print(df)

# 2.
# arr = np.array([1, 2, 3, 4, 5])
# df = pd.DataFrame(arr, columns=["Values"])
# df["Cumulative_Sum"] = df["Values"].cumsum()
# print(df)


# 3.
# A = np.array([[1, 2],
#               [3, 4]])
# B = np.array([[5, 6],
#               [7, 8]])
# result = np.matmul(A, B)
# print(result)

# 4.
# arr = np.random.randint(1, 10, 15)
# print("Array:", arr)
# print("Unique values:", np.unique(arr))

# 5.
# df = pd.DataFrame([[1,2,3],[4,5,6]], columns=["A","B","C"])
# new_df = df.T
# print(new_df)


# 6.
# arr = np.arange(2, 11).reshape(3, 3)
# print(arr)

# 7.
# arr = np.zeros(10)
# print(arr)
# arr[6] = 11
# print(arr)

# 8.
# arr = np.arange(12, 38)
# print(arr)

# 9.
# arr1 = np.array([0,10,20,40,60])
# arr2 = np.array([10,30,40])
# common = np.intersect1d(arr1, arr2)
# print("Common values:", common)

# 10.
# arr1 = np.array([0,10,20,40,60,80])
# arr2 = np.array([10,30,40,50,70,90])
# diff = np.setdiff1d(arr1, arr2)
# print(diff)

# 11.
# a = np.array([1, 2])
# b = np.array([4, 5])
# print("a > b", a > b)
# print("a >= b", a >= b)
# print("a < b", a < b)
# print("a <= b", a <= b)

# 12.
# arr = np.eye(3)
# print(arr)

# 13.
# arr = np.array([[2, 4, 6],
#                 [6, 8, 10]])
# print("Fourth element:", arr.flatten()[6])

# 14
# a = np.array([10, 20, 30])
# b = np.array([40, 50, 60])
# result = np.column_stack((a, b))
# print(result)

# 15
# arr = np.arange(12).reshape(3, 4)
# print(arr*3)
