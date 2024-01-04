# La réponse est y = 23

nb_a_battre = 255^3
result = 2
y = 1

while result < nb_a_battre:
    result = 2 ^ y
    y += 1
    print(result,y)