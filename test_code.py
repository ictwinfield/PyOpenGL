vertices = (
    (1, 2, 3),
    (3, 6, 7),
    (1, 5, 9),
    (-5, 6, 9)
)

print(vertices)

vs = []

for v in vertices:
    vs.append(tuple(i * 2 for i in v))

print(tuple(vs))