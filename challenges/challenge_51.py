# Create a function that receives a string and returns if it's a palindrome (a word that reads the same in reverse)
# Palindrome examples for testing: "madam", "racecar", "radar", "level"

def reverse(text):
    return text[::-1]
def pdrome(x):
    flipped_txt = reverse(x)
    if flipped_txt == x:
        return True
    else:
        return False
    
print(pdrome("hi!!"))
print(pdrome("racecar"))