import time 

my_time = int(input('Enter time : '))

while my_time > 0:
    print(f'00:{00}:{my_time:02}')
    time.sleep(1)
    my_time -= 1


print('Time is up')
