
# test (e**(-3*(x**2)))*(cos(4*x)) -2<x<4 n=4
# test e^(x^2)  1<3<  n=8
# 3x-x**2 0<3 n=3
#(e^(-2*x))*(sin(4*x)) 0<4 n=4
# Question #3
import math

def parse_function(expression):
    expression = expression.replace('^', '**')
    expression = expression.replace('sin', 'math.sin')
    expression = expression.replace('cos', 'math.cos')
    expression = expression.replace('tan', 'math.tan')
    expression = expression.replace('log', 'math.log')
    expression = expression.replace('sqrt', 'math.sqrt')
    expression = expression.replace('pi', 'math.pi')
    expression = expression.replace('e', 'math.e')
    return expression

def differentiate_twice(f, x, h=1e-5):
    return (f(x + 2*h) - 2*f(x + h) + f(x)) / (h**2)

def differentiate_four_times(f, x, h=1e-5):
    return (f(x + 4*h) - 4*f(x + 3*h) + 6*f(x + 2*h) - 4*f(x + h) + f(x)) / (h**4)

def trapezoidal_rule(f, a, b, n):
    delta_x = (b - a) / n
    integral = (f(a) + f(b)) / 2
    for i in range(1, n):
        integral += f(a + i * delta_x)
    integral *= delta_x
    return integral

def simpsons_rule(f, a, b, n):
    if n % 2 != 0:
        print("Error: Simpson's rule requires an even number of subintervals.")
        return None
    delta_x = (b - a) / n
    integral = f(a) + f(b)
    for i in range(1, n):
        integral += 4 * f(a + i * delta_x) if i % 2 != 0 else 2 * f(a + i * delta_x)
    integral *= delta_x / 3
    return integral

def truncation_error(rule, a, b, n, fourth_derivative_max=None, second_derivative_max=None):
    if rule == 'Trapezoidal':
        error_bound = ((b - a)**3 / (12 * n**2)) * second_derivative_max
    elif rule == 'Simpson':
        error_bound = ((b - a)**5 / (180 * n**4)) * fourth_derivative_max
    return error_bound

def main():
    print("Welcome to the Numerical Integration Program")

    f_input = input("Enter the function f(x):  ")
    f = lambda x: eval(parse_function(f_input))

    a_str = input("Enter the lower bound of the interval (a): ")
    a = math.pi if a_str.lower() == 'pi' else math.e if a_str.lower() == 'e' else float(a_str)

    b_str = input("Enter the upper bound of the interval (b): ")
    b = math.pi if b_str.lower() == 'pi' else math.e if b_str.lower() == 'e' else float(b_str)

    n = int(input("Enter the number of subintervals (n): "))

    print("\nChoose integration method:")
    print("1. Trapezoidal rule")
    print("2. Simpson's rule")
    method = int(input("Enter your choice (1 or 2): "))

    if method == 1:
        integral = trapezoidal_rule(f, a, b, n)
        rule_name = "Trapezoidal"
        second_derivative_max = max(abs(differentiate_twice(f, x)) for x in [a, b])
    elif method == 2:
        integral = simpsons_rule(f, a, b, n)
        rule_name = "Simpson"
        fourth_derivative_max = max(abs(differentiate_four_times(f, x)) for x in [a, b])

    if integral is not None:
        print("\nIntegral using", rule_name, "rule:")
        print("Interval (a, b):", (a, b))
        print("Number of subintervals (n):", n)
        print(rule_name, ":", integral)

        # Calculate truncation error and display it
        error = truncation_error(rule_name, a, b, n, fourth_derivative_max if method == 2 else None, second_derivative_max if method == 1 else None)
        if error is not None:
            print("Truncation error bound:", error)

if __name__ == "__main__":
    main()
