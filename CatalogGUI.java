//Andrew DeVoe
import java.awt.*;
import java.awt.image.*;
import java.io.*;
import javax.imageio.ImageIO;
import javax.swing.*;

public class CatalogGUI {

    private boolean aL, aF, tI, iS, sE, sN, lO, cO;
    private String authorLast, authorFirst, title, isbn, series, seriesNum, location, copies;
    private JPanel cardPane, start, addPane, changePane, findPane;
    private CardLayout cards;
    private JFrame frame;
    private Catalog catalog;
    private Font tnr;

    public CatalogGUI() {
        //Format ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————
        cards = new CardLayout();
        cardPane = new JPanel(cards);
        tnr = new Font("Times New Roman", Font.PLAIN, 20);
        aL = aF = tI = iS = sE = lO = cO = false;

        //Create first panel ——————————————————————————————————————————————————————————————————————————————————————————————————————
        start = new JPanel(new GridLayout(2,1));

        //Picture panel ———————————————————————————————————————————————————————————————————————————————————————————————————————————
        JPanel picture = new JPanel();
        try {
            BufferedImage img = ImageIO.read(new File("Bookcase.JPG"));
            Image dimg = img.getScaledInstance(400, 300, Image.SCALE_SMOOTH);
			ImageIcon icon = new ImageIcon(dimg);
            JLabel image = new JLabel(icon);
            picture.add(image);
        } catch(IOException e) {
            System.out.println(e);
        }

        //Makes selector panel ————————————————————————————————————————————————————————————————————————————————————————————————————
        JPanel selector = new JPanel(new GridLayout(3,1));

        //Makes welcome panel —————————————————————————————————————————————————————————————————————————————————————————————————————
        JPanel welcome = new JPanel();
        JLabel welcomeLabel = new JLabel("Welcome to the Book Catalog. Please choose what you wish to do.");
        welcomeLabel.setFont(tnr);
        welcome.add(welcomeLabel);

        //Makes choice panel ——————————————————————————————————————————————————————————————————————————————————————————————————————
        JPanel choice = new JPanel();
        //Add book button
        JButton addBook = new JButton("Add a Book");
        addBook.setFont(tnr);
        addBook.addActionListener(a -> {
            cards.show(cardPane, "add");
            frame.revalidate();
        });
        //Change book button
        JButton changeBook = new JButton("Change Book Details");
        changeBook.setFont(tnr);
        changeBook.addActionListener(a -> {
            cards.show(cardPane, "change");
            frame.revalidate();
        });
        //Find book button
        JButton findBook = new JButton("Find a Book");
        findBook.setFont(tnr);
        findBook.addActionListener(a -> {
            cards.show(cardPane, "find");
            frame.revalidate();
        });
        choice.add(addBook);
        choice.add(changeBook);
        choice.add(findBook);

        //Makes close panel ———————————————————————————————————————————————————————————————————————————————————————————————————————
        JPanel end = new JPanel();
        JButton close = new JButton("Close");
        close.setFont(tnr);
        close.addActionListener(a -> {
            frame.dispose();
        });
        end.add(close);

        //Adds to start panel —————————————————————————————————————————————————————————————————————————————————————————————————————
        selector.add(welcome);
        selector.add(choice);
        selector.add(end);
        start.add(picture);
        start.add(selector);
        cardPane.add(start, "start");
        addBook();
        cardPane.add(addPane, "add");
        changeBook();
        cardPane.add(changePane, "change");
        findBook();
        cardPane.add(findPane, "find");
        cards.show(cardPane, "start");
    }
    
    public void makeFrame() {
        frame = new JFrame("Book Catalog");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        frame.setSize((int)screenSize.getWidth(), (int)screenSize.getHeight());
        frame.add(cardPane);
        frame.setVisible(true);
    }

