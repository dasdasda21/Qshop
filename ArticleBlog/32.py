import re
string = 'hello\tworld \n I am xiaoming this is 2019 _time_'


# result = re.findall(r"...",string)   #三个字符
#result = re.findall(r"\w",string) 返回所以数字，字母，下滑现
#result = re.findall(r"\W",string)非数字字母下划线
#result = re.findall(r"\d\d",string)两个字符的数字
#result = re.findall(r"\D",string)非数字
#result = re.findall(r"[hl]",string)返回括号中的字符
#result = re.findall(r"[a-zA-Z0-9]",string)返回范围字符
#result = re.findall(r"h|l",string)返回两边的字符
#result = re.findall(r"he|lo|as|cs|ss|12",string)
#result = re.findall(r"h\w",string)h后面跟一个字符
result = re.findall(r"[h(\w)]",string)
# string ="123 323 666 878"
# result = re.findall(r"(\d)\d",string)
# print(result)
# result = re.findall(r"(?P<q>\d)\d(?P=q)",string)






print(result)