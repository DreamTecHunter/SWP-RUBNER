package factory_pattern;

import factory_pattern.Restaurants.BerlinPizzeria;
import factory_pattern.Restaurants.PizzaFactory;

import java.util.HashMap;
import java.util.Map;

public class Playground {
    private static Map<String, String> test = new HashMap<String, String>();

    public static void main(String[] args) {
        PizzaFactory bp = new BerlinPizzeria();
        System.out.println("Does " + bp.getClass().getSimpleName() + " has a Salami-pizza?");
        System.out.println("they have " + bp.getPizza("salamipizza"));
    }
}
