import re
text = "Pi is equal to 2..."
result_1 = re.sub(r"\d", "3.14", text)
print(result_1)
