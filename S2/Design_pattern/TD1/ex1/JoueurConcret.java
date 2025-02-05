package TD1.ex1;

public class JoueurConcret extends Joueur {
    public JoueurConcret() {
        this.strategy = new StrategieDefense(); 
    }
}