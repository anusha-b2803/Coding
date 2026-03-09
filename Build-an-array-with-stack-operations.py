class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        current_number = 1
        for target_number in target:
            while current_number < target_number:
                operations.extend(["Push", "Pop"])
                current_number += 1
            operations.append("Push")
            current_number += 1
      
        return operations