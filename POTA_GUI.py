from datetime import date,datetime,timezone
import tkinter, csv
from tkinter import messagebox

class Contact:
    def __init__(self, mycallsign, mypark, mypower, mymode, callsign, freq, QTH, date=date.today(), time=datetime.now(), in_RST="599", out_RST="599"):
    # Creating empty contact (QSO) record
        self._mycallsign = mycallsign
        self._mypark = mypark
        self._mypower = mypower
        self._mymode = mymode
        self._callsign = callsign
        self._freq = freq
        self._date = date
        self._time = time
        self._QTH = QTH
        self._in_RST = in_RST
        self._out_RST = out_RST

    def __str__(self):
    # Returning current contents
        output = (f"My Callsign: {self.mycallsign}          Their callsign: {self.callsign}\n"
                  f"Park: {self.mypark}                     Their QTH: {self.QTH}\n"
                  f"Power: {self.mypower}                   Mode: {self.mymode}\n"
                  f"Date: {self.date}                       Time: {self.time}\n"
                  f"My RST: {self.in_RST}                   Their RST: {self.out_RST}\n"
                  f"Frequency/Band: {self.freq}")
        return output

    @property
    def mycallsign(self):
        return self._mycallsign

    @mycallsign.setter
    def mycallsign(self, value):
        if value != "":
            self._mycallsign = value
        else:
            raise ValueError("My Callsign may not be blank")

    @property
    def mypark(self):
        return self._mypark

    @mypark.setter
    def mypark(self, value):
        if value != "":
            self._mypark = value
        else:
            raise ValueError("Park designation may not be blank")

    @property
    def mypower(self):
        return self._mypower

    @mypower.setter
    def mypower(self, value):
        if value != "":
            self._mypower = value
        else:
            raise ValueError("Power level may not be blank")

    @property
    def mymode(self):
        return self._mymode

    @mymode.setter
    def mymode(self, value):
        if value != "":
            self._mymode = value
        else:
            raise ValueError("Transmission mode may not be blank")

    @property
    def callsign(self):
        return self._callsign

    @callsign.setter
    def callsign(self, value):
        if value != "":
            self._callsign = value
        else:
            raise ValueError("Incoming callsign may not be blank")

    @property
    def freq(self):
        return self._freq

    @freq.setter
    def freq(self, value):
        if value != "":
            self._freq = value
        else:
            raise ValueError("Frequency may not be blank")

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if value != "" and isinstance(value, datetime.date):
            self._date = value
        elif value == "":
            raise ValueError("QSO Date may not be blank")
        else:
            raise ValueError("Invalid QSO Date")

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        if value != "" and isinstance(value, datetime):
            self._time = value
        elif value == "":
            raise ValueError("QSO Time may not be blank")
        else:
            raise ValueError("Invalid QSO Time")

    @property
    def QTH(self):
        return self._QTH

    @QTH.setter
    def QTH(self, value):
        self._QTH = value

    @property
    def in_RST(self):
        return self._in_RST

    @in_RST.setter
    def in_RST(self, value):
        if len(in_RST) == 3:
            if in_RST[0] in [1-5] and in_RST[1] in [1-9] and in_RST[2] in [1-9]:
                self._in_RST = value
            else:
                raise ValueError("Invalid RST Format #1")
        elif len(in_RST) == 2:
            if in_RST[0] in [1 - 5] and in_RST[1] in [1 - 9]:
                self._in_RST = value
            else:
                raise ValueError("Invalid RST Format #2")
        else:
            raise ValueError("Invalid RST Format #3")

    @property
    def out_RST(self):
        return self._out_RST

    @in_RST.setter
    def out_RST(self, value):
        if len(out_RST) == 3:
            if out_RST[0] in [1 - 5] and out_RST[1] in [1 - 9] and out_RST[2] in [1 - 9]:
                self._out_RST = value
            else:
                raise ValueError("Invalid RST Format #1")
        elif len(out_RST) == 2:
            if out_RST[0] in [1 - 5] and out_RST[1] in [1 - 9]:
                self._out_RST = value
            else:
                raise ValueError("Invalid RST Format #2")
        else:
            raise ValueError("Invalid RST Format #3")

