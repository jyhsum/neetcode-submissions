class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list(zip(position, speed))
        pair.sort(reverse=True) # 排序後的順序為位置最靠近終點的在前
        stack = []
        for p, s in pair:
            time = (target - p) / s
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]: #比較最靠近終點的會不會被次靠近的追上, 如果次靠近花的時間比較少或相等就代表會追上, 形成一個車隊
                stack.pop() # 只保留同一車隊的 time
        
        return len(stack)