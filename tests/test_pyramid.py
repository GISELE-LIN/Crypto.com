import pytest

def print_pyramid(n):
    result = []
    for i in range(1, n + 1):
        result.append(" " * (n - i) + "*" * (2 * i - 1))
    return "\n".join(result)

def test_print_pyramid():
    expected_output = "    *\n   ***\n  *****\n *******\n*********"
    print(f"✅ Expected Output:\n{expected_output}")
    
    assert print_pyramid(5) == expected_output, "Pyramid comparison error"