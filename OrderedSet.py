from collections import OrderedDict


class OrderedSet:
    def __init__(self):
        self.items = OrderedDict()

    def add(self, element):
        """Добавляет элемент в множество."""
        self.items[element] = None

    def remove(self, element):
        """Удаляет конкретный элемент из множества.
        Если элемента нет, то поднимает KeyError."""
        try:
            del self.items[element]
        except KeyError:
            raise KeyError(f"Element {element} not found in OrderedSet")

    def __len__(self):
        return self.items.__len__()

    def smallest(self):
        """Возвращает самый маленький элемент в множестве.
        Если множество пусто, возвращает None."""
        if self.items:
            return next(iter(self.items))
        return None

    def pop_smallest(self):
        val = self.smallest()
        if val is not None:
            self.remove(val)
        return val

    def __iter__(self):
        """Позволяет итерироваться по множеству."""
        return iter(self.items)

    def __contains__(self, element):
        """Позволяет использовать оператор `in` для проверки наличия элемента."""
        return element in self.items

    def __repr__(self):
        """Возвращает строковое представление множества."""
        return f"OrderedSet({list(self.items.keys())})"


if __name__ == "__main__":
    d = OrderedDict()
    d["a"] = 1
    d["c"] = 1
    d["b"] = 1
    d["x"] = 1
    print(d)