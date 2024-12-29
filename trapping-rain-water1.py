class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        area = 0
        cur_h_min = 0
        for j in range(len(height)):
            cur_h = height[j]

            if not cur_h:
                cur_h_min = 0
                continue

            while stack:
                h,i = stack[-1]

                if cur_h<h:
                    cur_area = (cur_h-cur_h_min)*(j-i-1)
                    area+=cur_area
                    cur_h_min = cur_h
                    break
                else: # cur_h>=h:  # 连根拔
                    stack.pop()
                    cur_area = (h-cur_h_min)*(j-i-1)
                    area+=cur_area
                    cur_h_min = h

            stack.append((cur_h, j))

        return area




