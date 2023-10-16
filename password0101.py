def printend(text):
        print(text,end='')

def use():
    words = input('$ ').lower()

    for i in words:
        if i == 'a':
            printend('100000')
        elif i == 'b':
            printend('100001')
        elif i == 'c':
            printend('100010')
        elif i == 'd':
            printend('100011')
        elif i == 'e':
            printend('100100')
        elif i == 'f':
            printend('100101')
        elif i == 'g':
            printend('100110')
        elif i == 'h':
            printend('100111')
        elif i == 'i':
            printend('101000')
        elif i == 'j':
            printend('101001')
        elif i == 'k':
            printend('101010')
        elif i == 'l':
            printend('101011')
        elif i == 'm':
            printend('101100')
        elif i == 'n':
            printend('101101')
        elif i == 'o':
            printend('101110')
        elif i == 'p':
            printend('101111')
        elif i == 'q':
            printend('110000')
        elif i == 'r':
            printend('110001')
        elif i == 's':
            printend('110010')
        elif i == 't':
            printend('110011')
        elif i == 'u':
            printend('110100')
        elif i == 'v':
            printend('110101')
        elif i == 'w':
            printend('110110')
        elif i == 'x':
            printend('110111')
        elif i == 'y':
            printend('111000')
        elif i == 'z':
            printend('111001')
        elif i == ' ':
            printend('111010')
        else:
            print(i, end='')
    input('\n--ENTER--')



def use2():
    words = input('$ ')
    numbers = ''
    j = 0
    for i in range(len(words)):
        if words[i] != '0' and words[i] != '1':
            printend(words[i])
        else:
            if (i + 1)% 6 != 0:
                numbers += words[i]
            else:
                numbers += words[i]
                if numbers == '100000':
                    printend('a')
                elif numbers == '100001':
                    printend('b')
                elif numbers == '100010':
                    printend('c')
                elif numbers == '100011':
                    printend('d')
                elif numbers == '100100':
                    printend('e')
                elif numbers == '100101':
                    printend('f')
                elif numbers == '100110':
                    printend('g')
                elif numbers == '100111':
                    printend('h')
                elif numbers == '101000':
                    printend('i')
                elif numbers == '101001':
                    printend('j')
                elif numbers == '101010':
                    printend('k')
                elif numbers == '101011':
                    printend('l')
                elif numbers == '101100':
                    printend('m')
                elif numbers == '101101':
                    printend('n')
                elif numbers == '101110':
                    printend('o')
                elif numbers == '101111':
                    printend('p')
                elif numbers == '110000':
                    printend('q')
                elif numbers == '110001':
                    printend('r')
                elif numbers == '110010':
                    printend('s')
                elif numbers == '110011':
                    printend('t')
                elif numbers == '110100':
                    printend('u')
                elif numbers == '110101':
                    printend('v')
                elif numbers == '110110':
                    printend('w')
                elif numbers == '110111':
                    printend('x')
                elif numbers == '111000':
                    printend('y')
                else:
                    printend('z')
                numbers = ''


what = input('(encryption -> E) OR (decrypt -> D) >> ').lower()

if what == 'e':
    use()
else:
    use2()