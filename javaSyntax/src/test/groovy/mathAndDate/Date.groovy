package mathAndDate


import java.time.LocalDate
import java.time.format.DateTimeFormatter

println "New date >> " + new Date()
println ""

LocalDate datePlus7 = LocalDate.parse("2023-03-28").plusMonths(7)

println(datePlus7)
println(datePlus7.getClass())

String datePlus7Str = datePlus7.toString()
println(datePlus7Str)

def today = LocalDate.now()
println("today: $today")

String datePlus7auto = LocalDate.now().plusMonths(7).toString()
println("today + 7 month: $datePlus7auto")

LocalDate depDate = LocalDate.now().plusDays(15)

println depDate.toString()
String depDateFormatted = depDate.format(DateTimeFormatter.ofPattern("dd.MM.yyyy"))
println "Formatted date: >> " + depDateFormatted