from tkinter import *
from customtkinter import *
import customtkinter as ctk
import timeit
import psutil

# CREATING OUR APPLICATION WINDOW
main = ctk.CTk()
main.title('Iskompass')
main.resizable(False,False)
main.iconbitmap('Assets/Iskompass.ico')
screenWidth = main.winfo_screenwidth()
screenHeight = main.winfo_screenheight()
appWidth = 450
appHeight = 800
x = (screenWidth/2)-(appWidth/2)
y = (screenHeight/2)-(appHeight/2)
main.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')



# TEXT ANIMATION FUNCTION 
def textAnimation():
    current_color = tapText.cget("fg")
    next_color = "white" if current_color == "#BAA1A1" else "#BAA1A1"
    tapText.config(fg=next_color)
    main.after(700, textAnimation)

# FORGETTING OF PAGES
def forgetPages():
    welcomePage.place_forget()
    homePage.place_forget()
    interfaithChapelPage.place_forget()
    lagoonPage.place_forget()
    mabiniPage.place_forget()
    visitorPage.place_forget()
    ovalPage.place_forget()
    gymPage.place_forget()
    poolPage.place_forget()
    categoryPage.place_forget()
    aboutPage.place_forget()
    eastWingClassroomPage.place_forget()
    westWingClassroomPage.place_forget()
    keyboardingLaboratoryPage.place_forget()
    computerLaboratoryPage.place_forget()
    stenographyLaboratoryPage.place_forget()
    languageLaboratoryPage.place_forget()
    scienceLaboratoryPage.place_forget()
    registrarOfficePage.place_forget()
    registrarOfficeListPage.place_forget()
    cashierOfficePage.place_forget()
    cashierOfficeListPage.place_forget()
    registrarRecordsPage.place_forget()
    admissionRegistrationPage.place_forget()
    scholarshipAssistancePage.place_forget()
    shsDepartmentPage.place_forget()
    medicalClinicServicePage.place_forget()
    dentalClinicServicePage.place_forget()
    directorOfficeMedicalPage.place_forget()
    accentureRoomPage.place_forget()
    claroRectoRoomPage.place_forget()
    audioVisualRoomPage.place_forget()
    overviewComfortRoomPage.place_forget()
    eastComfortRoomPage.place_forget()
    westComfortRoomPage.place_forget()
    southComfortRoomPage.place_forget()
    lagoonComfortRoomPage.place_forget()
    eastFacultiesPage.place_forget()
    mpcPage.place_forget()
    rotcPage.place_forget()
    hrdPage.place_forget()
    odPage.place_forget()
    fmoPage.place_forget()
    dscoPage.place_forget()
    ccPage.place_forget()
    dcsdPage.place_forget()
    postBaccPage.place_forget()
    nstpPage.place_forget()
    cssdPage.place_forget()
    westFacultiesPage.place_forget()
    driPage.place_forget()
    coePage.place_forget()
    coaPage.place_forget()
    cbaPage.place_forget()
    cosPage.place_forget()
    lagoonFoodStallPage.place_forget()
    lagoonSupplyPage.place_forget()
    discoverWestPage.place_forget()
    discoverEastPage.place_forget()
    discoverSouthPage.place_forget()
    eastEventHallPage.place_forget()
    eastLabPage.place_forget()
    eastMedOfficePage.place_forget()
    southEventHallPage.place_forget()
    southFacultiesPage.place_forget()
    southLabPage.place_forget()
    southTransOfficePage.place_forget()
    sNOCPage.place_forget()
    sOVPPage.place_forget()
    sConfRoomPage.place_forget()
    sOPPage.place_forget()
    sOUBPage.place_forget()
    sSPPOPage.place_forget()
    sPFOPage.place_forget()
    sOIAPage.place_forget()
    sHRMDPage.place_forget()
    sULOPage.place_forget()
    sGSOPage.place_forget()
    sPOPage.place_forget()
    sPMOBACPage.place_forget()
    sIIMSPage.place_forget()
    sLLSPage.place_forget()
    sISTRPage.place_forget()
    sGDOPage.place_forget()
    sSRPage.place_forget()
    sERMOPage.place_forget()
    sCCISOFRPage.place_forget()
    sDOMSPage.place_forget()
    sCOSFRPage.place_forget()
    sCAFPage.place_forget()
    sODPage.place_forget()
    sCPSPAPage.place_forget()
    sCOEDPage.place_forget()
    sCBAPage.place_forget()
    sCSSDPage.place_forget()
    sOCPSPage.place_forget()
    sIDSAPage.place_forget()
    westTransOfficePage.place_forget()
    
    
    for i in range (7):
        categoryFrames[0,i].configure(height=55, fg_color='#FFF3F3')
        categoryDropdownFrames[0,i].place(x=346, y=12)
        clickedcategoryDropdownFrames[0,i].place_forget()
        textImageContainer[0,0].configure(image=classroomTextImgPath, bg= '#FFF3F3')
        textImageContainer[0,1].configure(image=laboratoriesTextImgPath, bg= '#FFF3F3')
        textImageContainer[0,2].configure(image=facultiesTextImgPath, bg= '#FFF3F3')
        textImageContainer[0,3].configure(image=transactionTextImgPath, bg= '#FFF3F3')
        textImageContainer[0,4].configure(image=medicalOfficeTextImgPath, bg= '#FFF3F3')
        textImageContainer[0,5].configure(image=eventHallsTextImgPath, bg= '#FFF3F3')
        textImageContainer[0,6].configure(image=comfortRoomsTextImgPath, bg= '#FFF3F3')

# TIME AND SPACE COMPLEXITY FUNCTION   
def TimeComplexity(self):
    
    timer = timeit.timeit(lambda: self)
    print(f"____________________________________")
    print(f"Execution time: {timer:.6f} seconds")
    print(f"CPU utilization: {psutil.cpu_percent()}%") 
    print(f"Memory utilization: {psutil.virtual_memory().percent}%")    

# NAVIGATION FUNCTIONS    
def homesPage():
    forgetPages() 
    homePage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(homesPage)
  
def interfaithPage():
    forgetPages()  
    interfaithChapelPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(interfaithPage)

def lagoonsPage():
    forgetPages()  
    lagoonPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(lagoonsPage)
    
def mabinisPage():
    forgetPages()  
    mabiniPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(mabinisPage)
    
def visitorsPage():
    forgetPages()  
    visitorPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(visitorsPage)
    
def ovalsPage():
    forgetPages()  
    ovalPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(ovalsPage)
    
def gymsPage():
    forgetPages()  
    gymPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(gymsPage)
    
def poolsPage():
    forgetPages()  
    poolPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(poolsPage)    

    
def categoriesPage():
    forgetPages()  
    categoryPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(categoriesPage)

def optionReturnSearch(page,num):
    ReturnButton = returnSearchCategory(page,num)

def optionalReturnSpecific(page,num):
    ReturnButton = returnSearchSpecific(page,num)
    
def eastWingClassroomsPage(page,num):
    optionReturnSearch(page,num)
    forgetPages()
    eastWingClassroomPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(eastWingClassroomsPage)

def westWingClassroomsPage(page,num):
    optionReturnSearch(page,num)
    forgetPages()  
    westWingClassroomPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(westWingClassroomsPage)
    
def keyboardingLaboratoriesPage(page,num):
    optionReturnSearch(page,num)
    forgetPages()  
    keyboardingLaboratoryPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(keyboardingLaboratoriesPage)
    
def computerLaboratoriesPage(page,num):
    optionReturnSearch(page,num)
    forgetPages()  
    computerLaboratoryPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(computerLaboratoriesPage)
    
def stenographyLaboratoriesPage(page,num):
    optionReturnSearch(page,num)
    forgetPages()  
    stenographyLaboratoryPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(stenographyLaboratoriesPage)
    
def languageLaboratoriesPage(page,num):
    optionReturnSearch(page,num)
    forgetPages()  
    languageLaboratoryPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(languageLaboratoriesPage)
    
def scienceLaboratoriesPage(page,num):
    optionReturnSearch(page,num)
    forgetPages()  
    scienceLaboratoryPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(scienceLaboratoriesPage)
    
def registrarPage(page,num):
    optionReturnSearch(page,num)
    forgetPages()  
    registrarOfficePage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(registrarPage)
    
def registrarListPage(page,num):
    optionReturnSearch(page,num)
    forgetPages()  
    registrarOfficeListPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(registrarListPage)

def cashiersOfficePage(page,num):
    optionReturnSearch(page,num)
    forgetPages()  
    cashierOfficePage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(cashiersOfficePage)

def cashierListPage(page,num):
    optionReturnSearch(page,num)
    forgetPages()  
    cashierOfficeListPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(cashierListPage)

def registrarsRecordsPage(page,num):
    optionReturnSearch(page,num)
    forgetPages()  
    registrarRecordsPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(registrarsRecordsPage)

def admissionPage(page,num):
    optionReturnSearch(page,num)
    forgetPages()  
    admissionRegistrationPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(admissionPage)

def scholarshipPage(page,num):
    optionReturnSearch(page,num)
    forgetPages()  
    scholarshipAssistancePage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(scholarshipPage)

def shsDepartmentsPage(page,num):
    optionReturnSearch(page,num)
    forgetPages()  
    shsDepartmentPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(shsDepartmentsPage)
    
def medicalClinicServicesPage(page,num):
    optionReturnSearch(page,num)
    forgetPages()  
    medicalClinicServicePage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(medicalClinicServicesPage)

def dentalClinicServicesPage(page,num):
    optionReturnSearch(page,num)
    forgetPages()  
    dentalClinicServicePage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(dentalClinicServicesPage)

def directorOfficeMedicalsPage(page,num):
    optionReturnSearch(page,num)
    forgetPages()  
    directorOfficeMedicalPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(directorOfficeMedicalsPage)

def accentureRoomsPage(page,num):
    optionReturnSearch(page,num)
    forgetPages()  
    accentureRoomPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(accentureRoomsPage)

def claroRectoRoomsPage(page,num):
    optionReturnSearch(page,num)
    forgetPages()  
    claroRectoRoomPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(claroRectoRoomsPage)

def audioVisualRoomsPage(page,num):
    optionReturnSearch(page,num)
    forgetPages()  
    audioVisualRoomPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(audioVisualRoomsPage)

def overviewComfortRoomsPage(page,num):
    optionReturnSearch(page,num)
    forgetPages()  
    overviewComfortRoomPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(overviewComfortRoomsPage)
    
def eastComfortRoomsPage(page,num):
    optionReturnSearch(page,num)
    forgetPages()  
    eastComfortRoomPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(eastComfortRoomsPage)
    
def westComfortRoomsPage(page,num):
    optionReturnSearch(page,num)
    forgetPages()  
    westComfortRoomPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(westComfortRoomsPage)
    
def southComfortRoomsPage(page,num):
    optionReturnSearch(page,num)
    forgetPages()  
    southComfortRoomPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(southComfortRoomsPage)
    
def lagoonComfortRoomsPage(page,num):
    forgetPages()
    optionReturnSearch(page,num)  
    lagoonComfortRoomPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(lagoonComfortRoomsPage)


def lagoonFoodStallsPage():
    forgetPages() 
    lagoonFoodStallPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(lagoonFoodStallsPage)


def lagoonSuppliesPage():
    forgetPages() 
    lagoonSupplyPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(lagoonSuppliesPage)


def discoversEastPage():
    forgetPages() 
    discoverEastPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(discoversEastPage)
      
    

def discoversWestPage():
    forgetPages() 
    discoverWestPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(discoversWestPage)    
    

def discoversSouthPage():
    forgetPages() 
    discoverSouthPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(discoversSouthPage)    

def eastEventHallsPage(page,num):
    optionalReturnSpecific(page,num)
    forgetPages() 
    eastEventHallPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(eastEventHallsPage)

def eastLabsPage(page,num):
    optionalReturnSpecific(page,num)
    forgetPages()
    eastLabPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(eastLabsPage)    

def eastMedOfficesPage(page,num):
    optionalReturnSpecific(page,num)
    forgetPages()
    eastMedOfficePage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(eastMedOfficesPage)    

def southEventHallsPage(page,num):
    optionalReturnSpecific(page,num)
    forgetPages()
    southEventHallPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(southEventHallsPage)    

def southFacultiessPage(page,num):
    optionalReturnSpecific(page,num)
    forgetPages()
    southFacultiesPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(southFacultiessPage)    

def southLabsPage(page,num):
    optionalReturnSpecific(page,num)
    forgetPages()
    southLabPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(southLabsPage)    

def southTransOfficesPage(page,num):
    optionalReturnSpecific(page,num)
    forgetPages()
    southTransOfficePage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(southTransOfficesPage)    

def westTransOfficesPage(page,num):
    optionalReturnSpecific(page,num)
    forgetPages()
    westTransOfficePage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(westTransOfficesPage)    

# IF ELSE FOR 
def eastFacultiesPaging(number):
    forgetPages()
    if number == 0:
        eastFacultiesPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 1:
        mpcPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 2:
        rotcPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 3:
        hrdPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 4:
        odPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 5:
        fmoPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 6:
        dscoPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 7:
        ccPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 8:
        dcsdPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 9:
        postBaccPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 10:
        nstpPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 11:
        cssdPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(eastFacultiesPaging)    

def westFacultiesPaging(number):
    forgetPages()
    if number == 0:
        westFacultiesPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 1:
        driPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 2:
        shsDepartmentPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 3:
        coaPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 4:
        coePage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 5:
        cbaPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 6:
        cosPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(westFacultiesPaging)    

def southFacultiesPaging(number):
    forgetPages()
    if number == 0:
        southFacultiesPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 1:
        sNOCPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 2:
        sOVPPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 3:
        sConfRoomPage.place(x=0, y=0, relwidth=1, relheight=1) 
    elif number == 4:
        sOPPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 5:
        sOUBPage.place(x=0, y=0, relwidth=1, relheight=1) 
    elif number == 6:
        sSPPOPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 7:
        sPFOPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 8:
        sOIAPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 9:
        sHRMDPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 10:
        sULOPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 11:
        sGSOPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 12:
        sPOPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 13:
        sPMOBACPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 14:
        sIIMSPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 15:
        sLLSPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 16:
        sISTRPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 17:
        sGDOPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 18:
        sSRPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 19:
        sERMOPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 20:
        sCCISOFRPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 21:
        sDOMSPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 22:
        sCOSFRPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 23:
        sCAFPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 24:
        sODPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 25:
        sCPSPAPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 26:
        sCOEDPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 27:
        sCBAPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 28:
        sCSSDPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 29:
        sOCPSPage.place(x=0, y=0, relwidth=1, relheight=1)
    elif number == 30:
        sIDSAPage.place(x=0, y=0, relwidth=1, relheight=1)
    TimeComplexity(southFacultiesPaging)    

# ICON MENU FUNCTIONS
def iconOpenMenu1():
    homepageSearchBar = menuToggle(homePage)
def iconOpenMenu2():
    interfaithSearchBar = menuToggle(interfaithChapelPage)          
def iconOpenMenu3():
    lagoonSearchBar = menuToggle(lagoonPage)

# COLLAPSING CATEGORIES FUNCTIONS
def clickedCategory(row,col):
    for i in range (7):
        categoryFrames[0,i].configure(height=55, fg_color='#FFF3F3')
        categoryDropdownFrames[0,i].place(x=346, y=12)
        clickedcategoryDropdownFrames[0,i].place_forget()
        textImageContainer[0,0].configure(image=classroomTextImgPath, bg= '#FFF3F3')
        textImageContainer[0,1].configure(image=laboratoriesTextImgPath, bg= '#FFF3F3')
        textImageContainer[0,2].configure(image=facultiesTextImgPath, bg= '#FFF3F3')
        textImageContainer[0,3].configure(image=transactionTextImgPath, bg= '#FFF3F3')
        textImageContainer[0,4].configure(image=medicalOfficeTextImgPath, bg= '#FFF3F3')
        textImageContainer[0,5].configure(image=eventHallsTextImgPath, bg= '#FFF3F3')
        textImageContainer[0,6].configure(image=comfortRoomsTextImgPath, bg= '#FFF3F3')
          
    categoryFrames[row,col].configure(height=198, fg_color='#FFFFF0')
    categoryDropdownFrames[row,col].place_forget()
    clickedcategoryDropdownFrames[row,col].place(x=346, y=12)
    
    if row == 0 and col == 0:
        textImageContainer[row,col].configure(image=clickedclassroomTextImgPath, bg= '#FFFFF0')
    elif row == 0 and col == 1:
        textImageContainer[row,col].configure(image=clickedLaboratoriesTextImgPath, bg= '#FFFFF0')
    elif row == 0 and col == 2:
        textImageContainer[row,col].configure(image=clickedFacultiesTextImgPath, bg= '#FFFFF0')
    elif row == 0 and col == 3:
        textImageContainer[row,col].configure(image=clickedTransactionTextImgPath, bg= '#FFFFF0')
    elif row == 0 and col == 4:
        textImageContainer[row,col].configure(image=clickedMedicalOfficeTextImgPath, bg= '#FFFFF0')
    elif row == 0 and col == 5:
        textImageContainer[row,col].configure(image=clickedEventHallsTextImgPath, bg= '#FFFFF0')
    elif row == 0 and col == 6:
        textImageContainer[row,col].configure(image=clickedComfortRoomsTextImgPath, bg= '#FFFFF0')
    
    TimeComplexity(clickedCategory)    
      
def closedClickedCategory(row,col):
    categoryFrames[row,col].configure(height=55, fg_color='#FFF3F3')
    clickedcategoryDropdownFrames[row,col].place_forget()
    categoryDropdownFrames[row,col].place(x=346, y=12)

    if row == 0 and col == 0:
        textImageContainer[row,col].configure(image=classroomTextImgPath, bg= '#FFF3F3')
    elif row == 0 and col == 1:
        textImageContainer[row,col].configure(image=laboratoriesTextImgPath, bg= '#FFF3F3')
    elif row == 0 and col == 2:
        textImageContainer[row,col].configure(image=facultiesTextImgPath, bg= '#FFF3F3')
    elif row == 0 and col == 3:
        textImageContainer[row,col].configure(image=transactionTextImgPath, bg= '#FFF3F3')
    elif row == 0 and col == 4:
        textImageContainer[row,col].configure(image=medicalOfficeTextImgPath, bg= '#FFF3F3')
    elif row == 0 and col == 5:
        textImageContainer[row,col].configure(image=eventHallsTextImgPath, bg= '#FFF3F3')
    elif row == 0 and col == 6:
        textImageContainer[row,col].configure(image=comfortRoomsTextImgPath, bg= '#FFF3F3')
    
    TimeComplexity(closedClickedCategory)    
  
def clickedeastWingClassroom(row,col):
    eastWingClassroomFrame[row,col].configure(height=329, fg_color='#FFF3F3')
    eastWingDropdownButton[row,col].place_forget()
    eastWingClickedDropdownButton[row,col].place(x=351, y=13)

    if row == 0 and col == 0:
        eastWingContainerLabel[row,col].configure(image=eastWingClassroomBigPaths[0])
    elif row == 0 and col == 1:
        eastWingContainerLabel[row,col].configure(image=eastWingClassroomBigPaths[1])
    elif row == 0 and col == 2:
        eastWingContainerLabel[row,col].configure(image=eastWingClassroomBigPaths[2])
    elif row == 0 and col == 3:
        eastWingContainerLabel[row,col].configure(image=eastWingClassroomBigPaths[3])
    
    TimeComplexity(clickedeastWingClassroom)    
      
def closedClickedeastWingClassroom(row,col):
    eastWingClassroomFrame[row,col].configure(height=55, fg_color='#FFF3F3')
    eastWingClickedDropdownButton[row,col].place_forget()
    eastWingDropdownButton[row,col].place(x=351, y=13)

    if row == 0 and col == 0:
        eastWingContainerLabel[row,col].configure(image=eastWingClassroomSmallPaths[0])
    elif row == 0 and col == 1:
        eastWingContainerLabel[row,col].configure(image=eastWingClassroomSmallPaths[1])
    elif row == 0 and col == 2:
        eastWingContainerLabel[row,col].configure(image=eastWingClassroomSmallPaths[2])
    elif row == 0 and col == 3:
        eastWingContainerLabel[row,col].configure(image=eastWingClassroomSmallPaths[3])
    
    TimeComplexity(closedClickedeastWingClassroom)    
        
def clickedWestWingClassroom(row,col): 
    westWingClassroomFrame[row,col].configure(height=370, fg_color='#FFF3F3')
    westWingDropdownButton[row,col].place_forget()
    westWingClickedDropdownButton[row,col].place(x=351, y=13)

    if row == 0 and col == 0:
        westWingContainerLabel[row,col].configure(image=westWingClassroomBigPaths[0])
    elif row == 0 and col == 1:
        westWingContainerLabel[row,col].configure(image=westWingClassroomBigPaths[1])
    elif row == 0 and col == 2:
        westWingContainerLabel[row,col].configure(image=westWingClassroomBigPaths[2])
    elif row == 0 and col == 3:
        westWingContainerLabel[row,col].configure(image=westWingClassroomBigPaths[3])
    elif row == 0 and col == 4:
        westWingContainerLabel[row,col].configure(image=westWingClassroomBigPaths[4])
    
    TimeComplexity(clickedWestWingClassroom)
           
