#ifndef LINEAR_H
#define LINEAR_H

#include <stdio.h>

// Function to take input for coefficients
void input_equations(float *a1, float *b1, float *c1, float *a2, float *b2, float *c2) {
    printf("Enter coefficients of first equation (a1 b1 c1): ");
    scanf("%f %f %f", a1, b1, c1);
    printf("Enter coefficients of second equation (a2 b2 c2): ");
    scanf("%f %f %f", a2, b2, c2);
}

// Function to compute determinant
float determinant(float a1, float b1, float a2, float b2) {
    return (a1 * b2) - (a2 * b1);
}

// Function to solve equations
void solve_equations(float a1, float b1, float c1, float a2, float b2, float c2) {
    float det = determinant(a1, b1, a2, b2);

    if (det == 0) {
        printf("The equations have no unique solution (parallel or coincident lines).\n");
    } else {
        float x = (c1 * b2 - c2 * b1) / det;
        float y = (a1 * c2 - a2 * c1) / det;
        printf("Solution: x = %.2f, y = %.2f\n", x, y);
    }
}

#endif

