#
# Relation between Int and Char
#

# Char 2 Int -- ord() function
intA = ord('A')
intZhong = ord('中')
print(intA)       # result : 65
print(intZhong)   # result : 20013

# Int 2 Char -- chr() function
charA = chr(65)
charZhong = chr(20013)
print(charA)      # result : A
print(charZhong)  # result : 中

# Use Hexadecimal Int to define a String
unicodeString = "\u4e2d\u6587"
print(unicodeString)  # result : 中文



#
# Relation between Bytes and Char
#

x = "abc"   # This is a string
x = b"abc"  # This is a bytes

# String 2 Bytes -- encode() method
abcASCIIBytes = "abc".encode("ascii")  # English-string 2 ASCII-bytes
abcUTF_8Bytes = "abc".encode("utf-8")  # English-string 2 UTF-8-bytes
# Chinese-string can not turn into ASCII-bytes
ZhongWenUTF_8Bytes = "中文".encode("utf-8")  # Chinese-string 2 UTF-8-bytes

# Bytes 2 String -- decode() method
abcEnglishString = abcASCIIBytes.decode("ascii")  # ASCII-bytes 2 English-string
abcEnglishString = abcUTF_8Bytes.decode("utf-8")  # UTF-8-bytes 2 English-string
# ASCII-bytes can not turn into Chinese-string
ZhongWenChineseString = ZhongWenUTF_8Bytes.decode("utf-8")  # UTF-8-bytes 2 Chinese-string

# Difference between string and bytes measured by len() function
print(len(abcEnglishString))  # len of English-string, result : 3
print(len(abcASCIIBytes))     # len of ASCII-bytes,    result : 3
print(len(abcUTF_8Bytes))     # len of UTF-8-bytes,    result : 3

print(len(ZhongWenChineseString))  # len of Chinese-words, result : 2
print(len(ZhongWenUTF_8Bytes))     # len of UTF-8-bytes,   result : 6


