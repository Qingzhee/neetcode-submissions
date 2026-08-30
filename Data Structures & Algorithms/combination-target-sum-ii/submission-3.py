class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        arr = []
        candidates.sort()

        def combi(i, cur_sum, cur_comb):
            if cur_sum == target:
                if cur_comb not in arr:
                    arr.append(cur_comb.copy())
                return

            if i > len(candidates) - 1 or cur_sum > target:
                return

            cur_sum += candidates[i]
            cur_comb.append(candidates[i])
            combi(i + 1, cur_sum, cur_comb)

            cur_comb.pop()
            cur_sum -= candidates[i]
            while (
                i + 1 < len(candidates)
                and candidates[i] == candidates[i + 1]
            ):
                i += 1

            combi(i + 1, cur_sum, cur_comb)

        combi(0, 0, [])
        return arr
