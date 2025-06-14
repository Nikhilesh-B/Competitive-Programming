class Solution:
    def trap(self, height):
        ans = 0
        current = 0
        st = []
        while current < len(height):
            print("Current:", current)
            while len(st) != 0 and height[current] > height[st[-1]]:
                print("Before stack change:", st)
                top = st[-1]
                st.pop()
                if len(st) == 0:
                    break
                distance = current - st[-1] - 1
                bounded_height = (
                    min(height[current], height[st[-1]]) - height[top]
                )
                print("Distance:", distance)
                ans += distance * bounded_height
                print("After stack change:", st)
                print("Bounded height", bounded_height)
            st.append(current)
            current += 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.trap([3,1,3,2,3]))
