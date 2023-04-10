from glob import glob
import sys

from PySide6 import QtWidgets, QtUiTools,QtGui,QtCore


if __name__ == "__main__":
    print("Program start.")

    app = QtWidgets.QApplication(sys.argv)
    loader = QtUiTools.QUiLoader()
    window = loader.load("RDTNEW.ui", None)
    window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    ##################################################3
    window.show()
    
    def selectfcn():
         global filename
         filename= QtWidgets.QFileDialog.getExistingDirectory(window, 'Select Folder')
         if filename:
             window.dumploc.setText(filename)
    def dumpfcn():
        os.system("")
    def closefcn():
        exit()
        
    window.pushButton.clicked.connect(lambda: selectfcn())
    #window.dumpbtn.clicked.connect(lambda: dumpfcn())
    window.closebtn.clicked.connect(lambda: closefcn())
    window.minibtn_2.clicked.connect(lambda: window.showMinimized())
    window.home_btn.clicked.connect(lambda: window.stackedWidget.setCurrentWidget(window.home_page))
    window.contact_btn.clicked.connect(lambda: window.stackedWidget.setCurrentWidget(window.contact_page))
    window.infobtn.clicked.connect(lambda: window.stackedWidget.setCurrentWidget(window.Info_page) )
    window.home.clicked.connect(lambda: window.stackedWidget.setCurrentWidget(window.home_page))
    window.contact.clicked.connect(lambda: window.stackedWidget.setCurrentWidget(window.contact_page))
    window.info.clicked.connect(lambda: window.stackedWidget.setCurrentWidget(window.Info_page) )

    ########################################33333

    window.show()
    sys.exit(app.exec_())
