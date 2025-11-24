## week 10
# binary search tree'yi tekrardan yaptık. sınavda yapamamışız diyeymiş 
class Node:
    def __init__(self, name, score:int, lesson):
        self.name = name
        self.score = score
        self.lesson = lesson
        self.left = None
        self.right = None

    def pirint(self):
        print(self.name, self.score, self.lesson)

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, name, score, lesson):
        new = Node(name, score, lesson)
        parent = None
        current = self.root

        while current is not None:  ##yani root var olduğu sürece
            parent = current
            if score < current.score:  # şu anki öğrencinin sınav notu roottakinden küçükse
                current = current.left
            else:  # küçük değilse eşit de olabilir ama biz eşit olma olasılığını şimdi değerlendirmiyoruz
                current = current.right
            current = new

        if parent is None:
            self.root = new
        elif score < parent.score:
            parent.left = new
        else:
            parent.right = new





notlar = Tree()
o1 = Node("k", 100, "data")
o2 = Node("y", 70, "data")
o3 = Node("b", 90, "data")
notlar.insert(o1, o2, o3)
o1.pirint()