    public void addBook() {
        //Creates format items ——————————————————————————————————————————————————————————————————————————————————————————————————
        addPane = new JPanel(new GridLayout(2,1));

        //Creates content panel —————————————————————————————————————————————————————————————————————————————————————————————————
        JPanel inContent = new JPanel(new GridLayout(7,1));

        //Picture panel ———————————————————————————————————————————————————————————————————————————————————————————————————————————
        JPanel picture = new JPanel();
        try {
            BufferedImage img = ImageIO.read(new File("Bookcase.JPG"));
            Image dimg = img.getScaledInstance(400, 300, Image.SCALE_SMOOTH);
			ImageIcon icon = new ImageIcon(dimg);
            JLabel image = new JLabel(icon);
            picture.add(image);
        } catch(IOException e) {
            System.out.println(e);
        }

        //Title panel ———————————————————————————————————————————————————————————————————————————————————————————————————————————
        JPanel p1 = new JPanel();
        JLabel heading = new JLabel("Enter all of the information and hit \"Add Book\".");
        heading.setFont(tnr);
        p1.add(heading);

        //Author panel ——————————————————————————————————————————————————————————————————————————————————————————————————————————
        JPanel p2 = new JPanel();
        //Last Name
        JLabel lName = new JLabel("Author Last Name:");
        lName.setFont(tnr);
        JTextField lastName = new JTextField();
        lastName.setFont(tnr);
        lastName.setColumns(20);
        //First Name
        JLabel fName = new JLabel("Author First Name:");
        fName.setFont(tnr);
        JTextField firstName = new JTextField();
        firstName.setFont(tnr);
        firstName.setColumns(20);
        p2.add(lName);
        p2.add(lastName);
        p2.add(fName);
        p2.add(firstName);

        //Book title and ISBN panel —————————————————————————————————————————————————————————————————————————————————————————————
        JPanel p3 = new JPanel();
        //Book Title
        JLabel titleLabel = new JLabel("Enter the book title:");
        titleLabel.setFont(tnr);
        JTextField ttl = new JTextField();
        ttl.setFont(tnr);
        ttl.setColumns(20);
        //ISBN
        JLabel isbnLabel = new JLabel("Enter the book ISBN:");
        isbnLabel.setFont(tnr);
        JTextField sbn = new JTextField();
        sbn.setFont(tnr);
        sbn.setColumns(20);
        p3.add(titleLabel);
        p3.add(ttl);
        p3.add(isbnLabel);
        p3.add(sbn);

        //Series panel ——————————————————————————————————————————————————————————————————————————————————————————————————————————
        JPanel p4 = new JPanel();
        JLabel seriesLabel = new JLabel("Enter the series name (Type \"None\" if the book is not in a series):");
        seriesLabel.setFont(tnr);
        JTextField ser = new JTextField();
        ser.setFont(tnr);
        ser.setColumns(20);
        p4.add(seriesLabel);
        p4.add(ser);

        //Book number panel ———————————————————————————————————————————————————————————————————————————————————————————————————————
        JPanel p5 = new JPanel();
        JLabel seriesNumLabel = new JLabel("Enter the book's number in the series (Type \"0\" if the book is not in a series):");
        seriesNumLabel.setFont(tnr);
        JTextField serNum = new JTextField();
        serNum.setFont(tnr);
        serNum.setColumns(20);
        p5.add(seriesNumLabel);
        p5.add(serNum);

        //Location and Copies Panel —————————————————————————————————————————————————————————————————————————————————————————————
        JPanel p6 = new JPanel();
        //Location
        JLabel locationLabel = new JLabel("Select the location of the book:");
        locationLabel.setFont(tnr);
        String[] locations = new String[]{"Select", "Oxford Living Room", "Oxford Dining Room", "Oxford Office", "Oxford Basement", "Oxford Master Bedroom", "Oxford Andrew's Room", "Oxford Maddie's Room", "Harwitch", "Maddie Apartment", "Andrew Dorm"};
        JComboBox<String> locat = new JComboBox<>(locations);
        locat.setFont(tnr);
        locat.addActionListener(a -> {
            String tlocation = locat.getSelectedItem().toString();
            if(!tlocation.equals("Select")) {
                location = tlocation;
                lO = true;
            }
            tlocation = "";
        });
        //Copies
        JLabel copiesLabel = new JLabel("Select the number of copies of the book:");
        copiesLabel.setFont(tnr);
        String[] copiesChoices = new String[]{"Select", "1", "2", "3", "4", "5"};
        JComboBox<String> cop = new JComboBox<>(copiesChoices);
        cop.setFont(tnr);
        cop.addActionListener(a -> {
            String tcopies = cop.getSelectedItem().toString();
            if(!tcopies.equals("Select")) {
                copies = tcopies;
                cO = true;
            }
            tcopies = "";
        });
        p6.add(locationLabel);
        p6.add(locat);
        p6.add(copiesLabel);
        p6.add(cop);

        //Submit Panel ——————————————————————————————————————————————————————————————————————————————————————————————————————————
        JPanel p7 = new JPanel();
        //Add book button
        JButton addBook = new JButton("Add Book");
        addBook.setFont(tnr);
        addBook.addActionListener(a -> {
            //Gets textfield entries
            //Last Name
            String tauthorLast = lastName.getText();
            if(!tauthorLast.equals("")) {
                authorLast = tauthorLast;
                aL = true;
            }
            tauthorLast = "";
            //First Name
            String tauthorFirst = firstName.getText();
            if(!tauthorFirst.equals("")) {
                authorFirst = tauthorFirst;
                aF = true;
            }
            tauthorFirst = "";
            //Title
            String ttitle = ttl.getText();
            if(!ttitle.equals("")) {
                title = ttitle;
                tI = true;
            }
            ttitle = "";
            //ISBN
            String tisbn = sbn.getText();
            if(!tisbn.equals("")) {
                isbn = tisbn;
                iS = true;
            }
            tisbn = "";
            //Series
            String tseries = ser.getText();
            if(!tseries.equals("")) {
                series = tseries;
                sE = true;
            }
            tseries = "";
            //SeriesNum
            String tseriesNum = serNum.getText();
            if(!tseriesNum.equals("")) {
                seriesNum = tseriesNum;
                sN = true;
            }
            tseriesNum = "";

            //Makes sure all fields have been filled out
            String message = "";
            if(!aL)
                message += "Please make sure you entered the author's last name.\n";
            if(!aF)
                message +=  "Please make sure you entered the author's first name.\n";
            if(!tI)
                message +=  "Please make sure you entered the book's title.\n";
            if(!iS)
                message +=  "Please make sure you entered the book's isbn.\n";
            if(!sE)
                message += "Please make sure you entered the book's series or \"None\".\n";
            if(!sN)
                message += "Please make sure you entered the book's series number or \"0\".\n";
            if(!lO)
                message += "Please make sure you entered the book's location.\n";
            if(!cO)
                message += "Please make sure you entered the number of copies of the book.\n";
            if(!message.equals(""))
                JOptionPane.showMessageDialog(frame, message);

            //Creates the Catalog data
            if(aL && aF && tI && iS && sE && sN && lO && cO) {
            //Sends input to Catalog class
            catalog = new Catalog();
            catalog.addBook(authorLast, authorFirst, title, isbn, series, seriesNum, location, copies);
            if(catalog.getMatch()) {
                int in = JOptionPane.showConfirmDialog(frame, "The book has already been added, would you like to increase the number of copies?", "Select and Option", JOptionPane.YES_NO_OPTION, JOptionPane.ERROR_MESSAGE);
                if(in == 0) {
                    catalog.increaseCopies();
                    JOptionPane.showMessageDialog(frame, "The number of copies was increased.");
                }
                else if(in == 1)
                    JOptionPane.showMessageDialog(frame, "The number of copies was not increased.");
            }
            else
                JOptionPane.showMessageDialog(frame, "The book has been added.");

            //Resets the fields
            lastName.setText(null);
            firstName.setText(null);
            ttl.setText(null);
            sbn.setText(null);
            ser.setText(null);
            serNum.setText(null);
            locat.setSelectedItem("Select");
            cop.setSelectedItem("Select");
            cards.show(cardPane, "start");
            }
        });
        //Canel button
        JButton cancel = new JButton("Cancel");
        cancel.setFont(tnr);
        cancel.addActionListener(a -> {
            cards.show(cardPane, "start");
            frame.revalidate();
        });
        p7.add(addBook);
        p7.add(cancel);

        //Creates main panel and adds components ————————————————————————————————————————————————————————————————————————————————
        inContent.add(p1);
        inContent.add(p2);
        inContent.add(p3);
        inContent.add(p4);
        inContent.add(p5);
        inContent.add(p6);
        inContent.add(p7);
        addPane.add(picture);
        addPane.add(inContent);
    }

