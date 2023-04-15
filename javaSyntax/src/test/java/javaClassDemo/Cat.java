package javaClassDemo;

import java.util.Objects;

public class Cat {
    private final String name;
    private final int numberOfLives;
    private final String color;

    public Cat(String name, int numberOfLives, String color) {
        this.name = name;
        this.numberOfLives = numberOfLives;
        this.color = color;
    }

    public String getName() {
        return name;
    }

    public int getNumberOfLives() {
        return numberOfLives;
    }

    public String getColor() {
        return color;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Cat cat = (Cat) o;
        return numberOfLives == cat.numberOfLives &&
                Objects.equals(name, cat.name) &&
                Objects.equals(color, cat.color);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, numberOfLives, color);
    }

    @Override
    public String toString() {
        return "Cat{" +
                "name='" + name + '\'' +
                ", numberOfLives=" + numberOfLives +
                ", color='" + color + '\'' +
                '}';
    }
}
