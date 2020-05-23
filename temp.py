def pig_latin(text):
    say = []
    words = text.split(" ")
    for word in words:
        say.append(word[1:] + word[0] + "ay")
    return " ".join(say)

print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

# def octal_to_string(octal):
#     result = ""
#     value_letters = [(4,"r"),(2,"w"),(1,"x")]
#     # Iterate over each of the digits in octal
#     for x in [int(n) for n in str(octal)]:
#         # Check for each of the permissions values
#         for value, letter in value_letters:
#             if x >= value:
#                 result += letter
#                 x -= value
#             else:
#                 result += "-"
#     return result
#
# print(octal_to_string(755)) # Should be rwxr-xr-x
# print(octal_to_string(644)) # Should be rw-r--r--
# print(octal_to_string(750)) # Should be rwxr-x---
# print(octal_to_string(600)) # Should be rw-------


# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# newfilenames = []
#
# for i in filenames:
#     temp = i.split(".")
#     if temp[1] == "hpp":
#         newfilenames.append((i, temp[0]+"."+"h"))
#     else:
#         newfilenames.append((i, i))
#
# print (newfilenames) # Should be [('program.c', 'program.c'), ('stdio.hpp', 'stdio.h'), ('sample.hpp', 'sample.h'), ('a.out', 'a.out'), ('math.hpp', 'math.h'), ('hpp.out', 'hpp.out')]
