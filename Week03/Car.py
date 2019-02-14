import os
import csv


class BaseCar:

    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[-1]

class Car(BaseCar):
    
    def __init__(self, car_type, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__('car', brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count


class Truck(BaseCar):

    def __init__(self, car_type, brand, photo_file_name, carrying, body_width, body_height, body_length):
        super().__init__('truck', brand, photo_file_name, carrying)
        self.body_length = body_length
        self.body_width = body_width
        self.body_height = body_height

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(BaseCar):
    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        super().__init__('spec_machine', brand, photo_file_name, carrying)
        self.extra = extra


def parse_whl(whl):
    try:
        return [float(x) for x in whl.split('x')]
    except:
        return [None, None, None]

def get_car_list(csv_filepath):
    car_list = []
    with open(csv_filepath) as csv_f:
        reader = csv.reader(csv_f, delimiter=';')
        next(reader)
        for row in reader:
            try:
                car_type = row[0]
                brand = row[1]
                carrying = float(row[5])
                photo_file_name = row[3]
                if car_type == 'car':
                    passenger_seats_count = int(row[2])
                    car_list.append(Car(car_type, brand, photo_file_name, carrying, passenger_seats_count))                              

                elif car_type == 'truck':
                    whl = parse_whl(row[4])
                    print(*whl)
                    car_list.append(Truck(car_type, brand, photo_file_name, carrying, *whl))

                elif car_type == 'spec_machine':
                    extra = row[6]
                    car_list.append(SpecMachine(car_type, brand, photo_file_name, carrying, extra))

                else:
                    raise ValueError('Incorrect car_type')
            except Exception as err:
                print(err)
                continue
    return car_list

#get_car_list('F:\\Уроки\\CourseraSpec\\coursera_week3_cars.csv')

#matruck = Truck('truck', 'Man', 'file.png', 20, 8.0, 3.0, 2.5)
#print(matruck.body_width)
