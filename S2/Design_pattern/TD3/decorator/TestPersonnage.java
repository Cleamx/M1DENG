package TD3.decorator;

public class TestPersonnage {

	public static void main(String[] args) {
		Personnage p = new Humain("Titi");
		p.seDeplacer();

		Personnage p1 = new Orage(new Humain("Toto"));
		p1.seDeplacer();
	}
}
