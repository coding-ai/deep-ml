def matrix_dot_vector(a: list[list[int | float]], b: list[int | float]) -> list[int | float]:
    # Check if the matrix or vector is empty
    if not a or not b:
        return -1  # Return -1 if either matrix or vector is empty

    # Check if the matrix and vector can be multiplied
    if len(a[0]) != len(b):
        return -1  # Return -1 if dimensions don't match for dot product
    
    # Perform the dot product
    result = []
    for row in a:
        dot_product = sum(x * y for x, y in zip(row, b))
        result.append(dot_product)
    
    return result

# Test cases for the solution
def test_valid_matrix_dot_product():
    # Test case 1: Valid matrix and vector dimensions
    assert matrix_dot_vector([[1, 2, 3], [2, 4, 5], [6, 8, 9]], [1, 2, 3]) == [14, 25, 49]

def test_invalid_matrix_vector_dimensions():
    # Test case 2: Invalid dimensions (should return -1)
    assert matrix_dot_vector([[1, 2], [2, 4], [6, 8], [12, 4]], [1, 2, 3]) == -1

def test_empty_matrix_or_vector():
    # Test case 3: Empty matrix or vector (should return -1)
    assert matrix_dot_vector([], [1, 2]) == -1
    assert matrix_dot_vector([[1, 2]], []) == -1
    assert matrix_dot_vector([], []) == -1

# Run the tests if the script is executed directly
if __name__ == "__main__":
    test_valid_matrix_dot_product()
    test_invalid_matrix_vector_dimensions()
    test_empty_matrix_or_vector()
    print("All tests passed!")