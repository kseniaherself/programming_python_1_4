import re

def reading(way): 
    text = open(way, 'r', encoding = 'utf-8')
    f = text.read()
    text.close()
    return f

def regulF(f):
    regex = '([А-Я]\. [А-Я][а-я]+(\-[А-Я][а-я]+)*)'
    s = re.findall(regex, f)
    l1 = str(s)
    l1 = list(l1.split("'"))
    names = []
    i = 1
    while i < len(l1):
        names.append(l1[i])
        i += 4
    print('инициал + фамилия: ')
    for elem in names:
        print(elem)
    return names

def regulF2(f):
    regex2 = '(([А-Я]((\.)|([а-я]+))(\-)?)+ [А-Я][а-я]+(\-[А-Я][а-я]+)*)'
    res = re.findall(regex2, f)
    l2 = str(res)
    l2 = list(l2.split("'"))
    names2 = []
    j = 1
    while j < len(l2):
        names2.append(l2[j])
        j += 14
    print('вообще все имена: ')
    for element in names2:
        print(element)
    return names2

def main():
    way = input('введите название файла: ')
    val1 = reading(way)
    val2 = regulF(val1)
    val3 = regulF2(val1)

main()
