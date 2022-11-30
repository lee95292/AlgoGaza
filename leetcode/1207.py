
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        ndict={}
        udict={}
        for a in arr:
            ndict[a] = ndict[a]+1 if ndict.get(a) else 1
        for a in ndict.values():
            if udict.get(a):
                return False
            else:
                udict[a]=1
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.uniqueOccurrences([1,2,2,1,1,3]))
