# Approach - 2
inputStr = input("Enter the string - ")
vowelsList = []
vowels = {}

for c in inputStr:
    if c in vowelsList:
        if c in vowels:
            vowels[c] += 1
        else:
            vowels[c] = 1
            
print(vowels)
