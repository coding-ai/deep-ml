def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    # Check if the matrix is empty
    if not a:
        return -1  # Return -1 if the matrix is empty
    
    # Perform the transpose using zip and list comprehension
    return [list(row) for row in zip(*a)]

# Test cases for the solution
def test_transpose_matrix():
    # Test case 1: Valid matrix transpose
    assert transpose_matrix([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]]

    # Test case 2: Valid matrix transpose with different dimensions
    assert transpose_matrix([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]

    # Test case 3: Empty matrix (should return -1)
    assert transpose_matrix([]) == -1

# Run the tests if the script is executed directly
if __name__ == "__main__":
    # Run test cases to validate the function
    test_transpose_matrix()
    print("All tests passed!")