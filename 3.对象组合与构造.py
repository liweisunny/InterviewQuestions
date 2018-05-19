#__author:liwei
#date:2017/2/23

class Node(object):
    def __init__(self,sName):
        self._lChildren = []
        self.sName = sName

    def __repr__(self):
        return "<Node '{}'>".format(self.sName)

    def append(self,*args,**kwargs):
        self._lChildren.append(*args,**kwargs)

    def print_all_1(self):
        print (self)
        for oChild in self._lChildren:
            oChild.print_all_1()

    def print_all_2(self):
        def gen(o):
            lAll = [o]
            while lAll:
                oNext = lAll.pop(0)
                lAll.extend(oNext._lChildren)
                yield oNext
        for oNode in gen(self):
            print (oNode)

oRoot = Node("root")
oChild1 = Node("child1")
oChild2 = Node("child2")
oChild3 = Node("child3")
oChild4 = Node("child4")
oChild5 = Node("child5")
oChild6 = Node("child6")
oChild7 = Node("child7")
oChild8 = Node("child8")
oChild9 = Node("child9")
oChild10 = Node("child10")

oRoot.append(oChild1)
oRoot.append(oChild2)
oRoot.append(oChild3)
oChild1.append(oChild4)
oChild1.append(oChild5)
oChild2.append(oChild6)
oChild4.append(oChild7)
oChild3.append(oChild8)
oChild3.append(oChild9)
oChild6.append(oChild10)

oRoot.print_all_1()

# 执行结果：

    # <Node 'root'>
    # <Node 'child1'>
    # <Node 'child4'>
    # <Node 'child7'>
    # <Node 'child5'>
    # <Node 'child2'>
    # <Node 'child6'>
    # <Node 'child10'>
    # <Node 'child3'>
    # <Node 'child8'>
    # <Node 'child9'>

oRoot.print_all_2()

# 执行结果：
    # <Node 'root'>
    # <Node 'child1'>
    # <Node 'child2'>
    # <Node 'child3'>
    # <Node 'child4'>
    # <Node 'child5'>
    # <Node 'child6'>
    # <Node 'child8'>
    # <Node 'child9'>
    # <Node 'child7'>
    # <Node 'child10'>

# 说明：

# 对象的精髓就在于组合（composition）与对象构造（object construction）。对象需要有组合成分构成，而且得以某种方式初始化。这里也涉及到递归和生成器（generator）的使用。

# 生成器是很棒的数据类型。你可以只通过构造一个很长的列表，然后打印列表的内容，就可以取得与print_all_2类似的功能。生成器还有一个好处，就是不用占据很多内存。

# 有一点还值得指出，就是print_all_1会以深度优先（depth-first）的方式遍历树(tree),而print_all_2则是宽度优先（width-first）。

# 有时候，一种遍历方式比另一种更合适。但这要看你的应用的具体情况