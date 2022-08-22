from typing import List


class Solution:

    def combinationSum2(self,canditates: List[int], target:int) -> List[List[int]]:

        def backtrack(comb, remain, curr, results):

            if remain ==0:

                # make a dep copy of the resulted combination
                results.append(list(comb))
                return
            
            for next_curr in range(curr, len(canditates)):
                if next_curr > curr and canditates[next_curr] == canditates[next_curr-1]:
                    continue

                pick = canditates[next_curr]
                # Optimisation: skip the rest of the elements starting from 'curr' index
                if remain - pick <0:
                    break
                comb.append(pick)
                backtrack(comb,remain-pick,next_curr+1,results)
                comb.pop()
            
            canditates.sort()
            comb,results = [],[]
            backtrack(comb, target, 0, results)

            return results


