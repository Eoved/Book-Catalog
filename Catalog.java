import java.io.*;
import java.util.*;

//Andrew DeVoe

public class Catalog {

    private boolean match;
    private String lineMatch;
    private LinkedList<String> storedLines;
    private book input;
    private File booklist;

    public Catalog() {
        match = false;
        lineMatch = "";
    }

    public void addBook(String authorLast, String authorFirst, String title, String isbn, String series, String seriesNum, String location, String copies) {
        try {
            //Checks to see if the problem has been added
            input = new book(authorLast, authorFirst, title, isbn, series, Integer.parseInt(seriesNum), location, Integer.parseInt(copies));
            storedLines = new LinkedList<String>();
            booklist = new File("bookcatalog.dat");
            FileReader fileReader = new FileReader(booklist);
            BufferedReader bufferedReader = new BufferedReader(fileReader);
            String line = bufferedReader.readLine();
            while(line != null) {
                String[] lineData = line.split(";");
                String last = lineData[0];
                String first = lineData[1];
                String bookTitle = lineData[2];
                String bookISBN = lineData[3];
                String bookSeries = lineData[4];
                String bookSeriesNum = lineData[5];
                if(match == false) {
                    if(input.getLast().equals(last) && input.getFirst().equals(first) && input.getTitle().equals(bookTitle) && input.getISBN().equals(bookISBN)) {
                        match = true;
                        lineMatch = line;
                    }
                }
                if(!(input.getLast().equals(last) && input.getFirst().equals(first) && input.getTitle().equals(bookTitle) && input.getISBN().equals(bookISBN))) {
                    for(int i = 0; i < storedLines.size(); i++) {
                        String[] storedData = storedLines.get(i).split(";");
                        String lastS = storedData[0];
                        String firstS = storedData[1];
                        String bookTitleS = storedData[2];
                        String bookSeriesS = storedData[4];
                        String bookSeriesNumS = storedData[5];
                        String storedInfo = lastS + " " + firstS + " " + bookSeriesS + " " + bookSeriesNumS + " " + bookTitleS;
                        String lineInfo = last + " " + first + " " + bookSeries + " " + bookSeriesNum + " " + bookTitle;
                        if(lineInfo.compareToIgnoreCase(storedInfo) < 0) {
                            storedLines.add(i, line);
                            i = storedLines.size();
                        }
                    }
                }
                line = bufferedReader.readLine();
            }
            fileReader.close();
            bufferedReader.close();

            //Adds the problem if it has not been added
            if(match == false) {

                //Makes sure the book is added in alphabetical order
                for(int i = 0; i < storedLines.size(); i++) {
                    String[] storedData = storedLines.get(i).split(";");
                    String lastS = storedData[0];
                    String firstS = storedData[1];
                    String bookTitleS = storedData[2];
                    String bookSeriesS = storedData[4];
                    String bookSeriesNumS = storedData[5];
                    String storedInfo = lastS + " " + firstS + " " + bookSeriesS + " " + bookSeriesNumS + " " + bookTitleS;
                    String lineInfo = authorLast + " " + authorFirst + " " + series + " " + seriesNum + " " + title;
                    if(lineInfo.compareToIgnoreCase(storedInfo) < 0) {
                        storedLines.add(i, input.toString());
                        i = storedLines.size();
                    }
                }
                FileWriter fileWriter = new FileWriter(booklist, false);
		        BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);
		        PrintWriter printWriter = new PrintWriter(bufferedWriter, false);
		        printWriter.flush();
		        for(int i = 0; i < storedLines.size(); i++)
			    printWriter.println(storedLines.get(i));
		        printWriter.close();
		        bufferedWriter.close();
                fileWriter.close();
            }
        } catch (Exception e) {
            System.out.println(e);
        }
    }

    public boolean getMatch() {
        return match;
    }

    public void increaseCopies() {
        try {
            String[] bookInfo = lineMatch.split(";");
            String aL = bookInfo[0];
            String aF = bookInfo[1];
            String t = bookInfo[2];
            String is = bookInfo[3];
            String s = bookInfo[4];
            int sN = Integer.parseInt(bookInfo[5]);
            String l = bookInfo[6];
            int c = Integer.parseInt(bookInfo[7]);
            book newBook = new book(aL, aF, t, is, s, sN, l, c + 1);
            
            //Makes sure the book is added in alphabetical order
            for(int i = 0; i < storedLines.size(); i++) {
                String[] storedData = storedLines.get(i).split(";");
                String lastS = storedData[0];
                String firstS = storedData[1];
                String bookTitleS = storedData[2];
                String bookSeriesS = storedData[4];
                String bookSeriesNumS = storedData[5];
                String storedInfo = lastS + " " + firstS + " " + bookSeriesS + " " + bookSeriesNumS + " " + bookTitleS;
                String lineInfo = aL + " " + aF + " " + s + " " + sN + " " + t;
                if(lineInfo.compareToIgnoreCase(storedInfo) < 0) {
                    storedLines.add(i, newBook.toString());
                    i = storedLines.size();
                }
            }
            FileWriter fileWriter = new FileWriter(booklist, false);
		    BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);
		    PrintWriter printWriter = new PrintWriter(bufferedWriter, false);
		    printWriter.flush();
		    for(int i = 0; i < storedLines.size(); i++)
			printWriter.println(storedLines.get(i));
		    printWriter.close();
		    bufferedWriter.close();
            fileWriter.close();
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}