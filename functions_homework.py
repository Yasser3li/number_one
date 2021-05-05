# Question one:

def lesser_of_two_evens(num1,num2):
    if (num1 % 2 == 0) and (num2 % 2 == 0):
        return min(num1, num2)
    else:
        return max(num1, num2)

print(lesser_of_two_evens(2, 5))

# Question two:

def animal_crackers(words):
    two_words = words.lower().split()
    return two_words[0][0] == two_words[1][0]


print(animal_crackers('Tiger Tiger'))

# Question four:
def old_macdonald(name):
    new_word = ''
    count = 0
    for letter in name:
        if count == 0 or count == 3:
            new_word += letter.upper()
            count += 1
        else:
            new_word += letter
            count += 1
    return new_word

print(old_macdonald('macdonald'))

# Question five:
def makes_twenty(a, b):
    return (a == 20) or (b == 20) or (a+b == 20)

print(makes_twenty(20, 10))
print(makes_twenty(2, 3))
print(makes_twenty(15, 5))

# Question six:

def master_yoda(sentence):
    word_list = sentence.split()
    reverse_word_list = word_list[::-1]
    reverse_sentence = ' '.join(reverse_word_list)
    return reverse_sentence

print(master_yoda('Hello my name is Yasser'))

# Question seven:

def almost_there(n):
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)

print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

# Question eight:

def has_33(nums):
    current = 0
    for i in range(0, len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

print(has_33([1, 3, 4]))

# Question nine:
def paper_doll(text):
    new_text = ''
    for letter in text:
        new_text += letter * 3
    return new_text

print(paper_doll('Hello'))

# Question ten:

def blackjack(a, b, c):
    sum_nums = a + b + c

    if sum_nums > 21:
        if ((a == 11) or (b == 11) or (c == 11)) and sum_nums <= 31:
            return sum_nums - 10
        else:
            return 'BUST'
    else:
        return sum_nums

print(blackjack(11, 11, 11))