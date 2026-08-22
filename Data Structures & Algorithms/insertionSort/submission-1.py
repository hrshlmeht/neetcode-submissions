# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if len(pairs)==0:
            return pairs
        listofsequence=[pairs]
        sorted=[Pair(-1,-1)]+[pairs[0]]
        for pair_index in range(1,len(pairs)):
            for i in range(len(sorted)-1,-1,-1):
                if(pairs[pair_index].key>=sorted[i].key):
                    sorted.insert(i+1,pairs[pair_index])
                    break
            listofsequence.append(sorted[1:]+pairs[pair_index+1:])
        return listofsequence      