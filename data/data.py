import yaml

if __name__ == '__main__':

    with open('foo.yaml', 'r') as stream:
        dictionary = yaml.load(stream)
        for key, value in dictionary.items():
            print (key + " : " + str(value))