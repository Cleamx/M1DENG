package TD1.ex1;

public class TestJoueur {
    public static void testerJoueur() {
        Joueur joueur = new JoueurConcret();

        System.out.println("Test avec stratégie défense:");
        joueur.jouer();

        System.out.println("\nTest avec changement de stratégie en attaque:");
        joueur.setStrategy(new StrategieAttaque());
        joueur.jouer();
    }

    public static void main(String[] args) {
        testerJoueur();
    }
}