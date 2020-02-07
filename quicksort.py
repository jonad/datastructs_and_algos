from typing import *
from random import randint

class QuickSort:
    
    def sort_array(self, nums: List[int]) -> List[int]:
        self.sort_array_helper(nums, 0, len(nums) -1)
        return nums
    
    def sort_array_helper(self, nums:List[int], low:int, high:int) -> None:
        if low >= high:
            return
        else:
            pivot_index = randint(low, high)
            partition = self.partition(nums, pivot_index, low, high)
            self.sort_array_helper(nums, low, partition - 2)
            self.sort_array_helper(nums, partition, high)
            
    def partition(self, nums: List[int], pivot_index:int, low:int, high:int) -> int:
        pivot = nums[pivot_index]
        smaller, equals, larger = low, low, high
        while equals <= larger:
            if nums[equals] < pivot:
                nums[smaller], nums[equals] = nums[equals], nums[smaller]
                equals += 1
                smaller += 1
            elif nums[equals] == pivot:
                equals += 1
            else:
                nums[larger], nums[equals]  = nums[equals], nums[larger]
                larger -= 1
        return equals
        