primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
terceiro = int(input('Terceiro valor: '))
# VERIFICANDO QUEM É O MENOR
menor = primeiro 
if segundo < primeiro and segundo < terceiro:
    menor = segundo 
if terceiro < primeiro and terceiro < segundo:
    menor = terceiro
print(f'O menor valor digitado foi {menor}')

# VERIFICANDO QUEM É MAIOR
maior = primeiro 
if segundo > primeiro and segundo > terceiro:
    maior = segundo
if terceiro > primeiro and terceiro > segundo:
    maior = terceiro
print(f'O maior valor digitado foi {maior}')
