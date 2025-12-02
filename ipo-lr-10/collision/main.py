
def isCorrectRect(dots):
    x1,y1=dots[0]
    x2,y2=dots[1]
    if x1>x2 or y1>y2:
        return False
    else:
        return True
    
class RectCorrectError(Exception):
    pass 

def isCollisionRect(dots1,dots2):
    if not isCorrectRect(dots1):
        raise RectCorrectError("1й прямоугольник некоректный")
    elif not isCorrectRect(dots2):
        raise RectCorrectError("2й прямоугольник некоректный")
    else:
        x1,y1=dots1[0]
        x2,y2=dots1[1]
        x3,y3=dots2[0]
        x4,y4=dots2[1]
        if (x1>=x4 or x2<=x3)or (y1>=y4 or y2<=y3):
            return False
        else:
            return True
        


