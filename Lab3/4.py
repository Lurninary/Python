class DefaultList(list):
    def __init__(self, default_val):
        super().__init__()
        self.default = default_val


    def __getitem__(self, item):
        try:
            return list.__getitem__(self, item)

        except:
            return self.default

s = DefaultList(5)
s.extend([4, 10])
indexes = [1, 124, 1882]
for i in indexes:
    print(s[i], end=" ")

print("\n")

s = DefaultList(51)
s.extend([1, 5, 7])
indexes = [0, 2, 1000, -1]
for i in indexes:
    print(s[i], end=" ")
