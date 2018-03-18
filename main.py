import library_game
kol_pok = int(input())
nums = map(int, input().split())
k = list(nums)
n = k[0]
m = k[1]
card = [0] * 2
for i in range(2):
    card[i] = [0] * (n + 2)
    for j in range(n+2):
        card[i][j] = [0] * (m + 2)
for i in range(n):
    s = input()
    for j in range(m):
        if s[j] == '.':
            card[0][i + 1][j + 1] = 1
            card[1][i + 1][j + 1] = 1
        if s[j] == 'F':
            card[0][i + 1][j + 1] = 2
            card[1][i + 1][j + 1] = 2
        if s[j] == 'C':
            card[0][i + 1][j + 1] = 3
            card[1][i + 1][j + 1] = 3
library_game.f(kol_pok, card)
for i in range(n):
    for j in range(m):
        if card[1][i + 1][j + 1] == 0:
            print('#', end='')
        if card[1][i + 1][j + 1] == 1:
            print('.', end='')
        if card[1][i + 1][j + 1] == 2:
            print('F', end='')
        if card[1][i + 1][j + 1] == 3:
            print('C', end='')
    print()
