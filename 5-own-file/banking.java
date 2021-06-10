import java.util.HashMap;
import java.util.Map; 
import java.util.List;

/*This two enums help to distinguish accounts with money, employees, and customers*/
public enum Cash {EMPTY, NON_EMPTY;}
public enum Who {CUSTOMER, EMPLOYEE;}
/*The people class has the requires information of a person in a banking system*/
public class people {
    private String name;
    private Integer dateOfBirth; 
    private Integer SSN;
    
    public people(String name, Integer dateOfBirth, Integer SSN) {
        this.name = name;
        this.dateOfBirth = dateOfBirth;
        this.SSN = SSN; 
    }
}

/*Customer extends the people class, and can be identified my CUSTOMER enum.*/
public class customers extends people {
    private Integer customerId;
    private Who who;
    private customers (String name, Integer dateOfBirth, Integer SSN, Integer customerId, Who who) {
        super(name,dateOfBirth,SSN);
        this.customerId = customerId;
        this.who = who;
    }
    /*Returns customers ID*/
    public Integer getId(){

    } 
    /*Get SSN for varification*/
    public Integer getSSN (){

    }
}
/*Employee extends the people class and can be identified by EMPLOYEE enum. */
public class employees extends people {
    private Integer employeeId; 
    private Who who;
    private employees (String name, Integer dateOfBirth, Integer SSN, Integer employeeId, Who who) {
        super(name,dateOfBirth,SSN);
        this.employeeId = employeeId;
        this.who = who;
    }
/*Return customer ID */
    public Integer getId(){

    }
     
}

/*Savings account*/
public class saving {
    private Integer money;
    private Integer amount;
    private Integer ID;
    
    private saving(Integer ID, Integer money, Integer withdrawAmount) {
        this.ID = ID;
        this.money = money;
        this.amount = withdrawAmount;
    }    
/*Withdraw method, number of withdraws left increases, decrease the amount of withdraws left, return new balance*/
    public Integer withdraw(Integer money){
        if (this.amount > 0) {
            this.money-= money;
        }
        this.amount--;
        return this.money;
    }
/*Deposit method*/
    public Integer deposit(Integer money) {

    }
/*Can only withdraw a set number of times a month and then it is updated */
    public void withdrawUpdate(Integer update){
        this.amount = update;
    }

}
/*Checking account */
public class checking {
    private Integer money;
    private Integer ID;

    public checking(Integer ID, Integer money) {
        this.money = money;
        this.ID = ID;
    }
    /*withdraw method */
    public Integer withdraw(Integer money){
        
    }
/*deposit method */
    public Integer deposit(Integer money) {

    }
}

/*This is the Bank class */
public class bank {

    List<employees> emp; 
    List<customers> cus;
    Map<Integer, saving> save  = new HashMap<Integer, saving>();
    Map<Integer, checking> check = new HashMap<Integer, checking>();
/*Holds all the necessary information: List of employees, customers, checking and saving accounts.*/
    public bank(List<employees> emp, List<customers> cus, Map<Integer, checking> check, Map<Integer, saving> save) {
        this.emp = emp;
        this.cus = cus;
        this.check = check;
        this.save = save;

    }
/*Create checking, for existing customer*/
    public void createChecking(Integer ID, Integer money, Integer amount){

    }
/*Create saving, for existing customer */
    public void createSaving (Integer ID, Integer money) {


    }
    /*Hire employee, the Who parameter distiguishes between customer and employee */
    public void hireEmployee(String name, String dateOfBirth, String SSN, Integer employeeId, Who who){

    }
    /*add customer, the Who parameter distiguishes between customer and employee  */
    public void addCustomer (String name, String dateOfBirth, String SSN, Integer customerId,  Who who) {

    }
/*update the ammount of withdraws from a saving account using ID */
    public void updateSavingWithdraw (Integer Id, Integer update) {


    }


}

/* Clarifying Questions
    - Can we assume the bank provides checking and saving sevices? What are the differences between the two?
    Answer: Yes and the difference is how many times you can withdraw in a set time.
    - Can we assume it also has employees and customers?
    Answer: Yes and this have to be indentifiable. 
    - Is the bank allowed to give more money then in the account holders account. 
    Answer: No, if they ask for more money then they have just return 0 or all their money in the account*/


