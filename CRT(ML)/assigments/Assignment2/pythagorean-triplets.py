def generate_pythagorean_triplets(limit):
    triplets = [
        (a, b, c)
        for a in range(1, limit + 1)
        for b in range(a, limit + 1)
        for c in range(b, limit + 1)
        if a * a + b * b == c * c
    ]
    return triplets


limit = 50
pythagorean_triplets = generate_pythagorean_triplets(limit)

print(f"Pythagorean Triplets (a, b, c) where a, b, c <= :" + str(limit))
for triplet in pythagorean_triplets:
    print(triplet)

print(f"\nTotal number of triplets found: {len(pythagorean_triplets)}")