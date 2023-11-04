class DoubleElement:
    def __init__(self, *lst):
        self.list = lst
        self.cur_index = 0

    def __next__(self):
        if self.cur_index == len(self.list):
            raise StopIteration

        first = self.list[self.cur_index]
        self.cur_index += 1

        if self.cur_index == len(self.list):
            return first, None

        second = self.list[self.cur_index]
        self.cur_index += 1
        
        return first, second

    def __iter__(self):
        return self


def get_pairs():
    for current_pair in d_l:
        print(current_pair)


d_l = DoubleElement(1, 2, 3, 4)
get_pairs()

print()

d_l = DoubleElement(1, 2, 3, 4, 5)
get_pairs()

d_l = DoubleElement()
get_pairs()
