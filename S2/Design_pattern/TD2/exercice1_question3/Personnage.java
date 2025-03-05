package exercice1_question3;

public abstract class Personnage {
	private String nom;
	
	public Personnage(String nom){
		this.nom=nom;
	}
	public String getNom(){
		return nom;
	}
    public abstract void animer();
}
