# The Bag Abstract Data Type

class Bag:
    """
    The Bag Abstract Data Structure:
    A container that stores a collection in which duplicate values
    are allowed.
    """

    def __init__(self):
        self.bagItems = []
        return

    def length(self):
        return len(self.bagItems)

    def contains(self, item):
        return item in self.bagItems

    def add(self, item):
        return self.bagItems.append(item)

    def remove(self, item):
        if item in self.bagItems:
            return self.bagItems.remove(item)
        else:
            return "{item} is not in the bag"

    def __iter__(self):
        return BagIterator(self.bagItems)


class BagIterator:
    def __init__(self, listobject):
        self.listobject = listobject
        self.cur = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur < len(self.listobject):
            item = self.listobject[self.cur]
            self.cur += 1
            return item
        else:
            raise StopIteration


bag = Bag()
bag.add(19)
bag.add(20)
print(bag.length())
print(bag.contains(20))
for x in bag:
    print(x)
