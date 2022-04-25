gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]


gdict = {}

idx = 0
for g in set(gems):
    gdict[g] =  2**idx
    idx += 1

tree = []