    public void changeBook() {
        //Creates format items ————————————————————————————————————————————————————————————————————————————————————————————————————
        changePane = new JPanel(new GridLayout(2,1));
        JPanel changeInput = new JPanel(new GridLayout(2,1));

        //Picture panel ———————————————————————————————————————————————————————————————————————————————————————————————————————————
        JPanel picture = new JPanel();
        try {
            BufferedImage img = ImageIO.read(new File("Bookcase.JPG"));
            Image dimg = img.getScaledInstance(400, 300, Image.SCALE_SMOOTH);
			ImageIcon icon = new ImageIcon(dimg);
            JLabel image = new JLabel(icon);
            picture.add(image);
        } catch(IOException e) {
            System.out.println(e);
        }

        //changeInput ——————————————————————————————————————————————————————————————————————————————————————————————————————————————
        //Message
        JPanel p1 = new JPanel();
        JLabel message = new JLabel("This feature is currently in development.");
        message.setFont(tnr);
        p1.add(message);
        //Cancel Button
        JPanel p2 = new JPanel();
        JButton cancel = new JButton("Cancel");
        cancel.setFont(tnr);
        cancel.addActionListener(a -> {
            cards.show(cardPane, "start");
            frame.revalidate();
        });
        p2.add(cancel);
        changeInput.add(p1);
        changeInput.add(p2);

        //Creates display from compontents ————————————————————————————————————————————————————————————————————————————————————————
        changePane.add(picture);
        changePane.add(changeInput);
    }

