#import sys,os; sys.path.append(os.environ['BMESAHMETDIR']); import bmes

from tkinter import *
from tkinter.font import Font
from PIL import ImageTk, Image
from tkinter import ttk
from data_read import*
import re

class GUI:
    def __init__(self) -> None:
        self.master = Tk()
        self.master.title("Cancer Treatment TOOLBOX v1.0")
        self.master.geometry("1100x700")
        self.master.configure(bg="black")
        self.baseDIR = "C:\\Users\\sport\\Dropbox\\bmes550.RyanKrawczyk.rk836\\Final\\"
        self.createMainPage()
        self.createTreatmentPage()
        self.createTrialsPage()
        self.showMainPage()

    def create_treatments_button(self):
        self.treatment_button = Button(self.master, text="Treatments", bg ="white", width=10, height=2, font=("Arial", 32 ),command=self.showTreatmentPage)

    def create_trials_button(self):
        self.trials_button = Button(self.master, text="Trials", bg ="white", width=10, height=2, font=("Arial", 32 ),command=self.showTrialPage)

    def create_cancer_image(self):
        self.cancer_img = PhotoImage(file=self.baseDIR+"cancer.png")
        self.cancerImage = Label(self.master, image=self.cancer_img)

    def hideTreatmentPage(self):
        
        self.treatmentLabel.place_forget()
        self.tableOfTreatments.place_forget()
        self.treescrollx.place_forget()
        self.treescrolly.place_forget()
    
        self.filter_btn.place_forget()
        self.filterFDA_entry.place_forget()
        self.filter_FDA_label.place_forget()
        self.filter_TARGETS_entry.place_forget()
        self.filter_TARGETS_label.place_forget()
        self.goBack_button.place_forget()

    def createTreatmentLabel(self):
        self.treatmentLabel = Label(self.master, text="Treatments", font=("Arial", 40),bg="black",fg="white")

    def createTreeview(self):
        columns = ('DrugName', 'FDA','Targets')
        self.tableOfTreatments = ttk.Treeview(self.master,columns=columns,show='headings')
        s = ttk.Style()
        s.configure('Treeview', font=('Helvetica', 16),rowheight=59 , fieldbackground = "white")
        self.treescrolly = ttk.Scrollbar(self.master, orient="vertical", command=self.tableOfTreatments.yview)
        self.treescrollx = ttk.Scrollbar(self.master, orient="horizontal", command=self.tableOfTreatments.xview)
        self.tableOfTreatments.configure(xscrollcommand=self.treescrollx.set, yscrollcommand=self.treescrolly.set)
        
    def fillTable(self):
        tv1 = self.tableOfTreatments
        tv1.delete(*tv1.get_children())
        tv1["show"] = "headings"
        for column in tv1["columns"]:
            if column=="FDA":
                tv1.column(column, width = 100) 
            else:
                tv1.column(column, width = 350) 
            tv1.heading(column, text=column)

        df_rows = THE_LIST_OF_MEDICINES
        for row in df_rows:
            tv1.insert("", "end", values=row)

    def fillTable_w_input(self,input_):
        tv1 = self.tableOfTreatments
        tv1.delete(*tv1.get_children())
        tv1["show"] = "headings"
        for column in tv1["columns"]:
            if column=="FDA":
                tv1.column(column, width = 100) 
            else:
                tv1.column(column, width = 350) 
            tv1.heading(column, text=column)

        df_rows = input_
        for row in df_rows:
            tv1.insert("", "end", values=row)

    def createTreatmentSortButton(self):
        self.filter_btn = Button(self.master,command=self.filter,bg="white",text="Filter",width=10,height=1,font=("Arial",16))
        self.filter_FDA_label = Label(self.master, text="FDA Type:",bg="black",fg="white")
        self.filterFDA_entry = Entry(self.master,width=10)
        self.filter_TARGETS_label = Label(self.master, text="Target Type:",bg="black",fg="white")
        self.filter_TARGETS_entry = Entry(self.master,width=10)

    def filter(self):
        fda_filter = self.filterFDA_entry.get().upper()
        target_filter = self.filter_TARGETS_entry.get().upper()
        medicine_list =  THE_LIST_OF_MEDICINES
        outList = []

        if target_filter == "" and fda_filter == "":
            self.fillTable()
            return 
        elif fda_filter == "Y" and target_filter == "":
            for med in medicine_list:
                if med[1] == "Y":
                    outList.append(med)

            self.fillTable_w_input(outList)
    
        elif fda_filter == "N" and target_filter == "":
            for med in medicine_list:
                if med[1] == "N":
                    outList.append(med)
                
            self.fillTable_w_input(outList)

        elif fda_filter == "Y":
            for med in medicine_list:
                if med[1] == "Y":
                    outList.append(med)

            voidL = []

            for med in outList:
                if re.search(target_filter,med[2]):
                    voidL.append(med)
            self.fillTable_w_input(voidL)

        elif fda_filter == "N":
            for med in medicine_list:
                if med[1] == "N":
                    outList.append(med)

            voidL = []

            for med in outList:
                if re.search(target_filter,med[2]):
                    voidL.append(med)
            self.fillTable_w_input(voidL)

        elif fda_filter == "":
            for med in medicine_list:
                if re.search(target_filter,med[2]):
                    outList.append(med)
            self.fillTable_w_input(outList)

        """if fda_filter == "":
            for med in medicine_list:
                if re.search(target_filter,med[2]):
                    print(med)"""

    def filterTrials(self):
        genderFilter = self.Gender_Entry.get()
        NTCFilter = self.NTC_num_Entry.get()
        CancerTypeFilter = self.CancerType_Entry.get()
        AgeFilter = self.Age_Entry.get()
        CountryFilter = self.Country_Entry.get()

        trails_list = THE_LIST_OF_CANCERS
        the_filtered_output = trails_list
        theNTC_filter_out = []
        theGender_filter_out = []
        theAge_filter_out = []
        theCountry_filter_out = []
        theCancerType_filter_out = []

        

        if NTCFilter == "":
            theNTC_filter_out = trails_list
        else:
            for trail in trails_list:
                if re.search(NTCFilter,trail[0]):
                    theNTC_filter_out.append(trail)

        #print(theNTC_filter_out)

        if genderFilter == "":
            theGender_filter_out = theNTC_filter_out
        else:
            for trail in theNTC_filter_out:
                if re.search(genderFilter,trail[1]):
                    theGender_filter_out.append(trail)

        #print(theGender_filter_out)

        if AgeFilter == "":
            theAge_filter_out = theGender_filter_out
        else:
            for trail in theGender_filter_out:
                if re.search(AgeFilter,trail[2]):
                    theAge_filter_out.append(trail)

        #print(theAge_filter_out)

        if CountryFilter == "":
            theCountry_filter_out = theAge_filter_out
        else:
            for trail in theAge_filter_out:
                if re.search(CountryFilter,trail[3]):
                    theCountry_filter_out.append(trail)

        if CancerTypeFilter == "":
            theCancerType_filter_out = theCountry_filter_out
        else:
            for trail in theCountry_filter_out:
                if re.search(CancerTypeFilter,trail[4]):
                    theCancerType_filter_out.append(trail)

        self.fillTrialTable(theCancerType_filter_out)
        #print(theCancerType_filter_out)

    def createTrialSort_Labels(self):
        self.filter_trails = Button(self.master,command=self.filterTrials,bg="white",text="Filter",width=10,height=1,font=("Arial",25))
        self.NTC_num_label = Label(self.master, text="NTC Number:",bg="black",fg="white",font=('Arial',16))
        self.NTC_num_Entry = Entry(self.master,width=20,font=("Arial",16))
        self.Gender_label = Label(self.master, text="Gender:",bg="black",fg="white",font=('Arial',16))
        self.Gender_Entry = Entry(self.master,width=10,font=('Arial',16))
        self.Age_label = Label(self.master, text="Age:",bg="black",fg="white",font=('Arial',16))
        self.Age_Entry = Entry(self.master,width=10,font=('Arial',16))
        self.Country_label = Label(self.master, text="Country PI:",bg="black",fg="white",font=('Arial',16))
        self.Country_Entry = Entry(self.master,width=16,font=('Arial',16))
        self.CancerType_label = Label(self.master, text="Cancer Type:",bg="black",fg="white",font=('Arial',16))
        self.CancerType_Entry = Entry(self.master,width=20,font=('Arial',16))

    def showTrialPage(self):
        self.hideMainPage()
        self.treatmentLabel.place(x=400,y=20)
        self.tableOfTrials.place(x=50,y=300)
        self.treescrollx_.pack(side="bottom", fill="x")
        self.treescrolly_.pack(side="right", fill="y")
        self.fillTrialTable(THE_LIST_OF_CANCERS)
        self.NTC_num_label.place(x=60,y=200)
        self.NTC_num_Entry.place(x=200,y=200)
        self.Gender_label.place(x=60, y=250)
        self.Gender_Entry.place(x=200,y=250)
        self.CancerType_label.place(x=560, y=200)
        self.CancerType_Entry.place(x=760,y=200)
        self.Age_label.place(x=360,y=250)
        self.Age_Entry.place(x=460,y=250)
        self.Country_label.place(x=660,y=250)
        self.Country_Entry.place(x=810,y=250)
        self.filter_trails.place(x=850, y=120)
        self.goBack_button.place(x=0,y=0)

    def hideTrialPage(self):
        self.treatmentLabel.place_forget()
        self.tableOfTrials.place_forget()
        self.treescrollx_.place_forget()
        self.treescrolly_.place_forget()
    
        self.NTC_num_label.place_forget()
        self.NTC_num_Entry.place_forget()
        self.Gender_label.place_forget()
        self.Gender_Entry.place_forget()
        self.CancerType_label.place_forget()
        self.CancerType_Entry.place_forget()
        self.Age_label.place_forget()
        self.Age_Entry.place_forget()
        self.Country_label.place_forget()
        self.Country_Entry.place_forget()
        self.filter_trails.place_forget()
        self.goBack_button.place_forget()

    def fillTrialTable(self,input_):
        tv1 = self.tableOfTrials
        tv1.delete(*tv1.get_children())
        tv1["show"] = "headings"
        for column in tv1["columns"]:
            if column=="Gender" or column=="Country":
                tv1.column(column, width = 100) 
            elif column=="NTCNumber":
                tv1.column(column, width = 150) 
            else:
                tv1.column(column, width = 250) 
            tv1.heading(column, text=column)

        df_rows = input_
        for row in df_rows:
            tv1.insert("", "end", values=row)

    def createTrialsLabel(self):
        self.treatmentLabel = Label(self.master, text="Treatments", font=("Arial", 40),bg="black",fg="white")

    def createTrialsPage(self):
        self.createTrialsLabel()
        self.createTrialsTable()
        self.createTrialSort_Labels()

    def createTrialsTable(self):
        columns = ('NCTNumber', 'Gender','Age','Country', 'CancerType')
        self.tableOfTrials = ttk.Treeview(self.master,columns=columns,show='headings')
        s = ttk.Style()
        s.configure('Treeview', font=('Helvetica', 16),rowheight=35 , fieldbackground = "white")
        self.treescrolly_ = ttk.Scrollbar(self.master, orient="vertical", command=self.tableOfTrials.yview)
        self.treescrollx_ = ttk.Scrollbar(self.master, orient="horizontal", command=self.tableOfTrials.xview)
        self.tableOfTrials.configure(xscrollcommand=self.treescrollx_.set, yscrollcommand=self.treescrolly_.set)

    def createTreatmentPage(self):
        self.createTreatmentLabel()
        self.createTreeview()
        self.createTreatmentSortButton()

    def showTreatmentPage(self):
        self.hideMainPage()
        self.treatmentLabel.place(x=300,y=20)
        self.tableOfTreatments.place(x=100,y=100)
        self.treescrollx.pack(side="bottom", fill="x")
        self.treescrolly.pack(side="right", fill="y")
        self.fillTable()
        self.filter_btn.place(x=800,y=30)
        self.filterFDA_entry.place(x=700,y=30)
        self.filter_FDA_label.place(x=620,y=30)
        self.filter_TARGETS_entry.place(x=700,y=55)
        self.filter_TARGETS_label.place(x=600,y=55)
        self.goBack_button.place(x=0,y=0)

    def createMainPage(self):
        self.create_treatments_button()
        self.create_trials_button()
        self.create_cancer_image()
        self.create_goBackButton()

    def showMainPage(self):
        self.treatment_button.place(x=200,y=200)
        self.trials_button.place(x=500, y=200)
        self.cancerImage.place(x=350, y = 400)

    def hideMainPage(self):
        self.treatment_button.place_forget()
        self.trials_button.place_forget()
        self.cancerImage.place_forget()

    def mainloop(self):
        self.master.mainloop()

    def create_goBackButton(self):
        self.goBack_button = Button(self.master, text="BACK",command=self.goBack,width=10,height=3)

    def goBack(self):
        self.hideTreatmentPage()
        self.hideTrialPage()
        self.showMainPage()

gui = GUI()
gui.mainloop()