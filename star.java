
public class star {
    public static void main(String[] args) {
        // for(int i=1; i<4; i++){
        // for(int j=0; j<i; j++){
        // System.out.print("*");

        // }
        // System.out.println();

        // // for (int j=6; j>i; j--)
        // // System.out.print("*");
        // // System.out.println();

        // }
        for (int i = 1; i < 10; i++) {
            if (i >= 6) {

                for (int j = 10; j > i; j--) {
                    System.out.print("*");
                }

            } else {
                for (int j = 0; j < i; j++) {
                    System.out.print("*");
                }

            }
            System.out.println();

        }

    }

}
