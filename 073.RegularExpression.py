import re

#
# Because Regular Expressions often includes "\",
# Escape will becomes a problem.
#

# Example :
print("\\d")  # Result : \d

# Use r"" will be better
print(r"\d")  # Result : \d

# # #
# # # Regular Expression Rule
# # #


#
# Metacharacters
#

# Use | to match 2 or more atoms
print(re.match(r"Duang|duang", "Duang"))   # Matched
print(re.match(r"Duang|duang", "duang"))   # Matched
print(re.match(r"Duang|duang", "DUANG"))   # Not Matched
print(re.match(r"A|B|C", "A"))             # Matched
print(re.match(r"A|B|C", "B"))             # Matched
print(re.match(r"A|B|C", "C"))             # Matched
print(re.match(r"A|B|C", "D"))             # Not Matched

# Use [] to match any atom inside it
print(re.match(r"[1234567890]", "5"))      # Matched
print(re.match(r"[qwerty]", "q"))          # Matched
print(re.match(r"[0-9]", "5"))             # Matched
print(re.match(r"[0-9]", "q"))             # Not Matched

# Use [^] to match any atom NOT inside it
print(re.match(r"[^qwe]", "a"))            # Matched
print(re.match(r"[^qwe]", "b"))            # Matched
print(re.match(r"[^qwe]", "q"))            # Not Matched
print(re.match(r"[^qwe]", "w"))            # Not Matched
print(re.match(r"[^qwe]", "e"))            # Not Matched

# Use . to match any atom except "\n"
print(re.match(r".", "a"))                 # Matched
print(re.match(r".", "1"))                 # Matched
print(re.match(r".", ":"))                 # Matched
print(re.match(r".", "\r"))                # Matched
print(re.match(r".", "\n"))                # Not Matched

# Use \d to match a digit
print(re.match(r"\d", "0"))                # Matched
print(re.match(r"\d", "a"))                # Not Matched

# Use \D to match a NOT digit atom
print(re.match(r"\D", "a"))                # Matched
print(re.match(r"\D", ":"))                # Matched
print(re.match(r"\D", "0"))                # Not Matched

# Use \s to match a unvisitable atom
print(re.match(r"\s", " "))                # Matched
print(re.match(r"\s", "\n"))               # Matched
print(re.match(r"\s", "\r"))               # Matched
print(re.match(r"\s", "\t"))               # Matched
print(re.match(r"\s", "a"))                # Not Matched

# Use \S to match a NOT unvisitable atom
print(re.match(r"\S", "a"))                # Matched
print(re.match(r"\S", "b"))                # Matched
print(re.match(r"\S", "c"))                # Matched
print(re.match(r"\S", "\n"))               # Not Matched

# Use \w to match a digit, letter or underline (= [0-9A-Za-z_] )
print(re.match(r"\w", "a"))                # Matched
print(re.match(r"\w", "0"))                # Matched
print(re.match(r"\w", "_"))                # Matched
print(re.match(r"\w", ":"))                # Not Matched
print(re.match(r"\w", "\n"))               # Not Matched

# Use \W to match a atom except digit, letter or underline
print(re.match(r"\W", ":"))                # Matched
print(re.match(r"\W", "\n"))               # Matched
print(re.match(r"\W", "a"))                # Not Matched
print(re.match(r"\W", "0"))                # Not Matched
print(re.match(r"\W", "_"))                # Not Matched


#
# Quantifiers
#

# {n} indicates the preceding atom occurs n times
print(re.match(r"\d{5}", "12345"))         # Matched
print(re.match(r"\d{5}", "67890"))         # Matched
print(re.match(r"\d{5}", "1234"))          # Not Matched

# {n,m} indicates the preceding atom occurs n to m times
print(re.match(r"\d{3,5}", "123"))         # Matched
print(re.match(r"\d{3,5}", "1234"))        # Matched
print(re.match(r"\d{3,5}", "12345"))       # Matched
print(re.match(r"\d{3,5}", "12"))          # Not Matched

# * indicated the preceding atom occurs 0, 1 or more time
print(re.match(r"\d*", ""))                # Matched
print(re.match(r"\d*", "1"))               # Matched
print(re.match(r"\d*", "123"))             # Matched

# + indicated the preceding atom occurs 1 or more times
print(re.match(r"\d+", "1"))               # Matched
print(re.match(r"\d+", "123"))             # Matched
print(re.match(r"\d+", ""))                # Not Matched

# ? indicated the preceding atom occurs 0 or 1 times
print(re.match(r"\d?", ""))                # Matched
print(re.match(r"\d?", "1"))               # Matched


#
# Border Control
#

# ^n can make sure the string start with n
print(re.match(r"^J", "John"))             # Matched
print(re.match(r"^J", "Jackson"))          # Matched
print(re.match(r"^John", "John"))          # Matched
print(re.match(r"^J", "AJ"))               # Not Matched

# m$ can make sure the string end with m
print(re.search(r"s$", "Apples"))          # Matched
print(re.search(r"s$", "Tomatoes"))        # Matched
print(re.search(r"s$", "Hello"))           # Not Matched


#
# Model Unit
#

# Use () to wrap an expression
print(re.match(r"(P|p)ython", "Python"))   # Matched
print(re.match(r"(P|p)ython", "python"))   # Not Matched


#
# Escape
#

# Escape when using atoms with special meaning
print(re.match(r"\-", "-"))                # Matched


# # #
# # # Functions for Regular Expression
# # #


#
# Differences Between re.match() and re.search()
#

# re.match Match the String from scratch
print(re.match(r"s$", "Apples"))         # Not Matched
print(re.match(r"\w*s$", "Apples"))      # Matched "Apples"

# re.search() Match the String at any places
print(re.search(r"s$", "Apples"))        # Matched "s"


#
# Use re.split() to split the string easily
#

# str.split() can't work when it have multi spaces
print("a b   c".split(" "))              # Result : ['a', 'b', '', '', 'c']

# Use re.split() instead
print(re.split(r"\s+", "a b   c"))       # Result : ['a', 'b', 'c']

# More complex situation
print(re.split(r"[\s;,]+", "a,b;;  c"))  # Result : ['a', 'b', 'c']


#
# Group
#

# Use () to create a group
result = re.match(r"(\d{0,3})(\d{0,3})(\d*)", "1234567890")
print(result)  # Result : <re.Match object; span=(0, 10), match='1234567890'>
print(result.group(0))  # Result : 1234567890
print(result.group(1))  # Result : 123
print(result.group(2))  # Result : 456
print(result.group(3))  # Result : 7890
print(result.groups())  # Result : ('123', '456', '7890')


#
# Greed Match
#

# Because of the Greed Match, the (\d+) robbed all the numbers
print(re.match(r"^(\d+)(0*)$", "1234000").groups())
# Result : ('1234000', '')

# Use ? to let (\d+) not to do Greed Match
print(re.match(r"^(\d+?)(0*)$", "1234000").groups())
# Result : ('1234', '000')


#
# Compile the Regular Expression
#

re_telephone = re.compile(r"(\d{3})-(\d{1,8})")
print(re_telephone.match("010-12345").groups())  # Result : ('010', '12345')
print(re_telephone.match("010-8086").groups())   # Result : ('010', '8086')
