def selection_sort(array):
  """Sorts an array in ascending order using the selection sort algorithm.

  Args:
    array: A list of elements to be sorted.

  Returns:
    A sorted list of elements.
  """

  for i in range(len(array) - 1):
    smallest_index = i

    for j in range(i + 1, len(array)):
      if array[j] < array[smallest_index]:
        smallest_index = j

    array[i], array[smallest_index] = array[smallest_index], array[i]

  return array


# Example usage:

array = [5, 3, 2, 1, 4]
sorted_array = selection_sort(array)

print(sorted_array)
