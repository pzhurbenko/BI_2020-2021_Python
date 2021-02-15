from random import shuffle

def shuffle_word(word):
    word = list(word)
    shuffle(word)
    return ''.join(word)

print('Введите строку:')
string = input()

string_list = string.split() 
print ("The list of words is : " +  str(string_list)) 

result = []
temp = []
for i in string_list:
    temp.append(i[0])
    temp.append(shuffle_word(i[1:-1]))
    temp.append(i[-1])
    result.append(''.join(map(str, temp)))
    temp = []
print(' '.join(result))
