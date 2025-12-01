def isCorrectRect(dots):
    x1,y1=dots[0]
    x2,y2=dots[1]
    if x1>x2 or y1>y2:
        return False
    else:
        return True
