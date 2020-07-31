import subprocess

# Call a External Process
result = subprocess.call(["ping", "www.baidu.com"])
print(result)
print("Exit Code:", result)

# Call a External Process With Input
p = subprocess.Popen(["python"],
                     stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
output, err = p.communicate(b"s=\"Hello Blah\"\nprint(s)\nexit()")
print(output.decode("utf-8"))  # Result : Hello Blah
