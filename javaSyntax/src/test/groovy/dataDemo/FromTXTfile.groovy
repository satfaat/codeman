package dataDemo

String fileDemo = "..\\..\\resources\\notes\\noteEx.txt"

String testInput = new File(fileDemo).text
println(testInput)

println ""
List<String> inputText = new File(fileDemo).readLines()
for (String line : inputText) {
    println("Read by line... " + line)
}