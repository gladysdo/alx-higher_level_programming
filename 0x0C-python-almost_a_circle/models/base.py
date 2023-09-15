#!/usr/bin/python3
import json
import csv
import os.path

class Base:
    """ Base class for object serialization and deserialization. """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes instances of the Base class. """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Converts a list of dictionaries to a JSON string. """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Saves a list of objects to a JSON file. """
        filename = "{}.json".format(cls.__name__)
        list_dic = []

        if list_objs:
            list_dic = [obj.to_dictionary() for obj in list_objs]

        json_data = cls.to_json_string(list_dic)

        with open(filename, 'w') as f:
            f.write(json_data)

    @staticmethod
    def from_json_string(json_string):
        """ Converts a JSON string to a list of dictionaries. """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Creates an instance of the class and updates attributes using a dictionary. """
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        else:
            new = cls(10)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ Loads a list of instances from a JSON file. """
        filename = "{}.json".format(cls.__name__)

        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as f:
            list_str = f.read()

        list_dict = cls.from_json_string(list_str)
        list_ins = [cls.create(**item) for item in list_dict]

        return list_ins

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Saves a list of objects to a CSV file. """
        filename = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        if list_objs:
            for obj in list_objs:
                list_dic = [obj.to_dictionary().get(key) for key in list_keys]
                matrix.append(list_dic)

        with open(filename, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(matrix)

    @classmethod
    def load_from_file_csv(cls):
        """ Loads a list of instances from a CSV file. """
        filename = "{}.csv".format(cls.__name__)

        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            csv_list = list(reader)

        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        for csv_elem in csv_list:
            dict_csv = {}
            for key, value in zip(list_keys, csv_elem):
                dict_csv[key] = int(value)
            matrix.append(dict_csv)

        list_ins = [cls.create(**item) for item in matrix]

        return list_ins
