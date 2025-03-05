package exercice1_question3;

public class Orc extends Personnage {

	public Orc(String nom){
		super(nom);
	}
	public void animer(){
		System.out.println("L'orc terrifiant de nom "+ getNom()+" s'agite");
	}
}
