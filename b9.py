def jaccard_similarity(s1, s2):
    # Split strings into sets of words
    set1 = set(s1.strip().split())
    set2 = set(s2.strip().split())

    # Calculate intersection and union
    intersection = set1 & set2
    union = set1 | set2

    # Compute similarity with 6 decimal precision
    similarity = len(intersection) / len(union) if union else 1.0
    return f"{similarity:.6f}"

# Ask user for input from terminal
print("Enter the first string:")
s1 = input()

print("Enter the second string:")
s2 = input()

# Calculate and print result
print(jaccard_similarity(s1, s2))
