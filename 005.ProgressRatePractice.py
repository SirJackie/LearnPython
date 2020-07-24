lastScore = input("Please input your score on last examination:")
thisScore = input("Please input your score on this examination:")
lastScore = float(lastScore)
thisScore = float(thisScore)

print("Last Score:", lastScore)
print("This Score:", thisScore)
print("Progressed?", thisScore > lastScore)
print("Progressing Rate is %.5f %%." % ((thisScore-lastScore) / lastScore * 100))
