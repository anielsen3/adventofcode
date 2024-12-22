import sys

def find_start_of_packet(data, marker_length):
  # Initialize the previous characters to None
  prev_chars = [None] * marker_length

  # Iterate through the data one character at a time
  for i in range(len(data)):
    # Get the current character
    curr_char = data[i]

    # Check if the previous characters are all different
    all_different = True
    for j in range(marker_length):
      if prev_chars[j] == curr_char:
        all_different = False
        break

    if all_different:
      # If they are, return the index of the current character
      return i

    # Update the previous characters
    prev_chars = prev_chars[1:] + [curr_char]

  # If no start-of-packet marker was found, return -1
  return -1


data = open(sys.argv[1]).read()
data = "abcdefghijk"

print(find_start_of_packet(data, 4))