package DTO;

public record CatRecord (String name, int numberOfLives, String color) {
    public CatRecord(String name, String color) {
        this(name, 9, color);
    }
}
