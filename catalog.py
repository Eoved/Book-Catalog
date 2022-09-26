#andrew devoe
import mysql.connector, os, scrapebook, re, tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk

#start mySQL
os.system("sudo /usr/local/mysql/support-files/mysql.server start")

#bookboi
mydb = mysql.connector.connect(
    host = "localhost",
    user = "librarian",
    password = "bookboi",
    database = "book_catalog"
)

cursor = mydb.cursor()

#-------------------------------------------------------------------------------
#creates the main gui page
def main_page(root):
    #main page frame
    main_page = tk.Frame(root)
    main_page.columnconfigure(4, weight=5)
    main_page.rowconfigure(10, weight=1)
    main_page.pack()

    #image
    image_label = tk.Label(main_page, image=tk_image)
    image_label.grid(columnspan=4, rowspan=3)

    #heading
    head_label = tk.Label(main_page, text="book catalog")
    head_label.config(font=("Arial", 24))
    head_label.grid(column=1, row=3, columnspan=2, padx=5, pady=5)

    #empty labels
    empty_label = tk.Label(main_page)
    empty_label.grid(column=0, row=5, columnspan=4, padx=5, pady=5)
    empty_label2 = tk.Label(main_page)
    empty_label2.grid(column=0, row=6, columnspan=4, padx=5, pady=5)
    empty_label3 = tk.Label(main_page)
    empty_label3.grid(column=0, row=7, columnspan=4, padx=5, pady=5)
    empty_label4 = tk.Label(main_page)
    empty_label4.grid(column=0, row=9, columnspan=4, padx=5, pady=5)

    #buttons
    def selectbook_callback():
        main_page.destroy()
        search_book_page(root)
    
    selectbook_button = ttk.Button(main_page, text="search catalog", command=selectbook_callback)
    selectbook_button.grid(column=1, row=4, padx=5, pady=5)

    def addbook_callback():
        main_page.destroy()
        add_book_page(root)
    
    addbook_button = ttk.Button(main_page, text="add book", command=addbook_callback)
    addbook_button.grid(column=2, row=4, padx=5, pady=5)

    def quit_callback():
        root.destroy()

    quit_button = ttk.Button(main_page, text="quit", command=quit_callback)
    quit_button.grid(column=1, row=8, columnspan=2, padx=5, pady=5)

#-------------------------------------------------------------------------------
#searches book catalog
#1 is by field and 2 is all
search_type = 0
num_res = 0

