package exercice1_question3;

public class Troll extends Personnage {
	public Troll(String nom){
		super(nom);
	}
	public void animer(){
		System.out.println("Le troll de nom "+ getNom()+ " s'anime");
	}

}
