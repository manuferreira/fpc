expression = input()
clean_expression = [i for i in expression if i in '([{)]}']


def casamento_perfeito(clean_expression):
    stack = []

    for i in clean_expression: #seria legal usar um while aqui e uma variavel booleana pra conferir se o casamento foi imperfeito, pq dai evitaria de usar return, o professor disse q n era bom
        if i in "([{":
            stack.append(i)

        elif i in ")]}":
            if len(stack) != 0:
                opened = stack.pop()
                closed = i

                #conferindo se os delimitadores estão de acordo
                result = delimiters(opened, closed)
                if not result:
                    return 'casamento imperfeito'
        
            else:
                return 'casamento imperfeito'


    # se sobrar algum delimitador o casamento não é perfeito
    if len(stack) != 0:
        return 'casamento imperfeito'

    else:
        return 'casamento perfeito'



def delimiters(opened, closed):
    #n precisava conferir isso tudo aqui nao
    # if (opened == "(" and closed == ")") or (demais...): return True, else: return False
    list_opened = '([{'
    list_closed = ')]}'

    if opened == list_opened[0] and closed == list_closed[0]:
        return True

    elif opened == list_opened[1] and closed == list_closed[1]:
        return True

    elif opened == list_opened[2] and closed == list_closed[2]:
        return True

    else:
        return False


print(casamento_perfeito(clean_expression))
