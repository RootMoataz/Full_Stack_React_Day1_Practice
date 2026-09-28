def isPalindrome(input: str) -> bool:
    # Start one pointer at the beginning and one at the end
    left = 0
    right = len(input) - 1

    # Keep going until the pointers meet or cross in the middle
    while left < right:
        # Skip non-alphanumeric characters on the left
        if not input[left].isalnum():
            left += 1
        # Skip non-alphanumeric characters on the right
        elif not input[right].isalnum():
            right -= 1
        # Both are valid, compare them ignoring case
        else:
            if input[left].lower() != input[right].lower():
                return False
            left += 1
            right -= 1

    return True


# Test cases includes the following (input, expected result, what it checks)
test_cases = [
    ("racecar", True, "simple odd-length palindrome"),
    ("abba", True, "simple even-length palindrome"),
    ("hello", False, "simple non-palindrome"),
    ("RaceCar", True, "ignores letter casing"),
    ("A man, a plan, a canal: Panama", True, "ignores spaces and punctuation"),
    ("race a car", False, "non-palindrome with spaces"),
    ("No 'x' in Nixon", True, "mixed case and punctuation"),
    ("12321", True, "digits only"),
    ("12345", False, "digits, not a palindrome"),
    ("a1b2b1a", True, "letters and digits mixed"),
    ("", True, "empty string"),
    ("a", True, "single character"),
    (".,!", True, "only non-alphanumeric characters"),
    ("abo", False, "two different characters"),
]

passed = 0
for text, expected, description in test_cases:
    result = isPalindrome(text)
    status = "PASS" if result == expected else "FAIL"
    if result == expected:
        passed += 1
    print(f"{status} | {description:<35} | input: {text!r:<35} | expected: {expected}, got: {result}")

print(f"\n{passed}/{len(test_cases)} tests passed")
