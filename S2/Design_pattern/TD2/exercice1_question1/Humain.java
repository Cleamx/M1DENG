package exercice1_question1;

public class Humain extends Personnage {
	public Humain(String nom){
		super(nom);
	}
	public void animer(){
		System.out.println("Animation de l'humain de nom "+ getNom());
	}

}
