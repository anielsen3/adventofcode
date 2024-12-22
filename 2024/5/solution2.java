import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

class Day5 {

    private static int findMiddle(String page) {
        String[] ls = page.split(",");
        return Integer.valueOf(ls[ls.length/2]);
    }

    public static void main(String[] args) throws IOException {
        String input = String.join("\n",Files.readAllLines(Paths.get(args[0])));
        Set<String> rules = List.of(input.split("\n\n")[0].split("\n"));

        int count1 = 0, count2 = 0;
        for(String page : input.split("\n\n")[1].split("\n")) {
            String sortedPage = 
                String.join(",",
                    Arrays.stream(p.split(","))
                          .sorted((n1, n2) -> { if (rules.contains(n2 + "|" + n1)) { return 1; } else { return -1; } }));
            
            if (page.equals(sortedPage)) {
                count1 += findMiddle(page);
            }
            else {
                count2 += findMiddle(sortedPage);
            }
        }

        System.out.println("1: " + count1);
        System.out.println("2: " + count2);
    }
}