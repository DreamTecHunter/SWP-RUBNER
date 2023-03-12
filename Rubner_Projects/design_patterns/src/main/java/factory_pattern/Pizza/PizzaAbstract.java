package factory_pattern.Pizza;

public abstract class PizzaAbstract {
    public String text = "";

    public abstract void prepare();

    public void bake() {
        System.out.println("baked");
    }

    public void cut() {
        System.out.println("cut");
    }

    public void boxUp() {
        System.out.println("boxed up");
    }

    @Override
    public String toString() {
        return text;
    }
}
