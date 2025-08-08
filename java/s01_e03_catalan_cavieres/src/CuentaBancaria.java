package s01_e03_catalan_cavieres;

public class CuentaBancaria {

    // Atributos
    private float saldo;
    private String nombreTitular, rutTitular;
    
    // Constructores
    public CuentaBancaria() {    
    }

    public CuentaBancaria(float saldo, String nombreTitular, String rutTitular) {
        this.saldo = saldo;
        this.nombreTitular = nombreTitular;
        this.rutTitular = rutTitular;
    }
    

    // Setters    
    public void setSaldo(float saldo) {
        this.saldo = saldo;
    }

    public void setNombreTitular(String nombreTitular) {
        this.nombreTitular = nombreTitular;
    }

    public void setRutTitular(String rutTitular) {
        this.rutTitular = rutTitular;
    }
    

    // Getter
    public float getSaldo() {
        return this.saldo;
    }

    public String getNombreTitular() {
        return this.nombreTitular;
    }

    public String getRutTitular() {
        return this.rutTitular;
    }
    

    // Metodos
    
    public void depositarDinero(float deposito) {
        this.saldo = this.saldo + deposito;
    }

    public void retirarDinero(float retiro) {
        if (retiro <= this.saldo && retiro > 0) {
            this.saldo = this.saldo - retiro;
        }
        else {
            System.out.println("No hay saldo suficiente");
        }
    }

    public void mostrarSaldo() {
        System.out.println("Su saldo es: $" + this.saldo);
    }
}
