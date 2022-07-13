class Operations:
    def _sum(self, _list):
        sum = 0
        for i in _list:
            sum += i
        return sum


s = Operations()
mysum = s._sum