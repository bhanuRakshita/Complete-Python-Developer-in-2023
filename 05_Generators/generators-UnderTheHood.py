
#range
class SpecialRange:

    current = 0
    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if SpecialRange.current < self.last:
            num = SpecialRange.current
            SpecialRange.current +=1
            return num
        raise StopIteration
    
gen = SpecialRange(1,10)
print(gen)