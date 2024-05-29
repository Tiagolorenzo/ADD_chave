# dicionáario
pessoa = {
    'Nome':'Artur Miguel',
    'Idade':3,
    'Profissao':'Estudante'
}

nova_chave = input('Digite o nome do campo: ')
novo_valor = input('Informe valor do novo campo: ')
pessoa[nova_chave] = novo_valor

# exibe dados
for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')
