import java.util.Random;
import java.lang.*;

/** Generate random integers in a certain range. */
public final class RandomArrayFill {

    public static final void main(String... aArgs){
        System.out.println("Java run:");

        for (int arr_size = (int)Math.pow(10, 6); arr_size <= Math.pow(10, 7); arr_size += Math.pow(10, 6)){
            final long start = System.currentTimeMillis();
            float[] arr = new float[arr_size];
            Random random = new Random();
            float ran = random.nextFloat();
            for (int bla = 1; bla < arr_size; bla++) {
                arr[bla] = ran; 
            }

            final long end = System.currentTimeMillis();
            System.out.println("time elapsed for " + arr_size + " array size is: " + (end - start)/1000. + " seconds.");
        }

        System.out.println("done.");

    } 
}
