# Datas
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# Sort By Name
def by_name(t):
    return t[0]
L2 = sorted(L, key=by_name)
print(L2)  # Result : [('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]

# Sort By Score
def by_score(t):
    return t[1]
L2 = sorted(L, key=by_score)
print(L2)  # Result : [('Bart', 66), ('Bob', 75), ('Lisa', 88), ('Adam', 92)]
