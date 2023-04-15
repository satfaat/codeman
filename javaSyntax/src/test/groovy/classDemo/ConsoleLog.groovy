package classDemo

import DTO.CatRecord
import javaClassDemo.Cat

println "Class vs Record"
println("Class hashCode >> " + Cat.hashCode())
println("Record hashCode >> " + CatRecord.hashCode())
println ""

println("Class toString >> " + Cat.toString())
println("Record toString >> " + CatRecord.toString())

println ""
println "Instance init"
Cat catA = new Cat("Sphin", 9, "wight");
CatRecord catRecA = new CatRecord("Spin", 9, "White")
CatRecord catPower = new CatRecord("9liver", 'Gold')

println "L O G"
println("Sphin from class hashCode >> " + catA.hashCode())
println("Spin from Record hashCode >> " + catRecA.hashCode())
println ""

println("Sphin from class toString >> " + catA.toString())
println("Spin from record toString >> " + catRecA.toString())
println("9liver from record toString >> " + catPower.toString())
println ""

println "Enums demo"
println EnumDemo.AUTH.toString().toLowerCase()