import ctypes

# Load the shared library
lib = ctypes.CDLL('./solution.so')

# Define argument and return types for solve_equations
lib.solve_equations.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_float,
                                ctypes.c_float, ctypes.c_float, ctypes.c_float]
lib.solve_equations.restype = None

# Python wrapper function
def solve_from_c(a1, b1, c1, a2, b2, c2):
    lib.solve_equations(a1, b1, c1, a2, b2, c2)

# Take user input
print("Enter coefficients of first equation (a1 b1 c1): ")
a1, b1, c1 = map(float, input().split())

print("Enter coefficients of second equation (a2 b2 c2): ")
a2, b2, c2 = map(float, input().split())

# Call the C function
solve_from_c(a1, b1, c1, a2, b2, c2)

