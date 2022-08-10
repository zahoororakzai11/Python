"""
def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count

filename = input("Enter a filename: ")
with open(filename) as f:
    text = f.read()

print(count_char(text, "t"))"""

list = [55,44,33,22,11]
print(list[:2])