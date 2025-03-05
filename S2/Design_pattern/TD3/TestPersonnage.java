package TD3;

public class TestPersonnage {

		public static void main(String[] args) {
		Personnage s=new Troll("Diablo");
		s.courir();	
		s.marcher();
		s.sauter();

		Personnage t=new Tauren("Grom");
		t.courir();
		t.marcher();
		t.sauter();
	}

}
