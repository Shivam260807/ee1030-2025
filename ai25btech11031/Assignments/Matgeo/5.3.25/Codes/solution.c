#include "solution.h"

int main() {
    float a1, b1, c1, a2, b2, c2;

    // Input the equations
    input_equations(&a1, &b1, &c1, &a2, &b2, &c2);

    // Solve the equations
    solve_equations(a1, b1, c1, a2, b2, c2);

    return 0;
}

