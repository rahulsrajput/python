import time

# wait_time = 1
# max_retries = 5
# attempts = 0

# while (attempts < max_retries):
#     print('attemp:',attempts+1, 'wait time:',wait_time)

#     time.sleep(wait_time)
#     wait_time *= 2
#     attempts += 1



#############################

wait_time = 5
max_retries = 3
attempts = 0

password = input('Enter a password:')

while(attempts < max_retries):
    password_again = input('Enter a same password again: ')

    if password != password_again:
        print(f'You entered Wrong Password, Attempt: {attempts+1} and Wait Time: {wait_time}sec')
        time.sleep(wait_time)
        attempts += 1
        wait_time *= 2

    
    elif password == password_again:
        print('Thanks')
        break
    