my_dict = [input().lower() for _ in range(int(input()))]
text = {j for i in range(int(input())) for j in input().lower().split()}
print(*[w for w in text if w not in my_dict], sep="\n")

''' Решение со степика

words = set(input().lower() for i in range(int(input())))
text = set(('\n'.join(input().lower() for i in range(int(input())))).split())
print('\n'.join(text - words))

'''