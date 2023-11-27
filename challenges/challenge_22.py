# Ask for a text from the user. Replace all vowels from the text with the character "_" and print the result.
import re


userinp = input("say something I dare you\n")
replacedtxt = userinp.replace('a', '_')

print(replacedtxt)


# vowels = "aeiouAEIOU"
# replacedText2 = ""

# for character in userinp:
#   if character in vowels:
#     replacedText2 = replacedText2 + "_"
#   else:
#     replacedText2 = replacedText2 + character

# print(replacedText2)

replacedtxt2 = re.sub("[aeiouAEIOU]", "_", userinp)
print(replacedtxt2)