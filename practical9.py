import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print("Array:", arr)
print("Size:", arr.size)
print("Data Type:", arr.dtype)
print("Number of Dimensions:", arr.ndim)


import numpy as np
a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 5, 8, 10])
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)



import numpy as np
arr = np.array([12, 25, 8, 45, 30, 18, 50, 22, 35, 10])
print("Array:", arr)
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Sum:", np.sum(arr))
print("Average:", np.mean(arr))



import numpy as np
arr = np.arange(1, 21)
even = arr[arr % 2 == 0]
odd = arr[arr % 2 != 0]
print("Array:", arr)
print("Even Numbers:", even)
print("Odd Numbers:", odd)


import numpy as np
arr = np.arange(1, 13)
print("Original Array:", arr)
print("\n2 x 6 Matrix:")
print(arr.reshape(2, 6))
print("\n3 x 4 Matrix:")
print(arr.reshape(3, 4))
print("\n4 x 3 Matrix:")
print(arr.reshape(4, 3))



import numpy as np
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
b = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])
print("Matrix A:")
print(a)
print("Matrix B:")
print(b)
print("Addition:")
print(a + b)



import numpy as np
a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])
result = np.matmul(a, b)
print("Matrix A:")
print(a)
print("Matrix B:")
print(b)
print("Matrix Multiplication:")
print(result)


import numpy as np
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])
print("Original Matrix:")
print(arr)
print("Transpose:")
print(arr.T)


import numpy as np
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])
print("First Row:", arr[0])
print("Last Column:", arr[:, -1])
print("Diagonal:", np.diag(arr))
print("Second and Third Rows:")
print(arr[1:3])


import numpy as np
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])
print("Matrix:")
print(arr)
print("Row Sums:", np.sum(arr, axis=1))
print("Column Sums:", np.sum(arr, axis=0))


import numpy as np
arr = np.arange(1, 21)
print("Array:", arr)
print("First 5:", arr[:5])
print("Last 5:", arr[-5:])
print("Alternate Elements:", arr[::2])
print("Reverse:", arr[::-1])



import numpy as np
arr = np.array([25, 60, 45, 75, 30, 90, 55, 20, 80, 40])
print("Original Array:", arr)
arr[arr > 50] = 0
print("Modified Array:", arr)



import numpy as np
arr = np.array([45, 12, 89, 23, 7, 56, 34])
print("Original:", arr)
print("Ascending:", np.sort(arr))
print("Descending:", np.sort(arr)[::-1])


import numpy as np
arr = np.array([10, 20, 10, 30, 20, 40, 30, 50, 40])
print("Original Array:", arr)
print("Unique Elements:", np.unique(arr))



import numpy as np
a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])
print("Horizontal Concatenation:")
print(np.hstack((a, b)))
print("\nVertical Concatenation:")
print(np.vstack((a, b)))




import numpy as np
marks = np.array([78, 65, 89, 92, 56, 74, 81, 69, 95, 88])
print("Marks:", marks)
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
print("Average:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))




import numpy as np
marks = np.array([45, 67, 78, 89, 56, 92, 34, 76, 88, 65,
                  71, 55, 49, 95, 82, 61, 73, 84, 58, 90])
average = np.mean(marks)
print("Class Average:", average)
print("Marks Above Average:", marks[marks > average])


import numpy as np
arr = np.arange(1, 25).reshape(2, 3, 4)
print("3D Array:")
print(arr)
print("Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)



import numpy as np
arr = np.arange(1, 25).reshape(2, 3, 4)
print("First Element:", arr[0, 0, 0])
print("Last Element:", arr[1, 2, 3])
print("Element [0,1,2]:", arr[0, 1, 2])
print("Element [1,2,3]:", arr[1, 2, 3])



import numpy as np
arr = np.arange(1, 25).reshape(2, 3, 4)
print("Array:")
print(arr)
print("Sum of All Elements:", np.sum(arr))
print("Sum of Each Layer:", np.sum(arr, axis=(1, 2)))
print("Sum Along Rows:", np.sum(arr, axis=2))
print("Sum Along Columns:", np.sum(arr, axis=1))





import numpy as np
np.random.seed(10)
arr = np.random.randint(1, 101, size=(2, 3, 4))
print("Original Array:")
print(arr)
arr[arr > 50] = 0
print("\nModified Array:")
print(arr)



import numpy as np
np.random.seed(20)
arr = np.random.randint(1, 101, size=(3, 4, 5))
print("Array:")
print(arr)
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))



import numpy as np
arr = np.arange(1, 25).reshape(2, 3, 4)
print("Original 3D Array:")
print(arr)
flat = arr.flatten()
print("\nFlattened Array:")
print(flat)



import numpy as np
arr = np.arange(1, 28).reshape(3, 3, 3)
flat = arr.flatten()
print("3D Array:")
print(arr)
print("\nFlattened Array:")
print(flat)
print("Sum:", np.sum(flat))
print("Average:", np.mean(flat))
print("Maximum:", np.max(flat))
print("Minimum:", np.min(flat))




import numpy as np
np.random.seed(30)
arr = np.random.randint(1, 101, size=(3, 4, 5))
flat = arr.flatten()
average = np.mean(flat)
print("3D Array:")
print(arr)
print("\nElements Greater Than 50:")
print(flat[flat > 50])
print("\nEven Numbers:")
print(flat[flat % 2 == 0])
print("\nAverage:", average)
print("\nElements Less Than Average:")
print(flat[flat < average])