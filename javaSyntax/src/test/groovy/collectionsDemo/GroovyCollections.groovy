package collectionsDemo

println "Creating a map in Java"
Map<String, Integer> wordCounts = new HashMap<>();
wordCounts.put("Hello", 1);
wordCounts.put("Java", 1);
wordCounts.put("World", 2);

println "DICTIONARY, Creating a map in Groovy"
Map<String, Integer> wordCounts2 = ["Hello": 1, "Groovy": 1, "World": 2]


// LIST
List<String> races = Arrays.asList("Drazi", "Minbari", "Humans")

List<String> races2 = ["Drazi", "Minbari", "Humans"]

assert races == races2

String[] racesArray = ["Drazi", "Minbari", "Humans"]

assert racesArray[0] == "Drazi"
assert races[0] == "Drazi"
assert racesArray.size() == races2.size()

//Accessing lists
List<String> humanShips = ["Condor", "Explorer"]
assert humanShips.get(0) == "Condor"
assert humanShips[0] == "Condor"

humanShips.add("Hyperion")
humanShips << "Nova" << "Olympus"
assert humanShips[3] == "Nova"
assert humanShips[4] == "Olympus"
humanShips[3] = "Omega"
assert humanShips[3] == "Omega"

//Using an non-existing index
humanShips[8] = "Warlock"
assert humanShips[8] == "Warlock"
assert humanShips[7] == null


//Accessing maps
Map<String, String> personRoles = [:]
personRoles.put("Suzan Ivanova", "Lt. Commander")
personRoles["Stephen Franklin"] = "Doctor"

assert personRoles.get("Suzan Ivanova") == "Lt. Commander"
assert personRoles["Stephen Franklin"] == "Doctor"

personRoles["Suzan Ivanova"] = "Commander"
assert personRoles["Suzan Ivanova"] == "Commander"

// LinkedHashMap<String,String>
def dict_1 = [
        login : "path/point",
        search: "path/point2"
]
def dict_2 = [
        freeSeat: "path/point3",
        clean   : "path/point4"
]
println(dict_1.login)
dict_1.putAll(dict_2)
println(dict_1)