package exercice1_question1;

public class Troll extends Personnage {
	public Troll(String nom){
		super(nom);
	}
	public void animer(){
		System.out.println("Animation du troll de nom "+ getNom());
	}

}
