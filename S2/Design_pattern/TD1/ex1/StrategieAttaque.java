package TD1.ex1;

public class StrategieAttaque implements Strategy {
    @Override
    public void jouer() {
        System.out.println("Joue en attaque");
    }
}