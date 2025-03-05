package exercice1_question1;


/**
 * @author  vittori_e
 */
public class Simulateur {
 
	private Personnage monPersonnage;
		
		
		public Simulateur(String typePersonnage, String nom){
		
				if (typePersonnage.equals("troll"))
					monPersonnage=new Troll(nom);
				else if (typePersonnage.equals("orc"))
					     monPersonnage=new Orc(nom);
				    else  if (typePersonnage.equals("humain"))
						monPersonnage=new Humain(nom);
			 }
	public void simuler(){
		monPersonnage.animer();
	}
}
