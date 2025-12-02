from collision import isCorrectRect
from collision import isCollisionRect
from collision import intersectionAreaRect
from collision import intersectionAreaMultiRect
rectangles=[
    [(-3, 1), (9, 10)],
    [(-7, 0), (3, 12)],
    [(0, 0), (5, 5)],
    [(2, 2), (7, 7)]
]

print(intersectionAreaMultiRect(rectangles))