package TD3.decorator;

public class Orage extends Pouvoir {
    public Orage(Personnage personnage) {
        super(personnage);
    }

    public void seDeplacer() {
        super.seDeplacer();
        System.out.println("L'orage gronde.");
    }
    
}
