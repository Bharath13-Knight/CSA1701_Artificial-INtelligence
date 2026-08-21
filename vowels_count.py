text = input("Enter a string: ")
print("Number of vowels:", sum(c in "aeiouAEIOU" for c in text))
