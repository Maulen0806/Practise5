import re
text = "I love python"
result_1 = re.search(r"\d", text)
result_2 = re.search(r"\s", text)
if result_1:
    print("The string contains digits")
else:
    print("the string DOESN'T contain digit")
if result_2:
    print("String contains a white space character")
else:
    print("String DOESN'T contain a white space character")
