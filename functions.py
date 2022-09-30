# Função para o tratamento da data para tipo SQL
def format_data(vet):
    dt = []
    data = []
    for i in vet:
        j = i.replace('/', '-')
        k = j.split('-')
        for i in range((len(k) - 1), -1, -1):
            dt.append(k[i])
        data.append('-'.join(dt))
        dt.clear()
    vet.clear()
    for j in data:
        vet.append(j)


# Função para o tratamento dos valores da entrada.
def read_enter_num(values, vet, vet2):
    final = ''
    vet2.clear()
    vet.clear()
    for i in values['numero_nota']:
        if i == '\n':
            vet.append(final)
            final = ''
        final += i
    if final != '':
        vet.append(final)
    for i in vet:
        k = i.replace(',', '.')
        vet2.append(k.replace('\n', ''))


def read_enter_mod(values, vet, vet2):
    final = ''
    vet2.clear()
    vet.clear()
    for i in values['modelo_nota']:
        if i == '\n':
            vet.append(final)
            final = ''
        final += i
    if final != '':
        vet.append(final)
    for i in vet:
        k = i.replace(',', '.')
        vet2.append(k.replace('\n', ''))


def read_enter_serie(values, vet, vet2):
    final = ''
    vet2.clear()
    vet.clear()
    for i in values['serie_nota']:
        if i == '\n':
            vet.append(final)
            final = ''
        final += i
    if final != '':
        vet.append(final)
    for i in vet:
        k = i.replace(',', '.')
        vet2.append(k.replace('\n', ''))


def read_enter_data(values, vet, vet2):
    final = ''
    vet2.clear()
    vet.clear()
    for i in values['data_nota']:
        if i == '\n':
            vet.append(final)
            final = ''
        final += i
    if final != '':
        vet.append(final)
    format_data(vet)
    for i in vet:
        k = i + ' 00:00:00.000'
        vet2.append(k.replace('\n', ''))
