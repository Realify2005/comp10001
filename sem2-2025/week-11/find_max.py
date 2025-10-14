def find_max(numbers):
    """
    Find the maximum number in a list using recursion.
    """

    # Base case: if the list has only one element, return that element.
    if len(numbers) == 1:
        return numbers[0]
    
    # Recursive case: compare the first element with the maximum of the rest of the list and return the maximum.
    return max(numbers[0], find_max(numbers[1:]))

find_max([1, 2, 3, 4, 5])  # Output: 5.