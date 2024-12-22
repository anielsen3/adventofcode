import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;

class Day4 {

    private static String readString(char[][] input, int x, int y, int[] dxdy) {
        StringBuilder sb = new StringBuilder();

        while (y >= 0 && y < input.length && x >= 0 && x < input[y].length) {
            sb.append(input[y][x]);
            x += dxdy[0];
            y += dxdy[1];
        }

        return sb.toString();
    }

    private static long numXMASs(char[][] input, int x, int y) {
        int[][] directions = {{1, 1}, {1, 0}, {1, -1}, {0, 1}, {0, -1}, {-1, 1}, {-1, 0}, {-1, -1}};
        return Arrays.stream(directions)
            .filter(d -> readString(input, x, y, d).startsWith("XMAS"))
            .count();
    }

    private static long numX_MASs(char[][] input, int x, int y) {
        int[][] directions = {{1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
        return Arrays.stream(directions)
            .filter(d -> readString(input, x-d[0], y-d[1], d).startsWith("MAS"))
            .count();
    }

    public static void main(String[] args) throws IOException {
        char[][] input = Files.readAllLines(Paths.get(args[0])).stream()
            .map(s -> s.toCharArray()).toList().toArray(new char[0][0]);

        int count1 = 0, count2 = 0;
        for (int y=0; y<input.length; y++) {
            for (int x=0; x<input[y].length; x++) {
                count1 += numXMASs(input, x, y);               // Part 1
                count2 += numX_MASs(input, x, y) >= 2 ? 1 : 0; // Part 2
            }
        }
    
        System.out.println("1:" + count1);
        System.out.println("2:" + count2);
    }

}
