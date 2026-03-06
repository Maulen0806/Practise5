import re
text = "I love python"
result_1 = re.findall("l.*e", text)
result_2 = re.findall("Ronaldo", text)
print(result_1)
print(result_2)
