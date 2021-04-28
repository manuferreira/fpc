n = int(input())

def palavras_fibonacci(n):
    if n == 0:
        return 'b'
    elif n == 1:
        return 'a'
    else:
        return palavras_fibonacci(n-1) + palavras_fibonacci(n-2)

print(palavras_fibonacci(n))