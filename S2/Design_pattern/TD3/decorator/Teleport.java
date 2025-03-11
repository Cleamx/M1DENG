package TD3.decorator;

public class Teleport extends Pouvoir {
    public Teleport(Personnage personnage) {
        super(personnage);
    }

    public void seDeplacer() {
        super.seDeplacer();
        System.out.println("Le personnage se téléporte.");
    }
    
}
