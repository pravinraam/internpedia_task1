import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
special = string.punctuation

def Count_word(words):
    arr_word = words.split(' ')
    return len(arr_word)

def Count_length(words):
    lower_count =0
    upper_count =0
    number_count =0
    special_count =0
    space = 0

    for i in words:
        if i in lower:
            lower_count += 1
        elif i in upper:
            upper_count += 1
        elif i in digits:
              number_count += 1
        elif i in special:
            special_count += 1
        else:
            space += 1
    
    return [lower_count,upper_count,number_count,special_count,space]


if __name__ == '__main__':
    print('Welcome User..!')
    words = input('Enter a word to be count:')
    count = Count_word(words)
    length = Count_length(words)
    print(f'Total count of word is - {count}')
    print(f'Total Lower Letter of the Words is {length[0]}')
    print(f'Total Upper Letter of the Words is {length[1]}')
    print(f'Total Number Letter of the Words is {length[2]}')
    print(f'Total Special Symbol of the Words is {length[3]}')
    print(f'Total Space of the Words is {length[4]}')