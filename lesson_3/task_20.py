# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква
# имеет определенную ценность. В случае с английским алфавитом очки
# распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка;
# B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков;
# Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость
# введенного пользователем слова. Будем считать, что на вход подается только одно слово,
# которое содержит либо только английские, либо только русские буквы.
#
# *Пример:*
#
# ноутбук
#     12
word = input("Введите слово: ")

score = 0
for letter in word:
    if letter.lower() in 'aeioulnrst':
        score += 1
    elif letter.lower() in 'dg':
        score += 2
    elif letter.lower() in 'bcmp':
        score += 3
    elif letter.lower() in 'fhvwy':
        score += 4
    elif letter.lower() == 'k':
        score += 5
    elif letter.lower() in 'jx':
        score += 8
    elif letter.lower() in 'qz':
        score += 10
    elif letter.lower() in 'авеинорст':
        score += 1
    elif letter.lower() in 'дклмпу':
        score += 2
    elif letter.lower() in 'бгёья':
        score += 3
    elif letter.lower() in 'йы':
        score += 4
    elif letter.lower() in 'жзхцч':
        score += 5
    elif letter.lower() in 'шэю':
        score += 8
    elif letter.lower() in 'фщъ':
        score += 10

print(score)
