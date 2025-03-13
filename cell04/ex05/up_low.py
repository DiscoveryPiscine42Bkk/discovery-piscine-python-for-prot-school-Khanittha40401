A = input()
B = ''

for i in A:
  if i.islower():
    B += i.upper()
  else:
    B += i.lower()

print(B)