Hotel-Uniesp 🏨

Repositório criado como parte do desafio da disciplina Introdução à Programação com Python — UNIESP.

Projeto Python: Sistema de Gerenciamento de Quartos de Hotel

Autor: João Victor Pereira do Nascimento
Disciplina: Introdução à Programação

📌 Resumo da Lógica

O sistema foi desenvolvido utilizando uma lista de listas (matriz simples) chamada hotel, que armazena os quartos e seus respectivos status.

Como a matriz foi estruturada

Cada elemento dentro da lista principal (hotel) é uma sublista representando um quarto:

quartos[0] → número do quarto (inteiro)

quartos[1] → status do quarto

'livre'

ou o nome do hóspede após o check-in

Funcionamento geral

As funções principais (listar_quartos, check_in, check_out, buscar) utilizam busca sequencial com um loop for para:

localizar o quarto solicitado

verificar disponibilidade

modificar diretamente o status na matriz

encontrar hóspedes pelo nome

🚀 Desafio Superado
Problema enfrentado:

A maior dificuldade foi localizar corretamente o quarto dentro da matriz para atualizar seu status.

Em uma matriz, o índice da lista não corresponde ao número do quarto
(exemplo: quarto 102 pode estar na posição 2).

Diferente de um dicionário, não é possível acessar diretamente o quarto pelo número como chave.

Como foi resolvido:

Utilizando um loop:

for quartos in hotel:
    if reserva == quartos[0]:


Assim, quando a condição é satisfeita, a variável quartos passa a ser uma referência direta à sublista correspondente. Dessa forma:

quartos[1] = nome.strip()


modifica o status diretamente dentro da matriz original.
Em seguida, o uso do break impede buscas desnecessárias.

🧭 Manual Rápido de Execução

Salve o código em um arquivo .py (exemplo: hotel.py).

Abra o terminal e navegue até a pasta onde o arquivo está salvo.

Execute:

python hotel.py


Utilize o menu exibido na tela para acessar as funções do sistema.
