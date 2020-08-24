def anagrams(s):
    if s == '':
        return [s]
    else:
        ans = []
        for w in anagrams(s[1:]):
            for pos in range(len(w) + 1):
                ans.append(w[:pos] + s[0] + w[pos:])
        return ans

def main():
    data = 'abc'
    print(anagrams(data))

if __name__ == '__main__':
    main()