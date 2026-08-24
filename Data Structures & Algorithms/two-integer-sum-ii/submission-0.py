class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            need = target - numbers[i]

            front = i+1
            back = len(numbers) - 1            
            while front<=back:
                mid = int((front+back)/2)
                if numbers[mid] == need:
                    return [i + 1, mid + 1] 

                elif numbers[mid] < need:
                    front = mid + 1

                else:
                    back = mid - 1
        
            