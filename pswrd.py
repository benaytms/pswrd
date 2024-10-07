#!/usr/bin/env python3

# imports essential libraries:
# sys to check the external file
# and pyqt5 to use the GUI interface 
import sys
from PyQt5 import QtWidgets, QtGui, QtCore

# this is the path where the credentials are stored
# check README file to understand how to syntax it 
SAVE_PATH = './.credentials'


# this is a config to improve the font on the interface, so it's less pixelated
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseSoftwareOpenGL)

# function to get the passwords from the credentials file
# the way it works is that it'll look for all the entries with an equal sign(=)
# and then will passthrough the value on the left as the login
# and the one on the right as the password itself

# having all of this information we can create a GUI Interface that will show
# everything nicely

def load_credentials(file_path):
    credentials = {}
    
    with open( file_path, 'r' ) as file:
        
        for line in file:
            
            line = line.strip()
            if '=' in line:
                login, password = line.split('=', 1)
                credentials[ login.strip() ] = password.strip()
                
    return credentials

# this function is just to make the interface dark
def dark_theme():
    dark_palette = QtGui.QPalette()
    dark_palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))          # main window backgrund
    dark_palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)                 # text color
    dark_palette.setColor(QtGui.QPalette.Base, QtGui.QColor(25, 25, 25))            # items background color
    dark_palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))    # alternate background for itens
    dark_palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)                # tooltip color
    dark_palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.black)                # tooltip background color
    dark_palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)                      # normal text color
    dark_palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))           # button color
    dark_palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)                # button text color
    dark_palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)                  # bright text color
    dark_palette.setColor(QtGui.QPalette.Link, QtGui.QColor(42, 130, 218))           # link color
    dark_palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 130, 218))      # highlight color
    dark_palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)            # highlighted text color
    return dark_palette

# creates the window, the table, fills the table with the dictionary containing the credentials
# from load_credentials()
# then puts the table on the window and shows the window - there's a lot of customization of 
# fonts and sizes in the middle
def create_table(credentials):
    app = QtWidgets.QApplication(sys.argv)
    
    window= QtWidgets.QWidget()
    window.setGeometry(100, 100, 900, 840)  # window position and size
    window.setWindowTitle("Credentials Log")    # title
    
    table = QtWidgets.QTableWidget(window)
    table.setColumnCount(2) # login, password
    table.setHorizontalHeaderLabels(["Login", "Passwords"])
    
    table.setColumnWidth(0, 500)    # login column size
    table.setColumnWidth(1, 300)    # password column size
    
    table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)   # this is for the size of the actual values
    table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)

    
    #fill table
    table.setRowCount(len(credentials))
    for idx, (login, pswrd) in enumerate(credentials.items(), start=0):
        table.setItem(idx, 0, QtWidgets.QTableWidgetItem(login))
        table.setItem(idx, 1, QtWidgets.QTableWidgetItem(pswrd))
    
    font = QtGui.QFont("DejaVu Sans", 16)   # font chosen
    table.horizontalHeader().setFont(QtGui.QFont("DejaVu Sans", 18, QtGui.QFont.Bold))
    font.setStyleStrategy(QtGui.QFont.PreferAntialias)  # also improves font pixelation
    table.setFont(font)
    
    for i in range(table.columnCount()):    # heading aligment to the left
        header_item = table.horizontalHeaderItem(i)
        header_item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
    
    
    app.setPalette(dark_theme())    # sets the dark theme
    
    # shows the window with the elements loaded
    layout = QtWidgets.QVBoxLayout()
    layout.addWidget(table)
    window.setLayout(layout)
    
    window.show()
    sys.exit(app.exec_())
    
# main function calls
if __name__ == "__main__":
    
    credentials = load_credentials(SAVE_PATH)
    
    create_table(credentials)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
