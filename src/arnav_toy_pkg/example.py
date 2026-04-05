def quick_sort(arr: list) -> list:
    """
    Sorts a list of elements using the Quick Sort algorithm.

    Parameters
    ----------
    arr : list
        An unsorted list of comparable elements (e.g., integers or floats).

    Returns
    -------
    list
        A new list containing the sorted elements.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)