st = 'Print only the words that starts with s in this sentence'

# Question One:
for word in st.split():
    if word.startswith('s'):
        print(word)

# Question Two:
for n in range(2, 11, 2):
    print(n)

# Question Three:
list = []
for n in range(3, 50, 3):
    list.append(n)
print(list)

# Question Four
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word) % 2 == 0:
        print(word, 'even!')


# Question Five
for i in range(1, 101):
    if i % 3 == 0 and i % 5 != 0:
        print('Fizz')
    elif i % 5 == 0 and i % 3 != 0:
        print('Buzz')
    elif i % 15 == 0:
        print('FizzBuzz')
    else:
        print(i)

# Last Question:

st = 'Create a list of the first letters of every word in this string'
list = []
for word in st.split():
    list.append(word[0])
print(list)