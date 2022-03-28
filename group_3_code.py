
def main():
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



    customer_id_list = [i for i in range(101,1001)]
    def generate():
        customer_id = random.choice(customer_id_list)
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
        
        if customer_id in gender_dict.keys():
            gender = gender_dict[customer_id]
        else:
            gender = (random.choice(["male", "female", "other"]))
            gender_dict[customer_id] = gender
        return f'{customer_id};{gender};{booking_date};{booking_time};{pick_up_address};{pick};{drop};{drop_address}'

    while True:
        no = random.randint(20,101)
        count = 0
        data = ''
        for i in range(1,no+1):
            count = count + 1
            data = data + generate()+'\n'
        timestr = time.strftime("%d_%m_%Y_%H_%M_%S")
        filename = f'uber_data_{timestr}.log'
        file = open('C:\\Users\\rakray\\Documents\\Deloitte_Training\\case_study_2\\code\\deloitte-case-study-2\\logs\\{}'.format(filename),'w')
        file.write(data)
        file.close()
        print("log created")
        time.sleep(10)

if __name__ == "__main__":
    main()
