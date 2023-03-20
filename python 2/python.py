import os
import numpy as np
os.system('cls')
arr = np.array([3, 5, 6, 7])

print(arr[3])
print("----------------")
print("Nilai min = ", arr.min())
print("Nilai max = ", arr.max())
print("index nilai min = ", arr.argmin())
print("index nilai max = ", arr.argmax())
print("Nilai rata-rata = ", arr.mean())
print("total nilai = ", arr.sum())
print("standar deviasi = ", arr.std())

# Perubahan Data
arr[3] = 8;
print(arr[3])
# Perubahan Data

print("-------------------------------------------------------")

for x in arr:
    x = 8
    print(x)