#encoding:utf-8

n = 4
if n>3:
    print "bigger"

s="啦啦啦"
print s
#s.decode("ascii").encode("utf8")

fDict = {}.fromkeys(('id','score'),(1,2))
print fDict
for key in fDict.keys():
    print key
for value in fDict.values():
    print value

items = [('name','Mike'),('age','20')]
itemDict = dict(items)
print items
print itemDict

list = (['name','Mike'],['age','020'])
ddict = dict(list)
print list
print ddict

print ddict.get('age')
dddd = {'password':012}
print dddd.get('password')
print itemDict['name']


firstSet = set([3, 4, 5])
secondset =set([1,2,3])
print firstSet | secondset
print firstSet & secondset
print firstSet - secondset
firstset = set(['string','lalala'])
print firstset

print [x+2 for x in range(6) if x%2]

if 9>6:
    pass
    print "laala"

print (int)("123")

# def lalala(fun):
#     print ";akfjk"
#
# @lalala
# def ooo():
#     ooo.uuu="ladfljgadlkjaldj"
#     print "aksjfklj"
#
# ooo()


class people():
    def __init__(self,name,hair,height):  #子函数有多一个初始化掉不道父函数的self
        self.name=name
        self.hair="hair"
    def gethair(self):
        return self.hair

ppp = people('tom','black','12')
print ppp.gethair()
print ppp.hair

class boy(people):
    def __init__(self):
        self.hobby = "hobby"
        self.hair ="hari"

lll = boy()
print lll.gethair()

with open('/home/qin/下载/t2.txt','a') as writeFile:  #这个地方‘a'是追加’w‘是覆盖
    writeFile.write('success\n')

# with open('/home/qin/下载/t2.txt') as file:
#     for line in file.readline():
#         print line.strip()
with open('/home/qin/下载/t2.txt') as file:
    for line in file.readlines():
        print line