def closedClickedWestWingClassroom(row,col):
    westWingClassroomFrame[row,col].configure(height=55, fg_color='#FFF3F3')
    westWingClickedDropdownButton[row,col].place_forget()
    westWingDropdownButton[row,col].place(x=351, y=13)

    if row == 0 and col == 0:
        westWingContainerLabel[row,col].configure(image=westWingClassroomSmallPaths[0])
    elif row == 0 and col == 1:
        westWingContainerLabel[row,col].configure(image=westWingClassroomSmallPaths[1])
    elif row == 0 and col == 2:
        westWingContainerLabel[row,col].configure(image=westWingClassroomSmallPaths[2])
    elif row == 0 and col == 3:
        westWingContainerLabel[row,col].configure(image=westWingClassroomSmallPaths[3])
    elif row == 0 and col == 4:
        westWingContainerLabel[row,col].configure(image=westWingClassroomSmallPaths[4])

    TimeComplexity(closedClickedWestWingClassroom)

# SEARCHING FUNCTION
def searching(place,search):
    
    commandOptions = [
        discoversEastPage, discoversWestPage, discoversSouthPage,
        lambda: eastFacultiesPaging(0), lambda: westFacultiesPaging(0),
        lambda: southFacultiesPaging(0), lambda: eastWingClassroomsPage(eastWingClassroomPage,0),
        lambda: westWingClassroomsPage(westWingClassroomPage,0), 
        lambda: dentalClinicServicesPage(dentalClinicServicePage,0),
        lambda: medicalClinicServicesPage(medicalClinicServicePage,0),
        lambda: directorOfficeMedicalsPage(directorOfficeMedicalPage,0),
        lambda: claroRectoRoomsPage(claroRectoRoomPage,0),
        lambda: accentureRoomsPage(accentureRoomPage,0),
        lambda: audioVisualRoomsPage(audioVisualRoomPage,0),
        lambda: overviewComfortRoomsPage(overviewComfortRoomPage,0),
        lambda: keyboardingLaboratoriesPage(keyboardingLaboratoryPage,0),
        lambda: computerLaboratoriesPage(computerLaboratoryPage,0),
        lambda: stenographyLaboratoriesPage(stenographyLaboratoryPage,0),
        lambda: languageLaboratoriesPage(languageLaboratoryPage,0),
        lambda: scienceLaboratoriesPage(scienceLaboratoryPage,0),
        lambda: registrarPage(registrarOfficePage,0),
        lambda: registrarListPage(registrarOfficeListPage,0),
        lambda: cashiersOfficePage(cashierOfficePage,0),
        lambda: cashierListPage(cashierOfficeListPage,0),
        lambda: registrarsRecordsPage(registrarRecordsPage,0),
        lambda: admissionPage(admissionRegistrationPage,0),
        lambda: scholarshipPage(scholarshipAssistancePage,0),
        lambda: shsDepartmentsPage(shsDepartmentPage,0),
        interfaithPage, lagoonsPage, mabinisPage, visitorsPage,
        ovalsPage, gymsPage, poolsPage
    ]
    
    pageOptions = [
        "EAST WING", "WEST WING", "SOUTH WING",
        "EAST FACULTIES", "WEST FACULTIES", "SOUTH FACULTIES",
        "EAST CLASSROOM", "WEST CLASSROOM", "DENTAL CLINIC",
        "MEDICAL CLINIC", "MEDICAL OFFICE", "CLARO RECTO HALL",
        "ACCENTURE ROOM", "AUDIO VISUAL ROOM", "COMFORT ROOM",
        "KEYBOARDING LAB", "COMPUTER LAB", "STENOGRAPHY LAB",
        "LANGUAGE LAB", "SCIENCE LAB", "REGISTRAR",
        "REGISTRAR LIST", "CASHIER", "CASHIER LIST", "REGISTRAR RECORDS",
        "ADMISSION", "SCHOLARSHIP", "SHS DEPARTMENT",
        "CHAPEL", "LAGOON", "MABINI", "VISITOR",
        "OVAL", "GYM", "POOL"
    ]

    pageOptions2 = [
        "EAST", "WEST", "SOUTH",
        "EAST FAC", "WEST FAC", "SOUTH FAC",
        "EAST ROOMS", "WEST ROOMS", "DENTAL",
        "MEDICAL", "MED OFFICE", "CLARO M",
        "ACC ROOM", "AUDIO ROOM", "CR",
        "KEYBOARD", "COMP", "STENO",
        "LANGUAGE", "SCIENCE", "REGIS",
        "REGIS LIST", "CASHIER", "CASHIER LIST", "REGIS RECORDS",
        "ADMISSION", "SCHOLARSHIP", "SHS DEP",
        "CHAPEL", "CANTEEN", "MABINI SHRINE", "VISITOR LOUNGE",
        "BLEACHERS", "GYMNASIUM", "SWIMMING POOL"
    ]
    
    if not hasattr(searching, "container"):
        searching.container = {}

    
    
    for key in list(searching.container.keys()):
        searching.container[key].pack_forget()
        searching.container[key].destroy()
    searching.container.clear()

    
    for i in range(len(pageOptions)):
        button = ctk.CTkButton(
            place,
            width=230, height=31,
            corner_radius=20,
            fg_color='#550000', bg_color='#FFFFF0',
            text=search,
            command=lambda cmd=commandOptions[i]: (cmd(), place.place_forget())
        )
        searching.container[i] = button
    
    
    for i, option in enumerate(pageOptions):
        if search == option:
            searching.container[i].pack(pady=7)
            break


    for i, option in enumerate(pageOptions2):
        if search == option:
            searching.container[i].pack(pady=7)
            break
            

    
# UTILIZING CLASSES TO CREATE REUSABLE TEMPLATES FOR VARIABLES    
class menuToggle:
    def __init__(self, master):
           
        def iconCloseMenu():
                menuToggleFrame.place_forget()
                
            
        def aboutsPage():
                iconCloseMenu()
                homePage.place_forget()
                interfaithChapelPage.place_forget()
                lagoonPage.place_forget()   
                aboutPage.place(x=0, y=0, relwidth=1, relheight=1)
                
        def exitPage():
                iconCloseMenu()
                homePage.place_forget()
                interfaithChapelPage.place_forget()
                lagoonPage.place_forget()   
                welcomePage.place(x=0, y=0, relwidth=1, relheight=1)
                 
        menuToggleFrame = Frame(master, width=253, height=800, bg = '#5F0F0F')
        menuToggleFrame.place(x=-2, y=-1)

        iconUntoggleFrame = Frame(menuToggleFrame, width=203.23, height=61)
        iconUntoggleFrame.place(x=24.89, y=15)
           
        aboutAppButtonFrame = Frame(menuToggleFrame, width=193.9, height=33)
        aboutAppButtonFrame.place(x=29.03, y=140)
          
        exitButtonFrame = Frame(menuToggleFrame, width=193.9, height=33)
        exitButtonFrame.place(x=29.03, y=197)
            
        iconUntoggleImage = Button(iconUntoggleFrame, image=iconUntoggleImgPath, bd=0 ,command=iconCloseMenu , bg = '#5F0F0F', activebackground= "#5F0F0F")
        iconUntoggleImage.place(x=0, y=0, relheight=1, relwidth=1)
            
        aboutAppButtonImage = Button(aboutAppButtonFrame, image=aboutAppButtonImgPath, bd=0 ,command=aboutsPage , bg = '#5F0F0F', activebackground= "#5F0F0F")
        aboutAppButtonImage.place(x=0, y=0, relheight=1, relwidth=1)
            
        exitButtonImage = Button(exitButtonFrame, image=exitButtonImgPath, bd=0 ,command=exitPage , bg = '#5F0F0F', activebackground= "#5F0F0F")
        exitButtonImage.place(x=0, y=0, relheight=1, relwidth=1)  

class searchBars:
    def __init__(self,master):
        
        def removeSearchBar():
            search = searchEntry.get()
            search = search.upper()
            if search == '':
                searchScrollBarFrame.place_forget()
            main.after(2,removeSearchBar)

        def searchBar(event):
            search = searchEntry.get()
            search = search.upper()
            if search == '':
                removeSearchBar()
            elif search != '': 
                searchScrollBarFrame.place(x=125,y=63)
                searchScrollBarFrame.lift()
                searching(searchScrollBarFrame,search)
                
                
                
        ReturnFrame= Frame(master, width=37, height=37)
        ReturnFrame.place(x=37, y=32)
        ReturnButton = Button(ReturnFrame, image=categoryReturnButtonImgPath, bd=0 ,command=homesPage , bg = '#550000', activebackground= "#550000")
        ReturnButton.place(x=0, y=0, relheight=1, relwidth=1) 
        
        searchEntryFrame = Frame(master, width=320, height=39)
        searchEntryFrame.place(x=100, y=32)
        
       
        searchScrollBarFrame = CTkScrollableFrame(master , width=257, height=40, fg_color='#FFFFF0', bg_color='#FFFFF0')
        
        searchEntry = ctk.CTkEntry(searchEntryFrame, width=320, corner_radius=20.5,border_width=0, bg_color="#550000", fg_color="#FFFFF0")
        searchEntry.configure(placeholder_text="How can we help you?", fg_color="white", border_color="black")
        searchEntry.configure(placeholder_text_color="black")
        searchEntry.bind('<Return>', searchBar)
        searchEntry.place(x=0, y=0, relheight=1, relwidth=1) 

        searchIconFrame = Frame(master, width=20, height=19, bg = '#FFFFF0')
        searchIconFrame.place(x=391, y=42)

        searchIconImage = Label(searchIconFrame, image=searchIconImgPath)
        searchIconImage.place(x=0, y=0, relheight=1, relwidth=1)
        removeSearchBar()

class searchBarAndReturnButton:
    def __init__(self,master):
        ReturnFrame= Frame(master, width=37, height=37)
        ReturnFrame.place(x=30, y=38)
        
        
        
        ReturnButton = Button(ReturnFrame, image=categoryReturnButtonImgPath, bd=0 ,command=homesPage , bg = '#550000', activebackground= "#550000")
        ReturnButton.place(x=0, y=0, relheight=1, relwidth=1)  

        searchEntryFrame = ctk.CTkEntry(master, width=338, height=41, corner_radius=20.5, border_width=0,  bg_color="#550000", fg_color="#FFFFF0")
        searchEntryFrame.place(x=82, y=36)

        def removeSearchBar():
            search = searchEntry.get()
            search = search.upper()
            if search == '':
                searchScrollBarFrame.place_forget()
            main.after(2,removeSearchBar)

        def searchBar(event):
            search = searchEntry.get()
            search = search.upper()
            if search == '':
                removeSearchBar()
            elif search != '': 
                searchScrollBarFrame.place(x=125,y=63)
                searchScrollBarFrame.lift()
                searching(searchScrollBarFrame,search)
        
        
        searchScrollBarFrame = CTkScrollableFrame(master , width=257, height=40, fg_color='#FFFFF0', bg_color='#FFFFF0')
        
        searchEntry = ctk.CTkEntry(searchEntryFrame, width=270, border_width=0, bg_color="#FFFFF0", fg_color="#FFFFF0", placeholder_text='Search destination...', font=('arial',14))
        searchEntry.configure(placeholder_text_color="black")
        searchEntry.bind('<Return>', searchBar)
        searchEntry.place(x=54, y=6) 

        searchIconFrame = Frame(master, width=37, height=30, bg = '#FFFFF0')
        searchIconFrame.place(x=96, y=40)

        searchIconImage = Label(searchIconFrame, image=categorySearchIconImgPath)
        searchIconImage.place(x=0, y=0, relheight=1, relwidth=1)
        removeSearchBar()

class returnSearchCategory:
    def __init__(self,master,number):
        iconToggleFrame = Frame(master, width=64, height=61)
        iconToggleFrame.place(x=28, y=20.07)
        
        optionalPage = [categoriesPage,discoversEastPage,discoversWestPage,discoversSouthPage,lambda:eastLabsPage(eastLabPage,1),lambda:eastFacultiesPaging(0),lambda:westFacultiesPaging(0),lambda:southFacultiesPaging(0),
                        lambda: eastMedOfficesPage(eastMedOfficePage,2),lambda:registrarPage(registrarOfficePage,3),lambda:cashiersOfficePage(cashierOfficePage,3),lambda: shsDepartmentsPage(shsDepartmentPage,2)]
        paging = optionalPage[number]
        
        iconToggleButton = Button(iconToggleFrame, image=returnCategoryPageButtonImgPath, bd=0,command=paging , bg = '#FFFFF0', activebackground= "#FFFFF0")
        iconToggleButton.pack()
        
        searchEntryFrame = ctk.CTkEntry(master, width=338, height=41, corner_radius=20.5, border_width=0,  bg_color="#FFFFF0", fg_color="#550000")
        searchEntryFrame.place(x=82, y=20.07)

        def removeSearchBar():
            search = searchEntry.get()
            search = search.upper()
            if search == '':
                searchScrollBarFrame.place_forget()
            main.after(2,removeSearchBar)

        def searchBar(event):
            search = searchEntry.get()
            search = search.upper()
            if search == '':
                removeSearchBar()
            elif search != '': 
                searchScrollBarFrame.place(x=125,y=63)
                searchScrollBarFrame.lift()
                searching(searchScrollBarFrame,search)
            
        
        
        searchScrollBarFrame = CTkScrollableFrame(master , width=257, height=40, fg_color='#FFFFF0', bg_color='#FFFFF0')
        
        searchEntry = ctk.CTkEntry(searchEntryFrame, width=270, border_width=0, bg_color="#550000", fg_color="#550000", placeholder_text='Search destination...', font=('arial',14) , text_color="#942929", placeholder_text_color='#942929')
        searchEntry.configure(placeholder_text_color="#942929")
        searchEntry.bind('<Return>', searchBar)
        searchEntry.place(x=54, y=6) 

        searchIconFrame = Frame(master, width=37, height=30, bg = '#550000')
        searchIconFrame.place(x=96, y=23)

        searchIconImage = Label(searchIconFrame, image=specificCategorySearchIconImgPath, bg = '#550000')
        searchIconImage.place(x=0, y=0, relheight=1, relwidth=1)
        removeSearchBar()
         
class returnSearchSpecific:
    def __init__(self,master,number):
        iconToggleFrame = Frame(master, width=64, height=61)
        iconToggleFrame.place(x=28, y=20.07)
        
        optionalPage = [discoversEastPage,discoversWestPage,discoversSouthPage]
        paging = optionalPage[number]
        
        iconToggleButton = Button(iconToggleFrame, image=facultiesReturnImgPath, bd=0,command=paging , bg = '#FFEDED', activebackground= "#FFEDED")
        iconToggleButton.pack()
        
        searchEntryFrame = ctk.CTkEntry(master, width=338, height=41, corner_radius=20.5, border_width=0,  bg_color="#FFEDED", fg_color="#550000")
        searchEntryFrame.place(x=82, y=20.07)
        
        def removeSearchBar():
            search = searchEntry.get()
            search = search.upper()
            if search == '':
                searchScrollBarFrame.place_forget()
            main.after(2,removeSearchBar)

        def searchBar(event):
            search = searchEntry.get()
            search = search.upper()
            if search == '':
                removeSearchBar()
            elif search != '': 
                searchScrollBarFrame.place(x=125,y=63)
                searchScrollBarFrame.lift()
                searching(searchScrollBarFrame,search)
        
        searchScrollBarFrame = CTkScrollableFrame(master , width=257, height=40, fg_color='#FFFFF0', bg_color='#FFFFF0')
        
        searchEntry = ctk.CTkEntry(searchEntryFrame, width=270, border_width=0, bg_color="#550000", fg_color="#550000", placeholder_text='Search destination...', font=('arial',14) , text_color="#942929", placeholder_text_color='#942929')
        searchEntry.configure(placeholder_text_color="#942929")
        searchEntry.bind('<Return>', searchBar)
        searchEntry.place(x=54, y=6) 
        
        searchIconFrame = Frame(master, width=37, height=30, bg = '#550000')
        searchIconFrame.place(x=96, y=23)

        searchIconImage = Label(searchIconFrame, image=specificCategorySearchIconImgPath, bg = '#550000')
        searchIconImage.place(x=0, y=0, relheight=1, relwidth=1)
        global searchVar
        searchVar = searchEntry
        removeSearchBar()

# CREATING PAGE FRAMES IN OUR APPLICATION
welcomePage = ctk.CTkFrame(main, width=450, height=800)
homePage = ctk.CTkFrame(main, width=450, height=800)
aboutPage = ctk.CTkFrame(main, width=450, height=800)
interfaithChapelPage = ctk.CTkFrame(main, width=450, height=800)
lagoonPage = ctk.CTkFrame(main, width=450, height=800)


#OUTDOOR PAGES
mabiniPage = ctk.CTkFrame(main, width=450, height=800)
visitorPage = ctk.CTkFrame(main, width=450, height=800)
ovalPage = ctk.CTkFrame(main, width=450, height=800)
gymPage = ctk.CTkFrame(main, width=450, height=800)
poolPage = ctk.CTkFrame(main, width=450, height=800)

# CATEGORY PAGES
categoryPage = ctk.CTkFrame(main, width=450, height=800)

# CLASSROOM PAGES
eastWingClassroomPage = ctk.CTkFrame(main, width=450, height=800)
westWingClassroomPage = ctk.CTkFrame(main, width=450, height=800)

# SPECIFI CLASSROOM PAGES
eastWingClassroomPageSpecific = ctk.CTkFrame(main, width=450, height=800)
westWingClassroomPageSpecific = ctk.CTkFrame(main, width=450, height=800)

# LABORATORIES PAGES
keyboardingLaboratoryPage = ctk.CTkFrame(main, width=450, height=800)
computerLaboratoryPage = ctk.CTkFrame(main, width=450, height=800)
stenographyLaboratoryPage = ctk.CTkFrame(main, width=450, height=800)
languageLaboratoryPage = ctk.CTkFrame(main, width=450, height=800)
scienceLaboratoryPage = ctk.CTkFrame(main, width=450, height=800)

# SPECIFIC LABORATORIES PAGES
keyboardingLaboratoryPageSpecific = ctk.CTkFrame(main, width=450, height=800)
computerLaboratoryPageSpecific = ctk.CTkFrame(main, width=450, height=800)
stenographyLaboratoryPageSpecific = ctk.CTkFrame(main, width=450, height=800)
languageLaboratoryPageSpecific = ctk.CTkFrame(main, width=450, height=800)
scienceLaboratoryPageSpecific = ctk.CTkFrame(main, width=450, height=800)

# TRANSACTION PAGES
registrarOfficePage = ctk.CTkFrame(main, width=450, height=800)
registrarOfficeListPage = ctk.CTkFrame(main, width=450, height=800)
cashierOfficePage = ctk.CTkFrame(main, width=450, height=800)
cashierOfficeListPage = ctk.CTkFrame(main, width=450, height=800)
registrarRecordsPage = ctk.CTkFrame(main, width=450, height=800)
admissionRegistrationPage = ctk.CTkFrame(main, width=450, height=800)
scholarshipAssistancePage = ctk.CTkFrame(main, width=450, height=800)
shsDepartmentPage = ctk.CTkFrame(main, width=450, height=800)

# SPECIFIC TRANSACTION PAGES
registrarOfficePageSpecific = ctk.CTkFrame(main, width=450, height=800)
registrarOfficeListPageSpecific = ctk.CTkFrame(main, width=450, height=800)
cashierOfficePageSpecific = ctk.CTkFrame(main, width=450, height=800)
cashierOfficeListPageSpecific = ctk.CTkFrame(main, width=450, height=800)
registrarRecordsPageSpecific = ctk.CTkFrame(main, width=450, height=800)
admissionRegistrationPageSpecific = ctk.CTkFrame(main, width=450, height=800)
scholarshipAssistancePageSpecific = ctk.CTkFrame(main, width=450, height=800)
shsDepartmentPageSpecific = ctk.CTkFrame(main, width=450, height=800)

# EVENT HALL PAGES
medicalClinicServicePage = ctk.CTkFrame(main, width=450, height=800)
dentalClinicServicePage = ctk.CTkFrame(main, width=450, height=800)
directorOfficeMedicalPage = ctk.CTkFrame(main, width=450, height=800)

medicalClinicServicePageSpecific = ctk.CTkFrame(main, width=450, height=800)
dentalClinicServicePageSpecific = ctk.CTkFrame(main, width=450, height=800)
directorOfficeMedicalPageSpecific = ctk.CTkFrame(main, width=450, height=800)

