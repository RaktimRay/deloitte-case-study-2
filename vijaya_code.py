import faker as fake
import datetime
import time
import random


gender_dict = {}


f = fake.Faker()
def address_gen():
    add = [i for i in f.address().split('\n')]
    address = ''
    for i in add:
        address += i + ' '
    return address

# book and pick 5 to 15 min
def pick_gen(book_time):
    min_list = list(range(5,16))
    min = random.choice(min_list)
    # b = datetime.datetime.strptime(book_time, '%H:%M:%S')
    return (book_time  + datetime.timedelta(minutes=min))
# pick  and drop 15 to 120 min
def drop_gen(pick_time):
    min_list = list(range(15,120))
    min = random.choice(min_list)
    # b = datetime.datetime.strptime(pick_time, '%H:%M:%S')
    return (pick_time  + datetime.timedelta(minutes=min))
# check address
def addres_check(pick,drop):
    if pick != drop:
        return True

# price cal
def price(min):
    res  = 3 * min + random.randint(1,55)
    return res



customer_id_list = [i for i in range(100,1001)]
def generate():
    customer_id = random.choice(customer_id_list)
    booking_date = datetime.datetime.now().date()
    booking_time = datetime.datetime.now().time()
    book_date_time = datetime.datetime.now()
    pick_date_time = pick_gen(book_date_time)
    pick_time = pick_date_time.time()
    drop_date_time = drop_gen(pick_date_time)
    drop_time = drop_date_time.time()
    pick_up_address = address_gen()
    drop_address = address_gen()
    add_flag = True
    while add_flag:
        if addres_check(pick_up_address,drop_address):
            add_flag = False
    
    if customer_id in gender_dict.keys():
        gender = gender_dict[customer_id]
    else:
        gender = (random.choice(["male", "female"]))
        gender_dict[customer_id] = gender
    minutes_of_ride = (drop_date_time - pick_date_time).total_seconds() /60
    price_val = price(minutes_of_ride)
    
    return f'{customer_id};{gender};{booking_date};{booking_time};{pick_up_address};{pick_time};{drop_time};{drop_address};{price_val}'

while True:
    no = random.randint(20,101)
    data = ''
    for i in range(1,no+1):
        data = data + generate()+'\n'
    filename = f"uber_data_{(datetime.datetime.now().date())}_{(datetime.datetime.now().hour)}_{(datetime.datetime.now().minute)}_{(datetime.datetime.now().second)}.log"
    file = open('C:\\sample\\{}'.format(filename),'w')
    file.write(data)
    file.close()
    time.sleep(10)
