# Count the occurrence of each alphabhet in the string entered by the user

inputStr = input("Enter the string - ")
charCount = {}

for c in inputStr:
    if c is alpha():
        if c in charCount:
            charCount[c] += 1
        else:
            charCount = 1
            
print(charCount)