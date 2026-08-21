values = list(map(int, input("Enter values: ").split()))
position = 0
while position + 1 < len(values) and values[position + 1] > values[position]: position += 1
print("Peak:", values[position])
