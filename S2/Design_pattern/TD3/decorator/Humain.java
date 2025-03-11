package TD3.decorator;

public class Humain extends Personnage {
	public Humain(String nom) {
		super(nom);
	}

	public void seDeplacer() {
		System.out.println("L'humain de nom " + getNom() + " commence à avancer.");
	}

}
