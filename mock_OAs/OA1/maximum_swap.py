class Solution:
    def maxSwap(self, num: str) -> str:
        lst_numbers = [int(c) for c in num]
        mx = max(lst_numbers)


        if len(lst_numbers) == 1:
            return str(num)

        elif lst_numbers[0] == mx:
             return num[0]+self.maxSwap(num[1:])

        else:
            indexes = [i for i, n in enumerate(lst_numbers) if n==mx]
            mx_idx = max(indexes)
            temp = lst_numbers[0]
            lst_numbers[0] = mx
            lst_numbers[mx_idx] = temp
            return "".join([str(i) for i in lst_numbers])

    def maximumSwap(self, num: int) -> int:
        ms = self.maxSwap(num=str(num))
        return int(ms)


if __name__ == "__main__":
    s = Solution()
    num = 1000
    ans = s.maximumSwap(num=num)
    print(ans)