# EVENT HALL PAGES
accentureRoomPage = ctk.CTkFrame(main, width=450, height=800)
claroRectoRoomPage = ctk.CTkFrame(main, width=450, height=800)
audioVisualRoomPage = ctk.CTkFrame(main, width=450, height=800)

accentureRoomPageSpecific = ctk.CTkFrame(main, width=450, height=800)
claroRectoRoomPageSpecific = ctk.CTkFrame(main, width=450, height=800)
audioVisualRoomPageSpecific = ctk.CTkFrame(main, width=450, height=800)

# COMFORT ROOM PAGES
overviewComfortRoomPage = ctk.CTkFrame(main, width=450, height=800)
eastComfortRoomPage = ctk.CTkFrame(main, width=450, height=800)
westComfortRoomPage = ctk.CTkFrame(main, width=450, height=800)
southComfortRoomPage = ctk.CTkFrame(main, width=450, height=800)
lagoonComfortRoomPage = ctk.CTkFrame(main, width=450, height=800)

# DISCOVER PAGES
discoverSouthPage = ctk.CTkFrame(main, width=450, height=800)
discoverEastPage = ctk.CTkFrame(main, width=450, height=800)
discoverWestPage = ctk.CTkFrame(main, width=450, height=800)

# EAST FACULTIES PAGES
eastFacultiesPage = ctk.CTkFrame(main, width=450, height=800)
mpcPage = ctk.CTkFrame(main, width=450, height=800)
rotcPage = ctk.CTkFrame(main, width=450, height=800)
hrdPage = ctk.CTkFrame(main, width=450, height=800)
odPage = ctk.CTkFrame(main, width=450, height=800)
fmoPage = ctk.CTkFrame(main, width=450, height=800)
dscoPage = ctk.CTkFrame(main, width=450, height=800)
ccPage = ctk.CTkFrame(main, width=450, height=800)
dcsdPage = ctk.CTkFrame(main, width=450, height=800)
postBaccPage = ctk.CTkFrame(main, width=450, height=800)
nstpPage = ctk.CTkFrame(main, width=450, height=800)
cssdPage = ctk.CTkFrame(main, width=450, height=800)

# WEST FACULTIES PAGES
westFacultiesPage = ctk.CTkFrame(main, width=450, height=800)
driPage = ctk.CTkFrame(main, width=450, height=800)
coePage = ctk.CTkFrame(main, width=450, height=800)
coaPage = ctk.CTkFrame(main, width=450, height=800)
cbaPage = ctk.CTkFrame(main, width=450, height=800)
cosPage = ctk.CTkFrame(main, width=450, height=800)

# WEST FACULTIES PAGES
westTransOfficePage = ctk.CTkFrame(main, width=450, height=800)

# LAGOON FACULTIES PAGES
lagoonFoodStallPage = ctk.CTkFrame(main, width=450, height=800)
lagoonSupplyPage = ctk.CTkFrame(main, width=450, height=800)

# EAST FACULTIES PAGES
eastEventHallPage = ctk.CTkFrame(main, width=450, height=800)
eastLabPage = ctk.CTkFrame(main, width=450, height=800)
eastMedOfficePage = ctk.CTkFrame(main, width=450, height=800)

# SOUTH FACULTIES PAGES
southEventHallPage = ctk.CTkFrame(main, width=450, height=800)
southFacultiesPage = ctk.CTkFrame(main, width=450, height=800)
southLabPage = ctk.CTkFrame(main, width=450, height=800)
southTransOfficePage = ctk.CTkFrame(main, width=450, height=800)
sCAFPage = ctk.CTkFrame(main, width=450, height=800)
sCBAPage = ctk.CTkFrame(main, width=450, height=800)
sCCISOFRPage = ctk.CTkFrame(main, width=450, height=800)
sConfRoomPage = ctk.CTkFrame(main, width=450, height=800)
sCOEDPage = ctk.CTkFrame(main, width=450, height=800)
sCOSFRPage = ctk.CTkFrame(main, width=450, height=800)
sCPSPAPage = ctk.CTkFrame(main, width=450, height=800)
sCSSDPage = ctk.CTkFrame(main, width=450, height=800)
sDOMSPage = ctk.CTkFrame(main, width=450, height=800)
sERMOPage = ctk.CTkFrame(main, width=450, height=800)
sGDOPage = ctk.CTkFrame(main, width=450, height=800)
sGSOPage = ctk.CTkFrame(main, width=450, height=800)
sHRMDPage = ctk.CTkFrame(main, width=450, height=800)
sIDSAPage = ctk.CTkFrame(main, width=450, height=800)
sIIMSPage = ctk.CTkFrame(main, width=450, height=800)
sISTRPage = ctk.CTkFrame(main, width=450, height=800)
sLLSPage = ctk.CTkFrame(main, width=450, height=800)
sNOCPage = ctk.CTkFrame(main, width=450, height=800)
sOCPSPage = ctk.CTkFrame(main, width=450, height=800)
sODPage = ctk.CTkFrame(main, width=450, height=800)
sOIAPage = ctk.CTkFrame(main, width=450, height=800)
sOPPage = ctk.CTkFrame(main, width=450, height=800)
sOUBPage = ctk.CTkFrame(main, width=450, height=800)
sOVPPage = ctk.CTkFrame(main, width=450, height=800)
sPFOPage = ctk.CTkFrame(main, width=450, height=800)
sPMOBACPage = ctk.CTkFrame(main, width=450, height=800)
sPOPage = ctk.CTkFrame(main, width=450, height=800)
sSPPOPage = ctk.CTkFrame(main, width=450, height=800)
sSRPage = ctk.CTkFrame(main, width=450, height=800)
sULOPage = ctk.CTkFrame(main, width=450, height=800)

welcomePage.place(relwidth=1, relheight=1) 


# IMAGE ADDRESSES 
welcomeImgPath = PhotoImage(file="Assets/welcomePage/welcomePage.png")
homeImgPath = PhotoImage(file="Assets/homePage/mainPage.png")
iconToggleImageImgPath = PhotoImage(file="Assets/homePage/iconToggleImage.png")
aboutImgPath = PhotoImage(file="Assets/aboutPage/aboutAppImgPath.png")
interfaithChapelImgPath = PhotoImage(file="Assets/InterfaithChapelPage/interfaithChapelImage.png")
lagoonPageImgPath = PhotoImage(file="Assets/lagoonPage/lagoonPageImage.png")
mabiniShrineImgPath = PhotoImage(file="Assets/outdoorAreas/mabiniShrine.png")
basketBallCourtImgPath = PhotoImage(file="Assets/outdoorAreas/basketballCourt.png")
gymImgPath = PhotoImage(file="Assets/outdoorAreas/gymnasium.png")
swimmingPoolImgPath = PhotoImage(file="Assets/outdoorAreas/swimmingPool.png")
visitorsLoungeImgPath =PhotoImage(file="Assets/outdoorAreas/visitorsLounge.png")

viewCategoryPageImgPath = PhotoImage(file="Assets/categoriesPage/viewCategoryPageImage.png")
eastWingClassroomPageImgPath = PhotoImage(file="Assets/categoriesPage/eastWingPage/eastWingClassroomPageImage.png")
westWingClassroomPageImgPath = PhotoImage(file="Assets/categoriesPage/westWingPage/westWingClassroomPageImage.png")
keyboardingLaboratoryPageImgPath = PhotoImage(file="Assets/categoriesPage/laboratoriesPage/keyboardingLaboratoryPageImage.png")
computerLaboratoryPageImgPath = PhotoImage(file="Assets/categoriesPage/laboratoriesPage/computerLaboratoryPageImage.png")
stenographyLaboratoryPageImgPath = PhotoImage(file="Assets/categoriesPage/laboratoriesPage/stenographyLaboratoryPageImage.png")
languageLaboratoryPageImgPath= PhotoImage(file="Assets/categoriesPage/laboratoriesPage/languageLaboratoryPageImage.png")
scienceLaboratoryPageImgPath = PhotoImage(file="Assets/categoriesPage/laboratoriesPage/scienceLaboratoryPageImage.png")
registrarOfficePageImgPath = PhotoImage(file="Assets/categoriesPage/transactionPage/registrarOfficePageImage.png")
registrarOfficeListPageImgPath = PhotoImage(file="Assets/categoriesPage/transactionPage/registrarOfficeListPageImage.png")
cashierOfficePageImgPath = PhotoImage(file="Assets/categoriesPage/transactionPage/cashierOfficePageImage.png") 
cashierOfficeListPageImgPath = PhotoImage(file="Assets/categoriesPage/transactionPage/cashierOfficeListPageImage.png")
registrarRecordsPageImgPath = PhotoImage(file="Assets/categoriesPage/transactionPage/registrarRecordsPageImage.png")
admissionRegistrationPageImgPath = PhotoImage(file="Assets/categoriesPage/transactionPage/admissionRegistrationPageImage.png")
scholarshipAssistancePageImgPath = PhotoImage(file="Assets/categoriesPage/transactionPage/scholarshipAssistancePageImage.png")
shsDepartmentPageImgPath= PhotoImage(file="Assets/categoriesPage/transactionPage/shsDepartmentPageImage.png")
medicalClinicServicesPageImgPath = PhotoImage(file="Assets/categoriesPage/medicalOfficePage/medicalClinicServicesPageImage.png")
dentalClinicServicesPageImgPath = PhotoImage(file="Assets/categoriesPage/medicalOfficePage/dentalClinicServicesPageImage.png")
directorOfficeMedicalPageImgPath= PhotoImage(file="Assets/categoriesPage/medicalOfficePage/directorOfficeMedicalPageImage.png")
accentureRoomPageImgPath = PhotoImage(file="Assets/categoriesPage/eventHallsPage/accentureRoomImagePage.png")
claroRectoRoomPageImgPath = PhotoImage(file="Assets/categoriesPage/eventHallsPage/claroRectoRoomImagePage.png")
audioVisualRoomPageImgPath = PhotoImage(file="Assets/categoriesPage/eventHallsPage/audioVisualRoomImagePage.png")
overviewComfortRoomPageImgPath = PhotoImage(file="Assets/categoriesPage/comfortRoomPage/overviewComfortRoom.png")
eastComfortRoomPageImgPath = PhotoImage(file="Assets/categoriesPage/comfortRoomPage/eastComfortRoom.png")
westComfortRoomPageImgPath = PhotoImage(file="Assets/categoriesPage/comfortRoomPage/westComfortRoom.png")
southComfortRoomPageImgPath = PhotoImage(file="Assets/categoriesPage/comfortRoomPage/southComfortRoom.png")
lagoonComfortRoomPageImgPath = PhotoImage(file="Assets/categoriesPage/comfortRoomPage/lagoonComfortRoom.png")

eastFacultiesPageImgPath = PhotoImage(file="Assets/categoriesPage/eastFacultiesPage/eastFacultiesPageImage.png")
mpcPageImgPath = PhotoImage(file="Assets/categoriesPage/eastFacultiesPage/mpcPageImage.png")
rotcPageImgPath = PhotoImage(file="Assets/categoriesPage/eastFacultiesPage/rotcPageImage.png")
hrdPageImgPath = PhotoImage(file="Assets/categoriesPage/eastFacultiesPage/hrdPageImage.png")
odPageImgPath = PhotoImage(file="Assets/categoriesPage/eastFacultiesPage/odPageImage.png")
fmoPageImgPath = PhotoImage(file="Assets/categoriesPage/eastFacultiesPage/fmoPageImage.png")
dscoPageImgPath = PhotoImage(file="Assets/categoriesPage/eastFacultiesPage/dscoPageImage.png")
ccPageImgPath = PhotoImage(file="Assets/categoriesPage/eastFacultiesPage/ccPageImage.png")
dcsdPageImgPath = PhotoImage(file="Assets/categoriesPage/eastFacultiesPage/dcsdPageImage.png")
postBaccPageImgPath = PhotoImage(file="Assets/categoriesPage/eastFacultiesPage/postBaccPageImage.png")
nstpPageImgPath = PhotoImage(file="Assets/categoriesPage/eastFacultiesPage/nstpPageImage.png")
cssdPageImgPath = PhotoImage(file="Assets/categoriesPage/eastFacultiesPage/cssdPageImage.png")
mpcButtonImgPath = PhotoImage(file="Assets/categoriesPage/eastFacultiesPage/mpcButtonImage.png")
rotcButtonImgPath = PhotoImage(file="Assets/categoriesPage/eastFacultiesPage/rotcButtonImage.png")
hrdButtonImgPath = PhotoImage(file="Assets/categoriesPage/eastFacultiesPage/hrdButtonImage.png")
odButtonImgPath = PhotoImage(file="Assets/categoriesPage/eastFacultiesPage/odButtonImage.png")
fmoButtonImgPath = PhotoImage(file="Assets/categoriesPage/eastFacultiesPage/fmoButtonImage.png")
dscoButtonImgPath = PhotoImage(file="Assets/categoriesPage/eastFacultiesPage/dscoButtonImage.png")
ccButtonImgPath = PhotoImage(file="Assets/categoriesPage/eastFacultiesPage/ccButtonImage.png")
dcsdButtonImgPath = PhotoImage(file="Assets/categoriesPage/eastFacultiesPage/dcsdButtonImage.png")
postBaccButtonImgPath = PhotoImage(file="Assets/categoriesPage/eastFacultiesPage/postBaccButtonImage.png")
nstpButtonImgPath = PhotoImage(file="Assets/categoriesPage/eastFacultiesPage/nstpButtonImage.png")
cssdButtonImgPath = PhotoImage(file="Assets/categoriesPage/eastFacultiesPage/cssdButtonImage.png")

westFacultiesPageImgPath = PhotoImage(file="Assets/categoriesPage/westFacultiesPage/westFacultiesPageImage.png")
driPageImgPath = PhotoImage(file="Assets/categoriesPage/westFacultiesPage/driPageImage.png")
coePageImgPath = PhotoImage(file="Assets/categoriesPage/westFacultiesPage/coePageImage.png")
coaPageImgPath = PhotoImage(file="Assets/categoriesPage/westFacultiesPage/coaPageImage.png")
cbaPageImgPath = PhotoImage(file="Assets/categoriesPage/westFacultiesPage/cbaPageImage.png")
cosPageImgPath = PhotoImage(file="Assets/categoriesPage/westFacultiesPage/cosPageImage.png")
driButtonImgPath = PhotoImage(file="Assets/categoriesPage/westFacultiesPage/driButtonImage.png")
shsButtonImgPath = PhotoImage(file="Assets/categoriesPage/westFacultiesPage/shsButtonImage.png")
coaButtonImgPath = PhotoImage(file="Assets/categoriesPage/westFacultiesPage/coaButtonImage.png")
coeButtonImgPath = PhotoImage(file="Assets/categoriesPage/westFacultiesPage/coeButtonImage.png")
cbaButtonImgPath = PhotoImage(file="Assets/categoriesPage/westFacultiesPage/cbaButtonImage.png")
cosButtonImgPath = PhotoImage(file="Assets/categoriesPage/westFacultiesPage/cosButtonImage.png")

mapBarImgPath = PhotoImage(file="Assets/homePage/mapBar.png")
iconToggleImgPath = PhotoImage(file="Assets/homePage/iconToggle.png")
searchIconImgPath = PhotoImage(file="Assets/homePage/searchIcon.png")
viewAllButtonImgPath = PhotoImage(file="Assets/homePage/viewAll.png")
exitButtonImgPath = PhotoImage(file="Assets/homePage/exitButton.png")
iconUntoggleImgPath = PhotoImage(file="Assets/homePage/iconUntoggle.png")
lagoonButtonImgPath = PhotoImage(file="Assets/homePage/lagoonButton.png")
aboutAppButtonImgPath = PhotoImage(file="Assets/homePage/aboutAppButton.png")
eastWingButtonImgPath = PhotoImage(file="Assets/homePage/eastWingButton.png")
westWingButtonImgPath = PhotoImage(file="Assets/homePage/westWingButton.png")
southWingButtonImgPath = PhotoImage(file="Assets/homePage/southWingButton.png")

mabiniButtonImgPath = PhotoImage(file="Assets/homePage/mabiniButton.png")
visitorButtonImgPath = PhotoImage(file="Assets/homePage/visitorButton.png")
ovalButtonImgPath = PhotoImage(file="Assets/homePage/ovalButton.png")
gymButtonImgPath = PhotoImage(file="Assets/homePage/gymButton.png")
poolButtonImgPath = PhotoImage(file="Assets/homePage/poolButton.png")

interfaithChapelButtonImgPath = PhotoImage(file="Assets/homePage/interfaithChapelButton.png")
classroomCategoryButtonImgPath = PhotoImage(file="Assets/homePage/classroomCategoryButton.png")
facultiesCategoryButtonImgPath = PhotoImage(file="Assets/homePage/facultiesCategoryButton.png")
laboratoriesCategoryButtonImgPath = PhotoImage(file="Assets/homePage/laboratoriesCategoryButton.png")

mainPageChapelButtonImgPath = PhotoImage(file="Assets/interfaithChapelPage/mainPageButton.png")
lagoonPageChapelButtonImgPath = PhotoImage(file="Assets/interfaithChapelPage/lagoonPageButton.png")
interFaithChapelPageButtonImgPath = PhotoImage(file="Assets/interfaithChapelPage/interFaithChapelPageButton.png")
lagoonPageButtonImgPath = PhotoImage(file="Assets/lagoonPage/lagoonPageButton.png")
viewStallsButtonImgPath = PhotoImage(file="Assets/lagoonPage/viewStallsButton.png")
interFaithLagoonPageButtonImgPath = PhotoImage(file="Assets/lagoonPage/interFaithChapelPageButton.png")

categoryReturnButtonImgPath = PhotoImage(file="Assets/categoriesPage/categoryReturnButtonImage.png")
categorySearchIconImgPath = PhotoImage(file="Assets/categoriesPage/categorySearchIconImage.png")
classroomTextImgPath = PhotoImage(file="Assets/categoriesPage/classroomTextImage.png")
laboratoriesTextImgPath = PhotoImage(file="Assets/categoriesPage/laboratoriesTextImage.png")
facultiesTextImgPath = PhotoImage(file="Assets/categoriesPage/facultiesTextImage.png")
transactionTextImgPath = PhotoImage(file="Assets/categoriesPage/transactionOfficeTextImage.png")
medicalOfficeTextImgPath = PhotoImage(file="Assets/categoriesPage/medicalOfficeTextImage.png")
eventHallsTextImgPath = PhotoImage(file="Assets/categoriesPage/eventHallsTextImage.png")
comfortRoomsTextImgPath = PhotoImage(file="Assets/categoriesPage/comfortRoomsTextImage.png")
dropdownButtonImgPath = PhotoImage(file="Assets/categoriesPage/dropdownButtonImage.png")
clickedDropdownButtonImgPath = PhotoImage(file="Assets/categoriesPage/clickedDropdownButtonImage.png")
clickedclassroomTextImgPath = PhotoImage(file="Assets/categoriesPage/clickedClassroomTextImage.png")
clickedLaboratoriesTextImgPath = PhotoImage(file="Assets/categoriesPage/clickedLaboratoriesTextImage.png")
clickedFacultiesTextImgPath = PhotoImage(file="Assets/categoriesPage/clickedFacultiesTextImage.png")
clickedTransactionTextImgPath = PhotoImage(file="Assets/categoriesPage/clickedTransactionOfficeTextImage.png")
clickedMedicalOfficeTextImgPath = PhotoImage(file="Assets/categoriesPage/clickedMedicalOfficeTextImage.png")
clickedEventHallsTextImgPath = PhotoImage(file="Assets/categoriesPage/clickedEventHallsTextImage.png")
clickedComfortRoomsTextImgPath = PhotoImage(file="Assets/categoriesPage/clickedComfortRoomsTextImage.png")
discoverTextImgPath = PhotoImage(file="Assets/categoriesPage/discoverTextImage.png")
viewMainWingImgPath = PhotoImage(file="Assets/categoriesPage/viewMainWingImage.png")
eastWingCategoryImgpath =  PhotoImage(file="Assets/categoriesPage/eastWingImage.png")
westWingCategoryImgPath = PhotoImage(file="Assets/categoriesPage/westWingImage.png")
southWingCategoryImgPath = PhotoImage(file="Assets/categoriesPage/southWingImage.png")
eastWingClassroomImgPath = PhotoImage(file="Assets/categoriesPage/eastWingClassroomsImage.png")
westWingClassroomImgPath = PhotoImage(file="Assets/categoriesPage/westWingClassroomsImage.png")
keyboardingLaboratoryImgPath = PhotoImage(file="Assets/categoriesPage/keyboardingLaboratoryImage.png")
computerLaboratoryImgPath = PhotoImage(file="Assets/categoriesPage/computerLaboratoryImage.png")
scienceLaboratoryImgPath = PhotoImage(file="Assets/categoriesPage/scienceLaboratoryImage.png")
languageLaboratoryImgPath = PhotoImage(file="Assets/categoriesPage/languageLaboratoryImage.png")
stenographyLaboratoryImgPath = PhotoImage(file="Assets/categoriesPage/stenographyLaboratoryImage.png")
eastWingFacultiesImgPath = PhotoImage(file="Assets/categoriesPage/eastWingFacultiesImage.png") 
westWingFacultiesImgPath = PhotoImage(file="Assets/categoriesPage/westWingFacultiesImage.png")
southWingFacultiesImgPath = PhotoImage(file="Assets/categoriesPage/southWingFacultiesImage.png")
registrarOfficeImgPath = PhotoImage(file="Assets/categoriesPage/registrarOfficeImage.png")
cashierOfficeImgPath = PhotoImage(file="Assets/categoriesPage/cashierOfficeImage.png")
ourOfficeImgPath = PhotoImage(file="Assets/categoriesPage/OURImage.png")
arrsOfficeImgPath = PhotoImage(file="Assets/categoriesPage/ARSSImage.png")
osfOfficeImgPath = PhotoImage(file="Assets/categoriesPage/OSFAImage.png")
shsOfficeImgPath = PhotoImage(file="Assets/categoriesPage/shsAdministrationOfficeImage.png")
storageRoomImgPath = PhotoImage(file="Assets/categoriesPage/storageRoomImage.png")
recordsOfficeImgPath = PhotoImage(file="Assets/categoriesPage/recordsOfficeImage.png")
dentalServicesImgPath = PhotoImage(file="Assets/categoriesPage/dentalServicesImage.png")
medicalServicesImgPath = PhotoImage(file="Assets/categoriesPage/medicalServicesImage.png")
officeOfMedicalImgPath = PhotoImage(file="Assets/categoriesPage/officeOfMedicalImage.png")
rectoHallImageImgPath = PhotoImage(file="Assets/categoriesPage/rectoHallImage.png")
accentureRoomImgPath = PhotoImage(file="Assets/categoriesPage/accentureRoomImage.png")
audioVisualRoomImgPath = PhotoImage(file="Assets/categoriesPage/audioVisualRoomImage.png")
comfortRoomsImgPath = PhotoImage(file="Assets/categoriesPage/comfortRoomsImage.png")
viewCashierCounterImgPath = PhotoImage(file="Assets/categoriesPage/transactionPage/viewCashierCounterImage.png")
viewRegistratCounterImgPath = PhotoImage(file="Assets/categoriesPage/transactionPage/viewRegistratCounterImage.png")

