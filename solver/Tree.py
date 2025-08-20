class Tree:
    def __init__(self, value):
        self.value = value
        self.childs = {}
    
    def getChilds(self):
        return self.childs.values()
    
    def addChild(self, key, child):
        self.childs[key] = child
    
    def haveChild(self, key):
        return key in self.childs.keys()