s = input()

last_char = s[0]
last_len = 1

ans = 1

for c in s[1:]:
    if c == last_char:
        last_len += 1
    else:
        last_char = c
        last_len = 1
    ans = max(ans, last_len)

print(ans)
