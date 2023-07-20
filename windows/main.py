from distutils.command.build_scripts import first_line_re
from fnmatch import fnmatchcase
from glob import glob
import sys,os,pymongo
import hashlib
from PySide6 import QtWidgets, QtUiTools,QtGui,QtCore


if __name__ == "__main__":
    print("Program start.")

    app = QtWidgets.QApplication(sys.argv)
    loader = QtUiTools.QUiLoader()
    window = loader.load(".\\resources\\RDTNEW.ui", None)
    
    ##################################################3
    window.show()
    client=pymongo.MongoClient("mongodb+srv://neerajlovecyber:gamersnsp@rdtdb.grubyrx.mongodb.net/?retryWrites=true&w=majority")
    db = client["rdtapi"]
    collection = db["md5sum"]
    window.side_menu_closed.hide()
    #check checksum if presnt in data
    def decryptfcn(fname,passwd,foldername):
        cmd=".\\resources\\7za.exe x -p" +str(passwd)+" -mmt=on -aoa "+fname+" -o"+foldername 
        os.system(cmd)
        print("done")
    def encryptfcn(fname,passwd,foldername):
        cmd=".\\resources\\7za.exe a -t7z -mx=1 -mmt=on -p"+str(passwd)+" "+ fname +".7z "+fname
        os.system(cmd)
        print("done")
    def checksumdb(checksum):
        checksum=checksum
        query = {"checksum":checksum}
        count = collection.count_documents(query)
        if count > 0:
            print("Found matching documents")
            window.checkbtn_2.setText("Pass")
            window.checkbtn_2.setStyleSheet("background-color: rgb(17, 255, 0);");
        else:
            print("No matching documents found")
            window.checkbtn_2.setText("Fail")
            window.checkbtn_2.setStyleSheet("background-color: rgb(255, 0, 4);");


    #genrate checksum
    def genchecksum(a):  
        with open(a, "rb") as f:
            # read the contents of the file in chunks
            chunk_size = 4096
            hasher = hashlib.md5()
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                hasher.update(chunk)
        print(hasher.hexdigest())
        
        return str(hasher.hexdigest())

    #insertchecksum
    def insertdb(a):
        checksum=a
        print(checksum)
        mydict = {"checksum":checksum}
        print(mydict)
        print(collection.insert_one(mydict))
    
    def selectfcn():
         global filename
         filename= QtWidgets.QFileDialog.getExistingDirectory(window, 'Select Folder')
         if filename:
             window.dumploc.setText(filename)
             window.folderlock.setText(filename)
             
    def do_file():
        global fname
        fname = QtWidgets.QFileDialog.getOpenFileName(window, 'Select File')
        fname=fname[0]
        if fname:
             window.dumploc_3.setText(fname)
             window.dumploc_2.setText(fname)
    

             
    def dumpfcn():
        window.dumpbtn.setEnabled(False)
        window.dumpbtn.setText("Dumping ...")
        window.repaint()
        os.system(".\\resources\\winpmem.exe mem.raw --treads 4 --format raw --volume_format raw")
        os.system("move mem.raw "+filename)
        sumpath=filename+"/mem.raw"
        window.dumpbtn.setText("Genrating CheckSum")
        window.repaint()
        nsp=genchecksum(sumpath)
        insertdb(nsp)
        window.dumpbtn.setText("Completed")
        window.repaint()
        completedail = loader.load(".\\resources\\loadingdailog.ui", None)
        completedail.exec_()
        window.dumpbtn.setEnabled(True)
    
    def encdumpfcn():
        window.dumpbtn.setEnabled(False)
        window.dumpbtn.setText("Dumping ...")
        window.repaint()
        os.system(".\\resources\\winpmem.exe mem.raw --treads 4 --format raw --volume_format raw")
        os.system("move mem.raw "+filename)
        sumpath=filename+"/mem.raw"
        window.dumpbtn.setText("Genrating CheckSum")
        window.repaint()
        nsp=genchecksum(sumpath)
        insertdb(nsp)
        passwd=window.linepass_2.text()
        window.dumpbtn.setText("Encrypting ...")
        window.repaint()
        encryptfcn(sumpath,passwd,filename)
        window.dumpbtn.setText("Completed")
        window.repaint()
        completedail = loader.load(".\\resources\\loadingdailog.ui", None)
        completedail.exec_()
        window.dumpbtn.setEnabled(True)
    
    def checkbtnfcn():
        window.checkbtn_2.setText("Checking ...")
        window.checkbtn_2.setStyleSheet("background-color: rgb(0, 255, 255);");
        window.repaint()
        nsp=genchecksum(fname)
        checksumdb(nsp)
    def encbtnfcn():
        passewd=window.linepass.text()
        window.checkbtn_3.setText("Ecrypting ...")
        window.checkbtn_3.setStyleSheet("background-color: rgb(0, 255, 255);");
        window.repaint()
        encryptfcn(fname,passewd,filename)
        window.checkbtn_3.setText(" Done ")
        window.checkbtn_3.setStyleSheet("background-color: rgb(17, 255, 0);");
        window.repaint()
    def decbtnfcn():
        window.checkbtn_3.setText("Decrypting ...")
        window.checkbtn_3.setStyleSheet("background-color: rgb(0, 255, 255);");
        window.repaint()
        passewd=window.linepass.text()
        decryptfcn(fname,passewd,filename)
        window.checkbtn_3.setText(" Done ")
        window.checkbtn_3.setStyleSheet("background-color: rgb(17, 255, 0);");
        window.repaint()
    def dumpfcnbtn():    
        if window.checkBox.isChecked() == True:
            encdumpfcn()
        else:
            dumpfcn()
    def sidebarfcn():
        if window.pushButton_6.isChecked() == True:
            window.setFixedWidth(1000)
                        
        else:
            window.setFixedWidth(1100)

   
    def closefcn():
         sys.exit(app.exec_())
        
    window.pushButton.clicked.connect(lambda: selectfcn())
    
    window.dumpbtn.clicked.connect(lambda: dumpfcnbtn())
    window.closebtn.clicked.connect(lambda: closefcn())
    window.minibtn_2.clicked.connect(lambda: window.showMinimized())
    window.home_btn.clicked.connect(lambda: window.stackedWidget.setCurrentWidget(window.home_page))
    window.contact_btn.clicked.connect(lambda: window.stackedWidget.setCurrentWidget(window.contact_page))
    window.infobtn.clicked.connect(lambda: window.stackedWidget.setCurrentWidget(window.Info_page) )
    window.home.clicked.connect(lambda: window.stackedWidget.setCurrentWidget(window.home_page))
    window.contact.clicked.connect(lambda: window.stackedWidget.setCurrentWidget(window.contact_page))
    window.info.clicked.connect(lambda: window.stackedWidget.setCurrentWidget(window.Info_page) )
    window.check_btn.clicked.connect(lambda: window.stackedWidget.setCurrentWidget(window.checkpage))
    window.checkmini_btn.clicked.connect(lambda: window.stackedWidget.setCurrentWidget(window.checkpage) )
    window.checkselect.clicked.connect(lambda: do_file())
    window.selectfile.clicked.connect(lambda: do_file())
    window.selectfolder.clicked.connect(lambda:selectfcn())
    window.checkbtn.clicked.connect(lambda: checkbtnfcn())
    window.encbtn.clicked.connect(lambda: encbtnfcn())
    window.decbtn.clicked.connect(lambda: decbtnfcn())
    window.pushButton_6.clicked.connect(lambda: sidebarfcn())

    ########################################33333

    window.show()
    sys.exit(app.exec_())