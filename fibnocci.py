def fibonacci(n):
    fib_series = [0, 1]  # Initializing the series with first two numbers
    for i in range(2, n):
        fib_series.append(fib_series[i-1] + fib_series[i-2])  # Adding the last two numbers
    return fib_series[:n]  # Return only the required number of elements

# Input from user
n = int(input("Enter the number of terms: "))
print("Fibonacci Series:", fibonacci(n))