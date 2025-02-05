
public class Personnage {

	private String nom;
	private String categorie;
	private String arme;

	public Personnage(String nom, String categorie) {
		this.nom = nom;
		this.categorie = categorie;
		if (categorie.equals("Tauren"))
			arme = "Bouclier";
		else if (categorie.equals("Orc"))
			arme = "Baton";
		else if (categorie.equals("Troll"))
			arme = "Dague";
		else if (categorie.equals("Humain"))
			arme = "Epee";
		else
			arme = null;
	}

	public void seBattre() {
		if (arme.equals("Bouclier"))
			System.out.println(this + " se d�fend avec son Bouclier");
		else if (arme.equals("Baton"))
			System.out.println(this + " frappe avec son baton");
		else if (arme.equals("Epee"))
			System.out.println(this + " combat avec son �pee");
		else if (arme.equals("Dague"))
			System.out.println(this + " utilise sa dague pour se battre");
		else
			System.out.println(this + " ne peut pas se battre");
	}

	public String toString() {
		return nom + " (" + categorie + ") ";
	}

	public void changerArme(String arme) {
		this.arme = arme;
	}
}
