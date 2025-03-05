package exercice1_question1;

/**
 * @author  vittori_e
 */
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
