package exercice1_question3;

public class SimulateurTroll extends Simulateur {
	
	public SimulateurTroll(String nom){
		super(nom);
	}

	public Personnage getPersonnage(String nom){
	     return new Troll(nom);
	}
}
