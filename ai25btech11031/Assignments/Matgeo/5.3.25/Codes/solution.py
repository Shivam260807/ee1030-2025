def determinant(a1, b1, a2, b2):
    """Compute the determinant of coefficient matrix"""
    return a1 * b2 - a2 * b1

def solve_equations(a1, b1, c1, a2, b2, c2):
    """Solve the two equations using Cramer's Rule"""
    det = determinant(a1, b1, a2, b2)

    if det == 0:
        print("The equations have no unique solution (parallel or coincident lines).")
    else:
        x = (c1 * b2 - c2 * b1) / det
        y = (a1 * c2 - a2 * c1) / det
        print(f"Solution: x = {x:.2f}, y = {y:.2f}")

def main():
    print("Enter coefficients for the equations:")
    a1, b1, c1 = map(float, input("a1 b1 c1: ").split())
    a2, b2, c2 = map(float, input("a2 b2 c2: ").split())

    solve_equations(a1, b1, c1, a2, b2, c2)

if __name__ == "__main__":
    main()