eastClassroom2ndFloorImgPath = PhotoImage(file="Assets/categoriesPage/eastWingPage/eastClassroom2ndFloorImage.png")
eastClassroom3rdFloorImgPath = PhotoImage(file="Assets/categoriesPage/eastWingPage/eastClassroom3rdFloorImage.png")
eastClassroom4thFloorImgPath = PhotoImage(file="Assets/categoriesPage/eastWingPage/eastClassroom4thFloorImage.png")
eastClassroom5thFloorImgPath= PhotoImage(file="Assets/categoriesPage/eastWingPage/eastClassroom5thFloorImage.png")
secondFloorEastClassroomImgPath = PhotoImage(file="Assets/categoriesPage/eastWingPage/2ndFloorEastClassroomImage.png")
thirdFloorEastClassroomImgPath = PhotoImage(file="Assets/categoriesPage/eastWingPage/3rdFloorEastClassroomImage.png")
fourthFloorEastClassroomImgPath = PhotoImage(file="Assets/categoriesPage/eastWingPage/4thFloorEastClassroomImage.png")
fifthFloorEastClassroomImgPath = PhotoImage(file="Assets/categoriesPage/eastWingPage/5thFloorEastClassroomImage.png")

westClassroom2ndFloorImgPath = PhotoImage(file="Assets/categoriesPage/westWingPage/westClassroom2ndFloorImage.png")
westClassroom3rdFloorImgPath = PhotoImage(file="Assets/categoriesPage/westWingPage/westClassroom3rdFloorImage.png")
westClassroom4thFloorImgPath = PhotoImage(file="Assets/categoriesPage/westWingPage/westClassroom4thFloorImage.png")
westClassroom5thFloorImgPath= PhotoImage(file="Assets/categoriesPage/westWingPage/westClassroom5thFloorImage.png")
westClassroom6thFloorImgPath= PhotoImage(file="Assets/categoriesPage/westWingPage/westClassroom6thFloorImage.png")
secondFloorWestClassroomImgPath = PhotoImage(file="Assets/categoriesPage/westWingPage/secondFloorWestClassroomImage.png")
thirdFloorWestClassroomImgPath = PhotoImage(file="Assets/categoriesPage/westWingPage/thirdFloorWestClassroomImage.png")
fourthFloorWestClassroomImgPath = PhotoImage(file="Assets/categoriesPage/westWingPage/fourthFloorWestClassroomImage.png")
fifthFloorWestClassroomImgPath = PhotoImage(file="Assets/categoriesPage/westWingPage/fifthFloorWestClassroomImage.png")
sixthFloorWestClassroomImgPath = PhotoImage(file="Assets/categoriesPage/westWingPage/sixthFloorWestClassroomImage.png")

activeOverviewTab = PhotoImage(file="Assets/categoriesPage/comfortRoomPage/activeOverviewTab.png")
activeEastWingTab = PhotoImage(file="Assets/categoriesPage/comfortRoomPage/activeEastWingTab.png")
activeWestWingTab = PhotoImage(file="Assets/categoriesPage/comfortRoomPage/activeWestWingTab.png")
activeSouthWingTab = PhotoImage(file="Assets/categoriesPage/comfortRoomPage/activeSouthWingTab.png")
activeLagoonTab = PhotoImage(file="Assets/categoriesPage/comfortRoomPage/activeLagoonTab.png")
idleOverviewTab = PhotoImage(file="Assets/categoriesPage/comfortRoomPage/idleOverviewTab.png")
idleEastWingTab = PhotoImage(file="Assets/categoriesPage/comfortRoomPage/idleEastWingTab.png")
idleWestWingTab = PhotoImage(file="Assets/categoriesPage/comfortRoomPage/idleWestWingTab.png")
idleSouthWingTab = PhotoImage(file="Assets/categoriesPage/comfortRoomPage/idleSouthWingTab.png")
idleLagoonTab = PhotoImage(file="Assets/categoriesPage/comfortRoomPage/idleLagoonTab.png")

lagoonFoodStallPageImgPath = PhotoImage(file="Assets/lagoon/lagoonFoodStalls/lagooonStall.png")
lagoonBurgerImgPath = PhotoImage (file="Assets/lagoon/lagoonFoodStalls/fBurgersnSandwiches.png")
lagoonChickenliciousImgPath = PhotoImage(file="Assets/lagoon/lagoonFoodStalls/fChickenlicious.png" )
lagoonChickenChopImgPath = PhotoImage(file="Assets/lagoon/lagoonFoodStalls/fChknChop.png")
lagoonCuadroImgPath = PhotoImage(file="Assets/lagoon/lagoonFoodStalls/fCuadro.png")
lagoonCupOfTeaImgPath = PhotoImage(file="Assets/lagoon/lagoonFoodStalls/fCupofTea.png")
lagoonDavidsWingsImgPath = PhotoImage(file="Assets/lagoon/lagoonFoodStalls/fDavidsWings.png")
lagoonDavidsCafeImgPath = PhotoImage(file="Assets/lagoon/lagoonFoodStalls/fDavidsCafe.png")
lagoonFifthImgPath = PhotoImage(file="Assets/lagoon/lagoonFoodStalls/fFifth.png")
lagoonFLavorsofLagoonImgPath = PhotoImage(file="Assets/lagoon/lagoonFoodStalls/fFlavorsofLagoon.png")
lagoonFoodandSnackImgPath = PhotoImage(file="Assets/lagoon/lagoonFoodStalls/fFoodnSnack.png")
lagoonFudbookImgPath = PhotoImage(file="Assets/lagoon/lagoonFoodStalls/fFudbook.png")
lagoonGoHealthyImgPath = PhotoImage(file="Assets/lagoon/lagoonFoodStalls/fGoHealthy.png")
lagoonJToppingsImgPath = PhotoImage(file= "Assets/lagoon/lagoonFoodStalls/fJToppings.png")
lagoonKeemsImgPath = PhotoImage(file ="Assets/lagoon/lagoonFoodStalls/fKeems.png")
lagoonKoficcinoImgPath = PhotoImage(file = "Assets/lagoon/lagoonFoodStalls/fKoficcino.png")
lagoonLizasImgPath = PhotoImage(file="Assets/lagoon/lagoonFoodStalls/fLizas.png")
lagoonMamaThessImgPath = PhotoImage(file="Assets/lagoon/lagoonFoodStalls/fMamaThess.png")
lagoonMireseImgPath = PhotoImage(file = "Assets/lagoon/lagoonFoodStalls/fMirese.png")
lagoonMrBrewskoImgPath = PhotoImage(file = "Assets/lagoon/lagoonFoodStalls/fMrBrewsko.png")
lagoonPapritosImgPath = PhotoImage (file="Assets/lagoon/lagoonFoodStalls/fPapritos.png")
lagoonPuprenersImgPath = PhotoImage (file= "Assets/lagoon/lagoonFoodStalls/fPupreners.png")
lagoonWaffleImgPath = PhotoImage(file="Assets/lagoon/lagoonFoodStalls/fWaffleTime.png")
lagoonVirginShakeImgPath = PhotoImage(file="Assets/lagoon/lagoonFoodStalls/fVirginShake.png")
lagoonJibImgPath = PhotoImage(file="Assets/lagoon/lagoonFoodStalls/fJib.png")
lagoonPuroysImgPath = PhotoImage (file="Assets/lagoon/lagoonFoodStalls/fPuroys.png")
lagoonRewindasImgPath = PhotoImage (file = "Assets/lagoon/lagoonFoodStalls/fRewandas.png")
lagoonTrinasImgPath = PhotoImage(file="Assets/lagoon/lagoonFoodStalls/fTrinas.png")
lagoonUnivTopBurgerImgPath = PhotoImage (file="Assets/lagoon/lagoonFoodStalls/fUnivTopBurger.png")
lagoonBlessingPrintingImgPath = PhotoImage(file="Assets/lagoon/printingSuppliesShops/sBlessingPrinting.png")
lagoonCraftImgPath = PhotoImage(file="Assets/lagoon/printingSuppliesShops/sCraft.png")
lagoonMistyImgPath = PhotoImage(file="Assets/lagoon/printingSuppliesShops/sMisty.png")
lagoonPrintBestImgPath = PhotoImage(file="Assets/lagoon/printingSuppliesShops/sPrintbest.png")
lagoonPrintingShopsImgPath = PhotoImage(file="Assets/lagoon/printingSuppliesShops/sPrintingShops.png")
lagoonRizzImgPath = PhotoImage(file = "Assets/lagoon/printingSuppliesShops/sRizz.png")

lagoonOverviewButtonImgPath = PhotoImage(file="Assets/lagoon/lagoonFoodStalls/overviewButton.png")
lagoonSuppliesButtonImgPath = PhotoImage(file = "Assets/lagoon/lagoonFoodStalls/printSuppliesButton.png")
lagoonSuppliesButtonClickedImgPath = PhotoImage(file="Assets/lagoon/lagoonFoodStalls/printSuppliesButtonClicked.png")
lagoonFoodStallButtonImgPath = PhotoImage (file = "Assets/lagoon/lagoonFoodStalls/foodStallsButton.png")
lagoonFoodStallButtonClickedImgPath = PhotoImage (file = "Assets/lagoon/lagoonFoodStalls/foodStallsButtonClicked.png")


discoverBgImgPath = PhotoImage(file="Assets/discoverPage/discoverPageBg.png")
discoverEastCrImgPath = PhotoImage(file="Assets/discoverPage/eastWing/eComfortRooms.png")
discoverEastEventHallImgPath = PhotoImage(file="Assets/discoverPage/eastWing/eEventHall.png")
discoverEastFacultiesImgPath = PhotoImage(file="Assets/discoverPage/eastWing/eFaculties.png")
discoverEastLecRoomImgPath = PhotoImage(file="Assets/discoverPage/eastWing/eLecRoom.png")
discoverEastMedOfficesImgPath = PhotoImage(file="Assets/discoverPage/eastWing/eMedicalOffices.png")
discoverEastLabsImgPath = PhotoImage(file="Assets/discoverPage/westWing/wLabs.png")
discoverWestClassroomsImgPath = PhotoImage(file="Assets/discoverPage/westWing/wClassrooms.png")
discoverWestCrImgPath = PhotoImage(file="Assets/discoverPage/westWing/wComfortRooms.png")
discoverWestFacultiesImgPath = PhotoImage(file="Assets/discoverPage/westWing/wFaculties.png")
discoverWestLabsImgPath = PhotoImage(file="Assets/discoverPage/westWing/wLabs.png")
discoverWestTransOfficesImgPath = PhotoImage(file="Assets/discoverPage/westWing/wTransacOffices.png")
discoverSouthCrImgPath = PhotoImage(file="Assets/discoverPage/southWing/sComfortRooms.png")
discoverSouthEventHallImgPath = PhotoImage(file="Assets/discoverPage/southWing/sEventHall.png")
discoverSouthFacultiesImgPath = PhotoImage(file="Assets/discoverPage/southWing/sFaculties.png")
discoverSouthLabImgPath = PhotoImage(file="Assets/discoverPage/southWing/sLabs.png")
discoverSouthTransOfficeImgPath = PhotoImage(file="Assets/discoverPage/southWing/sTransacoffices.png")

discoverEastButtonImgPath = PhotoImage(file="Assets/discoverPage/eastWing/eastButton.png")
discoverEastClickedImgPath = PhotoImage(file="Assets/discoverPage/eastWing/eastButtonClicked.png")
discoverWestButtonImgPath = PhotoImage(file="Assets/discoverPage/westWing/westButton.png")
discoverWestClickedImgPath = PhotoImage(file="Assets/discoverPage/westWing/westButtonClicked.png")
discoverSouthButtonImgPath = PhotoImage(file="Assets/discoverPage/southWing/southButton.png")
discoverSouthClickedImgPath = PhotoImage(file="Assets/discoverPage/southWing/southButtonClicked.png")
discoverMainPageButtonImgPath = PhotoImage(file = "Assets/discoverPage/mainPageButton.png")

eastEventHallBgImgPath = PhotoImage(file="Assets/eastEventHallsPage/eEventHallsBg.png")
eastEventHallAccentureTabImgPath = PhotoImage(file="Assets/eastEventHallsPage/eAccentureRoomTab.png")
eastEventHallAudioVisTabImgPath = PhotoImage(file="Assets/eastEventHallsPage/eAudioVisRoomTab.png")

eastLabBgImgPath = PhotoImage(file="Assets/eastLaboratoriesPage/eLaboratoriesBg.png")
eastLabCompLabTabImgPath = PhotoImage(file="Assets/eastLaboratoriesPage/eCompLabTab.png")
eastLabScienceLabTabImgPath = PhotoImage(file="Assets/eastLaboratoriesPage/eScienceLabTab.png")
eastLabStenoLabTabImgPath = PhotoImage(file="Assets/eastLaboratoriesPage/eStenoLabTab.png")

eastMedOfficeBgImgPath = PhotoImage(file="Assets/eastMedicalOfficesPage/eMedOfficesBg.png")
eastDentalClinicTabImgPath = PhotoImage(file="Assets/eastMedicalOfficesPage/eDentalClinicServices.png")
eastODMedHealthTabImgPath = PhotoImage(file="Assets/eastMedicalOfficesPage/eODMedHealthServicesTab.png")
eastMedClinicTabImgPath = PhotoImage(file="Assets/eastMedicalOfficesPage/eMedClinicServices.png")

westTransactionBgImgPath = PhotoImage(file="Assets/westTransactionPage/wTransactionBG.png")
wARSSTabImgPath = PhotoImage(file="Assets/westTransactionPage/wARSSTab.png")
wOSFATabImgPath = PhotoImage(file="Assets/westTransactionPage/wOSFATab.png")
wOURTabImgPath = PhotoImage(file="Assets/westTransactionPage/wOURTab.png")
wSHSTabImgPath = PhotoImage(file="Assets/westTransactionPage/wSHSTab.png")

southFacBgImgPath = PhotoImage(file="Assets/southFacultiesPage/sFacultiesBg.png")
southFacCAFBgImgPath = PhotoImage(file="Assets/southFacultiesPage/sCAFBg.png")
southFacCAFTabImgPath = PhotoImage(file="Assets/southFacultiesPage/sCAFTab.png")
southFacCBABgImgPath = PhotoImage(file="Assets/southFacultiesPage/sCBABg.png")
southFacCBATabImgPath = PhotoImage(file="Assets/southFacultiesPage/sCBATab.png")
southFacCCISOFRBgImgPath = PhotoImage(file="Assets/southFacultiesPage/sCCISOFRBg.png")
southFacCCISOFRTabImgPath = PhotoImage(file="Assets/southFacultiesPage/sCCISOFRTab.png")
southFacCOEDBgImgPath = PhotoImage(file="Assets/southFacultiesPage/sCOEDBg.png")
southFacCOEDTabImgPath = PhotoImage(file="Assets/southFacultiesPage/sCOEDTab.png")
southFacConfRoomBgImgPath = PhotoImage(file="Assets/southFacultiesPage/sConfRoomBg.png")
southFacConfRoomTabImgPath = PhotoImage(file="Assets/southFacultiesPage/sConfRoomTab.png")
southFacCOSFRBgImgPath = PhotoImage(file="Assets/southFacultiesPage/sCOSFRBg.png")
southFacCOSFRTabImgPath = PhotoImage(file="Assets/southFacultiesPage/sCOSFRTab.png")
southFacCPSPABgImgPath = PhotoImage(file="Assets/southFacultiesPage/sCPSPABg.png")
southFacCPSPATabImgPath = PhotoImage(file="Assets/southFacultiesPage/sCPSPATab.png")
southFacCSSDBgImgPath = PhotoImage(file="Assets/southFacultiesPage/sCSSDBg.png")
southFacCSSDTabImgPath = PhotoImage(file="Assets/southFacultiesPage/sCSSDTab.png")
southFacDOMSBgImgPath = PhotoImage(file="Assets/southFacultiesPage/sDOMSBg.png")
southFacDOMSTabImgPath = PhotoImage(file="Assets/southFacultiesPage/sDOMSTab.png")
southFacERMOBgImgPath = PhotoImage(file="Assets/southFacultiesPage/sERMOBg.png")
southFacERMOTabImgPath = PhotoImage(file="Assets/southFacultiesPage/sERMOTab.png")
southFacGDOBgImgPath = PhotoImage(file="Assets/southFacultiesPage/sGDOBg.png")
southFacGDOTabImgPath = PhotoImage(file="Assets/southFacultiesPage/sGDOTab.png")
southFacGSOBgImgPath = PhotoImage(file="Assets/southFacultiesPage/sGSOBg.png")
southFacGSOTabImgPath = PhotoImage(file="Assets/southFacultiesPage/sGSOTab.png")
southFacHRMDBgImgPath = PhotoImage(file="Assets/southFacultiesPage/sHRMDBg.png")
southFacHRMDTabImgPath = PhotoImage(file="Assets/southFacultiesPage/sHRMDTab.png")
southFacIDSABgImgPath = PhotoImage(file="Assets/southFacultiesPage/sIDSABg.png")
southFacIDSATabImgPath = PhotoImage(file="Assets/southFacultiesPage/sIDSATab.png")
southFacIIMSBgImgPath = PhotoImage(file="Assets/southFacultiesPage/sIIMSBg.png")
southFacIIMSTabImgPath = PhotoImage(file="Assets/southFacultiesPage/sIIMSTab.png")
southFacISTRBgImgPath = PhotoImage(file="Assets/southFacultiesPage/sISTRBg.png")
southFacISTRTabImgPath = PhotoImage(file="Assets/southFacultiesPage/sISTRTab.png")
southFacLLSBgImgPath = PhotoImage(file="Assets/southFacultiesPage/sLLSBg.png")
southFacLLSTabImgPath = PhotoImage(file="Assets/southFacultiesPage/sLLSTab.png")
southFacNOCBgImgPath = PhotoImage(file="Assets/southFacultiesPage/sNOCBg.png")
southFacNOCTabImgPath = PhotoImage(file="Assets/southFacultiesPage/sNOCtab.png")
southFacOCPSBgImgPath = PhotoImage(file="Assets/southFacultiesPage/sOCPSBg.png")
southFacOCPSTabImgPath = PhotoImage(file="Assets/southFacultiesPage/sOCPSTab.png")
southFacODBgImgPath = PhotoImage(file="Assets/southFacultiesPage/sODBg.png")
southFacODTabImgPath = PhotoImage(file="Assets/southFacultiesPage/sODTab.png")
southFacOIABgImgPath = PhotoImage(file="Assets/southFacultiesPage/sOIABg.png")
southFacOIATabImgPath = PhotoImage(file="Assets/southFacultiesPage/sOIATab.png")
southFacOPBgImgPath = PhotoImage(file="Assets/southFacultiesPage/sOPBg.png")
southFacOPTabImgPath = PhotoImage(file="Assets/southFacultiesPage/sOPTab.png")
southFacOUBBgImgPath = PhotoImage(file="Assets/southFacultiesPage/sOUBBg.png")
southFacOUBTabImgPath =PhotoImage(file="Assets/southFacultiesPage/sOUBTab.png")
southFacOVPBgImgPath = PhotoImage(file="Assets/southFacultiesPage/sOVPBg.png")
southFacOVPTabImgPath = PhotoImage(file="Assets/southFacultiesPage/sOVPTab.png")
southFacPFOBgImgPath = PhotoImage(file="Assets/southFacultiesPage/sPFOBg.png")
southFacPFOTabImgPath = PhotoImage(file="Assets/southFacultiesPage/sPFOTab.png")
southFacPMOBACBgImgPath = PhotoImage(file="Assets/southFacultiesPage/sPMOBACBg.png")
southFacPMOBACTabImgPath = PhotoImage(file="Assets/southFacultiesPage/sPMOBACTab.png")
southFacPOBgImgPath = PhotoImage(file="Assets/southFacultiesPage/sPOBg.png")
southFacPOTabImgPath = PhotoImage(file="Assets/southFacultiesPage/sPOTab.png")
southFacSPPOBgImgPath = PhotoImage(file="Assets/southFacultiesPage/sSPPOBg.png")
southFacSPPOTabImgPath = PhotoImage(file="Assets/southFacultiesPage/sSPPOTab.png")
southFacSRBgImgPath = PhotoImage(file="Assets/southFacultiesPage/sSRBg.png")
southFacSRTabImgPath = PhotoImage(file="Assets/southFacultiesPage/sSRTab.png")
southFacULOBgImgPath = PhotoImage(file="Assets/southFacultiesPage/sULOBg.png")
southFacULOTabImgPath = PhotoImage(file="Assets/southFacultiesPage/sULOTab.png")

