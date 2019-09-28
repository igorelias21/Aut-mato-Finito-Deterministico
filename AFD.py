# n = int(input("Insira um número para criar N estados"))
afd = {}
# for q in range(n):
#     afd['q'+str(q)] = None
# print(afd)
estado1, caminho, estado2 = input(
            "Insira estados no formato:\nestado-caminho-estado_adjacente\n").split('-')
afd[estado1] = {caminho: estado2}
afd[estado1]['final'] = False
estado_inicial = ''
estado_final = ''
while True:
    try:
        estado1, caminho, estado2 = input('').split('-')
        if estado1 in afd:
            afd[estado1].update({caminho: estado2})
        else:
            afd[estado1] = {caminho: estado2}
        afd[estado1]['final'] = False
    except:
        print(afd)
        entrada = input('Insira 1 para continuar')
        if entrada != '1':
            while True:
                estado_final = input('Insira um estado final(ou nada para continuar):\n')
                if estado_final:
                    afd[estado_final]['final'] = True
                else:
                    break
            break
print(afd)
palavra = True
while palavra:
    palavra = input("Insira uma palavra para ser testada")
    estado_atual = 'q0'

    for letra in palavra:
        if letra in afd[estado_atual]:  # estado_atual pode nao estar no automato, mas nao seria deterministico
            estado_atual = afd[estado_atual][letra]
        else:
            estado_final += 'invalido'

    if afd[estado_atual]['final']:
        print('palavra válida')
    else:
        print('palavra inválida')

estados = sorted(afd.keys())
diferentes = {}
equivalentes = {}
incerto = {}
for i in range(len(estados)):
    for j in range(len(estados)):
        if i != j:
            if afd[estados[i]]['final'] != afd[estados[j]]['final']:
                if estados[i] in diferentes:
                    diferentes[estados[i]].append(estados[j])
                else:
                    diferentes[estados[i]] = [estados[j]]
            elif afd[estados[i]]['final']:
                if estados[i] in equivalentes:
                    equivalentes[estados[i]].append(estados[j])
                else:
                    equivalentes[estados[i]] = [estados[j]]
            else:
                if estados[i] in incerto:
                    incerto[estados[i]].append(estados[j])
                else:
                    incerto[estados[i]] = [estados[j]]

# print(diferentes)
# print(equivalentes)
# print(incerto)

chaves_incertas = sorted(incerto.keys())

for chave in chaves_incertas:
    copia_incerto = incerto[chave][:]
    for estado in copia_incerto:
        equivalente = True
        for caminho in afd[estado]:
            if chave != estado and afd[estado][caminho] != afd[chave][caminho] and chave != afd[estado][caminho] and estado != afd[chave][caminho] and chave != afd[chave][caminho] and estado != afd[estado][caminho]:
                equivalente = False
                if chave in diferentes:
                    diferentes[chave].append(estado)
                else:
                    diferentes[chave] = [estado]
                break
        if not equivalente:
            incerto[chave].remove(estado)
            if not incerto[chave]:
                del incerto[chave]

print(diferentes)
print(incerto)

'''
q0-0-q1
q0-1-q2
q1-0-q3
q1-1-q4
q2-0-q3
q2-1-q4
q3-0-q1
q3-1-q4
q4-0-q4
q4-1-q4
'''