# Задача 1
def chat_bot():
    while True:
        a = input()
        if a == "":
            print("Как классно, когда ты молчишь. Продолжай в том же духе!")
        elif a.upper() == a:
            print("Успокойся!") 
        elif "?" in a:
            print("Конечно!")  
        else:
            print("Ну и что")      
chat_bot ()           

# Задача 2        
def count_word(word):
    word_split = word.split(",")
    str_split = "".join(word_split).title()
    word_split = str_split.split()
    for i in set(word_split):
        print(word_split.count(i), i)
count_word("Mamatkulova Begimai") 

# Задача 3
n = "Money, money, money, it's always sunny, in the richmen's world"
n = n.lower()
n = n.split(' ')
res = {}
for i in n:
    i = i.lower()
    count = n.count(i)
    res.setdefault(i,count)         
print(res)

# Задача 4
def unique():
    word = input()
    word_dict = list(word)
    no_double = set(word)
    if len(word_dict) == len(no_double):
        print('True')
    else:
        print('False')
unique()            

    
               
