public class practice {
    public static void main(String[] args) {
  
        int[][] array = new int[20][2]; 

     

        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[1].length; j++) {
                array[i][j] = (int) ((Math.random() * 50001) + 50000);
            }
        }
       
        int[] storeTotal = new int[40];
        int[] storePrice1 = new int[20];
        int[] storePrice2 = new int[20];
        for (int i = 0; i < array.length; i++) {
            storePrice1[i] = array[i][0];
        }
        for (int i = 0; i < array.length; i++) {
            storePrice2[i] = array[i][1];
        }
        for (int i = 0; i < array.length; i++) {
            storeTotal[i] = storePrice1[i];
        }
        for (int i = 0; i < array.length; i++) {
            storeTotal[i + 20] = storePrice2[i];
        }

        int totalValue = 0;

        for (int i = 0; i < storeTotal.length; i++) {
            totalValue += storeTotal[i];
        }

        int average = totalValue / storeTotal.length;
        System.out.println("Average Price: " + average);

        int vary = 500000; // 차이
        int target = -1;
        for (int i = 0; i < storeTotal.length; i++) {
            if (vary > Math.abs(storeTotal[i] - average)) {
                vary = Math.abs(storeTotal[i] - average);
                target = i;
            }
        }

        System.out.println("closest price: " + storeTotal[target]);
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[1].length; j++) {
                if (array[i][j] == storeTotal[target]) {
                    System.out.println("closest door number :" + (i + 1) + "0" + (j + 1));
                }
            }
        }
    }
}