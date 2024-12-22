import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.regex.Pattern;

class Day3 {

    public static int multiply(String s) {
        return Pattern.compile("mul\\((\\d+),(\\d+)\\)").matcher(s)
            .results()
            .mapToInt(match -> Integer.valueOf(match.group(1)) * Integer.valueOf(match.group(2)))
            .sum();
    }

    public static void main(String[] args) throws IOException {
        String input = String.join("", Files.readAllLines(Paths.get(args[0])));
        System.out.println("1: " + multiply(input));

        input = input.replaceAll("don't\\(\\).*?(do\\(\\)|$)", "#");
        System.out.println("2: " + multiply(input));
    }
    
}
