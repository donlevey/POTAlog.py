# Written in PyCharm on Fedora Linux

from datetime import datetime
import tkinter, csv
from tkinter import messagebox, filedialog, ttk

logfile = "POTA_log.csv"

def main():

    def commit(logfile, MyCallsign, MyPark, Power, Mode, Callsign, Freq, QTH, Date, Time, In_RST, Out_RST):
        isgood = verify_data(Mode, Freq, Date, Time, In_RST, Out_RST)

        if isgood > 0:  return

        Date = format_date(Date)
        Time = format_time(Time)

        with open(logfile, 'a') as csvfile:
            filewriter = csv.writer(csvfile)
            filewriter.writerow((MyCallsign, MyPark, Power, Mode, Callsign, Freq, QTH, Date, Time, In_RST, Out_RST))

        entTime.delete(0, "end")
        entCallsign.delete(0, "end")
        entQTH.delete(0, "end")
        entOut_RST.delete(0, "end")
        entIn_RST.delete(0, "end")


    root = tkinter.Tk()
    root.geometry("800x350")
    root.title("POTA log")

    varMyCallsign   = tkinter.StringVar()
    varMyPark       = tkinter.StringVar()
    varMyPower      = tkinter.StringVar()
    varMyMode       = tkinter.StringVar()
    varCallsign     = tkinter.StringVar()
    varFreq         = tkinter.StringVar()
    varDate         = tkinter.StringVar()
    varTime         = tkinter.StringVar()
    varQTH          = tkinter.StringVar()
    varIn_RST       = tkinter.StringVar()
    varOut_RST      = tkinter.StringVar()

    def capsMyCallsign(event):
        varMyCallsign.set(varMyCallsign.get().upper())

    def capsMyPark(event):
        varMyPark.set(varMyPark.get().upper())

    def capsCallsign(event):
        varCallsign.set(varCallsign.get().upper())

    def capsQTH(event):
        varQTH.set(varQTH.get().upper())

    menubar = tkinter.Menu(root)

    filemenu = tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Set Logfile", command=set_logfile)
    filemenu.add_command(label="Close", command=on_closing)
    filemenu.add_separator()
    filemenu.add_command(label="Close Without Question", command=exit)

    actionmenu = tkinter.Menu(menubar, tearoff=0)
    actionmenu.add_command(label="Commit Record", command = lambda: commit(logfile,  entMyCallsign.get(), entMyPark.get(), entPower.get(), entMode.get(), entCallsign.get(), entFreq.get(), entQTH.get(), entDate.get(), entTime.get(), entIn_RST.get(), entOut_RST.get()))

    menubar.add_cascade(menu=filemenu, label="File")
    menubar.add_cascade(menu=actionmenu, label="Action")

    root.config(menu=menubar)

    root.columnconfigure(0, weight=30)
    root.columnconfigure(1, weight=20)
    root.columnconfigure(2, weight=20)
    root.columnconfigure(3, weight=50)
    root.columnconfigure(4, weight=20)
    root.columnconfigure(5, weight=20)


    canvas = tkinter.Canvas(root, height=150, width=180)
    canvas.grid(row=0, column=0, rowspan=5)
    gif1 = tkinter.PhotoImage(file='POTAlogo.gif')
    canvas.create_image(10, 10, anchor="nw", image=gif1)

    lblMyCallsign = tkinter.Label(root, text = "My Callsign", font = ("Arial", 12), justify="left")
    lblMyCallsign.grid(row=0, column=1)
    entMyCallsign = tkinter.Entry(root, width=10, font=("Arial", 12), textvariable=varMyCallsign)
    entMyCallsign.grid(row=0, column=2)
    entMyCallsign.bind("<KeyRelease>", capsMyCallsign)

    lblMyPark = tkinter.Label(root, text="My Park", font=("Arial", 12), justify="left")
    lblMyPark.grid(row=1, column=1)
    entMyPark = tkinter.Entry(root, width=10, font=("Arial", 12), textvariable=varMyPark)
    entMyPark.grid(row=1, column=2)
    entMyPark.bind("<KeyRelease>", capsMyPark)

    lblDate = tkinter.Label(root, text="Date", font=("Arial", 12), justify="left")
    lblDate.grid(row=2, column=1)
    entDate = tkinter.Entry(root, width=10, font=("Arial", 12), textvariable=varDate)
    entDate.grid(row=2, column=2)

    lblFreq = tkinter.Label(root, text="Freq. (MHz)", font=("Arial", 12), justify="left")
    lblFreq.grid(row=0, column=4)
    cmbFreq = ttk.Combobox(state="readonly", width=8, values=["1.6", "3.5", "7", "10", "14", "18", "21", "24", "28", "50", "144"], textvariable=varFreq)
    cmbFreq.grid(row=0, column=5)

    lblMode = tkinter.Label(root, text="Mode", font=("Arial", 12), justify="left")
    lblMode.grid(row=1, column=4)
    cmbMode = ttk.Combobox(state="readonly", width=8, values=["CW", "SSB", "Digital"], textvariable=varMyMode)
    cmbMode.grid(row=1, column=5)

    lblPower = tkinter.Label(root, text="Power", font=("Arial", 12), justify="left")
    lblPower.grid(row=2, column=4)
    entPower = tkinter.Entry(root, width=10, font=("Arial", 12), textvariable=varMyPower)
    entPower.grid(row=2, column=5)

    lblTime = tkinter.Label(root, text="Time", font=("Arial", 18))
    lblTime.grid(row=6, column=0, pady=20, sticky="s")
    entTime = tkinter.Entry(root, width=10, font=("Arial", 18), textvariable=varTime)
    entTime.grid(row=7, column=0, padx="10", sticky="s")

    lblCallsign = tkinter.Label(root, text="Callsign", font=("Arial", 18), justify="left")
    lblCallsign.grid(row=6, column=1)
    entCallsign = tkinter.Entry(root, width=10, font=("Arial", 18), textvariable=varCallsign)
    entCallsign.grid(row=7, column=1, padx="10", sticky="s")
    entCallsign.bind("<KeyRelease>", capsCallsign)

    lblQTH = tkinter.Label(root, text="QTH", font=("Arial", 18), justify="left")
    lblQTH.grid(row=6, column=2)
    entQTH = tkinter.Entry(root, width=10, font=("Arial", 18), textvariable=varQTH)
    entQTH.grid(row=7, column=2, padx="10", sticky="s")
    entQTH.bind("<KeyRelease>", capsQTH)

    lblOut_RST = tkinter.Label(root, text="Their RST", font=("Arial", 14), justify="left")
    lblOut_RST.grid(row=6, column=3)
    entOut_RST = tkinter.Entry(root, width=10, font=("Arial", 18), textvariable=varOut_RST)
    entOut_RST.grid(row=7, column=3, padx="10", sticky="s")

    lblIn_RST = tkinter.Label(root, text="My RST", font=("Arial", 14), justify="left")
    lblIn_RST.grid(row=6, column=4)
    entIn_RST = tkinter.Entry(root, width=5, font=("Arial", 18), textvariable=varIn_RST)
    entIn_RST.grid(row=7, column=4, padx="10", sticky="s")

    btnVerify = tkinter.Button(root, text="  Verify Data Format  ", font=("Arial", 16), command=lambda: verify_data(cmbMode.get(), cmbFreq.get(), entDate.get(), entTime.get(), entIn_RST.get(), entOut_RST.get()))
    btnVerify.grid(row=8, column=0, pady="20")

    btnCommit = tkinter.Button(root, text="     Commit Record     ", font=("Arial", 16), command=lambda: commit(logfile, entMyCallsign.get(), entMyPark.get(), entPower.get(), cmbMode.get(), entCallsign.get(), cmbFreq.get(), entQTH.get(), entDate.get(), entTime.get(), entIn_RST.get(), entOut_RST.get()))
    btnCommit.grid(row=8, column=4, pady="20")

    root.protocol("WM_DELETE", on_closing)
    root.mainloop()


