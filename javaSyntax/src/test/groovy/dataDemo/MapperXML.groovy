package dataDemo

import com.fasterxml.jackson.dataformat.xml.XmlMapper
import groovy.xml.XmlSlurper
import groovy.xml.slurpersupport.GPathResult


record Person(
        int age,
        String name
) {}

Person John = new Person(30, "John")

println("java object to xml")
XmlMapper xmlMapper = new XmlMapper()
String myXML = xmlMapper.writeValueAsString(John)
println("XML string from object: $myXML")


String xmlEx = '..\\..\\resources\\XML\\xmlEx.xml'
GPathResult xmlRoot = new XmlSlurper().parse(xmlEx)
assert xmlRoot.department.size() == 1
assert xmlRoot.department.@name == "sales"
assert xmlRoot.department.employee.size() == 2
assert xmlRoot.department.employee[0].firstName == "Orlando"
assert xmlRoot.department.employee[0].lastName == "Boren"
assert xmlRoot.department.employee[0].age == 24
assert xmlRoot.department.employee[1].firstName == "Diana"
assert xmlRoot.department.employee[1].lastName == "Colgan"
assert xmlRoot.department.employee[1].age == 28