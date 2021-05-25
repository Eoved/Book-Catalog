//Andrew DeVoe

public class book {
    
    private int seriesNum, copies;
    private String authorLast, authorFirst, title, isbn, series, location;

    public book() {
        authorLast = null;
        authorFirst = null;
        title = null;
        isbn = null;
        series = null;
        seriesNum = -1;
        location = null;
        copies = -1;
    }
    
    public book(String aL, String aF, String tI, String iS, String sE, int sN, String lO, int cO) {
        authorLast = aL;
        authorFirst = aF;
        title = tI;
        isbn = iS;
        series = sE;
        seriesNum = sN;
        location = lO;
        copies = cO;
    }

    public String getLast() {
        return authorLast;
    }

    public String getFirst() {
        return authorFirst;
    }

    public String getTitle() {
        return title;
    }

    public String getISBN() {
        return isbn;
    }

    public String getSeries() {
        return series;
    }

    public int getNum() {
        return seriesNum;
    }

    public String getLocation() {
        return location;
    }

    public int getCopies() {
        return copies;
    }

    public String toString() {
        return authorLast + ";" + authorFirst + ";" + title + ";" + isbn + ";" + series + ";" + seriesNum + ";" + location + ";" + copies;
    }
}