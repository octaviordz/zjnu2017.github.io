
// 1 - Compile:
// >javac test.javac

// 2 - Execute
// >java -cp . test

// 3 - Output 
// 'Hello Java'

// Note: '-cp .' add the current directory to the class path

public class test 
{
  public static void main(String[] args) 
  {
    String greet = "Hi";
	String name = "Smedley";
	String nickName = name.substring(0,4);
	if (nickName == name.substring(0,4));
	System.out.println("has real nickname");
	else if (greet + name == greet + nickName)
	System.out.println("no real nickname");
	else
	System.out.println("hmmm...changed names?");
  }
}
