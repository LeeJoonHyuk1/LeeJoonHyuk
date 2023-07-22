import java.util.ArrayList;

public class star2{
    public static void main(String[]args){
        int[][]array=new int[20][2];
        for (int i=0; i<array.length; i++){
            for (int j=0; j < array[1].length; j++){
                array[i][j]= (int)(Math.random()*100);
            }
        }

        for (int i=0; i<array.length; i++){
            for (int j=0; j<array[i].length; j++){
                System.out.print(array[i][j] + " ");
            }
            System.out.println();
        }
    }
}

