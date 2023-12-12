class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        for pos, v in sorted(zip(position, speed))[::-1]:
            dist = target - pos
            time = dist / v 
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)