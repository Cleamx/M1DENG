package TD3.adapter;

public abstract class Personnage implements Deplacable{
	private String nom;
	public Personnage(String nom){
		this.nom=nom;
	}
	public String getNom(){
		return nom;
	}
	public void courir(){
		System.out.println(getNom() + " : le "+ this.getClass().getSimpleName()+ " se met à  courir");
	}
	public void sauter(){
		System.out.println(getNom() + " : le "+  this.getClass().getSimpleName()+ " saute");
	}
	public void marcher(){
		System.out.println(getNom() + " : le " + this.getClass().getSimpleName()+ " se met à  marcher");
	}

 }
