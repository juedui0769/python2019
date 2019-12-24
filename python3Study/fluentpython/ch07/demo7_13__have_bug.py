# 7-13
def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        count += 1
        total += new_value
        return total / count

    return averager

if __name__ == '__main__':
    avg = make_averager()
    # UnboundLocalError: local variable 'count' referenced before assignment
    avg(10)