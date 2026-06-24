class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = defaultdict(int)
        for num in hand:
            count[num] += 1
        hand.sort()
        for num in hand:
            if count[num]:
                for i in range(num, num+groupSize):
                    if not count[i]:
                        return False
                    count[i] -= 1
        return True