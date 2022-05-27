import random
import time

def partition(array, low, high):
  pivot = array[len(array)//2]
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1
 

def quick_sort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    quick_sort(array, low, pi - 1)
    quick_sort(array, pi + 1, high)
 

array = [x for x in range(998)]
start_time = time.time()
quick_sort(array, 0, len(array) - 1)
end_time = time.time()
print(f'Sorted array: {array}')
print(f"The execution time is: {end_time-start_time}")