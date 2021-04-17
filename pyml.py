import yaml


users_f = 'db/users.yaml'  # file path for record/ read
tst_f = 'db/tstconf.yaml'  # file path for record/ read

users = [
    {
        'name': 'Smith',
        'occupation': 'gardener'
    },
    {
        'name': 'Lucy',
        'occupation': 'teacher'
    }
]

article_info = [
    {
        'Details': {
        'domain' : 'www.tutswiki.com',
        'language': 'python',
        'date': '11/09/2020'
        }
    }
]


def read_this(file):
    with open(file, "r") as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.FullLoader)
        print("Read successful")
    print(data)


def update_yml(file):
    with open(file, "r") as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.FullLoader)
        #print(data)
        #print("Read successful")
        data[0]['Details']['language'] = 'rust'
        #print('value of language updated')
    return data


def record_dt(file):
    with open(file, 'a') as yamlfile:  # a or w as second perameter
        data = yaml.dump(article_info, yamlfile)
        #data = yaml.dump(update_yml(tst_f), yamlfile)  # not working so
        #sorted = yaml.dump(users, sort_keys = True)
        print("Write successful")


# run functions
#read_this(tst_f)
record_dt(tst_f)
#data = update_yml(tst_f)
#print(data, type(data))
