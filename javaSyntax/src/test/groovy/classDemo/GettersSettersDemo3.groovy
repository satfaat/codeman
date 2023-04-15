package classDemo


class Person2 {
    String firstName
    String lastName
    int age
    String rank
}

Person2 susan = new Person2()
susan.firstName = "Susan"
susan.lastName = "Ivanova"
susan.rank = "Commander"

println "Person first name is $susan.firstName"
println "Person last name is $susan.lastName"
println "Person rank is $susan.rank"

susan.with {
    assert firstName == "Susan"
    assert lastName == "Ivanova"
    assert rank == "Commander"
}

Person2 lyta = new Person2()
lyta.setFirstName("Lyta")
lyta.setLastName("Alexander")

// groovy style
Person2 marcus = new Person2()
marcus.firstName = "Marcus"
marcus.lastName = "Cole"

println ""
System.out.println("Person first name is " + lyta.getFirstName())
System.out.println("Person last name is " + lyta.getLastName())

// groovy style
println ""
println("Person first name is " + marcus.firstName)
println("Person last name is " + marcus.lastName)
