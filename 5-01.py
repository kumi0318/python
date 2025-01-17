def sky(n):
    for i in range(1, n + 1):
        spaces = n - i
        
        if i == 1:
            print(' ' * spaces + '*')
        elif i == n:
            print(' ' * spaces + '* ' * i)
        else:
            # 中間行的星號首尾固定，之間填充適當的空格
            # 中間空格的數量為：2 * (行號 - 1) - 1
            print(' ' * spaces + '*' + ' ' * (2 * i - 3) + '*')

sky(3)
