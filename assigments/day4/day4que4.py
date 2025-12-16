def histogram(numbers):
    for n in numbers:
        print('*' * n)

# Input from user
lst = list(map(int, input("Enter integers separated by space: ").split()))

# Function call
histogram(lst)
