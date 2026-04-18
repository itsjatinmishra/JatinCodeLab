# def fizzBuzz(n):

n = int(input("Enter the value of n: "))


result = []
for i in range(n):
    value = i + 1
    if value % 3 == 0:
        result.append("Fizz")
    elif value % 5 == 0:
        result.append("Buzz")
    elif value % 3 == 0 and value % 5 == 0:
        result.append("FizzBuzz")
    else:
        iteration_str = str(value)
        result.append(iteration_str)

print(result)