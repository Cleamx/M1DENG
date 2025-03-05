package exercice1_question3;

public class SimulateurOrc extends Simulateur {

	public SimulateurOrc(String nom){
		super(nom);
	}

	public Personnage getPersonnage(String nom){
	     return new Orc(nom);
	}

}
