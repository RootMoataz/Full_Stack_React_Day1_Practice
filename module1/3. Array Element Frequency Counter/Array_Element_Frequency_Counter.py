def countFrequencies(arr: list[int], show_output: bool = True) -> list[tuple[int, int]]:
    # Two parallel lists: values[i] is a distinct number, counts[i] shows how many times the distinct number has appeared in our parrell list.
    values = []
    counts = []

    # Go through every number in the input
    for num in arr:
        found = False

        # Search the numbers we've already seen
        for i in range(len(values)):
            if values[i] == num:
                counts[i] += 1   # Seen before, so add 1 to its count
                found = True
                break            # Stop searching, we have found it

        # First time seeing this number, so add it with a count of 1
        if not found:
            values.append(num)
            counts.append(1)

    # Output the count of each distinct element
    if show_output:
        for i in range(len(values)):
            print(f"{values[i]} appears {counts[i]} time(s)")

    # Also return the results as (value, count) pairs so they can be tested
    return [(values[i], counts[i]) for i in range(len(values))]


# The task at hand, is to process an array and output the count of each distinct element
print("Example output for [4, 2, 4, 7, 2, 4]:")
countFrequencies([4, 2, 4, 7, 2, 4])


# Test cases includes the following (input, expected result, what it checks)
test_cases = [
    ([4, 2, 4, 7, 2, 4], [(4, 3), (2, 2), (7, 1)], "basic mix of repeats"),
    ([1, 2, 3, 4], [(1, 1), (2, 1), (3, 1), (4, 1)], "all distinct"),
    ([5, 5, 5, 5], [(5, 4)], "all the same"),
    ([], [], "empty array"),
    ([9], [(9, 1)], "single element"),
    ([-1, -1, 3, -1], [(-1, 3), (3, 1)], "negative numbers"),
    ([0, 0, 1, 0], [(0, 3), (1, 1)], "zeros"),
    ([3, 1, 3, 2, 1], [(3, 2), (1, 2), (2, 1)], "keeps first-appearance order"),
    ([1000000, 1000000], [(1000000, 2)], "large numbers"),
]

print("\nRunning tests:")
passed = 0
for arr, expected, description in test_cases:
    result = countFrequencies(arr, show_output=False)
    status = "PASS" if result == expected else "FAIL"
    if result == expected:
        passed += 1
    print(f"{status} | {description:<35} | input: {arr!r:<35} | expected: {expected}, got: {result}")

print(f"\n{passed}/{len(test_cases)} tests passed")