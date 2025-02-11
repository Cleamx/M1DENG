package TD1.ex2;

public class Marche implements DeplacementStrategy {

    private boolean aDesChaussures = true;
    
    public void setChaussures(boolean aDesChaussures) {
        this.aDesChaussures = aDesChaussures;
    }

    @Override
    public void seDeplacer() {
        if (aDesChaussures) {
            System.out.println("Je me déplace en marchant");
        } else {
            System.out.println("Je ne peut pas me déplacer sans chaussures");
        }
    }
}