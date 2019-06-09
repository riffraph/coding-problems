# given a integer k and a string s, find the length of the longest substring that contains at most k distinct characters
# e.g. given s = "abcba" and k = 2, ths longest substring with k distinct characters is "bcb"

class Substr:
    def __init__(self, k, chars):
        self.k = k
        self.chars = chars.copy()
        self.substr = ''.join(chars)

    def addChar(self, char):
        if not (char in self.chars):
            raise(f'char:{char} not in chars: {self.chars}')

        self.substr = self.substr + char


def findSubstr(string, k):
    longestLen = 0
    longestSubstr = None
    currSubstr = None
    buffer = []
    for char in string:
        buffer.append(char)

        if len(buffer) > k: 
            buffer = buffer[1:]

        if len(buffer) == k:
            if currSubstr is None:
                currSubstr = Substr(k, buffer)
                longestLen = len(currSubstr.substr)
                longestSubstr = currSubstr.substr

            else:
                # add to the substr if the characters haven't changed
                if char in currSubstr.chars:
                    currSubstr.addChar(char)

                # start a new substr and update longest substr
                else:
                    if len(currSubstr.substr) > longestLen:
                        longestLen = len(currSubstr.substr)
                        longestSubstr = currSubstr.substr

                    currSubstr = Substr(k, buffer)

    return longestSubstr


def test_1():
    s = 'abcba'
    k = 2
    assert(findSubstr(s, k) == 'bcb')

test_1()


def test_2():
    s = 'cgbaat'
    k = 3
    assert(findSubstr(s, k) == 'gbaa')

test_2()
