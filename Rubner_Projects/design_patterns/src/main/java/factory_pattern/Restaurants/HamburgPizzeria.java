package factory_pattern.Restaurants;

import factory_pattern.Pizza.standard.CalzonePizza;
import factory_pattern.Pizza.standard.QuattroPizza;
import factory_pattern.Pizza.standard.SalamiPizza;

public class HamburgPizzeria extends PizzaFactory {
    public HamburgPizzeria(){
        super(
                new SalamiPizza(),
                new CalzonePizza(),
                new QuattroPizza()
        );
    }
}
