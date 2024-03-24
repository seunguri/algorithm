import java.util.Arrays;
import java.util.HashSet;

public class MergeNames {
    
    public static String[] uniqueNames(String[] names1, String[] names2) {
      HashSet<String> setn1 = new HashSet<>(Arrays.asList(names1));
      HashSet<String> setn2 = new HashSet<>(Arrays.asList(names2));
      setn1.retainAll(setn2);
      return setn1.toArray(new String[0]);
    }
    
    public static void main(String[] args) {
        String[] names1 = new String[] {"Ava", "Emma", "Olivia"};
        String[] names2 = new String[] {"Olivia", "Sophia", "Emma"};
        System.out.println(String.join(", ", MergeNames.uniqueNames(names1, names2))); // should print Ava, Emma, Olivia, Sophia
    }
}