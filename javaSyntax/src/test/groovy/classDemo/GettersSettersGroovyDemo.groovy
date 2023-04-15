package classDemo

import DTO.PersonR

class GettersSettersGroovyDemo {
    static void main(String[] args){
        PersonR person = new PersonR(
                "John",
                "Strong",
                30,
                "Commander"
        )

        println "Person first name is $person.firstName"
        println "Person last name is $person.lastName"
        println "Person rank is $person.rank"
    }
}