southLabBgImgPath = PhotoImage(file="Assets/southLaboratoriesPage/sLaboratoriesBg.png")
southLabComLabTabImgPath = PhotoImage(file="Assets/southLaboratoriesPage/sCompLabTab.png")
southLabLanguageLabTabImgPath = PhotoImage(file="Assets/southLaboratoriesPage/sLanguageLabTab.png")

southTransOfficeBgImgPath = PhotoImage(file="Assets/southTransactionOfficesPage/sTransacOfficesBg.png")
southTransOfficeChasierTabImgPath = PhotoImage(file="Assets/southTransactionOfficesPage/sCahsierOfficesTab.png")
southTransOfficeRegisTabImgPath = PhotoImage(file="Assets/southTransactionOfficesPage/sRegisOfficesTab.png")

returnCategoryPageButtonImgPath = PhotoImage(file="Assets/categoriesPage/globalButtons/returnCategoryPageButtonImage.png")
facultiesReturnImgPath = PhotoImage(file="Assets/categoriesPage/globalButtons/facultiesReturnImage.png")
specificClickedDropdownButtonImgPath = PhotoImage(file="Assets/categoriesPage/globalButtons/specificClickedDropdownButtonImage.png")
specificDropdownButtonImgPath = PhotoImage(file="Assets/categoriesPage/globalButtons/specificDropdownButtonImage.png")
specificCategorySearchIconImgPath = PhotoImage(file="Assets/categoriesPage/globalButtons/specificCategorySearchIconImage.png")



aboutReturnButtonImgPath = PhotoImage(file="Assets/aboutPage/aboutReturnButton.png")



# BACKGROUND OF PAGES
welcomeImage = Button(welcomePage, image=welcomeImgPath, command=homesPage, borderwidth=0,relief=SUNKEN, background='#550000', activebackground= "#550000")
welcomeImage.place(x=0, y=0, relheight=1, relwidth=1) 

homePageImage = Label(homePage, image=homeImgPath)
homePageImage.place(x=0, y=0, relheight=1, relwidth=1) 

aboutPageImage = Label(aboutPage, image=aboutImgPath)
aboutPageImage.place(x=0, y=0, relheight=1, relwidth=1) 

interfaithChapelPageImage = Label(interfaithChapelPage, image=interfaithChapelImgPath)
interfaithChapelPageImage.place(x=0, y=0, relheight=1, relwidth=1)

lagoonPageImage = Label(lagoonPage, image=lagoonPageImgPath)
lagoonPageImage.place(x=0, y=0, relheight=1, relwidth=1)

#OUTDOOR AREAS
mabiniShrinePageImage = Label (mabiniPage, image=mabiniShrineImgPath)
mabiniShrinePageImage.place(x=0, y=0, relheight=1, relwidth=1)

gymnasiumPageImage = Label(gymPage, image=gymImgPath)
gymnasiumPageImage.place(x=0, y=0, relheight=1, relwidth=1)

basketballCourtPageImage = Label(ovalPage, image=basketBallCourtImgPath)
basketballCourtPageImage.place(x=0, y=0, relheight=1, relwidth=1)

swimmingPoolPageImage = Label(poolPage, image=swimmingPoolImgPath)
swimmingPoolPageImage.place(x=0, y=0, relheight=1, relwidth=1)

visitorLoungePageImage = Label(visitorPage, image= visitorsLoungeImgPath)
visitorLoungePageImage.place(x=0, y=0, relheight=1, relwidth=1)

#CATEGORIES PAGE
categoryPageImage = Label(categoryPage, image=viewCategoryPageImgPath)
categoryPageImage.place(x=0, y=0, relheight=1, relwidth=1)

eastWingClassroomPageImage = Label(eastWingClassroomPage, image=eastWingClassroomPageImgPath)
eastWingClassroomPageImage.place(x=0, y=0, relheight=1, relwidth=1)   

eastWingClassroomPageImage = Label(westWingClassroomPage, image=westWingClassroomPageImgPath)
eastWingClassroomPageImage.place(x=0, y=0, relheight=1, relwidth=1)  

keyboardingLaboratoryPageImage = Label(keyboardingLaboratoryPage, image=keyboardingLaboratoryPageImgPath)
keyboardingLaboratoryPageImage.place(x=0, y=0, relheight=1, relwidth=1)   

computerLaboratoryPageImage = Label(computerLaboratoryPage, image=computerLaboratoryPageImgPath)
computerLaboratoryPageImage.place(x=0, y=0, relheight=1, relwidth=1)

stenographyLaboratoryPageImage = Label(stenographyLaboratoryPage, image=stenographyLaboratoryPageImgPath)
stenographyLaboratoryPageImage.place(x=0, y=0, relheight=1, relwidth=1)

languageLaboratoryPageImage = Label(languageLaboratoryPage, image=languageLaboratoryPageImgPath)
languageLaboratoryPageImage.place(x=0, y=0, relheight=1, relwidth=1)

scienceLaboratoryPageImage = Label(scienceLaboratoryPage, image=scienceLaboratoryPageImgPath)
scienceLaboratoryPageImage.place(x=0, y=0, relheight=1, relwidth=1)

registrarOfficePageImage = Label(registrarOfficePage, image=registrarOfficePageImgPath)
registrarOfficePageImage.place(x=0, y=0, relheight=1, relwidth=1)

registrarOfficeListPageImage = Label(registrarOfficeListPage, image=registrarOfficeListPageImgPath)
registrarOfficeListPageImage.place(x=0, y=0, relheight=1, relwidth=1)

cashierOfficePageImage = Label(cashierOfficePage, image=cashierOfficePageImgPath)
cashierOfficePageImage.place(x=0, y=0, relheight=1, relwidth=1)

cashierOfficeListPageImage = Label(cashierOfficeListPage, image=cashierOfficeListPageImgPath)
cashierOfficeListPageImage.place(x=0, y=0, relheight=1, relwidth=1)

registrarRecordsPageImage = Label(registrarRecordsPage, image=registrarRecordsPageImgPath)
registrarRecordsPageImage.place(x=0, y=0, relheight=1, relwidth=1)

admissionRegistrationPageImage = Label(admissionRegistrationPage, image=admissionRegistrationPageImgPath)
admissionRegistrationPageImage.place(x=0, y=0, relheight=1, relwidth=1)

scholarshipAssistancePageImage = Label(scholarshipAssistancePage, image=scholarshipAssistancePageImgPath)
scholarshipAssistancePageImage.place(x=0, y=0, relheight=1, relwidth=1)

shsDepartmentPageImage = Label(shsDepartmentPage, image=shsDepartmentPageImgPath)
shsDepartmentPageImage.place(x=0, y=0, relheight=1, relwidth=1)

medicalClinicServicesPageImage = Label(medicalClinicServicePage, image=medicalClinicServicesPageImgPath)
medicalClinicServicesPageImage.place(x=0, y=0, relheight=1, relwidth=1)

dentalClinicServicesPageImage = Label(dentalClinicServicePage, image=dentalClinicServicesPageImgPath)
dentalClinicServicesPageImage.place(x=0, y=0, relheight=1, relwidth=1)

directorOfficeMedicalPageImage = Label(directorOfficeMedicalPage, image=directorOfficeMedicalPageImgPath)
directorOfficeMedicalPageImage.place(x=0, y=0, relheight=1, relwidth=1)

accentureRoomPageImage = Label(accentureRoomPage, image=accentureRoomPageImgPath)
accentureRoomPageImage.place(x=0, y=0, relheight=1, relwidth=1)

claroRectoRoomPageImagePage = Label(claroRectoRoomPage, image=claroRectoRoomPageImgPath)
claroRectoRoomPageImagePage.place(x=0, y=0, relheight=1, relwidth=1)

audioVisualRoomPageImagePage = Label(audioVisualRoomPage, image=audioVisualRoomPageImgPath)
audioVisualRoomPageImagePage.place(x=0, y=0, relheight=1, relwidth=1)

overviewComfortRoomPageImage = Label(overviewComfortRoomPage, image=overviewComfortRoomPageImgPath)
overviewComfortRoomPageImage.place(x=0, y=0, relheight=1, relwidth=1)

eastComfortRoomPageImage = Label(eastComfortRoomPage, image=eastComfortRoomPageImgPath)
eastComfortRoomPageImage.place(x=0, y=0, relheight=1, relwidth=1)

westComfortRoomPageImage = Label(westComfortRoomPage, image=westComfortRoomPageImgPath)
westComfortRoomPageImage.place(x=0, y=0, relheight=1, relwidth=1)

southComfortRoomPageImage = Label(southComfortRoomPage, image=southComfortRoomPageImgPath)
southComfortRoomPageImage.place(x=0, y=0, relheight=1, relwidth=1)

lagoonComfortRoomPageImage = Label(lagoonComfortRoomPage, image=lagoonComfortRoomPageImgPath)
lagoonComfortRoomPageImage.place(x=0, y=0, relheight=1, relwidth=1)

lagoonFoodStallImage = Label(lagoonFoodStallPage, image=lagoonFoodStallPageImgPath)
lagoonFoodStallImage.place (x=0, y=0, relwidth=1, relheight=1)

lagoonSuppliesImage = Label(lagoonSupplyPage, image=lagoonFoodStallPageImgPath)
lagoonSuppliesImage.place (x=0, y=0, relwidth=1, relheight=1)

eastPageBg = Label(discoverEastPage, image = discoverBgImgPath)
eastPageBg.place(x=0, y=0, relheight=1, relwidth=1)  

westPageBg = Label(discoverWestPage, image = discoverBgImgPath)
westPageBg.place(x=0, y=0, relheight=1, relwidth=1)  

southPageBg = Label(discoverSouthPage, image = discoverBgImgPath)
southPageBg.place(x=0, y=0, relheight=1, relwidth=1) 

eastEventHallBg = Label (eastEventHallPage, image = eastEventHallBgImgPath)
eastEventHallBg.place(x=0, y=0, relheight=1, relwidth=1) 

eastLabBg = Label (eastLabPage, image = eastLabBgImgPath)
eastLabBg.place(x=0, y=0, relheight=1, relwidth=1) 

eastMedOfficeBg = Label (eastMedOfficePage, image = eastMedOfficeBgImgPath)
eastMedOfficeBg.place(x=0, y=0, relheight=1, relwidth=1) 

westTransOfficeBg = Label (westTransOfficePage, image = westTransactionBgImgPath)
westTransOfficeBg.place(x=0, y=0, relheight=1, relwidth=1) 

southFacBg = Label (southFacultiesPage, image = southFacBgImgPath)
southFacBg.place(x=0, y=0, relheight=1, relwidth=1) 

sCAFPageBg = Label (sCAFPage, image = southFacCAFBgImgPath)
sCAFPageBg.place(x=0, y=0, relheight=1, relwidth=1) 

sTRansOfficeBg = Label (southTransOfficePage, image = southTransOfficeBgImgPath)
sTRansOfficeBg.place(x=0, y=0, relheight=1, relwidth=1) 

southLabBg = Label (southLabPage, image = southLabBgImgPath)
southLabBg.place(x=0, y=0, relheight=1, relwidth=1)

# LANDING PAGE FRAMES 
tapTextFrame = Frame(welcomePage, width=147, height=24)
tapTextFrame.place(x=130, y=703)

# LANDING PAGE LABELS
tapText = Label(tapTextFrame, text="Tap to continue", fg ='white', bg = '#550000', font=('Inter', 20))
tapText.pack()



# SEARCH BARS
homePageSearhBar = searchBars(homePage)
interfaithChapelSearchBar = searchBars(interfaithChapelPage)
lagoonSearchBar = searchBars(lagoonPage)
mabiniPageSearchBar = searchBars(mabiniPage)
swimmingPoolSearchBar = searchBars(poolPage)
gymSearchBar = searchBars(gymPage)
basketballSearchBar = searchBars(ovalPage)
visitorsLoungeSearchBar = searchBars(visitorPage)


# SEARCH AND RETURN BUTTON
categoryReturnAndSearch = searchBarAndReturnButton(categoryPage)
lagoonFoodStallReturnAndSearch = searchBarAndReturnButton(lagoonFoodStallPage)
lagoonSupplyReturnAndSearch = searchBarAndReturnButton(lagoonSupplyPage)
discoverEastReturnAndSearch = searchBarAndReturnButton(discoverEastPage)
discoverWastReturnAndSearch = searchBarAndReturnButton(discoverWestPage)
discoverSouthReturnAndSearch = searchBarAndReturnButton(discoverSouthPage)





# HOME PAGE MAP BAR
mapBarFrame = CTkScrollableFrame(homePage, width=400, height=400, bg_color = '#550000',fg_color='#400000', border_color='#400000', scrollbar_button_color='#5F0F0F',
                                 scrollbar_button_hover_color='#FFFFF0', orientation="horizontal")
mapBarFrame.place(x=23, y=147)

mapBarImage = Label(mapBarFrame, image=mapBarImgPath, bg='#400000')
mapBarImage.pack()

# HOME PAGE FRAMES
iconToggleFrame1 = Frame(homePage, width=64, height=61)
iconToggleFrame1.place(x=28, y=20.07)

categoryViewAllFrame = Frame(homePage, width=57, height=18, bg='#550000')
categoryViewAllFrame.place(x=363, y=586)

categoryBarFrame = Frame(homePage, width=400, height=149, bg='#550000')
categoryBarFrame.place(x=25, y=615) 

eastWingButtonFrame = Frame(mapBarFrame, width=55, height=14.4)
eastWingButtonFrame.place(x=94.15, y=374.06)

westWingButtonFrame = Frame(mapBarFrame, width=55, height=14.4)
westWingButtonFrame.place(x=4.28, y=283.23)

southWingButtonFrame = Frame(mapBarFrame, width=58, height=14.4)
southWingButtonFrame.place(x=4.66, y=362.13)

interfaithChapelButtonFrame = Frame(mapBarFrame, width=69, height=13)
interfaithChapelButtonFrame.place(x=188, y=348)

lagoonButtonFrame = Frame(mapBarFrame, width=43, height=13)
lagoonButtonFrame.place(x=121.66, y=160.78)

mabiniButtonFrame = Frame(mapBarFrame, width=63, height=14)
mabiniButtonFrame.place(x=245, y=258.75)

visitorButtonFrame = Frame(mapBarFrame, width=66, height=14)
visitorButtonFrame.place(x=516.38, y=69.31)

ovalButtonFrame = Frame(mapBarFrame, width=93, height=14)
ovalButtonFrame.place(x=463, y=264.89)

gymButtonFrame = Frame(mapBarFrame, width=88, height=14)
gymButtonFrame.place(x=398, y=15.32)

poolButtonFrame = Frame(mapBarFrame, width=67, height=14)
poolButtonFrame.place(x=285.27, y=8.25)

classroomCategoryButtonFrame = Frame(categoryBarFrame, width=120, height=140)
classroomCategoryButtonFrame.place(x=5, y=6.08)

facultiesCategoryButtonFrame = Frame(categoryBarFrame, width=120, height=140)
facultiesCategoryButtonFrame.place(x=139, y=6.08)

laboratoriesCategoryButtonFrame = Frame(categoryBarFrame, width=120, height=140)
laboratoriesCategoryButtonFrame.place(x=275, y=6.08)

# HOME PAGE BUTTONS
iconToggleButton = Button(iconToggleFrame1, image=iconToggleImgPath, bd=0,command=iconOpenMenu1 , bg = '#550000', activebackground= "#550000")
iconToggleButton.pack()

eastWingButton = Button(eastWingButtonFrame, image=eastWingButtonImgPath, bd=0, command=discoversEastPage, activebackground= "#550000")
eastWingButton.place(x=0, y=0, relheight=1, relwidth=1) 

westWingButton = Button(westWingButtonFrame, image=westWingButtonImgPath, bd=0, command=discoversWestPage, activebackground= "#550000")
westWingButton.place(x=0, y=0, relheight=1, relwidth=1) 

southWingButton = Button(southWingButtonFrame, image=southWingButtonImgPath, bd=0, command=discoversSouthPage, activebackground= "#550000")
southWingButton.place(x=0, y=0, relheight=1, relwidth=1) 

interfaithChapelButton = Button(interfaithChapelButtonFrame, image=interfaithChapelButtonImgPath, bd=0, command=interfaithPage, activebackground= "#732A18")
interfaithChapelButton.place(x=0, y=0, relheight=1, relwidth=1) 

lagoonButton = Button(lagoonButtonFrame, image=lagoonButtonImgPath, bd=0, command=lagoonsPage, activebackground= "#5DC040")
lagoonButton.place(x=0, y=0, relheight=1, relwidth=1)

mabiniButton = Button(mabiniButtonFrame, image=mabiniButtonImgPath, bd=0, command=mabinisPage, activebackground= "#5DC040")
mabiniButton.place(x=0, y=0, relheight=1, relwidth=1) 

visitorButton = Button(visitorButtonFrame, image=visitorButtonImgPath, bd=0, command=visitorsPage, activebackground= "#716663")
visitorButton.place(x=0, y=0, relheight=1, relwidth=1) 

ovalButton = Button(ovalButtonFrame, image=ovalButtonImgPath, bd=0, command=ovalsPage, activebackground= "#95AB32")
ovalButton.place(x=0, y=0, relheight=1, relwidth=1) 

gymButton = Button(gymButtonFrame, image=gymButtonImgPath, bd=0, command=gymsPage, activebackground= "#5D0303")
gymButton.place(x=0, y=0, relheight=1, relwidth=1) 

poolButton = Button(poolButtonFrame, image=poolButtonImgPath, bd=0, command=poolsPage, activebackground= "#719BDB")
poolButton.place(x=0, y=0, relheight=1, relwidth=1)  

categoryViewAllButton = Button(categoryViewAllFrame, image=viewAllButtonImgPath, bd=0, command=categoriesPage, activebackground= "#550000")
categoryViewAllButton.place(x=0, y=0, relheight=1, relwidth=1) 

classroomCategoryButton = Button(classroomCategoryButtonFrame, image=classroomCategoryButtonImgPath, bd=0, activebackground= "#550000")
classroomCategoryButton.place(x=0, y=0, relheight=1, relwidth=1)

facultiesCategoryButton = Button(facultiesCategoryButtonFrame, image=facultiesCategoryButtonImgPath, bd=0, activebackground= "#550000")
facultiesCategoryButton.place(x=0, y=0, relheight=1, relwidth=1) 

laboratoriesCategoryButton = Button(laboratoriesCategoryButtonFrame, image=laboratoriesCategoryButtonImgPath, bd=0, activebackground= "#550000")
laboratoriesCategoryButton.place(x=0, y=0, relheight=1, relwidth=1)  



# INTERFAITH CHAPEL PAGE
iconToggleFrame2 = Frame(interfaithChapelPage, width=64, height=61)
iconToggleFrame2.place(x=28, y=20.07)

iconToggleButton2 = Button(iconToggleFrame2, image=iconToggleImgPath, bd=0,command=iconOpenMenu2 , bg = '#550000', activebackground= "#550000")
iconToggleButton2.pack()

