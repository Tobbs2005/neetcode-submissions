class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        for i, triplet in enumerate(triplets):
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                del triplets[i]
        
        res = [False] * 3
        for triplet in triplets:
            for i in range(3):
                if triplet[i] == target[i]:
                    res[i] = True
        return all(res)