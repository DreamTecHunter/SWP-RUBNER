package factory_pattern.Restaurants;

import factory_pattern.Pizza.BerlinPizzas.BerlinSalamiPizza;
import factory_pattern.Pizza.standard.HawaiiPizza;
import factory_pattern.Pizza.standard.SalamiPizza;
import factory_pattern.Pizza.standard.StagioniPizza;

public class BerlinPizzeria extends PizzaFactory {
    public BerlinPizzeria() {
        super(
                new BerlinSalamiPizza(),
                new SalamiPizza(),
                new StagioniPizza(),
                new HawaiiPizza()
        );
    }
}
