#!/usr/bin/env python3
import sys
import os
import csv


class CarBase:
    """Базовый класс с общими методами и атрибутами"""

    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        self.car_type = car_type

    def get_photo_file_ext(self):
        exp = os.path.splitext(self.photo_file_name)
        return exp[1]


class Car(CarBase):
    """Класс легковой автомобиль"""

    def __init__(self, car_type, brand, photo_file_name, carrying,
                 passenger_seats_count):

        super().__init__(car_type, brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    """Класс грузовой автомобиль"""

    def __init__(self, car_type, brand, photo_file_name, carrying,
                 body_whl="", body_length=None, body_width=None,
                 body_height=None):

        super().__init__(car_type, brand, photo_file_name, carrying)
        self.body_whl = body_whl
        self.body_length = body_length
        self.body_width = body_width
        self.body_height = body_height

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.extra = extra


def parse(whl):

    if whl == "":
        list_whl = [0, 0, 0]
        return list_whl

    else:
        try:
            body_length, body_width, body_height = whl.split('x')
            if body_height != '' and body_width != '' and body_length != '':
                list_whl = [body_length, body_width, body_height]
            else:
                list_whl = None
            return list_whl
        except ValueError:
            return None


def get_car_list(csv_filename):

    # это наш список, который будем возвращать
    car_list = []

    with open(csv_filename) as csv_fd:
        # создаем объект csv.reader для чтения csv-файла
        reader = csv.reader(csv_fd, delimiter=';')

        # пропускаем заголовок
        next(reader)

        for row in reader:

            if len(row) == 7:

                if row[0] == 'car':

                    try:
                        car_obj = Car(row[0], row[1], row[3], float(row[5]),
                                      int(row[2]))
                        car_list.append(car_obj)

                    except ValueError:
                        pass

                if row[0] == 'truck':

                    temp_list = parse(row[4])

                    if temp_list is not None:
                        try:

                            truck_obj = Truck(row[0], row[1], row[3],
                                              float(row[5]), row[4],
                                              float(temp_list[0]),
                                              float(temp_list[1]),
                                              float(temp_list[2]))
                            car_list.append(truck_obj)

                        except ValueError:
                            pass

                if row[0] == 'spec_machine':
                    try:
                        spec_machine_obj = SpecMachine(row[0], row[1],
                                                       row[3],
                                                       float(row[5]), row[6])
                        car_list.append(spec_machine_obj)

                    except ValueError:
                        pass

    return car_list


if __name__ == "__main__":
    print(get_car_list(sys.argv[1]))