mainPageChapelFrame = Frame(interfaithChapelPage, width=90, height=28, bg='#550000')
mainPageChapelFrame.place(x=33, y=100) 

lagoonChapelFrame = Frame(interfaithChapelPage, width=74, height=28, bg='#550000')
lagoonChapelFrame.place(x=268, y=100) 

interfaithChapelFrame = Frame(interfaithChapelPage, width=129, height=28, bg='#550000')
interfaithChapelFrame.place(x=131, y=100)

mainPageChapelButton = Button(mainPageChapelFrame, image=mainPageChapelButtonImgPath, command=homesPage, bd=0, activebackground= "#550000")
mainPageChapelButton.place(x=0, y=0, relheight=1, relwidth=1)  

lagoonChapelButton = Button(lagoonChapelFrame, image=lagoonPageChapelButtonImgPath,  command=lagoonsPage, bd=0, activebackground= "#550000")
lagoonChapelButton.place(x=0, y=0, relheight=1, relwidth=1)  

interfaithChapelButton = Button(interfaithChapelFrame, image=interFaithChapelPageButtonImgPath, command=interfaithPage, bd=0, activebackground= "#550000")
interfaithChapelButton.place(x=-1, y=0, relheight=1, relwidth=1)   



# LAGOON PAGE
iconToggleFrame3 = Frame(lagoonPage, width=64, height=61)
iconToggleFrame3.place(x=28, y=20.07)

iconToggleButton3 = Button(iconToggleFrame3, image=iconToggleImgPath, bd=0,command=iconOpenMenu3 , bg = '#550000', activebackground= "#550000")
iconToggleButton3.pack()

mainPageLagoonFrame = Frame(lagoonPage, width=90, height=28, bg='#550000')
mainPageLagoonFrame.place(x=33, y=100) 

lagoonPageButtonFrame = Frame(lagoonPage, width=74, height=28, bg='#550000')
lagoonPageButtonFrame.place(x=268, y=100) 

interfaithChapelFrame = Frame(lagoonPage, width=129, height=28, bg='#550000')
interfaithChapelFrame.place(x=131, y=100)

viewStallsFrame = Frame(lagoonPage, width=62, height=9, bg='#121211')
viewStallsFrame.place(x=367, y=668)

mainPageLagoonButton = Button(mainPageLagoonFrame, image=mainPageChapelButtonImgPath, command=homesPage, bd=0, activebackground= "#550000")
mainPageLagoonButton.place(x=0, y=0, relheight=1, relwidth=1)  

lagoonPageButton = Button(lagoonPageButtonFrame, image=lagoonPageButtonImgPath, command=lagoonsPage, bd=0, activebackground= "#550000")
lagoonPageButton.place(x=0, y=0, relheight=1, relwidth=1)  

interfaithLagoonButton = Button(interfaithChapelFrame, image=interFaithLagoonPageButtonImgPath, command=interfaithPage, bd=0, activebackground= "#550000")
interfaithLagoonButton.place(x=-1, y=0, relheight=1, relwidth=1) 

viewStallsButton = Button(viewStallsFrame, image=viewStallsButtonImgPath, command = lagoonFoodStallsPage, bd=0, activebackground= "#121211", )
viewStallsButton.place(x=-1, y=0, relheight=1, relwidth=1)

#LAGOON BUTTONS
lagoonOverviewButtonFrames= Frame(lagoonFoodStallPage, width=90, height=28)
lagoonOverviewButtonFrames.place(x=31, y=127)

lagoonOverviewButtonFrame= Frame(lagoonSupplyPage, width=90, height=28)
lagoonOverviewButtonFrame.place(x=31, y=127)

lagoonSuppliesButtonFrame= Frame(lagoonFoodStallPage, width=141, height=28)
lagoonSuppliesButtonFrame.place(x=228, y=127)

lagoonSuppliesClickedFrame = Frame (lagoonSupplyPage, width=141, height=28)
lagoonSuppliesClickedFrame.place(x=228, y=127)

lagoonFoodStallButtonFrame = Frame (lagoonSupplyPage, width=91, height=28)
lagoonFoodStallButtonFrame.place(x=129, y=127)

lagoonFoodStallClickedFrame = Frame (lagoonFoodStallPage, width=91, height=28)
lagoonFoodStallClickedFrame.place(x=129, y=127)

lagoonOverviewButtons = Button (lagoonOverviewButtonFrames, image=lagoonOverviewButtonImgPath, command =lagoonsPage, bd=0 , bg = '#FFFFF0', activebackground= "#FFFFF0")
lagoonOverviewButtons.place(x=0, y=0, relheight=1, relwidth=1)  

lagoonOverviewButton = Button (lagoonOverviewButtonFrame, image=lagoonOverviewButtonImgPath, command =lagoonsPage, bd=0 , bg = '#FFFFF0', activebackground= "#FFFFF0")
lagoonOverviewButton.place(x=0, y=0, relheight=1, relwidth=1)  

lagoonSuppliesButton = Button (lagoonSuppliesButtonFrame, image = lagoonSuppliesButtonImgPath, command =lagoonSuppliesPage ,bd=0, bg = '#FFFFF0', activebackground= "#FFFFF0")
lagoonSuppliesButton.place(x=0, y=0, relheight=1, relwidth=1)

lagoonSuppliesClickedButton = Button (lagoonSuppliesClickedFrame, image = lagoonSuppliesButtonClickedImgPath, bd=0, bg = '#FFFFF0', activebackground= "#FFFFF0")
lagoonSuppliesClickedButton.place(x=0, y=0, relheight=1, relwidth=1)

lagoonFoodStallsButton = Button (lagoonFoodStallButtonFrame, image = lagoonFoodStallButtonImgPath,command =lagoonFoodStallsPage, bd=0, bg = '#FFFFF0', activebackground= "#FFFFF0")
lagoonFoodStallsButton.place(x=0, y=0, relheight=1, relwidth=1)

lagoonFoodStallsClickedButton = Button (lagoonFoodStallClickedFrame, image = lagoonFoodStallButtonClickedImgPath, bd=0, bg = '#FFFFF0', activebackground= "#FFFFF0")
lagoonFoodStallsClickedButton.place(x=0, y=0, relheight=1, relwidth=1)


lagoonSupplyFrame = ctk.CTkScrollableFrame(lagoonSupplyPage, width=430, height=567, bg_color='#FFFFF0', fg_color='#FFFFF0', scrollbar_button_color='#550000', scrollbar_button_hover_color='#550000')
lagoonSupplyFrame.place(x=0, y=167)

supplyNames = ["A1", "A2", "A3", "A4", "A5", "A6"]
supplyImagePaths = [lagoonPrintingShopsImgPath, lagoonPrintBestImgPath, lagoonBlessingPrintingImgPath, lagoonRizzImgPath, lagoonCraftImgPath, lagoonMistyImgPath]
supplyFrames = {}
supplyImageContainer = {}


for names in supplyNames:
    row = ord(names[0]) - ord("A")
    col = int(names[1]) - 1
    supplyFrame = ctk.CTkFrame(lagoonSupplyFrame, width=387, height=132, bg_color='#FFFFF0', fg_color='#FFFFF0')
    supplyFrame.pack(pady=(0, 13))
    supplyFrames[row, col] = supplyFrame

                                                    
for i in range(len(supplyNames)): 
    row = ord(supplyNames[i][0]) - ord("A")
    col = int(supplyNames[i][1]) - 1
    supply = Label(supplyFrames[row, col], image=supplyImagePaths[i], bg='#FFFFF0')
    supply.place(x=0, y=0, relwidth=1, relheight=1)
    supplyImageContainer[row, col] = supply



lagoonFoodStallFrame = ctk.CTkScrollableFrame(lagoonFoodStallPage, width=430, height=567, bg_color='#FFFFF0', fg_color='#FFFFF0', scrollbar_button_color='#550000', scrollbar_button_hover_color='#550000')
lagoonFoodStallFrame.place(x=0, y=167)

foodNames = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", 
             "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9",
             "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"]
foodImagePaths = [lagoonPuprenersImgPath, lagoonTrinasImgPath, lagoonMrBrewskoImgPath, lagoonWaffleImgPath,
                  lagoonKoficcinoImgPath, lagoonCuadroImgPath, lagoonGoHealthyImgPath, lagoonFudbookImgPath,
                  lagoonPapritosImgPath, lagoonRewindasImgPath, lagoonPuroysImgPath, lagoonFLavorsofLagoonImgPath,
                  lagoonKeemsImgPath, lagoonVirginShakeImgPath, lagoonLizasImgPath, lagoonJibImgPath,
                  lagoonJToppingsImgPath, lagoonCupOfTeaImgPath, lagoonChickenliciousImgPath, lagoonMireseImgPath,
                  lagoonDavidsCafeImgPath, lagoonDavidsWingsImgPath, lagoonBurgerImgPath, lagoonMamaThessImgPath,
                  lagoonFifthImgPath, lagoonUnivTopBurgerImgPath, lagoonChickenChopImgPath]
foodFrames = {}
foodImageContainer = {}


for names in foodNames:
    row = ord(names[0]) - ord("A")
    col = int(names[1]) - 1
    foodFrame = ctk.CTkFrame(lagoonFoodStallFrame, width=387, height=132, bg_color='#FFFFF0', fg_color='#FFFFF0')
    foodFrame.pack(pady=(0, 13))
    foodFrames[row, col] = foodFrame

                                                    
for i in range(len(foodNames)):  
    row = ord(foodNames[i][0]) - ord("A")
    col = int(foodNames[i][1]) - 1
    food = Label(foodFrames[row, col], image=foodImagePaths[i], bg='#FFFFF0')
    food.place(x=0, y=0, relwidth=1, relheight=1)
    foodImageContainer[row, col] = food

# CATEGORY PAGE
categoryScrollBarFrame =ctk.CTkScrollableFrame(categoryPage, width=394, height=608, fg_color = '#550000', bg_color = '#550000', scrollbar_button_color='#550000', scrollbar_button_hover_color='#5F0F0F')
categoryScrollBarFrame.place(x=22,y=152)

categoryFrameNames = ["A1", "A2", "A3", "A4", "A5", "A6", "A7"]
textImagePaths = [classroomTextImgPath, laboratoriesTextImgPath, facultiesTextImgPath, transactionTextImgPath, 
                  medicalOfficeTextImgPath, eventHallsTextImgPath, comfortRoomsTextImgPath]
laboratoriesImagePaths = [keyboardingLaboratoryImgPath, computerLaboratoryImgPath, scienceLaboratoryImgPath,
                          languageLaboratoryImgPath, stenographyLaboratoryImgPath]
transactionImagePaths = [registrarOfficeImgPath, cashierOfficeImgPath, ourOfficeImgPath, arrsOfficeImgPath,
                         osfOfficeImgPath, shsOfficeImgPath, storageRoomImgPath, recordsOfficeImgPath]
categoryFrames = {}
categoryDropdownFrames = {}
clickedcategoryDropdownFrames = {}
textImageContainer = {}
laboratoriesImageContainer = {}
transactionImageContainer = {}
textImageCol = 0
laboratoriesImageCol = 0
transactionImageCol = 0

for name in categoryFrameNames:
    row = ord(name[0]) - ord("A")
    col = int(name[1]) - 1
    categoryFrame = ctk.CTkFrame(categoryScrollBarFrame, width=390, height=55, corner_radius=15, bg_color='#550000', fg_color='#FFF3F3')
    categoryFrame.pack(pady=(0,13))
    categoryFrames[row,col] = categoryFrame

for imagePath in textImagePaths:
    text =  Label(categoryFrames[0,textImageCol], image=imagePath ,bg= '#FFF3F3' )
    text.place(x=13, y=15)
    textImageContainer[0,textImageCol] = text
    textImageCol += 1
      
for name in categoryFrameNames:
    row = ord(name[0]) - ord("A")
    col = int(name[1]) - 1
    dropdownButton = Button(categoryFrames[row,col], image=dropdownButtonImgPath, bd=0, bg='#FFF3F3', activebackground='#FFF3F3')
    dropdownButton.place(x=346, y=12)
    categoryDropdownFrames[row,col] = dropdownButton
    
for name in categoryFrameNames:
    row = ord(name[0]) - ord("A")
    col = int(name[1]) - 1
    dropdownButton = Button(categoryFrames[row,col], image=clickedDropdownButtonImgPath, bd=0, bg='#FFFFF0', activebackground='#FFFFF0')
    clickedcategoryDropdownFrames[row,col] = dropdownButton 

laboratoriesInsideScrollableFrame = ctk.CTkScrollableFrame(categoryFrames[0,1], width=360, height=120, bg_color='#FFFFF0', fg_color='#FFFFF0', orientation="horizontal", scrollbar_button_color='#550000', scrollbar_button_hover_color='#5F0F0F')
laboratoriesInsideScrollableFrame.place(x=9, y=55)

transactionInsideScrollableFrame = ctk.CTkScrollableFrame(categoryFrames[0,3], width=360, height=120, bg_color='#FFFFF0', fg_color='#FFFFF0', orientation="horizontal", scrollbar_button_color='#550000', scrollbar_button_hover_color='#5F0F0F')
transactionInsideScrollableFrame.place(x=9, y=55)

for imagePath in laboratoriesImagePaths:
    LaboratoryButton = Button(laboratoriesInsideScrollableFrame, image=imagePath, bd=0, bg='#FFFFF0', activebackground='#FFFFF0')
    LaboratoryButton.pack(side=LEFT, padx=(0,12))
    laboratoriesImageContainer[0,laboratoriesImageCol] = LaboratoryButton
    laboratoriesImageCol += 1
    
for imagePath in transactionImagePaths:
    facultiesButton = Button(transactionInsideScrollableFrame, image=imagePath, bd=0, bg='#FFFFF0', activebackground='#FFFFF0')
    facultiesButton.pack(side=LEFT, padx=(0,12))
    transactionImageContainer[0,transactionImageCol] = facultiesButton
    transactionImageCol += 1

eastWingClassroomButton = Button(categoryFrames[0,0], image=eastWingClassroomImgPath, bd=0, command=lambda: eastWingClassroomsPage(eastWingClassroomPage,0), bg='#FFFFF0', activebackground='#FFFFF0')
eastWingClassroomButton.place(x=15 , y=55)

westWingClassroomButton = Button(categoryFrames[0,0], image=westWingClassroomImgPath, bd=0, command=lambda: westWingClassroomsPage(westWingClassroomPage,0), bg='#FFFFF0', activebackground='#FFFFF0')
westWingClassroomButton.place(x=128, y=55)

dentalServicesButton = Button(categoryFrames[0,4], image=dentalServicesImgPath, bd=0, command=lambda: dentalClinicServicesPage(dentalClinicServicePage,0),  bg='#FFFFF0', activebackground='#FFFFF0')
dentalServicesButton.place(x=15 , y=55)

medicalServicesButton = Button(categoryFrames[0,4], image=medicalServicesImgPath, bd=0, command=lambda: medicalClinicServicesPage(medicalClinicServicePage,0),  bg='#FFFFF0', activebackground='#FFFFF0')
medicalServicesButton.place(x=128, y=55)

directorOfficeMedicalButton = Button(categoryFrames[0,4], image=officeOfMedicalImgPath, bd=0, command=lambda: directorOfficeMedicalsPage(directorOfficeMedicalPage,0),  bg='#FFFFF0', activebackground='#FFFFF0')
directorOfficeMedicalButton.place(x=240, y=55)

rectoHallButton = Button(categoryFrames[0,5], image=rectoHallImageImgPath, bd=0, command=lambda: claroRectoRoomsPage(claroRectoRoomPage,0),  bg='#FFFFF0', activebackground='#FFFFF0')
rectoHallButton.place(x=15 , y=55)

accentureRoomButton = Button(categoryFrames[0,5], image=accentureRoomImgPath, bd=0, command=lambda: accentureRoomsPage(accentureRoomPage,0),  bg='#FFFFF0', activebackground='#FFFFF0')
accentureRoomButton.place(x=128, y=55)

audioVisualRoomButton = Button(categoryFrames[0,5], image=audioVisualRoomImgPath, command=lambda: audioVisualRoomsPage(audioVisualRoomPage,0),  bd=0, bg='#FFFFF0', activebackground='#FFFFF0')
audioVisualRoomButton.place(x=240, y=55)

comfortRoomsButton = Button(categoryFrames[0,6], image=comfortRoomsImgPath, bd=0, command=lambda: overviewComfortRoomsPage(overviewComfortRoomPage,0),  bg='#FFFFF0', activebackground='#FFFFF0')
comfortRoomsButton.place(x=15, y=55)

eastWingFacultiesButton = Button(categoryFrames[0,2], image=eastWingFacultiesImgPath, command=lambda: eastFacultiesPaging(0), bd=0, bg='#FFFFF0', activebackground='#FFFFF0')
eastWingFacultiesButton.place(x=14 , y=55)

westWingFacultiesButton = Button(categoryFrames[0,2], image=westWingFacultiesImgPath, bd=0,  command=lambda: westFacultiesPaging(0), bg='#FFFFF0', activebackground='#FFFFF0')
westWingFacultiesButton.place(x=127, y=55)

southWingFacultiesButton = Button(categoryFrames[0,2], image=southWingFacultiesImgPath, bd=0, command=lambda: southFacultiesPaging(0), bg='#FFFFF0', activebackground='#FFFFF0')
southWingFacultiesButton.place(x=240, y=55)


categoryDropdownFrames[0,0].configure(command=lambda: clickedCategory(0,0))
categoryDropdownFrames[0,1].configure(command=lambda: clickedCategory(0,1))
categoryDropdownFrames[0,2].configure(command=lambda: clickedCategory(0,2))
categoryDropdownFrames[0,3].configure(command=lambda: clickedCategory(0,3))
categoryDropdownFrames[0,4].configure(command=lambda: clickedCategory(0,4))
categoryDropdownFrames[0,5].configure(command=lambda: clickedCategory(0,5))
categoryDropdownFrames[0,6].configure(command=lambda: clickedCategory(0,6))

clickedcategoryDropdownFrames[0,0].configure(command=lambda: closedClickedCategory(0,0))
clickedcategoryDropdownFrames[0,1].configure(command=lambda: closedClickedCategory(0,1))
clickedcategoryDropdownFrames[0,2].configure(command=lambda: closedClickedCategory(0,2))
clickedcategoryDropdownFrames[0,3].configure(command=lambda: closedClickedCategory(0,3))
clickedcategoryDropdownFrames[0,4].configure(command=lambda: closedClickedCategory(0,4))
clickedcategoryDropdownFrames[0,5].configure(command=lambda: closedClickedCategory(0,5))
clickedcategoryDropdownFrames[0,6].configure(command=lambda: closedClickedCategory(0,6))

categoryDiscoverFrame = Frame(categoryScrollBarFrame, width=390, height=128, bg='#550000',)
categoryDiscoverFrame.pack(pady=(0,13))

discoverText = Label(categoryDiscoverFrame, image=discoverTextImgPath, bg= '#550000')
discoverText.place(x=0, y=0)

viewMainWingButton = Button(categoryDiscoverFrame, image=viewMainWingImgPath, command = discoversEastPage, bd=0, bg='#550000', activebackground='#550000')
viewMainWingButton.place(x=332, y=10)

eastWingCategoryButton = Button(categoryDiscoverFrame, image=eastWingCategoryImgpath, command = discoversEastPage ,bd=0, bg='#550000', activebackground='#550000')
eastWingCategoryButton.place(x=0, y=33)

westWingCategoryButton = Button(categoryDiscoverFrame, image=westWingCategoryImgPath, command = discoversWestPage, bd=0, bg='#550000', activebackground='#550000')
westWingCategoryButton.place(x=135, y=33)

southWingCategoryButton = Button(categoryDiscoverFrame, image=southWingCategoryImgPath, command= discoversSouthPage, bd=0, bg='#550000', activebackground='#550000')
southWingCategoryButton.place(x=270, y=33)   


# EAST WING CLASSROM PAGE
eastWingClassroomScrollBarFrame =ctk.CTkScrollableFrame(eastWingClassroomPage, width=387, height=392, fg_color = '#550000', bg_color = '#550000', scrollbar_button_color='#550000', scrollbar_button_hover_color='#5F0F0F')
eastWingClassroomScrollBarFrame.place(x=31,y=378)

eastWingClassroomFrameNames = ["A1", "A2", "A3", "A4"]
eastWingClassroomBigPaths = [eastClassroom2ndFloorImgPath, eastClassroom3rdFloorImgPath, eastClassroom4thFloorImgPath, eastClassroom5thFloorImgPath]
eastWingClassroomSmallPaths = [secondFloorEastClassroomImgPath, thirdFloorEastClassroomImgPath, fourthFloorEastClassroomImgPath, fifthFloorEastClassroomImgPath]
eastWingClassroomFrame = {}
eastWingContainerLabel = {}
eastWingDropdownButton = {}
eastWingClickedDropdownButton = {}

