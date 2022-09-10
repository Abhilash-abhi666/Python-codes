stats = {100:3,40:2,25:22,105:2}
a=max(stats.items(), key = lambda x: x[0])
print(a)