class GUI:
    def __init__(self):
        self.logfile = "POTA_log.csv"

        self.root = tkinter.Tk()
        self.root.geometry("800x350")

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

        self.menubar = tkinter.Menu(self.root)

        self.filemenu = tkinter.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Set Logfile", command=self.set_logfile)
        self.filemenu.add_command(label="Close", command=self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close Without Question", command=exit)

        self.actionmenu = tkinter.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="Commit Record", command=self.commit)

        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")

        self.root.config(menu=self.menubar)

        self.root.columnconfigure(0, weight=30)
        self.root.columnconfigure(1, weight=20)
        self.root.columnconfigure(2, weight=20)
        self.root.columnconfigure(3, weight=50)
        self.root.columnconfigure(4, weight=20)
        self.root.columnconfigure(5, weight=20)


        self.canvas = tkinter.Canvas(self.root, height=150, width=180)
        self.canvas.grid(row=0, column=0, rowspan=5)
        self.gif1 = tkinter.PhotoImage(file='POTAlogo.gif')
        self.canvas.create_image(10, 10, anchor="nw", image=self.gif1)

        self.lblMyCallsign = tkinter.Label(self.root, text = "My Callsign", font = ("Arial", 12), justify="left")
        self.lblMyCallsign.grid(row=0, column=1)
        self.entMyCallsign = tkinter.Entry(self.root, width=10, font=("Arial", 12), textvariable=varMyCallsign)
        self.entMyCallsign.grid(row=0, column=2)

        self.lblMyPark = tkinter.Label(self.root, text="My Park", font=("Arial", 12), justify="left")
        self.lblMyPark.grid(row=1, column=1)
        self.entMyPark = tkinter.Entry(self.root, width=10, font=("Arial", 12), textvariable=varMyPark)
        self.entMyPark.grid(row=1, column=2)

        self.lblDate = tkinter.Label(self.root, text="Date", font=("Arial", 12), justify="left")
        self.lblDate.grid(row=2, column=1)
        self.entDate = tkinter.Entry(self.root, width=10, font=("Arial", 12), textvariable=varDate)
        self.entDate.grid(row=2, column=2)

        self.lblFreq = tkinter.Label(self.root, text="Frequency", font=("Arial", 12), justify="left")
        self.lblFreq.grid(row=0, column=4)
        self.entFreq = tkinter.Entry(self.root, width=10, font=("Arial", 12), textvariable=varFreq)
        self.entFreq.grid(row=0, column=5)

        self.lblMode = tkinter.Label(self.root, text="Mode", font=("Arial", 12), justify="left")
        self.lblMode.grid(row=1, column=4)
        self.entMode = tkinter.Entry(self.root, width=10, font=("Arial", 12), textvariable=varMyMode)
        self.entMode.grid(row=1, column=5)

        self.lblPower = tkinter.Label(self.root, text="Power", font=("Arial", 12), justify="left")
        self.lblPower.grid(row=2, column=4)
        self.entPower = tkinter.Entry(self.root, width=10, font=("Arial", 12), textvariable=varMyPower)
        self.entPower.grid(row=2, column=5)

        self.lblTime = tkinter.Label(self.root, text="Time", font=("Arial", 18))
        self.lblTime.grid(row=6, column=0, pady=20, sticky="s")
        self.entTime = tkinter.Entry(self.root, width=10, font=("Arial", 18), textvariable=varTime)
        self.entTime.grid(row=7, column=0, padx="10", sticky="s")

        self.lblCallsign = tkinter.Label(self.root, text="Callsign", font=("Arial", 18), justify="left")
        self.lblCallsign.grid(row=6, column=1)
        self.entCallsign = tkinter.Entry(self.root, width=10, font=("Arial", 18), textvariable=varCallsign)
        self.entCallsign.grid(row=7, column=1, padx="10", sticky="s")

        self.lblQTH = tkinter.Label(self.root, text="QTH", font=("Arial", 18), justify="left")
        self.lblQTH.grid(row=6, column=2)
        self.entQTH = tkinter.Entry(self.root, width=10, font=("Arial", 18), textvariable=varQTH)
        self.entQTH.grid(row=7, column=2, padx="10", sticky="s")

        self.lblOut_RST = tkinter.Label(self.root, text="Their RST", font=("Arial", 18), justify="left")
        self.lblOut_RST.grid(row=6, column=3)
        self.entOut_RST = tkinter.Entry(self.root, width=10, font=("Arial", 18), textvariable=varOut_RST)
        self.entOut_RST.grid(row=7, column=3, padx="10", sticky="s")

        self.lblIn_RST = tkinter.Label(self.root, text="My RST", font=("Arial", 18), justify="left")
        self.lblIn_RST.grid(row=6, column=4)
        self.entIn_RST = tkinter.Entry(self.root, width=10, font=("Arial", 18), textvariable=varIn_RST)
        self.entIn_RST.grid(row=7, column=4, padx="10", sticky="s")

#        contact = Contact(varMyCallsign.get(), varMyPark.get(), varMyPower.get(), varMyMode.get(), varCallsign.get(), varFreq.get(), varQTH.get(), varDate.get(), varTime.get(), varIn_RST.get(), varOut_RST.get())

        self.btnCommit = tkinter.Button(self.root, text="Commit Record", font=("Arial", 16), command=self.commit)
        self.btnCommit.grid(row=8, column=2, pady="20")

        self.root.protocol("WM_DEKETE", self.on_closing)
        self.root.mainloop()


    def on_closing(self):
        print("Goodbye Cruel World")
        if messagebox.askyesno(title = "Quit?", message="Do you want to quit without saving?"):
            self.root.destroy()

    def commit(self):
        with open(self.logfile, 'a') as csvfile:
            filewriter = csv.writer(csvfile)
            filewriter.writerow((self.entMyCallsign.get(), self.entMyPark.get(), self.entPower.get(), self.entMode.get(), self.entCallsign.get(), self.entFreq.get(), self.entQTH.get(), self.entDate.get(), self.entTime.get(), self.entIn_RST.get(), self.entOut_RST.get()))

        self.entTime.delete(0, "end")
        self.entCallsign.delete(0, "end")
        self.entQTH.delete(0, "end")
        self.entOut_RST.delete(0, "end")
        self.entIn_RST.delete(0, "end")

    def set_logfile(self):
        pass
