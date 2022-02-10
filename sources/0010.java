class Mirror {
    static int a = 3;
    int x = 2;
    int y = x;

    static {
        System.out.println("a = " + a);
    }

    {
        System.out.println("x = " + x);
        System.out.println("y = " + y);
    }

    public Mirror() {
        System.out.println("I am created");
    }
}

public class Program {
    public static void main(String[] args) {
        Mirror mirror = new Mirror();
        Mirror mirror2 = new Mirror();
    }
}

// a = 3
// x = 2
// y = 2
// I am created
// x = 2
// y = 2
// I am created
