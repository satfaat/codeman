package groovyDemo

def createName(String firstName,String lastName)
{
    return "$lastName, $firstName"
}

def createMilitaryName(def firstName,def lastName, def rank)
{
    return "$lastName, $firstName ($rank)"
}

def fullName = createName "Susan","Ivanova"
println fullName

def militaryName = createMilitaryName "Susan","Ivanova","Commander"
println militaryName