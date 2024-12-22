import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

class Day5 {

    private static String findMiddle(String[] ls) {
        return ls[ls.length/2];
    }

    private static int part1(String[] pages, List<Pattern> regexes) {
        return Arrays.stream(pages)
            .filter(p -> !regexes.stream().anyMatch(r -> r.matcher(p).matches()))
            .mapToInt(p -> Integer.valueOf(findMiddle(p.split(","))))
            .sum();
    }

    private static String reorder(List<Pattern> regexes, String l) {
        boolean foundMatch = true;
        while (foundMatch) {
            foundMatch = false;
            for (Pattern regex: regexes) {
                Matcher m = regex.matcher(l);
                if (m.matches()) {
                    foundMatch = true;
                    l = m.group(1) + m.group(4) + m.group(3) + m.group(2) + m.group(5);
                }
            }    
        }

        return l;
    }

    private static int part2(String[] pages, List<Pattern> regexes) {
        return Arrays.stream(pages)
            .filter(p -> regexes.stream().anyMatch(r -> r.matcher(p).matches()))
            .mapToInt(p -> Integer.valueOf(findMiddle(reorder(regexes, p).split(","))))
            .sum();
    }

    public static void main(String[] args) throws IOException {
        String input = String.join("\n",Files.readAllLines(Paths.get(args[0])));
        String[] rules = input.split("\n\n")[0].split("\n");
        String[] pages = input.split("\n\n")[1].split("\n");

        // Create regexes that match disordered pages 
        List<Pattern> regexes = Arrays.stream(rules)
            .map(l -> {
                String[] nums = l.split("\\|");
                return Pattern.compile("(.*)(" + nums[1] + ")(.*)(" + nums[0] + ")(.*)");                       
            }).toList();

        System.out.println("1: " + part1(pages, regexes));
        System.out.println("2: " + part2(pages, regexes));
    }
}