package TD1.ex2;

public class Jeu {

    public static void main(String[] args) {
        Personnage p = new Tauren("Diablo");
		System.out.println(p.toString());
        p.seBattre(); 

        p.changerArme(new Epee());
        p.seBattre(); 
        p.seDeplacer();
    }
}