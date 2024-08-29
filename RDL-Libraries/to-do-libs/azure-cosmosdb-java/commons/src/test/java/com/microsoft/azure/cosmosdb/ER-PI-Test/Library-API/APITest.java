import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class APITest {

    public static void ReadInterleavings() {
        String directoryPath = "interleavings/";
        File directory = new File(directoryPath);

        if (directory.exists() && directory.isDirectory()) {
            for (int i = 0; i < 30; i++) {
                File file = new File(directoryPath + "ils_" + (i + 1) + ".txt");
                if (file.isFile()) {
                    System.out.println("Reading file: " + file.getName());
                    try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
                        String line;
                        while ((line = reader.readLine()) != null) {
                            System.out.println(line);
                        }
                    } catch (IOException e) {
                        System.err.println("Error reading file: " + file.getName());
                        e.printStackTrace();
                    }
                    System.out.println(); // Add a blank line between files
                }
            }
        } else {
            System.err.println("Directory does not exist or is not a directory: " + directoryPath);
        }
    }

    public static void main(String[] args) {
        ReadInterleavings();
    }
}