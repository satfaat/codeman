import yaml

if __name__ == '__main__':

    with open('foo.yaml', 'r') as stream:
        dictionary = yaml.load(stream)
        for key, value in dictionary.items():
            print (key + " : " + str(value))

    # reading from csv files
    with open("test.csv", mode="r") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            print(row)