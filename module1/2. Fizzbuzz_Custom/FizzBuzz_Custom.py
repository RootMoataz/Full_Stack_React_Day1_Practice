def fizzbuzz(number: int) -> str:
    # Check both first, otherwise 15 would stop at "Fizz" and never reach the "FizzBuzz"
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    # % gives the remainder; a remainder of 0 means it divides evenly
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    # Not a multiple of 3 or 5, so return the number itself as text
    else:
        return str(number)


# The task we have at hand: Loop from 1 to 50 and print the result for each number
# range(1, 51) stops BEFORE the 51th step, so it can include the 50th step at the end
print("FizzBuzz from 1 to 50:")
for i in range(1, 51):
    print(fizzbuzz(i))


# Test cases includes the following (input, expected result, what it checks)
test_cases = [
    (1, "1", "plain number"),
    (2, "2", "plain number"),
    (3, "Fizz", "first multiple of 3"),
    (5, "Buzz", "first multiple of 5"),
    (9, "Fizz", "multiple of 3 only"),
    (10, "Buzz", "multiple of 5 only"),
    (15, "FizzBuzz", "first multiple of both"),
    (30, "FizzBuzz", "multiple of both"),
    (45, "FizzBuzz", "last multiple of both in range"),
    (49, "49", "plain number near the end"),
    (50, "Buzz", "last number in range"),
]

print("\nRunning tests:")
passed = 0
for number, expected, description in test_cases:
    result = fizzbuzz(number)
    status = "PASS" if result == expected else "FAIL"
    if result == expected:
        passed += 1
    print(f"{status} | {description:<35} | input: {number!r:<35} | expected: {expected}, got: {result}")

print(f"\n{passed}/{len(test_cases)} tests passed")