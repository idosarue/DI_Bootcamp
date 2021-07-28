# 1
import random
def get_words_from_file(file):
    with open(file,mode='r',encoding = 'utf-8') as f:
        secret_data = f.readlines() 
        return secret_data


def get_random_sentence(length):
    word_li = get_words_from_file("sowpods.txt")
    li = []
    for _ in range(length):
        x = random.choice(word_li)
        li.append(x[:-2])
    return " ".join(li).lower()


def main():
    '''
    program excepts int between 2 and 20
    '''
    try:
        user_input = int(input('How long do you want the sentecne to be? enter an int between 2 and 20: '))
        if 2 <= user_input <= 20:
            return get_random_sentence(user_input)
        else:
            return 'your num isn\'t between 2 and 20'
    except ValueError:
       return 'not a number'
print(main.__doc__)
print(main())


# 2

import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""



s = json.loads(sampleJson)['company']['employee']['payable']['salary']
sample_dict = json.loads(sampleJson)

sample_dict["company"]["employee"]['birthdate'] = '1'
print(sample_dict)
with open('nwe.txt', 'w') as f:
    json.dump(sample_dict, f)
