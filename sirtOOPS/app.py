# class Operations:
#     __count = 0

#     def __init__(self, n, m):
#         self.__n = n
#         self.__m = m
#         Operations.__count += 1

#     # def show(self):
#     #     return f"{self.__n}, {self.__m}"

#     def __str__(self):
#         return f"{self.__n}, {self.__m}"

#     @classmethod
#     def showcount(cls):
#         return cls.__count


# s = Operations(12, 34)
# i = Operations(3, 66)
# print(Operations.showcount())
# print(s)


# from MyOp.Operations import mysum
# print(sum([1, 2, 3, 4, 5]))
# print(mysum([1, 2, 3, 4, 5]))


class A:
    def __init__(self):
        pass

    def __str__(self):
        return "Helooooo"

    def show_a():
        return "This is A class"


class B(A):
    pass


r = B()
r.show_a()

# z = A()
# print(z)
