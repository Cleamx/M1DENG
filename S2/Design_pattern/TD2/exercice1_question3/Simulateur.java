package exercice1_question3;

public abstract class Simulateur {
    private Personnage monPersonnage;
	public Simulateur(String nom){
			monPersonnage=getPersonnage(nom);
	}
	public abstract Personnage getPersonnage(String nom);
	
	public void simuler(){
		monPersonnage.animer();
	}
}
