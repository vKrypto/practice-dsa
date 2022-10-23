import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;



class Result {

    /*
     * Complete the 'maximumQuality' function below.
     *
     * The function is expected to return a LONG_INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER_ARRAY packets
     *  2. INTEGER channels
     */

    public static long maximumQuality(List<Integer> packets, int channels){
    // Write your code here
        int n = packets.size();
        
        double answer = 0;
        if(n == channels) {
            for(int i = 0;i<n;i++) {
                answer += packets.get(i);
            }
            return (long)answer;
        }
        Collections.sort(packets);
        
        for(int i = n - channels+1;i<n;i++) {
            answer += packets.get(i);
        }
        
        n = n-channels;
        if(n%2 == 0) {
            // odd
            answer += packets.get(n/2);
        }
        else {
            //even
            double value = packets.get(n/2) + packets.get((n/2) + 1);
            answer += value/2;
        }
        return (long)Math.ceil(answer);
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int packetsCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> packets = IntStream.range(0, packetsCount).mapToObj(i -> {
            try {
                return bufferedReader.readLine().replaceAll("\\s+$", "");
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
            .map(String::trim)
            .map(Integer::parseInt)
            .collect(toList());

        int channels = Integer.parseInt(bufferedReader.readLine().trim());

        long result = Result.maximumQuality(packets, channels);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
