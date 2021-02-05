# singles = []
# doubles = []
# triples = []
#
# for i in range(0,21):
#     singles.append(i)
#     doubles.append(i*2)
#     triples.append(i*3)
# num = 2
# allPossibleVals = []
# for s in singles:
#     for d in doubles:
#         for t in triples:
#             allPossibleVals.append(s+t+d)
#
#
# for s in singles:
#     for d in singles:
#         for t in singles:
#             allPossibleVals.append(s+t+d)
#
# for s in doubles:
#     for d in doubles:
#         for t in doubles:
#             allPossibleVals.append(s+t+d)
#
# for s in triples:
#     for d in triples:
#         for t in triples:
#             allPossibleVals.append(s+t+d)
#
# memo = []
# vals = []
# counter = 0
# for x in range(0,181):
#     if x not in allPossibleVals:
#         counter += 1
#         vals.append(x)
# print(vals)
# print(counter)
#