def on_closing():
#    print("Goodbye Cruel World")
    if messagebox.askyesno(title = "Quit?", message="Do you want to quit without saving?"):
        root.destroy()


def set_logfile():
    global logfile

    filetypes = (('CSV files', '*.csv'), ('All files', '*.*'))
    returnfile = filedialog.asksaveasfilename(title='Open a logfile', initialdir='~', filetypes=filetypes)
    if returnfile != "": logfile = returnfile


def verify_data(Mode, Freq, In_RST, Out_RST):
    errors = 0

    if validate_mode(Mode) != 0:
        show_error("Invalid Mode")
        errors += 1

    if validate_freq(Freq) != 0:
        show_error("Invalid Freq Band")
        errors += 1

    if validate_RST(Out_RST) != 0:
        show_error("Invalid Outgoing RST")
        errors += 1

    if validate_RST(In_RST) != 0:
        show_error("Invalid Incoming RST")
        errors += 1

    print("Errors: ", errors)
    if errors > 0:
        show_error(f"Total errors: {errors}")
        return errors
    else:
        messagebox.showinfo("Validate", "No Errors")
        return errors


def format_date(Date):
    if Date != "":
        return Date
    else:
        today = datetime.utcnow().date()
        return today

def format_time(Time):
    if Time != "":
        return Time
    else:
        now = datetime.utcnow()
        current_time = now.strftime("%H:%M:%S")
        return current_time


def validate_mode(mode):
    if mode in ["CW", "SSB", "Digital"]:
        return 0
    else:
        return 1


def validate_freq(freq):
    if freq in ["1.5", "3.5", "7", "10", "14", "18", "21", "24", "28", "50", "144"]:
        return 0
    else:
        return 1


def validate_RST(rst):
    if len(rst) == 3:
        if (int(rst[0]) in range(1, 6)) and (int(rst[1]) in range(1, 10)) and (int(rst[2]) in range(1, 10)):
           return 0
        else:
           return 1
    elif len(rst) == 2:
        if (int(rst[0]) in range(1, 6)) and (int(rst[1]) in range(1, 10)):
           return 0
        else:
           return 1
    else:
        return 1

def show_error(message):
    messagebox.showerror("ERROR", message)


if __name__ == "__main__":
    main()







#
#       export to ADIF format
#       export to Cabrillo format
#       uplocad to Logbook OF The World (may not be possible without authorization)
#