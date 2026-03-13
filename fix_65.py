# src/FreeCADGui/SelectionView.py

import FreeCADGui
import PySide2.QtWidgets as QtWidgets
import PySide2.QtGui as QtGui
import PySide2.QtCore as QtCore

class EnhancedSelectionView(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(EnhancedSelectionView, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Enhanced Selection View')
        self.setGeometry(300, 300, 400, 300)

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.selectionList = QtWidgets.QListWidget()
        self.layout.addWidget(self.selectionList)

        self.selectionList.itemSelectionChanged.connect(self.onSelectionChanged)

        self.updateSelectionList()

    def updateSelectionList(self):
        self.selectionList.clear()
        for obj in FreeCADGui.Selection.getSelection():
            item = QtWidgets.QListWidgetItem(obj.Label)
            item.setData(QtCore.Qt.UserRole, obj)
            self.selectionList.addItem(item)

    def onSelectionChanged(self):
        selectedItems = self.selectionList.selectedItems()
        if selectedItems:
            selectedItem = selectedItems[0]
            selectedObject = selectedItem.data(QtCore.Qt.UserRole)
            FreeCADGui.Selection.clearSelection()
            FreeCADGui.Selection.addSelection(selectedObject)

# src/FreeCADGui/MainWindow.py

def setupEnhancedSelectionView():
    mainWin = FreeCADGui.getMainWindow()
    if mainWin:
        enhancedView = EnhancedSelectionView(mainWin)
        mainWin.addDockWidget(QtCore.Qt.RightDockWidgetArea, enhancedView)

# src/FreeCADGui/init.py

def setup():
    setupEnhancedSelectionView()