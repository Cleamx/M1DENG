package exercice1_question1;

public class Orc extends Personnage {

	public Orc(String nom){
		super(nom);
	}
	public void animer(){
		System.out.println("Animation de l'orc de nom "+ getNom());
	}
}
