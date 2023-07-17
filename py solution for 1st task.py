from math import floor  # Импортирую floor для того, чтобы удобно округлить ответ

f = open('experiment.txt')
n = int(f.readline())
res_list = [[0 for x in range(2)] for y in range(26)]  # создаю генератор для хранения максимального и минимального
# KDA в каждой команде. Латинских букв 26, одно макс число, одно мин число, поэтому матрица сделана размером 2 26(не
# знаю как корректно это описать). Но этот прием с алфавитом Артем неоднократно показывал

for i in range(n):
    stek = f.readline().split()  # В строках 10-13 идет считывание переменных. Скорее всего можно было бы сделать
    # компактнее, но тогда не все мои потенциальные ученики поймут это
    team_name = stek[0]
    k, d, a = int(stek[1]), int(stek[2]), int(stek[3])
    koeff = (k + a) / d  # Считаю kda по заданной формуле
    team_index = ord(team_name) - ord('A')  # Определяю индекс названия команды, чтобы потом занести все в матрицу
    for j in range(2):  # В строках 16-27 заношу максимальное и минимальное значения kda в матрицу. Весь этот гемор с
        # if и for - else сделан для того, чтобы избежать занесения результатов одного и того же человека в обе
        # ячейки команды. И еще, чтобы сначала шел максимум, а потом минимум, чтобы потом было легче перезаполнять
        # эти значения
        if res_list[team_index][j] == 0:
            res_list[team_index][j] = koeff
            if res_list[team_index][0] < res_list[team_index][1]:
                res_list[team_index][0], res_list[team_index][1] = res_list[team_index][1], res_list[team_index][0]
            break
    else:
        res_list[team_index][0] = max(res_list[team_index][0], koeff)
        res_list[team_index][1] = min(res_list[team_index][1], koeff)

tek_res = 0  # промежуточная переменная для поиска максимума из всех результатов kda

for i in range(len(res_list)):
    for j in range(2):
        if res_list[i][j] > tek_res:  # тут просто перебираем все элементы и ищем максимум + еще сохраняем название
            # команды, тк нам нужна буква, которая идет в алфавите раньше, то используем знак ">"
            tek_res = res_list[i][j]
            ans1 = chr(i + ord('A'))  # тут из известного индекса получаю название нужной команды(букву)
            ans2 = min(res_list[i])  # тут сохраняю второй ответ (минимальное значение kda в нужной команде)
print(ans1, floor(ans2))  # принчу ответ.
