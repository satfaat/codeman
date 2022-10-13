import csv


data = {
    'path_1': 'db.tst/tst.csv',
    'path_2': 'db.tst/output.csv',
    'path_3': 'db.tst/dict_output.csv'
}

dt_csv = [
    "first_name,last_name,city".split(","),
    "Tyrese,Hirthe,Strackeport".split(","),
    "Jules,Dicki,Lake Nickolasville".split(","),
    "Dedric,Medhurst,Stiedemannberg".split(",")
]

def csv_reader(csv_file, dict_reader):
    if dict_reader == 'on':
        """read a csv using DictReader"""
        csv_data = csv.DictReader(csv_file, delimiter=',')
        for line in csv_data:
            print(f'{line["first_name"]} {line["last_name"]}')
    else:
        """Read a csv file"""
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            print(" ".join(row))

def csv_writer(data, path):
    """
    write data to a csv
    """
    with open(path, "w", newline='') as csv_rewrite:
        csv_writer = csv.writer(csv_rewrite, delimiter=',')
        for line in data:
            csv_writer.writerow(line)

def r_open_csv(path, func, csv_reader):
    """
    csv_reader can be 'on' or 'off':
    on = with DictReader
    off = without DictReader
    """
    try:
        with open(path, 'r') as some_csv:
            func(some_csv, csv_reader)
    except FileNotFoundError:
        print(f"No such file: {path}")


if __name__ == "__main__":
    #r_open_csv(data['path_1'], csv_reader, "oon")
    #csv_writer(dt_csv, data['path_2'])
    print(dt_csv[0])