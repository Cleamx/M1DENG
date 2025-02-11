package TD1.ex2;

public abstract class Personnage {
    protected String nom;
    protected String categorie;
    protected ArmeStrategy arme;
    protected DeplacementStrategy deplacement;


    public Personnage(String nom, String categorie, ArmeStrategy arme, DeplacementStrategy deplacement) {
        this.nom = nom;
        this.categorie = categorie;
        this.arme = arme;
        this.deplacement = deplacement;
    }

    public void seBattre() {
        arme.utiliserArme();
    }

    public void changerArme(ArmeStrategy arme) {
		System.out.println("La nouvelle arme est " + arme);
        this.arme = arme;
    }

    public void seDeplacer() {
        deplacement.seDeplacer();
    }

    @Override
    public String toString() {
        return nom + " (" + categorie + ")";
    }
}