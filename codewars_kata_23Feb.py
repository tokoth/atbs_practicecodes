# You get an array of numbers, return the sum of all of the positives ones.

# Example [1,-4,7,12] => 1 + 7 + 12 = 20

# Note: if there is nothing to sum, the sum is default to 0.

# My solution


def positive_sum(arr):
    # Check the array is not empty
    if len(arr) > 0:
        sum = 0
        # Sum all the positive values of the array
        for i in arr:
            if i > 0:
                sum += i
        return sum 
    else:
        return 0


# Test
print(positive_sum([1,-4,7,12]))
print(positive_sum([]))

# Write a function `greet` that returns "hello world!"

def greet():
    return 'hello world!'


# Test 
print(greet())