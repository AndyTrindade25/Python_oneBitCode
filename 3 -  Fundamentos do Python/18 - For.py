gamesList = ["Fifa", "God of War", "Red Dead 2", "Uncharted"]

# 1 - Iterando valores de uma lista
#for game in gamesList:
    #print(game)
    
    
# 2 - Quando a condição for atendida, o Loop será encerrado

# for game in gamesList:
#     if game == "Read Dead 2":
#         break
#     print(game)
    
    
# 3 - Quando a condição for atendida, o Loop vai para a próxima iteração
# for game in gamesList:
#     if game == "Red Dead 2":
#         continue
#     print(game)

#4 - Avaliação do jogo
gameName = input('Digite o nome do jogo\n')
gameRating = int(input('Digite quantas avaliações deseja fazer no jogo\n'))

sum = 0
for i in range(gameRating):
    note = float(input('Digite a nota para o jogo\n'))
    sum += note #sum = sum = note
print(f"Média de avaliação do jogo {gameName} é {sum/gameRating}")