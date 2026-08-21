text = input("Enter the text: ")
pattern = input("Enter the pattern: ")
positions = [i for i in range(len(text) - len(pattern) + 1)
             if text[i:i + len(pattern)] == pattern]
print("Pattern found at positions:", positions if positions else "none")
