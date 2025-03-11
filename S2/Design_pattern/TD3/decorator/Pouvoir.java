package TD3.decorator;

public abstract class Pouvoir extends Personnage{
    public Personnage personnage;

    public Pouvoir(Personnage personnage) {
        super(personnage.getNom());
        this.personnage = personnage;
    }

    public void seDeplacer() {
        this.personnage.seDeplacer();
    }
}
