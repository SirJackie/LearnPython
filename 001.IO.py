# Print Function
print("Hello World!")
print("The quick brown fox", "jumps over", "the lazy dog")
print("1024 X 768 =", 1024 * 768)

# Input Function
sentence = input()
name = input("Please enter your name:")
print(sentence, name)

# Format the String
sentence = "Hi %s, your score is %d." % ("Bart", 59)
print(sentence)  # Result : Hi Bart, your score is 59.

# Format the String With % Inside
sentence = "%d %% Finished." % 59
print(sentence)  # Result : 59 % Finished.

# Format the Int
print("%d"   % 1)  # result:1
print("%2d"  % 1)  # result: 1
print("%02d" % 1)  # result:01

# Format the Float
num = 10/3
print("%.1f" % num)  # 3.3
print("%.2f" % num)  # 3.33
print("%.3f" % num)  # 3.333

# The %s works anytime!
print("%s" % "Hello")
print("%s" % 100)
print("%s" % 0.5)
