
import faker as fake
import datetime
import time
import random

customer_id = 0
f = fake.Faker()
def address_gen():
    add = [i for i in f.address().split('\n')]
    address = ''
    for i in add:
        address += i + ' '
    return address
def compare_times(time1,time2):
    if int(time1.split(':')[0]) + 5 > int(time2.split(':')[0]):
        time11 = datetime.datetime.strptime(time1, '%H:%M:%S')
        time22 = datetime.datetime.strptime(time2, '%H:%M:%S')
        return time22 > time11
    else:
        return False
def addres_check(pick,drop):
    if pick != drop:
        return True




def generate():
    globals()['customer_id'] += 1
    booking_date = f.date()
    booking_time = f.time()
    pick_up_address = address_gen()
    pick_flag = True
    pick = ''
    while pick_flag:
        pick = f.time()
        if compare_times(booking_time,pick):
            pick_flag = False
    
    drop_flag = True
    drop = ''
    while drop_flag:
        drop = f.time()
        if compare_times(pick,drop):
            drop_flag = False
    drop_address = address_gen()
    add_flag = True
    while add_flag:
        if addres_check(pick_up_address,drop_address):
            add_flag = False

        


    return f'{customer_id};{booking_date};{booking_time};{pick_up_address};{pick};{drop};{drop_address}'

while True:
    no = random.randint(10,100)
    count = 0
    data = ''
    for i in range(1,no+1):
        count = count + 1
        data = data + generate()+'\n'
    filename = f'uber_data_{time.time()}_{count+1}.log'
    file = open('C:\\Users\\rakray\\Documents\\Deloitte_Training\\case_study_2\\code\\deloitte-case-study-2\\logs\\{}'.format(filename),'w')
    file.write(data)
    file.close()
    time.sleep(10)