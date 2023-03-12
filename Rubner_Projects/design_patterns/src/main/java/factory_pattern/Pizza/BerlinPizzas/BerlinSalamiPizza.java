package factory_pattern.Pizza.BerlinPizzas;

import factory_pattern.Pizza.standard.SalamiPizza;

public class BerlinSalamiPizza extends SalamiPizza {
    @Override
    public void prepare() {
        this.text = "SpecialBerlin" + this.text;
    }
}
