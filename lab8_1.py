class CombStr():
    """docstring for CombStr"""
    def __init__(self, string):
        self.string = string


    def count_substrings(self, length):
        string = self.string
        subs = []
        if type(length) is not int or length < 0 or length > len(string):
            return False

        if length == 0 :
            return 0

        for i in range(len(string)) :
            sub = string[i:length + i]
            if len(sub) == length :
                subs.append(sub)
        subset = set(subs)
        print(subset)

        count = len(subset)

        return count