def search_book_page(root):
    #main page frame
    search_page = tk.Frame(root)
    search_page.columnconfigure(8, weight=5)
    search_page.rowconfigure(10, weight=1)
    search_page.pack()

    #image
    image_label = tk.Label(search_page, image=tk_image)
    image_label.grid(columnspan=4, rowspan=3)

    #heading
    head_label = tk.Label(search_page, text="search catalog")
    head_label.config(font=("Arial", 24))
    head_label.grid(column=1, row=3, columnspan=2, padx=5, pady=5)

    #author last name
    last_frame = tk.Frame(search_page)
    last_label = tk.Label(last_frame, text="author last name:")
    last = tk.Entry(last_frame)
    last_label.pack(side=LEFT)
    last.pack(side=RIGHT)
    last_frame.grid(column=1, row=4, padx=5, pady=5, sticky=E)

    #author first name
    first_frame = tk.Frame(search_page)
    first_label = tk.Label(first_frame, text="author first name:")
    first = tk.Entry(first_frame)
    first_label.pack(side=LEFT)
    first.pack(side=RIGHT)
    first_frame.grid(column=2, row=4, padx=5, pady=5, sticky=E)

    #book title
    title_frame = tk.Frame(search_page)
    title_label = tk.Label(title_frame, text="book title:")
    title = tk.Entry(title_frame)
    title_label.pack(side=LEFT)
    title.pack(side=RIGHT)
    title_frame.grid(column=1, row=5, padx=5, pady=5, sticky=E)

    #series
    series_frame = tk.Frame(search_page)
    series_label = tk.Label(series_frame, text="book series:")
    series = tk.Entry(series_frame)
    series_label.pack(side=LEFT)
    series.pack(side=RIGHT)
    series_frame.grid(column=2, row=5, padx=5, pady=5, sticky=E)

    #isbn
    isbn_frame = tk.Frame(search_page)
    isbn_label = tk.Label(isbn_frame, text="book isbn:")
    isbn = tk.Entry(isbn_frame)
    isbn_label.pack(side=LEFT)
    isbn.pack(side=RIGHT)
    isbn_frame.grid(column=1, row=6, padx=5, pady=5, sticky=E)

    #loaned
    loaned_frame = tk.Frame(search_page)
    loaned_label = tk.Label(loaned_frame, text="loaned to:")
    loaned = tk.Entry(loaned_frame)
    loaned_label.pack(side=LEFT)
    loaned.pack(side=RIGHT)

    #digital
    digital_frame = tk.Frame(search_page)
    digital_label = tk.Label(digital_frame, text="digital format:")
    digital = StringVar(digital_frame)
    digital_cb = ttk.Combobox(digital_frame, textvariable=digital)
    digital_cb['values'] = ("ibook", "glose book", "pdf")
    digital_cb['state'] = 'readonly'
    digital_cb.set("select")
    digital_label.pack(side=LEFT)
    digital_cb.pack(side=RIGHT)

    def location_callback(*args):
        loaned_frame.grid_forget()
        digital_frame.grid_forget()
        val = loc.get()
        if(val == "loaned"):
            loaned_frame.grid(column=2, row=7, padx=5, pady=5, sticky=E)
        elif(val == "digital"):
            digital_frame.grid(column=2, row=7, padx=5, pady=5, sticky=E)

    #location
    loc_frame = tk.Frame(search_page)
    loc_label = tk.Label(loc_frame, text="book location:")
    loc = StringVar(loc_frame)
    loc_cb = ttk.Combobox(loc_frame, textvariable=loc)
    loc_cb['values'] = ("anne's house", "keith's house", "maddie's apartment", "andrew's apartment", "ruthie's house", "loaned", "digital")
    loc_cb['state'] = 'readonly'
    loc_cb.set("select")
    loc_label.pack(side=LEFT)
    loc_cb.pack(side=RIGHT)
    loc_frame.grid(column=2, row=6, padx=5, pady=5, sticky=E)
    loc.trace('w', location_callback)

    #empty label
    empty_label = tk.Label(search_page)
    empty_label.grid(column=1, row=7, padx=5, pady=5)

    #buttons
    button_frame = ttk.Frame(search_page)

    def back_callback():
        search_page.destroy()
        main_page(root)
    back_button = ttk.Button(button_frame, text="back", command=back_callback)
    back_button.pack(side=LEFT)

    def search_callback():
        global search_type, num_res 
        search_type = 1
        num_res = 0
        #gets values in field
        initial = TRUE
        lst = []
        search_command = "SELECT * FROM owned_books WHERE"
        lname = last.get()
        fname = first.get()
        t = title.get()
        s = series.get()
        num = isbn.get()
        location = loc.get()
        if(location == "loaned"):
            location = "loaned to " + loaned.get()
        elif(location == "digital"):
            location = digital.get()

        #appends to the select command string
        if(lname != ""):
            search_command += " author_last LIKE %s"
            initial = FALSE
            lst.append(lname)
        if(fname != ""):
            if initial:
                search_command += " author_first LIKE %s"
                initial = FALSE
            else:
                search_command += " AND author_last LIKE %s"
            lst.append(fname)
        if(t != ""):
            if initial:
                search_command += " title LIKE %s"
                initial = FALSE
            else:
                search_command += " AND title LIKE %s"
            lst.append(t)
        if(s != ""):
            if initial:
                search_command += " series LIKE %s"
                initial = FALSE
            else:
                search_command += " AND series LIKE %s"
            lst.append(s)
        if(num != ""):
            if initial:
                search_command += " isbn LIKE %s"
                initial = FALSE
            else:
                search_command += " AND isbn LIKE %s"
            lst.append(num)
        if(location != "select" and location != ""):
            if initial:
                search_command += " location=%s"
                initial = FALSE
            else:
                search_command += " AND location=%s"
            lst.append(location)
        search_command += " ORDER BY author_last, author_first, series, title"
        if(initial):
            messagebox.showinfo("showinfo", "must search by at least one field", icon="error")
        else:
            try:
                temp = []
                for l in lst:
                    l = "%" + l + "%"
                    temp.append(l)
                lst = temp
                cursor.execute(search_command, lst)
                results = cursor.fetchall()
                show_results(results)
            except:
                messagebox.showinfo("showinfo", "error fetching results", icon="error")

    search_button = ttk.Button(button_frame, text="search", command=search_callback)
    search_button.pack(side=LEFT)

    def searchall_callback():
        global search_type, num_res
        search_type = 2
        num_res = 0
        search_command = "SELECT * FROM owned_books ORDER BY author_last, author_first, series, title"
        try:
            cursor.execute(search_command)
            results = cursor.fetchall()
            if(results == []):
                messagebox.showinfo("showinfo", "no results", icon="error")
            else:
                show_results(results)
        except:
            if(not results == []):
                messagebox.showinfo("showinfo", "no results", icon="error")

    searchall_button = ttk.Button(button_frame, text="view all books", command=searchall_callback)
    searchall_button.pack(side=RIGHT)

    def show_results(lst):
        results_frame = ttk.Frame(search_page)
        ttk.Label(results_frame, text="author(s)     title     series     isbn     location").pack(padx=5, pady=5)
        #loaned
        update_loaned_frame = tk.Frame(search_page)
        update_loaned_label = tk.Label(update_loaned_frame, text="loaned to:")
        update_loaned = tk.Entry(update_loaned_frame)
        update_loaned_label.pack(side=LEFT)
        update_loaned.pack(side=RIGHT)
        #digital
        update_digital_frame = tk.Frame(search_page)
        update_digital_label = tk.Label(update_digital_frame, text="digital format:")
        update_digital = StringVar(update_digital_frame)
        update_digital_cb = ttk.Combobox(update_digital_frame, textvariable=update_digital)
        update_digital_cb['values'] = ("ibook", "glose book", "pdf")
        update_digital_cb['state'] = 'readonly'
        update_digital_cb.set("select")
        update_digital_label.pack(side=LEFT)
        update_digital_cb.pack(side=RIGHT)

        def update_location_callback(*args):
            update_loaned_frame.grid_forget()
            update_digital_frame.grid_forget()
            val = update_loc.get()
            if(val == "loaned"):
                update_loaned_frame.grid(column=5, row=6, columnspan=2, padx=5, pady=5, sticky=E)
            elif(val == "digital"):
                update_digital_frame.grid(column=5, row=6, columnspan=2, padx=5, pady=5, sticky=E)

        #location
        update_loc_frame = tk.Frame(search_page)
        update_loc_label = tk.Label(update_loc_frame, text="new book location:")
        update_loc = StringVar(update_loc_frame)
        update_loc_cb = ttk.Combobox(update_loc_frame, textvariable=update_loc)
        update_loc_cb['values'] = ("anne's house", "keith's house", "maddie's apartment", "andrew's apartment", "ruthie's house", "loaned", "digital")
        update_loc_cb['state'] = 'readonly'
        update_loc_cb.set("select")
        update_loc_label.pack(side=LEFT)
        update_loc_cb.pack(side=RIGHT)
        update_loc_frame.grid(column=5, row=5, columnspan=2, padx=5, pady=5)
        update_loc.trace('w', update_location_callback)

        #from https://blog.teclado.com/tkinter-scrollable-frames/
        canvas = tk.Canvas(results_frame, width=600, height=214, background="white")
        xscrollbar = ttk.Scrollbar(results_frame, orient="horizontal", command=canvas.xview)
        xscrollbar.pack(side=BOTTOM, fill=X)
        yscrollbar = ttk.Scrollbar(results_frame, orient="vertical", command=canvas.yview)
        yscrollbar.pack(side=RIGHT, fill=Y)
        scrollable_frame = ttk.Frame(canvas)
        scrollable_frame.bind("<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)

        def on_enter(e):
            canvas.bind_all('<MouseWheel>', lambda event: canvas.yview_scroll(-1 * event.delta, 'units'))
            canvas.bind_all('<Shift-MouseWheel>', lambda event: canvas.xview_scroll(-1 * event.delta, 'units'))
        def on_leave(e):
            canvas.unbind_all('<MouseWheel>')
            canvas.unbind_all('<Shift-MouseWheel>')
        canvas.bind('<Enter>', on_enter)
        canvas.bind('<Leave>', on_leave)
        book_lst = []
        global num_res
        for i in lst:
            #switch to match/case statements eventually
            if(i[1] == "" and i[2] == "" and i[3] == "" and i[5] == ""):
                words = i[0]+". "+i[4]+". "+i[6]+". "+i[7]
            elif(i[1] == "" and i[2] == "" and i[3] == ""):
                words = i[0]+". "+i[4]+"; "+i[5]+". "+i[6]+". "+i[7]
            elif(i[2] == "" and i[3] == "" and i[5] == ""):
                words = i[0]+", "+i[1]+". "+i[4]+". "+i[6]+". "+i[7]
            elif(i[1] == "" and i[3] == "" and i[5] == ""):
                words = i[0]+" and "+i[2]+". "+i[4]+". "+i[6]+". "+i[7]
            elif(i[1] == "" and i[3] == ""):
                words = i[0]+", and "+i[2]+". "+i[4]+"; "+i[5]+". "+i[6]+". "+i[7]
            elif(i[1] == "" and i[5] == ""):
                words = i[0]+", and "+i[3]+" "+i[2]+". "+i[4]+". "+i[6]+". "+i[7]
            elif(i[2] == "" and i[3] == ""):
                words = i[0]+", "+i[1]+". "+i[4]+"; "+i[5]+". "+i[6]+". "+i[7]
            elif(i[3] == "" and i[5] == ""):
                words = i[0]+", "+i[1]+" and "+i[2]+". "+i[4]+". "+i[6]+". "+i[7]
            elif(i[1] == ""):
                words = i[0]+" and "+i[3]+" "+i[2]+". "+i[4]+"; "+i[5]+". "+i[6]+". "+i[7]
            elif(i[3] == ""):
                words = i[0]+", "+i[1]+" and "+i[2]+". "+i[4]+"; "+i[5]+". "+i[6]+". "+i[7]
            elif(i[5] == ""):
                words = i[0]+", "+i[1]+" and "+i[3]+" "+i[2]+". "+i[4]+". "+i[6]+". "+i[7]
            else:
                words = i[0]+", "+i[1]+" and "+i[3]+" "+i[2]+". "+i[4]+"; "+i[5]+". "+i[6]+". "+i[7]
            if(i[8] != ""):
                words += " "+i[8]+"."
            else:
                words += "."
            book_str = tk.StringVar()
            tk.Checkbutton(scrollable_frame, text=words, onvalue=words, offvalue="", variable=book_str).pack(anchor='w')
            book_lst.append(book_str)
            num_res += 1
        ttk.Label(results_frame, text=str(num_res)+" results").pack(padx=5, pady=5, side=BOTTOM)
        canvas.pack(side=LEFT, fill="both", expand=True)

        def alter_callback():
            location = update_loc.get()
            if(location == "select"):
                messagebox.showinfo("showinfo", "pick a new location", icon="error")
            else:
                try:
                    for book in book_lst:
                        words = book.get()
                        if(words == ""): continue
                        if words.find(',') > -1: has_fname = TRUE 
                        else: has_fname = FALSE
                        if words.find(';') > -1: has_series = TRUE 
                        else: has_series = FALSE
                        temp = re.split(r"[,.;]", words)
                        for i in range(len(temp)):
                            temp[i] = str(temp[i].strip())
                            if(temp[i] == ""):
                                temp.pop(i)
                                i -= 1
                        if(location == "loaned"):
                            location = "loaned to " + update_loaned.get()
                        elif(location == "digital"):
                            location = update_digital.get()
                        temp.insert(0, location)

                        cmd = "UPDATE owned_books SET location=%s WHERE "
                        if(has_fname and has_series):
                            cmd += "author_last=%s AND author_first=%s AND title=%s AND series=%s AND isbn=%s AND location=%s"
                        elif(has_fname):
                            cmd += "author_last=%s AND author_first=%s AND title=%s AND isbn=%s AND location=%s"
                        elif(has_series):
                            cmd += "author_last=%s AND title=%s AND series=%s AND isbn=%s AND location=%s"

                        cursor.execute(cmd, temp)
                        mydb.commit()
                        if(search_type == 1):
                            search_callback()
                        elif(search_type == 2):
                            searchall_callback()
                    messagebox.showinfo("showinfo", "location(s) updated", icon="info")
                except:
                    messagebox.showinfo("showinfo", "could not update location(s)", icon="error")

        alter_button = ttk.Button(search_page, text="change location of selected book(s)", command=alter_callback)
        alter_button.grid(column=5, row=7, columnspan=2, padx=5, pady=5)

        results_frame.grid(column=4, row=0, columnspan=4, rowspan=5)
    button_frame.grid(column=1, row=8, columnspan=2, padx=5, pady=5)

#-------------------------------------------------------------------------------
#creates the add book gui page
def add_book_page(root):
    #add book frame
    add_book = tk.Frame(root)
    add_book.columnconfigure(4, weight=5)
    add_book.rowconfigure(11, weight=1)
    add_book.pack()

    #image
    image_label = tk.Label(add_book, image=tk_image)
    image_label.grid(columnspan=4, rowspan=3)

    #heading
    head_label = tk.Label(add_book, text="add book")
    head_label.config(font=("Arial", 24))
    head_label.grid(column=1, row=3, columnspan=2, padx=5, pady=5)

    #author last name
    last_frame = tk.Frame(add_book)
    last_label = tk.Label(last_frame, text="author last name:")
    last = tk.Entry(last_frame)
    last_label.pack(side=LEFT)
    last.pack(side=RIGHT)
    last_frame.grid(column=1, row=4, padx=5, pady=5, sticky=E)

    #author first name
    first_frame = tk.Frame(add_book)
    first_label = tk.Label(first_frame, text="author first name:")
    first = tk.Entry(first_frame)
    first_label.pack(side=LEFT)
    first.pack(side=RIGHT)
    first_frame.grid(column=2, row=4, padx=5, pady=5, sticky=E)

    #second author last name
    two_last_frame = tk.Frame(add_book)
    two_last_label = tk.Label(two_last_frame, text="second author last name:")
    two_last = tk.Entry(two_last_frame)
    two_last_label.pack(side=LEFT)
    two_last.pack(side=RIGHT)
    two_last_frame.grid(column=1, row=5, padx=5, pady=5, sticky=E)

    #second author first name
    two_first_frame = tk.Frame(add_book)
    two_first_label = tk.Label(two_first_frame, text="second author first name:")
    two_first = tk.Entry(two_first_frame)
    two_first_label.pack(side=LEFT)
    two_first.pack(side=RIGHT)
    two_first_frame.grid(column=2, row=5, padx=5, pady=5, sticky=E)

    #book title
    title_frame = tk.Frame(add_book)
    title_label = tk.Label(title_frame, text="book title:")
    title = tk.Entry(title_frame)
    title_label.pack(side=LEFT)
    title.pack(side=RIGHT)
    title_frame.grid(column=1, row=6, padx=5, pady=5, sticky=E)

    #series
    series_frame = tk.Frame(add_book)
    series_label = tk.Label(series_frame, text="book series:")
    series = tk.Entry(series_frame)
    series_label.pack(side=LEFT)
    series.pack(side=RIGHT)
    series_frame.grid(column=2, row=6, padx=5, pady=5, sticky=E)

    #isbn
    isbn_frame = tk.Frame(add_book)
    isbn_label = tk.Label(isbn_frame, text="book isbn:")
    isbn = tk.Entry(isbn_frame)
    isbn_label.pack(side=LEFT)
    isbn.pack(side=RIGHT)
    isbn_frame.grid(column=1, row=7, padx=5, pady=5, sticky=E)

    #isbn search
    def search_callback():
        num = isbn.get()
        if(num == ""):
            messagebox.showinfo("showinfo", "invalid isbn", icon="warning")
        else:
            book_info = scrapebook.crawl(num)
            if(book_info == "error"):
                messagebox.showinfo("showinfo", "could not find book", icon="warning")
            else:
                name = str(book_info[0])
                t = str(book_info[1])
                l = ""
                f = ""
                space = name.rfind(' ')
                if(space > -1):
                    l = name[space+1:]
                    f = name[:space]
                else:
                    l = name
                res = messagebox.askquestion("search result", "Is the book " + t + " by " + name + "?")
                if(res == "yes"):
                    last.delete(0, tk.END)
                    last.insert(0, l)
                    first.delete(0, tk.END)
                    first.insert(0, f)
                    title.delete(0, tk.END)
                    title.insert(0, t)

    search_button = ttk.Button(add_book, text="search by isbn", command=search_callback)
    search_button.grid(column=1, row=8, padx=5, pady=5)

    #loaned
    loaned_frame = tk.Frame(add_book)
    loaned_label = tk.Label(loaned_frame, text="loaned to:")
    loaned = tk.Entry(loaned_frame)
    loaned_label.pack(side=LEFT)
    loaned.pack(side=RIGHT)

    #digital
    digital_frame = tk.Frame(add_book)
    digital_label = tk.Label(digital_frame, text="digital format:")
    digital = StringVar(digital_frame)
    digital_cb = ttk.Combobox(digital_frame, textvariable=digital)
    digital_cb['values'] = ("ibook", "glose book", "pdf")
    digital_cb['state'] = 'readonly'
    digital_cb.set("select")
    digital_label.pack(side=LEFT)
    digital_cb.pack(side=RIGHT)

    def location_callback(*args):
        loaned_frame.grid_forget()
        digital_frame.grid_forget()
        val = loc.get()
        if(val == "loaned"):
            loaned_frame.grid(column=2, row=8, padx=5, pady=5, sticky=E)
        elif(val == "digital"):
            digital_frame.grid(column=2, row=8, padx=5, pady=5, sticky=E)

    #location
    loc_frame = tk.Frame(add_book)
    loc_label = tk.Label(loc_frame, text="book location:")
    loc = StringVar(loc_frame)
    loc_cb = ttk.Combobox(loc_frame, textvariable=loc)
    loc_cb['values'] = ("anne's house", "keith's house", "maddie's apartment", "andrew's apartment", "ruthie's house", "loaned", "digital")
    loc_cb['state'] = 'readonly'
    loc_cb.set("select")
    loc_label.pack(side=LEFT)
    loc_cb.pack(side=RIGHT)
    loc_frame.grid(column=2, row=7, padx=5, pady=5, sticky=E)
    loc.trace('w', location_callback)

    #empty label
    empty_label = tk.Label(add_book)
    empty_label.grid(column=1, row=8, columnspan=2, padx=5, pady=5)

    #extra location
    exloc_frame = tk.Frame(add_book)
    exloc_label = tk.Label(exloc_frame, text="detailed location:")
    exloc = tk.Entry(exloc_frame)
    exloc_label.pack(side=LEFT)
    exloc.pack(side=RIGHT)
    exloc_frame.grid(column=1, columnspan=2, row=9, padx=5, pady=5, sticky=E)

    #buttons
    button_frame = ttk.Frame(add_book)

    def cancel_callback():
        add_book.destroy()
        main_page(root)

    cancel_button = ttk.Button(button_frame, text="cancel", command=cancel_callback)
    cancel_button.pack(side=LEFT)

    def submit_callback():
        lst = [last.get(), first.get(), two_last.get(), two_first.get(), title.get(), series.get(), isbn.get()]
        location = loc.get()
        if(location == "loaned"):
            lst.append("loaned to " + loaned.get())
        elif(location == "digital"):
            lst.append(digital.get())
        else:
            lst.append(location)
        lst.append(exloc.get())
        try:
            #insert into owned_books
            insert = "INSERT INTO owned_books (author_last, author_first, second_last, second_first, title, series, isbn, location, detailed_loc) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(insert, lst)
            mydb.commit()
            messagebox.showinfo("showinfo", "book added", icon="info")
            add_book.destroy()
            add_book_page(root)
        except:
            messagebox.showinfo("showinfo", "book could not be added", icon="error")

    submit_button = ttk.Button(button_frame, text="submit", command=submit_callback)
    submit_button.pack(side=RIGHT)

    button_frame.grid(column=1, columnspan=2, row=10, padx=5, pady=5)

    #empty label
    empty_label2 = tk.Label(add_book)
    empty_label2.grid(column=1, row=11, columnspan=2, padx=5, pady=5)

    add_book.pack()

#-------------------------------------------------------------------------------
#make gui window
root = tk.Tk()
root.title('book catalog')
img = Image.open("bookcase.png")
img = img.resize((400,300))
tk_image = ImageTk.PhotoImage(img)
main_page(root)
root.mainloop()

#stop mySQL
os.system("sudo /usr/local/mysql/support-files/mysql.server stop")