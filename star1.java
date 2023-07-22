// public class star1 {

//   public static void main(String[] args) {
//     for (int i = 1; i <6; i++) {
//       for (int j = 6; j > i; j--) {
//         System.out.print("*");
//       }
//       System.out.println();
//     }
//   }
// }
// public class star1{
//     public static void main(String[]args){
//         for (int i=1; i<6; i++){
//             if (i>=4){
//                 for (int j=6; j>i; j--){
//                     System.out.print("*");
//                 }
//             }else {
//                 for (int j=0; j<i; j++ ){
//                     System.out.print("*");
//                 }
//             }System.out.println();
//         }
//     }
// // }
// public class star1{
//     public static void main(String[]args){
//         for (int i=1; i<5; i++){
//             for (int j=0; j<i; j++){
//                 System.out.print("*");
//             }System.out.println();
//         }
//     }
// }

// public class star1 {

//   public static void main(String[] args) {
//     for (int j = 0; j < 1000000; j++) {
//       for (int i = 0; i < 2*j+1 ; i++) {
//         if (i == 0) {
//           System.out.print("*");
//         }
//         if (j>0&&i==2*j){
//           System.out.print("*");

//         }System.out.print(" ");

//       }
//       System.out.println();
//     }
//   }
// }
// public class star1{
//   public static void main(String[]args){
//     for(int i=0; i<5; i++){
//       for(int j=0; j<9-2*i; j++ ){
//         System.out.print("*");
//       }System.out.println();
//     }
//   }
// }

public class star1 {

  public static void main(String[] args) {
    int[] array = new int[] { 4, 5, 1, 8, 10, 9 };
    for (int j = 0; j < array.length; j++) {
      for (int i = 0; i < array.length - 1; i++) {
        if (array[i] < array[i + 1]) {
          int temp = 0;
          temp = array[i];
          array[i] = array[i + 1];
          array[i + 1] = temp;
        }
      }
    }
    for(int i=0; i<array.length; i++){
      System.out.println(array[i]);
    }
  }
}
