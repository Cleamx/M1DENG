package TD1.ex1;

public abstract class Joueur {
    protected Strategy strategy;

    public void setStrategy(Strategy strategy) {
        this.strategy = strategy;
    }

    public void jouer() {
        strategy.jouer();
    }
}