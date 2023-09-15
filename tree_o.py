class Arvore_o:
    def _init_(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def _str_(self, level=0):
        ret = "\t" * level + repr(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

