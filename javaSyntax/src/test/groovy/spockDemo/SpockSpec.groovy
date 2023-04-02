package spockDemo

class SpockSpec extends spock.lang.Specification {
    def "Functions aka closures"(){
        when: "do math"
        Closure powerOf2 = { int n -> return n * 2}
        Closure sum2digits = { x,y -> x + y}

        then: "double numbers"
        assert powerOf2(3) == 6
        assert sum2digits(3,5) ==8
        assert sum2digits(3,sum2digits(2,5)) == 10
    }

    def "Data generator 1"(){
        given: "Setup"
        Expando smartIterator = new Expando()
        smartIterator.counter = 0;
        smartIterator.limit = 4;
        smartIterator.hasNext = { return counter < limit}
        smartIterator.next = {return counter++}
        smartIterator.restartFrom = {from->counter = from}

        String castToStr = String.valueOf(1234)

        println(smartIterator.dump())
        println "$castToStr ${castToStr.getClass()}"

        when:
        for(Integer number:smartIterator as Iterator<Integer>)
        {
            println "Next number is $number"
        }
        println "Reset smart iterator"
        smartIterator.restartFrom(2)

        then:
        for(Integer number:smartIterator as Iterator<Integer>)
        {
            println "Next number is $number"
        }
    }

    def "demo for Spock assert lists"() {
        when:
        List<String> all = ["Vorlon","Shadows","Minbari", "Humans","Drazi"]
        List<String> firstOnes = ["Vorlon","Shadows"]

        then:
        all.subList(0, all.indexOf("Humans")) != firstOnes
    }
}
