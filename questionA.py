class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def _print(self):
        return [self.start,self.end]

    def isOverlap(line1,line2):
        case: bool = line1.start < line2.end and line2.start < line1.end
        return case

if __name__ == "__main__":
    line1 = Line(1,5)
    line2 = Line(-1,1)
    
    line3 = Line(2,6)
    line4 = Line(4,5)
  
    print(Line._print(line1),Line._print(line2),Line.isOverlap(line1,line2))
    print(Line._print(line3),Line._print(line4),Line.isOverlap(line3,line4))
