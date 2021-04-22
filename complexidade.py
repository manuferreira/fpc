string = input().split()

array = [i if not i.isdigit() else int(i) for i in string]
pilha = []


def complexidade(array):
    total_global = 0

    for i in range(len(array)):
        if array[i] == "INICIO":
            pilha.append(array[i])
        
        elif array[i] == "OP":
            pilha.append(array[i+1])

        elif array[i] == "LOOP":
            pilha.append(array[i+1])
            pilha.append(array[i])

        elif array[i] == "FIMLOOP" or array[i] == "FIM":
            total_interno = 0
            elem = pilha.pop()

            while elem != "INICIO" and elem != "LOOP":
                total_interno += elem
                elem = pilha.pop()
            
            if elem == "LOOP":
                elem = pilha.pop()
                total_interno *= elem
                pilha.append(total_interno)

    return total_interno

print(complexidade(array))    