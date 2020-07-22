# n, char1 =

split_word = input()
n = int(input())
char1 = input()

split_word = split_word[:n] + char1 + split_word[n+1:]
print(split_word)
