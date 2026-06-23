class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # find the pivot of the smaller array

        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A
        
        # swap arrays so A is smaller

        l = 0
        r = len(A)-1

        while True:
            i = (l+r)//2
            j = half - i - 2 # not sure

            Aleft = A[i] if i >= 0 else -float("inf")
            Aright = A[i+1] if i + 1 < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else -float("inf")
            Bright = B[j+1] if j + 1 < len(B) else float("inf")

            correct = (Aleft <= Bright and Bleft <= Aright)
            if correct:
                if total % 2 == 1:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

