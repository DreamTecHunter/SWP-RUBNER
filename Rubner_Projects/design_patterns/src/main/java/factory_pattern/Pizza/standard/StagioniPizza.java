package factory_pattern.Pizza.standard;

import factory_pattern.Pizza.PizzaAbstract;

public class StagioniPizza extends PizzaAbstract {
    @Override
    public void prepare() {
        this.text = this.getClass().getName();
    }
}
