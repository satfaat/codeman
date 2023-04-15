package classDemo;

public enum EnumDemo {
    AUTH("auth"),
    HOME("home");

    private final String endpoint;

    EnumDemo(String endpoint) {
        this.endpoint = endpoint;
    }
}
