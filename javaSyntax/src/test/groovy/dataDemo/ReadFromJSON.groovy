package dataDemo

import groovy.json.JsonSlurper


String jsonEx = '..\\..\\resources\\JSON\\jsonEx.json'
def jsonRoot = new JsonSlurper().parse(new File(jsonEx))
println(jsonRoot)
println(jsonRoot.staff.department.name)
assert jsonRoot.staff.department.name == "sales"
assert jsonRoot.staff.department.employee.size() == 2
assert jsonRoot.staff.department.employee[0].firstName == "Orlando"
assert jsonRoot.staff.department.employee[0].lastName == "Boren"
assert jsonRoot.staff.department.employee[0].age == "24"
assert jsonRoot.staff.department.employee[1].firstName == "Diana"
assert jsonRoot.staff.department.employee[1].lastName == "Colgan"
assert jsonRoot.staff.department.employee[1].age == "28"