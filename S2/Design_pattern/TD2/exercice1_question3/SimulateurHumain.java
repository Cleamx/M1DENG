package exercice1_question3;

public class SimulateurHumain extends Simulateur {

	public SimulateurHumain(String nom){
		super(nom);
	}

	public Personnage getPersonnage(String nom){
	     return new Humain(nom);
	}

}
