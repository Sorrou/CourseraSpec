mal = [str(num) for num in input()]
print(mal)

print(list(zip(
  filter(bool, range(3)),
  [x for x in range(3) if x]
)))
