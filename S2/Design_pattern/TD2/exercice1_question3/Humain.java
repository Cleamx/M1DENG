package exercice1_question3;

public class Humain extends Personnage {
	public Humain(String nom){
		super(nom);
	}
	public void animer(){
		System.out.println("Le sage humain de nom "+ getNom()+ " se met � bouger");
	}

}
