import sys

input = [l.strip() for l in open(sys.argv[1]).readlines()]

# Parse the input into a list of (start, end) tuples
section_assignments = []
for assignment in input:
  start, end = map(int, assignment.split('-'))
  section_assignments.append((start, end))

# Keep track of the number of pairs with a fully contained assignment
num_overlapping_pairs = 0

# Iterate over all pairs of section assignments
for i in range(len(section_assignments)):
  for j in range(i + 1, len(section_assignments)):
    # Check if one assignment fully contains the other
    if (section_assignments[i][0] <= section_assignments[j][0] and
        section_assignments[i][1] >= section_assignments[j][1]):
      num_overlapping_pairs += 1
    elif (section_assignments[i][0] >= section_assignments[j][0] and
          section_assignments[i][1] <= section_assignments[j][1]):
      num_overlapping_pairs += 1

# Print the result
print(num_overlapping_pairs)