for name in eastWingClassroomFrameNames:
    row = ord(name[0]) - ord("A")
    col = int(name[1]) - 1
    eastWingClassroom = ctk.CTkFrame(eastWingClassroomScrollBarFrame, width=390, height=55, corner_radius=15, bg_color='#550000', fg_color='#FFF3F3')
    eastWingClassroom.pack(pady=(0,13))
    eastWingClassroomFrame[row,col] = eastWingClassroom

for i in range(len(eastWingClassroomFrameNames)):
    row = ord(eastWingClassroomFrameNames[i][0]) - ord("A")
    col = int(eastWingClassroomFrameNames[i][1]) - 1
    eastWingClassroom = Label(eastWingClassroomFrame[row, col], image=eastWingClassroomSmallPaths[i], bg='#550000')
    eastWingClassroom.place(x=0, y=0, relwidth=1, relheight=1)
    eastWingContainerLabel[row, col] = eastWingClassroom
    
for name in eastWingClassroomFrameNames:
    row = ord(name[0]) - ord("A")
    col = int(name[1]) - 1
    dropdownButton = Button(eastWingClassroomFrame[row,col], image=dropdownButtonImgPath, bd=0, bg='#FFF3F3', activebackground='#FFF3F3')
    dropdownButton.place(x=351, y=13)
    eastWingDropdownButton[row,col] = dropdownButton
    
for name in eastWingClassroomFrameNames:
    row = ord(name[0]) - ord("A")
    col = int(name[1]) - 1
    dropdownButton = Button(eastWingClassroomFrame[row,col], image=clickedDropdownButtonImgPath, bd=0, bg='#FFFFF0', activebackground='#FFFFF0')
    eastWingClickedDropdownButton[row,col] = dropdownButton 

eastWingDropdownButton[0,0].configure(command=lambda: clickedeastWingClassroom(0,0))
eastWingDropdownButton[0,1].configure(command=lambda: clickedeastWingClassroom(0,1))
eastWingDropdownButton[0,2].configure(command=lambda: clickedeastWingClassroom(0,2))
eastWingDropdownButton[0,3].configure(command=lambda: clickedeastWingClassroom(0,3))

eastWingClickedDropdownButton[0,0].configure(command=lambda: closedClickedeastWingClassroom(0,0))
eastWingClickedDropdownButton[0,1].configure(command=lambda: closedClickedeastWingClassroom(0,1))
eastWingClickedDropdownButton[0,2].configure(command=lambda: closedClickedeastWingClassroom(0,2))
eastWingClickedDropdownButton[0,3].configure(command=lambda: closedClickedeastWingClassroom(0,3))

# WEST WING CLASSROM PAGE
westWingClassroomScrollBarFrame =ctk.CTkScrollableFrame(westWingClassroomPage, width=387, height=392, fg_color = '#550000', bg_color = '#550000', scrollbar_button_color='#550000', scrollbar_button_hover_color='#5F0F0F')
westWingClassroomScrollBarFrame.place(x=31,y=378)

westWingClassroomFrameNames = ["A1", "A2", "A3", "A4", "A5"]
westWingClassroomBigPaths = [westClassroom2ndFloorImgPath, westClassroom3rdFloorImgPath, westClassroom4thFloorImgPath, westClassroom5thFloorImgPath, westClassroom6thFloorImgPath]
westWingClassroomSmallPaths = [secondFloorWestClassroomImgPath, thirdFloorWestClassroomImgPath, fourthFloorWestClassroomImgPath, fifthFloorWestClassroomImgPath, sixthFloorWestClassroomImgPath]
westWingClassroomFrame = {}
westWingContainerLabel = {}
westWingDropdownButton = {}
westWingClickedDropdownButton = {}

for name in westWingClassroomFrameNames:
    row = ord(name[0]) - ord("A")
    col = int(name[1]) - 1
    westWingClassroom = ctk.CTkFrame(westWingClassroomScrollBarFrame, width=390, height=55, corner_radius=15, bg_color='#550000', fg_color='#FFF3F3')
    westWingClassroom.pack(pady=(0,13))
    westWingClassroomFrame[row,col] = westWingClassroom

for i in range(len(westWingClassroomFrameNames)): 
    row = ord(westWingClassroomFrameNames[i][0]) - ord("A")
    col = int(westWingClassroomFrameNames[i][1]) - 1
    westWingClassroom = Label(westWingClassroomFrame[row, col], image=westWingClassroomSmallPaths[i], bg='#550000')
    westWingClassroom.place(x=0, y=0, relwidth=1, relheight=1)
    westWingContainerLabel[row, col] = westWingClassroom
    
for name in westWingClassroomFrameNames:
    row = ord(name[0]) - ord("A")
    col = int(name[1]) - 1
    dropdownButton = Button(westWingClassroomFrame[row,col], image=dropdownButtonImgPath, bd=0, bg='#FFF3F3', activebackground='#FFF3F3')
    dropdownButton.place(x=351, y=13)
    westWingDropdownButton[row,col] = dropdownButton
    
for name in westWingClassroomFrameNames:
    row = ord(name[0]) - ord("A")
    col = int(name[1]) - 1
    dropdownButton = Button(westWingClassroomFrame[row,col], image=clickedDropdownButtonImgPath, bd=0, bg='#FFFFF0', activebackground='#FFFFF0')
    westWingClickedDropdownButton[row,col] = dropdownButton 

westWingDropdownButton[0,0].configure(command=lambda: clickedWestWingClassroom(0,0))
westWingDropdownButton[0,1].configure(command=lambda: clickedWestWingClassroom(0,1))
westWingDropdownButton[0,2].configure(command=lambda: clickedWestWingClassroom(0,2))
westWingDropdownButton[0,3].configure(command=lambda: clickedWestWingClassroom(0,3))
westWingDropdownButton[0,4].configure(command=lambda: clickedWestWingClassroom(0,4))

westWingClickedDropdownButton[0,0].configure(command=lambda: closedClickedWestWingClassroom(0,0))
westWingClickedDropdownButton[0,1].configure(command=lambda: closedClickedWestWingClassroom(0,1))
westWingClickedDropdownButton[0,2].configure(command=lambda: closedClickedWestWingClassroom(0,2))
westWingClickedDropdownButton[0,3].configure(command=lambda: closedClickedWestWingClassroom(0,3))
westWingClickedDropdownButton[0,4].configure(command=lambda: closedClickedWestWingClassroom(0,4))

# LABORATORIES PAGES
laboratoriesImageContainer[0,0].configure(command=lambda: keyboardingLaboratoriesPage(keyboardingLaboratoryPage,0))
laboratoriesImageContainer[0,1].configure(command=lambda: computerLaboratoriesPage(computerLaboratoryPage,0))
laboratoriesImageContainer[0,2].configure(command=lambda: stenographyLaboratoriesPage(stenographyLaboratoryPage,0))
laboratoriesImageContainer[0,3].configure(command=lambda: languageLaboratoriesPage(languageLaboratoryPage,0))
laboratoriesImageContainer[0,4].configure(command=lambda: scienceLaboratoriesPage(scienceLaboratoryPage,0))

# TRANSACTION PAGES
viewRegistratCounterButton = Button(registrarOfficePage, image=viewRegistratCounterImgPath, bd=0, command=lambda:registrarListPage(registrarOfficeListPage,9), bg='#800E13', activebackground='#800E13')
viewRegistratCounterButton.place(x=243, y=721)
viewCashierCounterButton = Button(cashierOfficePage, image=viewCashierCounterImgPath, bd=0, command=lambda:cashierListPage(cashierOfficeListPage,10), bg='#800E13', activebackground='#800E13')
viewCashierCounterButton.place(x=242, y=723)

transactionImageContainer[0,0].configure(command=lambda:registrarPage(registrarOfficePage,0))
transactionImageContainer[0,1].configure(command=lambda:cashiersOfficePage(cashierOfficePage,0))
transactionImageContainer[0,2].configure(command=lambda:registrarsRecordsPage(registrarRecordsPage,0))
transactionImageContainer[0,3].configure(command=lambda:admissionPage(admissionRegistrationPage,0))
transactionImageContainer[0,4].configure(command=lambda:scholarshipPage(scholarshipAssistancePage,0))
transactionImageContainer[0,5].configure(command=lambda:shsDepartmentsPage(shsDepartmentPage,0))




# COMFORT ROOM PAGES
comfortRoomScrollableFrameNames = ["A1", "A2", "A3", "A4", "A5"]
comfortRoomPagesPath = [overviewComfortRoomPage, eastComfortRoomPage, westComfortRoomPage, southComfortRoomPage, lagoonComfortRoomPage]
comfortRoomActiveTabPaths = [activeOverviewTab, activeEastWingTab, activeWestWingTab, activeSouthWingTab, activeLagoonTab]
comfortRoomIdleTabPaths = [idleOverviewTab, idleEastWingTab, idleWestWingTab, idleSouthWingTab, idleLagoonTab]


comfortRoomCommandPaths1 = [lambda:overviewComfortRoomsPage(overviewComfortRoomPage,0),lambda: eastComfortRoomsPage(eastComfortRoomPage,1),lambda: westComfortRoomsPage(westComfortRoomPage,2),lambda: southComfortRoomsPage(southComfortRoomPage,3),lambda: lagoonComfortRoomsPage(lagoonComfortRoomPage,0)]
comfortRoomScrollableFrames = {}
overviewComfortRoomButtons = {}
eastComfortRoomButtons = {}
westComfortRoomButtons = {}
southComfortRoomButtons = {}
lagoonComfortRoomButtons = {}

for name in comfortRoomScrollableFrameNames:
    row = ord(name[0]) - ord("A")
    col = int(name[1]) - 1
    comfortRoomScrollableFrame =ctk.CTkScrollableFrame(comfortRoomPagesPath[col], width=398, height=130, fg_color = '#FFFFF0', bg_color = '#FFFFF0', scrollbar_button_color='#550000', scrollbar_button_hover_color='#5F0F0F', orientation='horizontal')
    comfortRoomScrollableFrame.place(x=27,y=137)
    comfortRoomScrollableFrames[row,col] = comfortRoomScrollableFrame

for name in comfortRoomScrollableFrameNames:
    
    
    
    
    row = ord(name[0]) - ord("A")
    col = int(name[1]) - 1
    if col == 0:
        activeButton = Button(comfortRoomScrollableFrames[0,0], image=comfortRoomActiveTabPaths[col], bd=0, bg='#FFFFF0', activebackground='#FFFFF0')
        activeButton.pack(side=LEFT,padx=(0,17))
        overviewComfortRoomButtons[row,col] = activeButton
    else:
        idleButton = Button(comfortRoomScrollableFrames[0,0], image=comfortRoomIdleTabPaths[col], bd=0, command=comfortRoomCommandPaths1[col] , bg='#FFFFF0', activebackground='#FFFFF0')
        idleButton.pack(side=LEFT,padx=(0,17))
        overviewComfortRoomButtons[row,col] = idleButton
        
    if col == 1:
        activeButton = Button(comfortRoomScrollableFrames[0,1], image=comfortRoomActiveTabPaths[col], bd=0, bg='#FFFFF0', activebackground='#FFFFF0')
        activeButton.pack(side=LEFT,padx=(0,17))
        eastComfortRoomButtons[row,col] = activeButton
    else:
        idleButton = Button(comfortRoomScrollableFrames[0,1], image=comfortRoomIdleTabPaths[col], bd=0, command=comfortRoomCommandPaths1[col] , bg='#FFFFF0', activebackground='#FFFFF0')
        idleButton.pack(side=LEFT,padx=(0,17))
        eastComfortRoomButtons[row,col] = idleButton
        
    if col == 2:
        activeButton = Button(comfortRoomScrollableFrames[0,2], image=comfortRoomActiveTabPaths[col], bd=0, bg='#FFFFF0', activebackground='#FFFFF0')
        activeButton.pack(side=LEFT,padx=(0,17))
        westComfortRoomButtons[row,col] = activeButton
    else:
        idleButton = Button(comfortRoomScrollableFrames[0,2], image=comfortRoomIdleTabPaths[col], bd=0, command=comfortRoomCommandPaths1[col] , bg='#FFFFF0', activebackground='#FFFFF0')
        idleButton.pack(side=LEFT,padx=(0,17))
        westComfortRoomButtons[row,col] = idleButton
        
    if col == 3:
        activeButton = Button(comfortRoomScrollableFrames[0,3], image=comfortRoomActiveTabPaths[col], bd=0, bg='#FFFFF0', activebackground='#FFFFF0')
        activeButton.pack(side=LEFT,padx=(0,17))
        southComfortRoomButtons[row,col] = activeButton
    else:
        idleButton = Button(comfortRoomScrollableFrames[0,3], image=comfortRoomIdleTabPaths[col], bd=0, command=comfortRoomCommandPaths1[col] , bg='#FFFFF0', activebackground='#FFFFF0')
        idleButton.pack(side=LEFT,padx=(0,17))
        southComfortRoomButtons[row,col] = idleButton
        
    if col == 4:
        activeButton = Button(comfortRoomScrollableFrames[0,4], image=comfortRoomActiveTabPaths[col], bd=0, bg='#FFFFF0', activebackground='#FFFFF0')
        activeButton.pack(side=LEFT,padx=(0,17))
        lagoonComfortRoomButtons[row,col] = activeButton
    else:
        idleButton = Button(comfortRoomScrollableFrames[0,4], image=comfortRoomIdleTabPaths[col], bd=0, command=comfortRoomCommandPaths1[col] , bg='#FFFFF0', activebackground='#FFFFF0')
        idleButton.pack(side=LEFT,padx=(0,17))
        lagoonComfortRoomButtons[row,col] = idleButton



# EAST FACULTIES PAGE
eastFacultyPageFrameNames = [eastFacultiesPage, mpcPage, rotcPage, hrdPage, odPage, fmoPage, dscoPage
                  , ccPage, dcsdPage, postBaccPage, nstpPage, cssdPage]
eastFacultyPageImagePath = [eastFacultiesPageImgPath, mpcPageImgPath, rotcPageImgPath, hrdPageImgPath, odPageImgPath,
                            fmoPageImgPath, dscoPageImgPath, ccPageImgPath, dcsdPageImgPath, postBaccPageImgPath,
                            nstpPageImgPath, cssdPageImgPath]
eastFacultyButtonPath = [mpcButtonImgPath, rotcButtonImgPath, hrdButtonImgPath, odButtonImgPath,
                            fmoButtonImgPath, dscoButtonImgPath, ccButtonImgPath, dcsdButtonImgPath, postBaccButtonImgPath,
                            nstpButtonImgPath, cssdButtonImgPath]
eastFacultyPageImageLabels = {}
eastFacultyPageButtons = {}
eastFacultyReturnSearchButtons = {}

for i in range(len(eastFacultyPageFrameNames)): 
    pageLabels = Label(eastFacultyPageFrameNames[i], image=eastFacultyPageImagePath[i])
    pageLabels.place(x=0, y=0, relwidth=1, relheight=1)
    eastFacultyPageImageLabels[0, i] = pageLabels
    
eastFacultyScrollBarFrame =ctk.CTkScrollableFrame(eastFacultiesPage, width=390, height=510, fg_color = '#FFEDED', bg_color = '#FFEDED', scrollbar_button_color='#550000', scrollbar_button_hover_color='#5F0F0F')
eastFacultyScrollBarFrame.place(x=28,y=157)


for i in range(len(eastFacultyButtonPath)):
    
    eastFacultyButtons = Button(eastFacultyScrollBarFrame, image=eastFacultyButtonPath[i], bd=0, command=lambda i=i+1: eastFacultiesPaging(i), bg='#FFEDED', activebackground='#FFEDED')
    eastFacultyButtons.pack(pady=(0,17))
    eastFacultyPageButtons[0,i] = eastFacultyButtons



for i in range(len(eastFacultyPageFrameNames)):
    if i == 0:
        eastFacultyReturnSearch = returnSearchSpecific(eastFacultiesPage,0)
        eastFacultyReturnSearchButtons[0,i] = eastFacultyReturnSearch 
    else:
        eastFacultyReturnSearch = returnSearchCategory(eastFacultyPageFrameNames[i],5)
        eastFacultyReturnSearchButtons[0,i] = eastFacultyReturnSearch



# WEST FACULTIES PAGE
westFacultyPageFrameNames = [westFacultiesPage, driPage, coaPage, coePage, cbaPage, cosPage]
westFacultyPageImagePath = [westFacultiesPageImgPath, driPageImgPath, coaPageImgPath, coePageImgPath, cbaPageImgPath, cosPageImgPath]
westFacultyButtonPath = [driButtonImgPath , shsButtonImgPath, coaButtonImgPath, coeButtonImgPath, cbaButtonImgPath, cosButtonImgPath]
westFacultyPageImageLabels = {}
westFacultyPageButtons = {}
westFacultyReturnSearchButtons = {}

for i in range(len(westFacultyPageFrameNames)): 
    pageLabels = Label(westFacultyPageFrameNames[i], image=westFacultyPageImagePath[i])
    pageLabels.place(x=0, y=0, relwidth=1, relheight=1)
    westFacultyPageImageLabels[0, i] = pageLabels
    
westFacultyScrollBarFrame =ctk.CTkScrollableFrame(westFacultiesPage, width=390, height=510, fg_color = '#FFEDED', bg_color = '#FFEDED', scrollbar_button_color='#550000', scrollbar_button_hover_color='#5F0F0F')
westFacultyScrollBarFrame.place(x=28,y=157)

for i in range(len(westFacultyButtonPath)): 
    westFacultyButtons = Button(westFacultyScrollBarFrame, image=westFacultyButtonPath[i], bd=0, command=lambda i=i+1: westFacultiesPaging(i) , bg='#FFEDED', activebackground='#FFEDED')
    westFacultyButtons.pack(pady=(0,17))
    westFacultyPageButtons[0,i] = westFacultyButtons


for i in range(len(westFacultyPageFrameNames)):
    if i == 0:
        westFacultyReturnSearch = returnSearchSpecific(westFacultiesPage,1)
        westFacultyReturnSearchButtons[0,i] = westFacultyReturnSearch 
    else:
        westFacultyReturnSearch = returnSearchCategory(westFacultyPageFrameNames[i],6)
        westFacultyReturnSearchButtons[0,i] = westFacultyReturnSearch

# SOUTH FACULTIES PAGE
southFacultyPageFrameNames = [southFacultiesPage, sNOCPage, sOVPPage, sConfRoomPage, sOPPage, sOUBPage, 
                              sSPPOPage, sPFOPage, sOIAPage, sHRMDPage, sULOPage,
                              sGSOPage, sPOPage, sPMOBACPage, sIIMSPage, sLLSPage,
                              sISTRPage, sGDOPage, sSRPage, sERMOPage, sCCISOFRPage,
                              sDOMSPage, sCOSFRPage, sCAFPage, sODPage, sCPSPAPage, 
                              sCOEDPage, sCBAPage, sCSSDPage, sOCPSPage, sIDSAPage]

southFacultyPageImagePath = [southFacBgImgPath, southFacNOCBgImgPath, southFacOVPBgImgPath, southFacConfRoomBgImgPath, southFacOPBgImgPath, southFacOUBBgImgPath,
                             southFacSPPOBgImgPath, southFacPFOBgImgPath, southFacOIABgImgPath, southFacHRMDBgImgPath, southFacULOBgImgPath, 
                             southFacGSOBgImgPath, southFacPOBgImgPath, southFacPMOBACBgImgPath, southFacIIMSBgImgPath, southFacLLSBgImgPath, 
                             southFacISTRBgImgPath, southFacGDOBgImgPath, southFacSRBgImgPath, southFacERMOBgImgPath, southFacCCISOFRBgImgPath, 
                             southFacDOMSBgImgPath, southFacCOSFRBgImgPath, southFacCAFBgImgPath, southFacODBgImgPath, southFacCPSPABgImgPath, 
                             southFacCOEDBgImgPath, southFacCBABgImgPath, southFacCSSDBgImgPath, southFacOCPSBgImgPath, southFacIDSABgImgPath]

southFacultyButtonPath = [southFacNOCTabImgPath, southFacOVPTabImgPath, southFacConfRoomTabImgPath, southFacOPTabImgPath, southFacOUBTabImgPath,
                          southFacSPPOTabImgPath, southFacPFOTabImgPath, southFacOIATabImgPath, southFacHRMDTabImgPath, southFacULOTabImgPath, 
                          southFacGSOTabImgPath, southFacPOTabImgPath, southFacPMOBACTabImgPath, southFacIIMSTabImgPath, southFacLLSTabImgPath,
                          southFacISTRTabImgPath, southFacGDOTabImgPath, southFacSRTabImgPath, southFacERMOTabImgPath, southFacCCISOFRTabImgPath, 
                          southFacDOMSTabImgPath, southFacCOSFRTabImgPath, southFacCAFTabImgPath, southFacODTabImgPath,southFacCPSPATabImgPath,
                          southFacCOEDTabImgPath, southFacCBATabImgPath, southFacCSSDTabImgPath, southFacOCPSTabImgPath, southFacIDSATabImgPath]
