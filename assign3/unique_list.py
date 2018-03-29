class unique_list(list):
    def append(self,n):
        if(n not in self):
            return list.append(self,n)
        else:
            return self
    def extend(self, li):
        l = list(li - (self & li))
        return list.extend(self,l)
    def insert(self, n , m):
        if(m not in self):
            return list.insert(n, m)
        else:
            return self
    def __setitem__(self, n, m):
        if (m not in self):
             self[n]=m
