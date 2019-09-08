package challenge;

public class HelloWorld {

	public static void main(String[] args){
		// TODO Auto-generated method stub
		try {
			String str2= null;
			if (str2.equals("Hello World"))
			{
				System.out.println("Same");
			}
		}
		catch(NullPointerException e) 
        { 
			e.printStackTrace();
        }
		
	}

}
