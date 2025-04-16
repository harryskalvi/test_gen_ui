import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer

import test_hkr_logic as logic
import test_hkr_db as db

class MainApp(QMainWindow):
    lstCurrentCombination = []  # Placeholder for the current combination
    dictCombinations = {}  # Placeholder for the dictionary of combinations

    def __init__(self):
        super().__init__()
        loadUi("gen_ui_hkr_v01.ui", self)  # Load UI file
        
        # Initialize timer
        self.countdown_timer = QTimer()
        self.countdown_timer.timeout.connect(self.update_countdown)
        self.remaining_time = 0

        self.show_screen(0)

        # Navigation buttons (replace with correct object names)
        self.btnCombinationMode.clicked.connect(lambda: self.event_CombinationMode())
        self.btnSparringMode.clicked.connect(lambda: self.event_SparringMode())
        self.btnGlobalSettings.clicked.connect(lambda: self.event_GlobalSettings())

        self.btnProceedCombination.clicked.connect(lambda: self.event_ProceedCombination())
        self.btnCreateNewCombination.clicked.connect(lambda: self.event_CreateNewCombination())
        self.btnSaveCombination.clicked.connect(lambda: self.event_SaveCombination())

        self.btnBack_2.clicked.connect(lambda: self.event_Back())
        self.btnHome_2.clicked.connect(lambda: self.event_Home())
        self.btnBack_3.clicked.connect(lambda: self.event_Back())
        self.btnHome_3.clicked.connect(lambda: self.event_Home())
        
        self.btnPauseWorkout.clicked.connect(lambda: self.event_PauseWorkout())
        self.btnStopWorkout.clicked.connect(lambda: self.event_StopWorkout())
        self.btnAcceptSettings.clicked.connect(lambda: self.event_AcceptSettings())
        self.btnCancelSettings.clicked.connect(lambda: self.event_Cancel())
        
        self.btnJab.clicked.connect(lambda: self.event_Jab())
        self.btnCross.clicked.connect(lambda: self.event_Cross())
        self.btnLHook.clicked.connect(lambda: self.event_LHook())
        self.btnRHook.clicked.connect(lambda: self.event_RHook())
        self.btnLUpperCut.clicked.connect(lambda: self.event_LUppercut())
        self.btnRUpperCut.clicked.connect(lambda: self.event_RUppercut())

    def start_countdown(self, seconds):
        self.remaining_time = seconds
        self.lcdTimer.display(self.remaining_time)
        self.countdown_timer.start(1000)  # 1-second interval

    def update_countdown(self):
        self.remaining_time -= 1
        self.lcdTimer.display(self.remaining_time)

        if self.remaining_time <= 0:
            self.countdown_timer.stop()
            logic.endWorkout()  # Call the endWorkout function when countdown ends

    def show_screen(self, index):
        self.stackedWidget.setCurrentIndex(index)
        if index == 3 and self.checkBoxLoop.isChecked(): 
            self.start_countdown(10)  # Start countdown from 10
            self.lcdTimer.show()  # Show the timer display
        else:
            self.lcdTimer.hide()  # Hide the timer display
    
    def event_CombinationMode(self):
        # self.show_screen(1)
        self.event_SelectCombination()
        # logic.beginCombination()

    def event_SparringMode(self):
        self.show_screen(3)
        logic.beginSparring()

    def event_GlobalSettings(self):
        self.show_screen(4)

    def event_CreateNewCombination(self):
        self.show_screen(2)
        self.listCreateCombination.clear()
        self.textEdit.clear()
        self.lstCurrentCombination = []

    def event_SaveCombination(self):
        for index in range(self.listCreateCombination.count()):
            self.lstCurrentCombination.append(self.listCreateCombination.item(index).text())
        curCombiName = self.textEdit.toPlainText()
        dictTempCombination = {curCombiName: self.lstCurrentCombination}
        db.insertCombination(dictTempCombination)
        # self.dictCombinations[curCombiName] = self.lstCurrentCombination
        self.event_SelectCombination()

    def event_SelectCombination(self):
        self.show_screen(1)
        
        self.dictCombinations = db.getAllCombinations()
        print(self.dictCombinations)
        
        self.listSelectCombination.clear()

        for key in self.dictCombinations.keys():
            # print(key)
            self.listSelectCombination.addItem(key)
    
    def event_ProceedCombination(self):
        selected_item = self.listSelectCombination.currentItem()
        if selected_item:
            selected_text = selected_item.text()
            combination = self.dictCombinations[selected_text]
            # print("Selected Combination Name: ", selected_text)
            # print("Combination: ", combination)
            self.show_screen(3)
            logic.beginCombination(combination, self.checkBoxLoop.isChecked())

    def event_PauseWorkout(self):
        self.show_screen(0)

    def event_StopWorkout(self):
        self.show_screen(0)

    def event_AcceptSettings(self):
        self.show_screen(0)

    def event_Back(self):
        self.show_screen(0)

    def event_Home(self):
        self.show_screen(0)

    def event_Cancel(self):
        self.show_screen(0)

    def event_Jab(self):
        # print("Jab action triggered.")
        self.listCreateCombination.addItem("Jab")

    def event_Cross(self):
        # print("Cross action triggered.")
        self.listCreateCombination.addItem("Cross")

    def event_LHook(self):
        # print("Left Hook action triggered.")
        self.listCreateCombination.addItem("LeftHook")
    
    def event_RHook(self):
        # print("Right Hook action triggered.")
        self.listCreateCombination.addItem("RightHook")
    
    def event_LUppercut(self):
        # print("Left Uppercut action triggered.")
        self.listCreateCombination.addItem("LeftUppercut")

    def event_RUppercut(self):
        # print("Right Uppercut action triggered.")
        self.listCreateCombination.addItem("RightUppercut")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())