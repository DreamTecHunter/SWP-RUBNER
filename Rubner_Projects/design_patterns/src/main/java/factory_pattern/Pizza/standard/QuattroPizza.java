package factory_pattern.Pizza.standard;

import factory_pattern.Pizza.PizzaAbstract;

public class QuattroPizza extends PizzaAbstract {
    @Override
    public void prepare() {
        this.text = this.getClass().getName();

    }
}
