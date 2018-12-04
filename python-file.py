# hello world
print('hello world')


# variáveis
mensagem = 'hello world'
print(mensagem)


# mudando case
nome = "victor palmerini"
print(name.title())
print(name.upper())
print(name.lowe())


# concatenando strings
primeiro_nome = 'victor'
ultimo_nome = 'palmerini'

nome_completo = primeiro_nome + ultimo_nome
print(nome_completo)
print('Hello' + nome_completo.title() + '!')

hello = 'Hello' + nome_completo.title() + '!'
print(hello)


# operações básicas
soma = 2 + 3
subtracao = 3 - 2
multiplicacao = 2*3
divisao_decimal = 3/2
divisao_inteira = 3//2
potencia = 3**2


# tipos
type(soma)
type(nome_completo)
type(divisao_decimal)
type(divisao_inteira)


# listas
frutas = ['maçã', 'banana', 'abacate', 'laranja', 'melancia']
print(frutas[1])
print(frutas[0].title())
print(frutas[-1])
print(frutas[-2])

mensagem = 'Minha fruta preferida é' + frutas[-1].title()
print(mensagem)

# modificando elementos de uma lista
frutas[-1] = 'manga'
print(frutas)			# fruits = ['maçã', 'banana', 'abacate', 'laranja', 'manga']

# adicionando
frutas.append('abacaxi')
print(frutas)			# fruits = ['maçã', 'banana', 'abacate', 'laranja', 'manga', 'abacaxi']

frutas.insert(0, 'figo')
print(frutas)			# fruits = ['figo', 'maçã', 'banana', 'abacate', 'laranja', 'manga', 'abacaxi']

# removendo
ultima_fruta = frutas.pop()
print(ultima_fruta)		# fruits = ['figo', 'maçã', 'banana', 'abacate', 'laranja', 'manga']

fruta_qualquer = frutas.pop(2)
print(fruta_qualquer)	# fruits = ['figo', 'maçã', 'abacate', 'laranja', 'manga']

fruta.remove('abacate')
print(fruits)

fruta_ruim = 'figo'
fruta.remove(fruta_ruim) # fruits = ['maçã', 'abacate', 'laranja', 'manga']

# ordenação
frutas_ordenadas = fruta.sort()
print(frutas_ordenadas)
print(frutas)

# ordenação reversa
frutas_reversas = frutas.reverse()
print(frutas_reversas)
print(frutas)

# tamanho do vetor
tamanho_frutas = len(frutas)
print(tamanho_frutas)


# laços
for fruta in frutas:
	print(fruta)

for i in range(len(frutas)):
	print(fruta[i])

for i in range(2,len(frutas)):
	print(frutas)

numeros = list(range(1,11))

for numero in numeros:
	print(numero)

numero_pares = list(range(1,11,2))

for fruta in frutas:
	print('Gosto muito de' + fruta.title())

print('Acabou o laço!')


quadrados = []
for i in range(1,11):
	quadrado = i**2
	quadrados.append(quadrado)

print(quadrados)

print(min(quadrados))
print(max(quadrados))
print(sum(quadrados))


print(frutas[0:2])
print(frutas[:2])
print(frutas[2:])
print(frutas[2:3])

for fruta in frutas[:2]:
	print('Só gosto de ' + fruta)


# condicionais
for fruta in frutas:
	if fruta == 'laranja':
		print(fruta.upper())
	else:
		print(fruta.title())

for fruta in frutas:
	if len(fruta) > 4:
		print('Essa fruta tem nome curto:' + fruta.lower())
	else:
		print('Essa fruta tem nome longo:' + fruta.upper())

manga_boolean = 'maçã' in frutas
print(manga_boolean)

for fruta in frutas:
	if len(fruta) < 5:
		print(fruta.lower())
	elif len(fruta) < 7:
		print(fruta.title())
	else:
		print(fruta.upper())



# funções
def hello_world():
	print('hello world')

hello_world()


def printa_mensagem(mensagem):
	print(mensagem)

printa_mensagem('Olar')

saudação = 'Olá, como está você?'
printa_mensagem(saudação)


def formata_nome(primeiro_nome, ultimo_nome):
	nome_completo = primeiro_nome.title() + ' ' + ultimo_nome.title()
	return nome_completo

nome = formata_nome('victor', 'palmerini')
print(nome)

primeiro = 'gustavo'
ultimo = 'soares'
print(formata_nome(primeiro, ultimo))


def percorre_lista(lista):
	for elemento in lista:
		print(elemento)

percorre_lista()


def limpa_lista(lista):
	while(lista):
		lista.pop()

limpa_lista(frutas)
print(frutas)
