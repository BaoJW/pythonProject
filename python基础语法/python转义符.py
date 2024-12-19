"""
    python的转义符:
        转义符，即 \+特殊功能的首字符
    1. \n: 换行
    2. \t: 制表符
    3. \r: 覆盖
    4. \b: 删除
    5. \\: 两个反斜线表示一个\
    6. 原字符: 使转义字符不起作用，写在前面，用r或R
"""

print("hello\nworld")
print("hello\tworld")
print("hello\rworld")
print("hello\bworld")
print("hello\\world")
print(r"hello\nworld")
print(R"hello\nworld")