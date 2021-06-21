import yaml


file = 'db/tstconf.yaml'

def read_this(file):
    with open(file, "r") as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.FullLoader)
        print("Read successful")
    print(data)

read_this(file)