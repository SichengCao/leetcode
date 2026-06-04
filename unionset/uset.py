class UnionSet:

    def __init__(self,size):
        self.father = [0]*(size+1)

        for i in range(1,size+1):
            self.father[i] = i

    def find(self,u):
        if u == self.father[u]:
            return u
        self.father[u] = self.find(self.father[u])
        return self.father[u]

    def isSame(self,a,b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return True
        else:
            return False

    def join(self,a,b):
        fa = self.find(a)
        fb = self.find(b)

        if fa == fb:
            return

        # root连root
        self.father[fa] = fb




if __name__ == "__main__":

    us = UnionSet(4)

    us.join(1, 2)
    us.join(1, 3)
    us.join(2, 4)
    us.join(3, 4)

    print(us.isSame(1, 4))   # False

    print(us.father)

