## Python 3.9.13
## Generating Random.txt with random numbers inside
## Count of rows you can enter by command line
import random
count=0
## Check is enter value digit
while count==0:
    count=input('Please, enter count of strings \n')
    if not count.isdigit():
        count=0
        print('Only digits is enterable')
## Creating Random.txt
r=open('Random.txt', 'w')
r.close()
r=open('Random.txt', 'a')
## Writing strings in Random.txt
for i in range(int(count)):
    for j in range(random.randint(1, 10)):
        r.write(f'{random.randint(0, 1000)} ')
    if i!=int(count)-1:
        r.write('\n')
r.close()
