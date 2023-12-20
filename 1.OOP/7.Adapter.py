import csv
import json


class JsonConverter:
    def __init__(self):
        self.__lines = []

    def read_file(self, filename: str):
        with open(filename, 'r') as jsonfile:
            lines = json.load(jsonfile)
            for line in lines:
                self.__lines.append(line)
            print(self.__lines)

    def write_file_1way(self, filename:str):
        with open(filename, 'w', newline='') as csvwriter:
            writer_csv = csv.writer(csvwriter)
            counter = 0
            for data in self.__lines:
                if counter == 0:
                    header = data.keys()
                    writer_csv.writerow(header)
                    counter += 1
                writer_csv.writerow(data.values())

    def write_file_2way(self, filename: str):
        fieldnames = ['first_name', 'last_name', 'age', 'gender', 'salary']
        with open(filename, 'w', newline='') as csvwriter:
            writer_csv = csv.DictWriter(csvwriter, fieldnames=fieldnames)
            writer_csv.writeheader()
            writer_csv.writerows(self.__lines)
        self.cleanup()

    def cleanup(self):
        self.__lines = []


converter = JsonConverter()
converter.read_file('file.json')
converter.write_file_1way('file1.csv')
converter.write_file_2way('file2.csv')
