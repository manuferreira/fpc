input_data = input().split()
qtde_containers = int(input_data[0])
tam_container = int(input_data[1])
tam_overflow = int(input_data[2])
qtde_insercoes = int(input_data[3])
tam_total_containers = qtde_containers*tam_container

# tamanho da lista
hash_table_size = qtde_containers * tam_container + tam_overflow
hash_table = [None] * hash_table_size


def inserir():
    for elem in range(4, qtde_insercoes+4):
        chave = int(input_data[elem])
        container = chave % qtde_containers
        pos_container = container * tam_container
        ocupado = True

        i = pos_container
        while i < (pos_container+tam_container+1) and ocupado:
            if hash_table[i] is None:
                hash_table[i] = chave
                ocupado = False
            i += 1

        # guardando no overflow
        j = tam_total_containers
        while j < (tam_overflow+tam_total_containers+1) and ocupado:
            if hash_table[j] is None:
                hash_table[j] = chave
                ocupado = False
            j += 1


def busca(chave_buscada):
    count = 0
    container_busca = chave_buscada % qtde_containers
    pos_container_busca = container_busca * tam_container

    i = pos_container_busca
    not_coincide = True

    while i < (pos_container_busca + tam_container) and not_coincide:
        count += 1
        if hash_table[i] == chave_buscada:
            not_coincide = False

        elif hash_table[i] is None:
            not_coincide = False
        i += 1


    j = tam_total_containers
    while j < (tam_overflow+tam_total_containers) and not_coincide:
        count += 1

        if hash_table[j] == chave_buscada:
            not_coincide = False

        elif hash_table[j] is None:
            not_coincide = False
        j += 1

    return count


inserir()

for i in range(12, len(input_data)):
    chave_buscada = int(input_data[i])
    print(busca(chave_buscada), end=' ')
