package classDemo

import groovy.json.JsonSlurper
import groovy.transform.CompileStatic
import groovy.transform.Immutable
import groovy.transform.stc.POJO
import lombok.Data

@POJO
@Immutable
@CompileStatic
class PojoPoint {
    int x, y

    static void main(String[] args) {
        PojoPoint point = new PojoPoint(1, 1)
        println(point.toString())
        println(point.dump())
        println(point.x)
    }
}

public record PersonDTO(String firstName, String lastName, int age) {}

println("DTO: " + PersonDTO)
println("DTO extended: " + PersonDTO.dump())

record Address(String country, String city) {}

public record Employee(int id,
                       String firstName,
                       String lastName
) {}

println("Employee DTO: " + Employee.dump())
println("Employee DTO: " + Employee.toString())
println("======")

println("======Nested Record")

record Rectangle(int length, int width) {
    record BigRectangle(int num) {
        public BigRectangle {
            num = num * 2;
        }
    }
}


Employee e1 = new Employee(1001, "Derok", "Dranf");
println(e1.dump())
System.out.println(e1.toString());
System.out.println(e1.toString().getClass());

class Account {
    String id
    BigDecimal value
    Date createdAt
}

def jsonSlurper = new JsonSlurper()
Account account = jsonSlurper.parseText('{"id":"123", "value":15.6 }') as Account
Account account2
        = jsonSlurper.parseText('{"id":"123","createdAt":"2018-01-01T02:00:00+0000"}') as Account
Object objPerson1 = jsonSlurper.parseText('{ "name": "John", "ID" : "1"}')
println(account.dump())
println(objPerson1)


final String jsonSearch = """
                {"adults": 3,
                "children": 1,
                "infants": 3,
                "infantsWithSeats": 0,
                "departureAirport": "LED",
                "departureDateThere": "2023-07-20",
                "arrivalAirport": "SVO",
                "departureDateBack": "2023-08-20",
                "serviceClass": "E"}""";
println(jsonSearch)

println("How to use lombok @Data")

@Data
public class DemoDTO {
    /*
    * Data transport object aka DTO
    * */

    private Integer status;
    private String message;
    private Body body;

    @Data
    static class Body {
        private String orderId;
    }
}

println("====== Lombok data demo: " + DemoDTO.dump())

DemoDTO demoDTO1 = new DemoDTO()
demoDTO1.setProperty("status", 123)
demoDTO1.setProperty("message", "msg")
DemoDTO.Body demoBody = new DemoDTO.Body()
demoBody.setProperty("orderId", "Some order id")
demoDTO1.setProperty("body", demoBody)

println(demoDTO1.dump())
println(demoDTO1.toString())
println(demoBody.dump())