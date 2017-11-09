
class D_Table:

    def __init__(self):
        self.table = []
        self.size = 0 #Størrelsen på listen
        self.num = 0 #Antall elementer i listen [1,2,NONE,NONE] har num=2 og size = 4

    def __str__(self):
        return str(self.table) + "\nSize: " + str(self.size) + "\nAntall: " + str(self.num)


    def insert(self,x):
        if len(self.table) == 0:
            self.table.append(None)
            self.size = 1
        if self.num == self.size:
            extension = [None]*self.size
            self.table += extension
            self.size *= 2
        self.table[self.num] = x
        self.num += 1

table = D_Table()
print(table)
for x in range(1,11):
    table.insert(x)
print(table)
