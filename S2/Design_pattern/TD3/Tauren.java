package TD3;

public class Tauren extends Personnage {
    private TaurenEtranger taurenEtranger;

    public Tauren(String nom){
        super(nom);
        taurenEtranger = new TaurenEtranger();
    }

    @Override
    public void marcher() {
        taurenEtranger.avancer();
    }

    @Override
    public void courir() {
        taurenEtranger.trotter();
    }

    @Override
    public void sauter() {
        System.out.println("Le tauren saute!");
    }
    
}