    public void findBook() {
        //Creates format items ————————————————————————————————————————————————————————————————————————————————————————————————————
        findPane = new JPanel(new GridLayout(2,1));
        JPanel findInput = new JPanel(new GridLayout(2,1));

        //Picture panel ———————————————————————————————————————————————————————————————————————————————————————————————————————————
        JPanel picture = new JPanel();
        try {
            BufferedImage img = ImageIO.read(new File("Bookcase.JPG"));
            Image dimg = img.getScaledInstance(400, 300, Image.SCALE_SMOOTH);
			ImageIcon icon = new ImageIcon(dimg);
            JLabel image = new JLabel(icon);
            picture.add(image);
        } catch(IOException e) {
            System.out.println(e);
        }

        //findInput ———————————————————————————————————————————————————————————————————————————————————————————————————————————————
        //Message
        JPanel p1 = new JPanel();
        JLabel message = new JLabel("This feature is currently in development.");
        message.setFont(tnr);
        p1.add(message);
        //Cancel Button
        JPanel p2 = new JPanel();
        JButton cancel = new JButton("Cancel");
        cancel.setFont(tnr);
        cancel.addActionListener(a -> {
            cards.show(cardPane, "start");
            frame.revalidate();
        });
        p2.add(cancel);
        findInput.add(p1);
        findInput.add(p2);

        //Creates display from compontents ————————————————————————————————————————————————————————————————————————————————————————
        findPane.add(picture);
        findPane.add(findInput);
    }
}