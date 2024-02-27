
class Add:

    def __call__(self, value):
        return sum(value)

a = Add()
total = a([1,2,3,4,5,6])
print(total)