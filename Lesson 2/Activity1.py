# Count the occurrence of vowels in the string entered by the user

# Approach - 1
inputStr = input("Enter the string - ")
vowels = {
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0
    }
    
for c in inputStr:
    if c in vowels:
        vowels[c] += 1
        
print(vowels)
