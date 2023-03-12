package factory_pattern.Restaurants;

import factory_pattern.Pizza.standard.HawaiiPizza;
import factory_pattern.Pizza.standard.SalamiPizza;
import factory_pattern.Pizza.standard.StagioniPizza;

public class RostockPizzeria extends PizzaFactory {
    public RostockPizzeria() {
        super(
                new SalamiPizza(),
                new HawaiiPizza(),
                new StagioniPizza()
        );
    }
}
