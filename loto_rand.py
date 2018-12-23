import random
import emoji

print("""Vamos tentar sua sorte. Um número entre 1 e 20 foi gerado automaticamente. Você tem apenas 5 chances para descobrir qual número é.""")
print('Boa sorte!')

number = random.randint(1, 20)

t = 0

while t < 5:
    t = t + 1
    shots = int(input('\nTentativa número {}: '.format(t)))

    if shots == number:
        print(emoji.emojize('Parabéns! Você é demais :sunglasses:!', use_aliases=True))
        break

    elif shots < number and t < 5:
        print('Quase lá. O número está um pouco acima...')

    elif shots > number and t < 5:
        print('Quase lá. O número está um pouco abaixo...')

    elif t == 3 and shots != number:
        print(emoji.emojize("""Aw que triste :cry:. Não desista ainda, talvez sua sorte esteja dormindo :simple_smile:.""", use_aliases=True))
        break
