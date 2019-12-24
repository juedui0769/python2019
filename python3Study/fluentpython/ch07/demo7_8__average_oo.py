# 7-8

class Averager():
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)

if __name__ == '__main__':
    avg = Averager()
    _avg = avg(10)
    print(_avg)
    _avg = avg(11)
    print(_avg)
    _avg = avg(12)
    print(_avg)