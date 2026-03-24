ALPHA = ['a', 'b', 'c', 'd']
ALPHA_IDX = {ch: i for i, ch in enumerate(ALPHA)}


def next_string(s):
    s = list(s)
    i = len(s) - 1
    while i >= 0:
        if s[i] != 'd':
            s[i] = ALPHA[ALPHA_IDX[s[i]] + 1]
            return ''.join(s)
        else:
            s[i] = 'a'
            i -= 1
    return 'a' * (len(s) + 1)


def is_palindrome(s):
    return s == s[::-1]


def previous_palindrome(s):
    cur = s
    while True:
        cur = list(cur)
        i = len(cur) - 1
        while i >= 0:
            if cur[i] != 'a':
                cur[i] = ALPHA[ALPHA_IDX[cur[i]] - 1]
                for j in range(i + 1, len(cur)):
                    cur[j] = 'd'
                break
            else:
                cur[i] = 'd'
                i -= 1
        else:
            cur = ['d'] * (len(cur) - 1)

        cur = ''.join(cur)
        if not cur:
            return None
        if is_palindrome(cur):
            return cur


def count_palindromes_behind(s):
    n = len(s)

    def gen_palindromes(length):
        half_len = (length + 1) // 2
        total = 4 ** half_len
        for num in range(total):
            digits = []
            tmp = num
            for _ in range(half_len):
                digits.append(ALPHA[tmp % 4])
                tmp //= 4
            digits.reverse()
            first_half = digits
            if length % 2 == 0:
                pal = first_half + first_half[::-1]
            else:
                pal = first_half + first_half[-2::-1]
            yield ''.join(pal)

    count = 0
    for pal in gen_palindromes(n):
        if pal < s:
            count += 1
        elif pal >= s:
            break
    return count


def count_strings_containing(n, s):
    if len(s) > n:
        return 0
    m = len(s)

    fail = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and s[i] != s[j]:
            j = fail[j - 1]
        if s[i] == s[j]:
            j += 1
        fail[i] = j

    dp = [[0] * m for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(m):
            if dp[i][j] == 0:
                continue
            for ch in ALPHA:
                k = j
                while k > 0 and ch != s[k]:
                    k = fail[k - 1]
                if ch == s[k]:
                    k += 1
                if k < m:
                    dp[i + 1][k] += dp[i][j]

    avoiding = sum(dp[n][j] for j in range(m))
    return 4 ** n - avoiding


def main():
    
    print("Strings over A = {a, b, c, d}")
    
    print("\n- 1.1 next_string -")
    for t in ['aaa', 'bccc', 'ddd', 'cbcd', 'ddcbdc']:
        print(f"  Chuoi tiep theo cua({t!r}) = {next_string(t)!r}")

    print("\n- 1.2 previous_palindrome -")
    for t in ['aab', 'bccc', 'dddd', 'cbcd', 'ddcbdc']:
        print(f"  Chuoi truoc do cua({t!r}) = {previous_palindrome(t)!r}")

    print("\n- 1.3 count_palindromes_behind -")
    for t in ['aab', 'cbcd', 'dddd', 'ddcbdc']:
        print(f"  So luong chuoi doi xung cua ({t!r}) = {count_palindromes_behind(t)}")

    print("\n- 1.4 count_strings_containing(n, s) -")
    for n, s in [(3, 'ab'), (4, 'ab'), (5, 'ab'), (3, 'aa')]:
        print(f"  So luong cac chuoi co do dai ({n}, {s!r}) = {count_strings_containing(n, s)}")


if __name__ == "__main__":
    main()