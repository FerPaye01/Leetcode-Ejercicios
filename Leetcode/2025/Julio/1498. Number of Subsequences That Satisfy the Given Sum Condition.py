"""You are given an array of integers nums and an integer target.

Return the number of non-empty subsequences of nums such that the sum of the 
minimum and maximum element on it is less or equal to target. Since the answer
 may be too large, return it modulo 10^9 + 7."""

"""from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        #print("tamaño array nums = ",n)
        nums.sort()
        cnt, module = 0, 10**9 + 7
        def minmax(s,target):
            ns = len(s)
            #print("subsecuencia = ",s)
            #print("tamaño subsecuencia = ",ns)
            left, right= 0, ns-1
            #print("left y right = ", left, right)
            while left<=right:
                sum = (s[left]+s[right])
                #print("suma de", s[left], " y " , s[right], sum)
                if sum <= target:
                    #print("Cumplio el criterio objetivo")
                    return True
                else:
                    left+=1 
            return False
        #criterio es tener el minimo y el maximo elemento de la subsecuencia
        #criterio contar la subsecuencia si la suma del minimo y maximo sea menor o igual al target
        for mask in range(1<<n):
            curr=[]
            for i in range(n):
                if mask & (1<<i):
                    curr.append(nums[i])
                    #print("Construyendo subsecuencia = ", curr)
            #print("fin de construccion de subsecuencia = ",curr)
            if minmax(curr,target):
                #print("Respuesta de si la subsecuencia cumplio o no", minmax(curr,target))
                cnt+=1
                #print("conteo actual =", cnt)
        return cnt
"""
from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        MOD = 10**9+7
        right=len(nums)-1
        left=0
        cnt=0
        while left<=right:
            if nums[right]+nums[left]<=target:
                cnt=(cnt + (1<<(right-left)) % MOD) % MOD
                #se cuenta lo maximo que puede llegar
                left+=1
            else:
                right-=1
        return cnt
def main():
    sol = Solution()

    test_cases = [
        ([3, 5, 6, 7], 9),      # Esperado: 4
        ([3, 3, 6, 8], 10),     # Esperado: 6
        ([2, 3, 3, 4, 6, 7], 12), # Esperado: 61
        ([5, 2, 4, 1, 7, 6, 8], 16),  # Esperado: 127
    ]

    for i, (nums, target) in enumerate(test_cases):
        result = sol.numSubseq(nums, target)
        print(f"Test case {i + 1}: nums = {nums}, target = {target} → Result = {result}")

if __name__ == "__main__":
    main()
