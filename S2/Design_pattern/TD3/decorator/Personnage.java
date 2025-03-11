package TD3.decorator;

public abstract class Personnage {
	private String nom;

	public Personnage(String nom) {
		this.nom = nom;
	}

	public String getNom() {
		return nom;
	}

	public abstract void seDeplacer();
}