southFacultyPageImageLabels = {}
southFacultyPageButtons = {}
southFacultyReturnSearchButtons = {}

for i in range(len(southFacultyPageFrameNames)): 
    pageLabels = Label(southFacultyPageFrameNames[i], image=southFacultyPageImagePath[i])
    pageLabels.place(x=0, y=0, relwidth=1, relheight=1)
    southFacultyPageImageLabels[0, i] = pageLabels
    
southFacultyScrollBarFrame =ctk.CTkScrollableFrame(southFacultiesPage, width=390, height=510, fg_color = '#FFEDED', bg_color = '#FFEDED', scrollbar_button_color='#550000', scrollbar_button_hover_color='#5F0F0F')
southFacultyScrollBarFrame.place(x=28,y=157)

for i in range(len(southFacultyButtonPath)): 
    southFacultyButtons = Button(southFacultyScrollBarFrame, image=southFacultyButtonPath[i], bd=0, command=lambda i=i+1: southFacultiesPaging(i) , bg='#FFEDED', activebackground='#FFEDED')
    southFacultyButtons.pack(pady=(0,17))
    southFacultyPageButtons[0,i] = southFacultyButtons


for i in range(len(southFacultyPageFrameNames)):
    if i == 0:
        southFacultyReturnSearch = returnSearchSpecific(southFacultiesPage,2)
        southFacultyReturnSearchButtons[0,i] = southFacultyReturnSearch 
    else:
        southFacultyReturnSearch = returnSearchCategory(southFacultyPageFrameNames[i],7)
        southFacultyReturnSearchButtons[0,i] = southFacultyReturnSearch

#EAST DISCOVER PAGE
eastButtonFrame = Frame(discoverEastPage, width=384, height=28, bg='#550000')
eastButtonFrame.place(x=25, y=83)

eButtonNames = ["A1", "A2", "A3", "A4"]
eButtonFrames = {}
for names in eButtonNames:
    row = ord(names[0]) - ord("A")
    col = int(names[1]) - 1
    eButtonFrame = ctk.CTkFrame(eastButtonFrame, width=90, height=28, bg_color="#550000", fg_color="#550000")
    eButtonFrame.pack(padx=(8, 0), pady=(5, 0), side=LEFT)
    eButtonFrames[row, col] = eButtonFrame

eMPButton = Button (eButtonFrames[0,0], image=discoverMainPageButtonImgPath, command = categoriesPage,  bd=0, activebackground= "#550000")
eMPButton.place(x=0, y=0, relheight=1, relwidth=1)  

eEWButton = Button (eButtonFrames[0,1], image=discoverEastClickedImgPath, bd=0, activebackground= "#550000")
eEWButton.place(x=0, y=0, relheight=1, relwidth=1)  

eWWButton = Button (eButtonFrames[0,2], image=discoverWestButtonImgPath, command = discoversWestPage,  bd=0, activebackground= "#550000")
eWWButton.place(x=0, y=0, relheight=1, relwidth=1)  

eSWButton = Button (eButtonFrames[0,3], image=discoverSouthButtonImgPath, command = discoversSouthPage,  bd=0, activebackground= "#550000")
eSWButton.place(x=0, y=0, relheight=1, relwidth=1)  

#EAST DISCOVER BUTTONS
discoverEastFrame = ctk.CTkScrollableFrame(discoverEastPage, width=423, height=665, bg_color='#550000', fg_color='#550000', scrollbar_button_color='#FFFFF0', scrollbar_button_hover_color='#FFFFF0')
discoverEastFrame.place(x=10, y=119)

eastNames = ["A1", "A2", "A3", "A4", "A5", "A6"]
eastFrames = {}

for names in eastNames:
    row = ord(names[0]) - ord("A")
    col = int(names[1]) - 1
    eastFrame = ctk.CTkFrame(discoverEastFrame, width=391, height=144, bg_color="#550000", fg_color="#550000")
    eastFrame.pack(pady=(0, 13))
    eastFrames[row, col] = eastFrame                            

eastLecRoomButton = Button (eastFrames[0,0], image =discoverEastLecRoomImgPath, bd=0, command=lambda: eastWingClassroomsPage(eastWingClassroomPage,1), activebackground= "#550000")
eastLecRoomButton.place(x=0, y=0, relwidth=1, relheight=1)

eastFacultiesButton = Button(eastFrames[0,1], image =discoverEastFacultiesImgPath, command= lambda: eastFacultiesPaging(0), bd=0, activebackground= "#550000")
eastFacultiesButton.place(x=0, y=0, relwidth=1, relheight=1)

eastEventHallButton = Button (eastFrames[0,2], image =discoverEastEventHallImgPath, command=lambda: eastEventHallsPage(eastEventHallPage,0) ,bd=0, activebackground= "#550000") 
eastEventHallButton.place(x=0, y=0, relwidth=1, relheight=1)

eastMedOfficesButton = Button (eastFrames[0,3], image = discoverEastMedOfficesImgPath, command =lambda: eastMedOfficesPage(eastMedOfficePage,0), bd=0, activebackground= "#550000")
eastMedOfficesButton.place(x=0, y=0, relwidth=1, relheight=1)

eastLabsButton = Button (eastFrames[0,4], image = discoverEastLabsImgPath, command=lambda: eastLabsPage(eastLabPage,0), bd=0, activebackground= "#550000")
eastLabsButton.place(x=0, y=0, relwidth=1, relheight=1)

eastCRButton = Button (eastFrames[0,5], image = discoverEastCrImgPath, bd=0, command=lambda: eastComfortRoomsPage(eastComfortRoomPage,1), activebackground= "#550000") #RESERVED COMMAND
eastCRButton.place(x=0, y=0, relwidth=1, relheight=1)

# EAST LABORATORIES 
eastLabsScrollBarFrame =ctk.CTkScrollableFrame(eastLabPage, width=390, height=510, fg_color = '#FFEDED', bg_color = '#FFEDED', scrollbar_button_color='#550000', scrollbar_button_hover_color='#5F0F0F')
eastLabsScrollBarFrame.place(x=28,y=157)

eastCompLabButton = Button(eastLabsScrollBarFrame, image=eastLabCompLabTabImgPath,command=lambda: computerLaboratoriesPage(computerLaboratoryPage,3), bd=0, bg='#FFEDED', activebackground='#FFEDED')#RESERVD COMMAND
eastCompLabButton.pack(pady=(0,17))

eastStenoLabButton = Button(eastLabsScrollBarFrame, image=eastLabStenoLabTabImgPath, bd=0, command=lambda: stenographyLaboratoriesPage(stenographyLaboratoryPage,3), bg='#FFEDED', activebackground='#FFEDED')#RESERVD COMMAND
eastStenoLabButton.pack(pady=(0,17))

eastScienceLabButton = Button(eastLabsScrollBarFrame, image=eastLabScienceLabTabImgPath, command=lambda: scienceLaboratoriesPage(scienceLaboratoryPage,3), bd=0, bg='#FFEDED', activebackground='#FFEDED')#RESERVD COMMAND
eastScienceLabButton.pack(pady=(0,17))

# EAST MED OFFICES 
eastMedScrollBarFrame =ctk.CTkScrollableFrame(eastMedOfficePage, width=390, height=510, fg_color = '#FFEDED', bg_color = '#FFEDED', scrollbar_button_color='#550000', scrollbar_button_hover_color='#5F0F0F')
eastMedScrollBarFrame.place(x=28,y=157)

eastODButton = Button(eastMedScrollBarFrame, image=eastODMedHealthTabImgPath, bd=0,  command= lambda :directorOfficeMedicalsPage (directorOfficeMedicalPage, 0), bg='#FFEDED', activebackground='#FFEDED')#RESERVD COMMAND
eastODButton.pack(pady=(0,17))

eastMedClinicButton = Button(eastMedScrollBarFrame, image=eastMedClinicTabImgPath,  command= lambda :medicalClinicServicesPage(medicalClinicServicePage, 0), bd=0, bg='#FFEDED', activebackground='#FFEDED')#RESERVD COMMAND
eastMedClinicButton.pack(pady=(0,17))

eastDentalButton = Button(eastMedScrollBarFrame, image=eastDentalClinicTabImgPath,  command= lambda :dentalClinicServicesPage(dentalClinicServicePage, 0), bd=0, bg='#FFEDED', activebackground='#FFEDED')#RESERVD COMMAND
eastDentalButton.pack(pady=(0,17))

# EAST EVENT HALLS
eastEventHallScrollBarFrame =ctk.CTkScrollableFrame(eastEventHallPage, width=390, height=510, fg_color = '#FFEDED', bg_color = '#FFEDED', scrollbar_button_color='#550000', scrollbar_button_hover_color='#5F0F0F')
eastEventHallScrollBarFrame.place(x=28,y=157)

eastAudioVisButton = Button(eastEventHallScrollBarFrame, image=eastEventHallAudioVisTabImgPath, bd=0,  command= lambda: audioVisualRoomsPage (audioVisualRoomPage, 0),  bg='#FFEDED', activebackground='#FFEDED')#RESERVD COMMAND
eastAudioVisButton.pack(pady=(0,17))    

eastAccentureButton = Button(eastEventHallScrollBarFrame, image=eastEventHallAccentureTabImgPath, bd=0,  command=  lambda:accentureRoomsPage (accentureRoomPage, 0), bg='#FFEDED', activebackground='#FFEDED')#RESERVD COMMAND
eastAccentureButton.pack(pady=(0,17))



#WEST DISCOVER PAGE
westButtonFrame = Frame(discoverWestPage, width=384, height=28, bg='#550000')
westButtonFrame.place(x=25, y=83)

wButtonNames = ["A1", "A2", "A3", "A4"]
wButtonFrames = {}
for names in wButtonNames:
    row = ord(names[0]) - ord("A")
    col = int(names[1]) - 1
    wButtonFrame = ctk.CTkFrame(westButtonFrame, width=90, height=28, bg_color="#550000", fg_color="#550000")
    wButtonFrame.pack(padx=(8, 0), pady=(5, 0), side=LEFT)
    wButtonFrames[row, col] = wButtonFrame

wMPButton = Button (wButtonFrames[0,0], image=discoverMainPageButtonImgPath, command = categoriesPage,  bd=0, activebackground= "#550000")
wMPButton.place(x=0, y=0, relheight=1, relwidth=1)  

wEWButton = Button (wButtonFrames[0,1], image=discoverEastButtonImgPath,  command = discoversEastPage, bd=0, activebackground= "#550000")
wEWButton.place(x=0, y=0, relheight=1, relwidth=1)  

wWWButton = Button (wButtonFrames[0,2], image=discoverWestClickedImgPath, bd=0, activebackground= "#550000")
wWWButton.place(x=0, y=0, relheight=1, relwidth=1)  

wSWButton = Button (wButtonFrames[0,3], image=discoverSouthButtonImgPath, command = discoversSouthPage,  bd=0, activebackground= "#550000")
wSWButton.place(x=0, y=0, relheight=1, relwidth=1)  

#DISCOVER WEST BUTTONS
discoverWestFrame = ctk.CTkScrollableFrame(discoverWestPage, width=423, height=665, bg_color='#550000', fg_color='#550000', scrollbar_button_color='#FFFFF0', scrollbar_button_hover_color='#FFFFF0')
discoverWestFrame.place(x=14, y=119)

westNames = ["A1", "A2", "A3", "A4", "A5"]
westFrames = {}

for names in westNames:
    row = ord(names[0]) - ord("A")
    col = int(names[1]) - 1
    westFrame = ctk.CTkFrame(discoverWestFrame, width=391, height=144,bg_color="#550000", fg_color="#550000")
    westFrame.pack(pady=(0, 13))
    westFrames[row, col] = westFrame

westClassroomButton = Button (westFrames[0,0], image = discoverWestClassroomsImgPath,  command=lambda: westWingClassroomsPage(westWingClassroomPage,2), bd=0, activebackground= "#550000") #RESERVD COMMAND
westClassroomButton.place(x=0, y=0, relwidth=1, relheight=1)

westLabsButton = Button (westFrames[0,1], image = discoverWestLabsImgPath, bd=0,  command=lambda: keyboardingLaboratoriesPage(keyboardingLaboratoryPage,2), activebackground= "#550000") #RESERVD COMMAND
westLabsButton.place(x=0, y=0, relwidth=1, relheight=1)

westFacultiesButton = Button (westFrames[0,2], image = discoverWestFacultiesImgPath, bd=0,  command=lambda: westFacultiesPaging(0), activebackground= "#550000") #RESERVD COMMAND
westFacultiesButton.place(x=0, y=0, relwidth=1, relheight=1)

westTransOfficeButton = Button (westFrames[0,3], image = discoverWestTransOfficesImgPath, bd=0,command=lambda: westTransOfficesPage(westTransOfficePage,1), activebackground= "#550000") #RESERVD COMMAND
westTransOfficeButton.place(x=0, y=0, relwidth=1, relheight=1)

westBathroomButton = Button (westFrames[0,4], image = discoverWestCrImgPath, bd=0,  command=lambda: westComfortRoomsPage(westComfortRoomPage,2), activebackground= "#550000") #RESERVD COMMAND
westBathroomButton.place(x=0, y=0, relwidth=1, relheight=1)

# WEST TRANSACT PAGE
westTransScrollBarFrame =ctk.CTkScrollableFrame(westTransOfficePage, width=390, height=510, fg_color = '#FFEDED', bg_color = '#FFEDED', scrollbar_button_color='#550000', scrollbar_button_hover_color='#5F0F0F')
westTransScrollBarFrame.place(x=28,y=157)

wARSSButton = Button(westTransScrollBarFrame, image=wARSSTabImgPath, bd=0,  command=lambda: admissionPage(admissionRegistrationPage,2), bg='#FFEDED', activebackground='#FFEDED')#RESERVD COMMAND
wARSSButton.pack(pady=(0,17))

wOSFAButton  = Button(westTransScrollBarFrame, image=wOSFATabImgPath, bd=0,  command=lambda: scholarshipPage(scholarshipAssistancePage,2), bg='#FFEDED', activebackground='#FFEDED')#RESERVD COMMAND
wOSFAButton .pack(pady=(0,17))

wOURButton  = Button(westTransScrollBarFrame, image=wOURTabImgPath, bd=0,  command=lambda: registrarsRecordsPage(registrarRecordsPage,2), bg='#FFEDED', activebackground='#FFEDED')#RESERVD COMMAND
wOURButton .pack(pady=(0,17))

wSHSButton  = Button(westTransScrollBarFrame, image=wSHSTabImgPath, bd=0,  command=lambda: shsDepartmentsPage(shsDepartmentPage,2), bg='#FFEDED', activebackground='#FFEDED')#RESERVD COMMAND
wSHSButton .pack(pady=(0,17))

#SOUTH DISCOVER PAGE
southButtonFrame = Frame(discoverSouthPage, width=384, height=28, bg='#550000')
southButtonFrame.place(x=25, y=83)

sButtonNames = ["A1", "A2", "A3", "A4"]
sButtonFrames = {}
for names in sButtonNames:
    row = ord(names[0]) - ord("A")
    col = int(names[1]) - 1
    sButtonFrame = ctk.CTkFrame(southButtonFrame, width=90, height=28, bg_color="#550000", fg_color="#550000")
    sButtonFrame.pack(padx=(8, 0), pady=(5, 0), side=LEFT)
    sButtonFrames[row, col] = sButtonFrame

sMPButton = Button (sButtonFrames[0,0], image=discoverMainPageButtonImgPath, command = categoriesPage,  bd=0, activebackground= "#550000")
sMPButton.place(x=0, y=0, relheight=1, relwidth=1)  

sEWButton = Button (sButtonFrames[0,1], image=discoverEastButtonImgPath,  command = discoversEastPage, bd=0, activebackground= "#550000")
sEWButton.place(x=0, y=0, relheight=1, relwidth=1)  

sWWButton = Button (sButtonFrames[0,2], image=discoverWestButtonImgPath,command = discoversWestPage, bd=0, activebackground= "#550000")
sWWButton.place(x=0, y=0, relheight=1, relwidth=1)  

sSWButton = Button (sButtonFrames[0,3], image=discoverSouthClickedImgPath,  bd=0, activebackground= "#550000")
sSWButton.place(x=0, y=0, relheight=1, relwidth=1)  

#SOUTH DISCOVER BUTTONS
discoverSouthFrame = ctk.CTkScrollableFrame(discoverSouthPage, width=423, height=665, bg_color='#550000', fg_color='#550000', scrollbar_button_color='#FFFFF0', scrollbar_button_hover_color='#FFFFF0')
discoverSouthFrame.place(x=14, y=119)

southNames = ["A1", "A2", "A3", "A4", "A5"]
southFrames = {}


for names in southNames:
    row = ord(names[0]) - ord("A")
    col = int(names[1]) - 1
    southFrame = ctk.CTkFrame(discoverSouthFrame, width=391, height=144, bg_color="#550000", fg_color="#550000")
    southFrame.pack(pady=(0, 13))
    southFrames[row, col] = southFrame


southLabButton = Button (southFrames[0,0], image = discoverSouthLabImgPath, command =lambda: southLabsPage(southLabBg,2), bd=0, activebackground= "#550000")
southLabButton.place(x=0, y=0, relwidth=1, relheight=1) 

southFacultiesButton = Button (southFrames[0,1], image = discoverSouthFacultiesImgPath, command=lambda: southFacultiesPaging(0), bd=0, activebackground= "#550000")
southFacultiesButton.place(x=0, y=0, relwidth=1, relheight=1) 

southTransOfficeButton = Button (southFrames[0,2], image = discoverSouthTransOfficeImgPath, command=lambda: southTransOfficesPage(southTransOfficePage,2) , bd=0, activebackground= "#550000") 
southTransOfficeButton.place(x=0, y=0, relwidth=1, relheight=1) 

southEventHallButton = Button (southFrames[0,3], image = discoverSouthEventHallImgPath, command =lambda: claroRectoRoomsPage(claroRectoRoomPage,3), bd=0, activebackground= "#550000")
southEventHallButton.place(x=0, y=0, relwidth=1, relheight=1) 

southBathroomButton = Button (southFrames[0,4], image = discoverSouthCrImgPath, bd=0,  command=lambda: southComfortRoomsPage(southComfortRoomPage,3), activebackground= "#550000") #RESERVD COMMAND
southBathroomButton.place(x=0, y=0, relwidth=1, relheight=1) 

# SOUTH TRANSACTION OFFICES 
southTraansOfficeScrollBarFrame =ctk.CTkScrollableFrame(southTransOfficePage, width=390, height=510, fg_color = '#FFEDED', bg_color = '#FFEDED', scrollbar_button_color='#550000', scrollbar_button_hover_color='#5F0F0F')
southTraansOfficeScrollBarFrame.place(x=28,y=157)

southRegisButton = Button(southTraansOfficeScrollBarFrame, image=southTransOfficeRegisTabImgPath, bd=0, command=lambda:registrarPage(registrarOfficePage,3), bg='#FFEDED', activebackground='#FFEDED')#RESERVD COMMAND
southRegisButton.pack(pady=(0,17))

southCashButton = Button(southTraansOfficeScrollBarFrame, image=southTransOfficeChasierTabImgPath, bd=0,  command=lambda: cashiersOfficePage(cashierOfficePage,3), bg='#FFEDED', activebackground='#FFEDED')#RESERVD COMMAND
southCashButton.pack(pady=(0,17))

# SOUTH LABORATORIES
southLabScrollBarFrame =ctk.CTkScrollableFrame(southLabPage, width=390, height=510, fg_color = '#FFEDED', bg_color = '#FFEDED', scrollbar_button_color='#550000', scrollbar_button_hover_color='#5F0F0F')
southLabScrollBarFrame.place(x=28,y=157)

southLabCompLabButton = Button(southLabScrollBarFrame, image=southLabComLabTabImgPath, bd=0,  command=lambda: computerLaboratoriesPage(computerLaboratoryPage,3), bg='#FFEDED', activebackground='#FFEDED')#RESERVD COMMAND
southLabCompLabButton.pack(pady=(0,17))

southLabLangButton = Button(southLabScrollBarFrame, image=southLabLanguageLabTabImgPath, bd=0,  command=lambda: languageLaboratoriesPage(languageLaboratoryPage,3), bg='#FFEDED', activebackground='#FFEDED')#RESERVD COMMAND
southLabLangButton.pack(pady=(0,17))


# ABOUT PAGE
aboutReturnFrame = Frame(aboutPage, width=37, height=37)
aboutReturnFrame.place(x=30, y=38)

aboutReturnButton = Button(aboutReturnFrame, image=aboutReturnButtonImgPath, bd=0 ,command=homesPage , bg = '#5F0F0F', activebackground= "#5F0F0F")
aboutReturnButton.place(x=0, y=0, relheight=1, relwidth=1)  





textAnimation()
# CREATING THE LOOP THAT MAKES OUR APPLICATION RUN
main.mainloop()