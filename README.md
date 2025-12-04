# Hotel-Uniesp
Repositório criado para desafio da materia de introdução a programação com python


 Projeto Python: Sistema de Gerenciamento de Quartos de Hotel
Nome: João victor Pereira do Nascimento
Disciplina: Introdução a Programação
Resumo da Lógica
O sistema de gerenciamento de quartos de hotel foi construído usando uma lista de listas em Python, que funciona como uma matriz simples, nomeada como hotel.
Estrutura da Matriz:
Cada elemento dentro da lista principal (hotel) é uma sublista que representa um único quarto.
O primeiro elemento de cada sublista (quartos[0]) armazena o número do quarto (um valor inteiro).
O segundo elemento de cada sublista (quartos[1]) armazena o status do quarto. Ele é inicialmente a string 'livre' ou, após um check-in, o nome do hóspede (uma string).
Todas as funções do programa (listar_quartos, check_in, check_out, buscar) utilizam uma busca sequencial simples (laço for) para iterar sobre essa matriz e encontrar o quarto ou o hóspede desejado para realizar as operações de consulta ou atualização.
Desafio Superado
O desafio mais notável ao trabalhar com essa estrutura foi a necessidade de achar e modificar o status do quarto correto durante as operações de check-in e check-out.
Dificuldade ("Achar o índice do quarto"): Diferente de usar um dicionário, onde a chave seria o número do quarto, nesta matriz não podemos simplesmente buscar pelo índice (posição) do quarto na lista hotel, pois esse índice não corresponde ao número do quarto (por exemplo, o quarto de número 102 pode estar no índice 2).
Resolução: A solução foi usar a iteração direta (for quartos in hotel:). Quando a condição é satisfeita (if reserva == quartos[0]:), a variável quartos dentro do laço se torna uma referência direta à sublista do quarto encontrado. Assim, ao modificar quartos[1] (por exemplo, quartos[1] = nome.strip()), a alteração é feita diretamente na matriz hotel original, garantindo que o status seja atualizado permanentemente antes de sair do laço usando break.
 Manual Rápido
Salve o código em um arquivo com extensão .py (ex: hotel.py).
Abra o terminal ou prompt de comando e navegue até a pasta do arquivo.
Execute o código digitando: python hotel.py e use as opções do menu.
