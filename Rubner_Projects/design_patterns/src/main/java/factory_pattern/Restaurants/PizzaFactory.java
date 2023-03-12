package factory_pattern.Restaurants;

import factory_pattern.Pizza.PizzaAbstract;

import java.util.HashMap;
import java.util.Map;


public abstract class PizzaFactory {
    private Map<String, PizzaAbstract> menu = new HashMap<String, PizzaAbstract>();

    public PizzaFactory(PizzaAbstract... pizzas) {
        for (int i = 0; i < pizzas.length; i++) {
            this.menu.put(pizzas[i].getClass().getSimpleName().toUpperCase(), pizzas[i]);
        }
    }

    public PizzaAbstract getPizza(String name) {
        // Is not needed, because the map accept null-input and returns null.
        /*
        if (name == null) {
            return null;
        }
        */
        return this.menu.get(name.toUpperCase());
    }
}
