import tkinter as tk
import service
from tkinter.ttk import Style
import schemaData

class GUI:

    selectedYearPage = 1
    weight = 600
    height = 350
    limitPages = 100

    # конструктор формы, в котором происходят все вызовы функций
    def __init__(self):
        self.Service = service.Service()
        self.__createWindow()
        self.__initializeBindVariablesString()
        self.__addWidgets()
        self.__start()

    # инициализация привязанных строковых переменных
    def __initializeBindVariablesString(self):
        self.statusLabelField = tk.StringVar(self.mainWindow)
        self.statusLabelField.set(f'год {self.selectedYearPage} из {self.Service.getYearsCounter()}')
        
        # входные данные
        self.netProfitEntryField = tk.StringVar(self.mainWindow)
        self.netProfitEntryField.set('0')

        self.depreciationDeductionsField = tk.StringVar(self.mainWindow)
        self.depreciationDeductionsField.set('0')

        self.investmentsField = tk.StringVar(self.mainWindow)
        self.investmentsField.set('0')

        self.koefDiscountField = tk.StringVar(self.mainWindow)
        self.koefDiscountField.set('0')

        # выходные данные
        self.cashFlowField = tk.StringVar(self.mainWindow)
        self.cashFlowField.set('0')

        self.discountCashFlowField = tk.StringVar(self.mainWindow)
        self.discountCashFlowField.set('0')

        self.risingDiscountCashFlowField = tk.StringVar(self.mainWindow)
        self.risingDiscountCashFlowField.set('0')

    #размещение главного окна по центру
    def __centerWindowAndGeometry(self):
        sw = self.mainWindow.winfo_screenwidth()
        sh = self.mainWindow.winfo_screenheight()
 
        x = (sw - self.weight) / 2
        y = (sh - self.height) / 2
        self.mainWindow.geometry('%dx%d+%d+%d' % (self.weight, self.height, x, y))

    # создание и настройка главного окна
    def __createWindow(self):
        self.mainWindow = tk.Tk()
        self.mainWindow.title('DiscountingProfit')
        self.mainWindow.resizable(width=False, height=False)
        self.__centerWindowAndGeometry()

        Style().configure("Window", padding=(10, 10, 10, 10), font='serif 10')

        # разметка сетки главного окна
        # разметка колонок
        self.mainWindow.columnconfigure(0, pad=20)
        self.mainWindow.columnconfigure(1, pad=20)
        self.mainWindow.columnconfigure(2, pad=20)
        # разметка строк
        self.mainWindow.rowconfigure(0, pad=10)
        self.mainWindow.rowconfigure(1, pad=10)
        self.mainWindow.rowconfigure(2, pad=10)
        self.mainWindow.rowconfigure(3, pad=10)
        self.mainWindow.rowconfigure(4, pad=10)
        self.mainWindow.rowconfigure(5, pad=10)
        self.mainWindow.rowconfigure(6, pad=10)
        self.mainWindow.rowconfigure(7, pad=10)
        self.mainWindow.rowconfigure(8, pad=10)
        self.mainWindow.rowconfigure(9, pad=10)

        self.mainWindow.bind_all('<Key>', self._onKeyRelease, '+')

    # добавление и настройка виджетов
    def __addWidgets(self):

        # первая строка

        self.prevbtn = tk.Button(self.mainWindow, text='назад', command=self.prevPage)
        self.prevbtn.grid(row=0, column=0, sticky=tk.W+tk.E+tk.N+tk.S)

        self.statusLabel = tk.Label(self.mainWindow, textvariable=self.statusLabelField)
        self.statusLabel.grid(row=0, column=1, sticky=tk.W+tk.E+tk.N+tk.S)

        self.nextbtn = tk.Button(self.mainWindow, text='далее', command=self.nextPage)
        self.nextbtn.grid(row=0, column=2, sticky=tk.W+tk.E+tk.N+tk.S)

        # вторая строка

        self.inputFieldLabel = tk.Label(self.mainWindow, text='Входные данные:')
        self.inputFieldLabel.grid(row=1, column=0, sticky=tk.W+tk.E+tk.N+tk.S)

        self.outputFieldLabel = tk.Label(self.mainWindow, text='Выходные данные:')
        self.outputFieldLabel.grid(row=1, column=2, sticky=tk.W+tk.E+tk.N+tk.S)

        # первый столбец (Вводимые данные)

        self.inputLabel_1 = tk.Label(self.mainWindow, text='Чистая прибыль, руб.', width=30)
        self.inputLabel_1.grid(row=2, column=0, sticky=tk.N+tk.S)

        self.inputEntry_1 = tk.Entry(self.mainWindow, textvariable=self.netProfitEntryField, width=30)
        self.inputEntry_1.grid(row=3, column=0, sticky=tk.N+tk.S)
        self.inputEntry_1.bind('<KeyRelease>', self.changeInputData)

        self.inputLabel_2 = tk.Label(self.mainWindow, text='Амортизационные отчисления, руб.', width=30)
        self.inputLabel_2.grid(row=4, column=0, sticky=tk.N+tk.S)

        self.inputEntry_2 = tk.Entry(self.mainWindow, textvariable=self.depreciationDeductionsField, width=30)
        self.inputEntry_2.grid(row=5, column=0, sticky=tk.N+tk.S)
        self.inputEntry_2.bind('<KeyRelease>', self.changeInputData)

        self.inputLabel_3 = tk.Label(self.mainWindow, text='Инвестиции, руб.', width=30)
        self.inputLabel_3.grid(row=6, column=0, sticky=tk.N+tk.S)

        self.inputEntry_3 = tk.Entry(self.mainWindow, textvariable=self.investmentsField, width=30)
        self.inputEntry_3.grid(row=7, column=0, sticky=tk.N+tk.S)
        self.inputEntry_3.bind('<KeyRelease>', self.changeInputData)

        self.inputLabel_4 = tk.Label(self.mainWindow, text='Коэффициент дисконтирования', width=30)
        self.inputLabel_4.grid(row=8, column=0, sticky=tk.N+tk.S)

        self.inputEntry_4 = tk.Entry(self.mainWindow, textvariable=self.koefDiscountField, width=30)
        self.inputEntry_4.grid(row=9, column=0, sticky=tk.N+tk.S)
        self.inputEntry_4.bind('<KeyRelease>', self.changeInputData)

        # третий столбец (Выводимые данные)

        self.outputLabel_1 = tk.Label(self.mainWindow, text='Денежный поток, руб.', width=30)
        self.outputLabel_1.grid(row=2, column=2, sticky=tk.N+tk.S)

        self.outputEntry_1 = tk.Entry(self.mainWindow, textvariable=self.cashFlowField, state='readonly', width=30)
        self.outputEntry_1.grid(row=3, column=2, sticky=tk.N+tk.S)

        self.outputLabel_2 = tk.Label(self.mainWindow, text='Дисконтированный денежный\nпоток, руб.', width=30)
        self.outputLabel_2.grid(row=4, column=2, rowspan=2, sticky=tk.N+tk.S)

        self.outputEntry_2 = tk.Entry(self.mainWindow, textvariable=self.discountCashFlowField, state='readonly', width=30)
        self.outputEntry_2.grid(row=6, column=2, sticky=tk.N+tk.S)

        self.outputLabel_3 = tk.Label(self.mainWindow, text='Дисконтированный денежный\nпоток нарастающим итогом, руб.', width=30)
        self.outputLabel_3.grid(row=7, column=2, rowspan=2, sticky=tk.N+tk.S)

        self.outputEntry_3 = tk.Entry(self.mainWindow, textvariable=self.risingDiscountCashFlowField, state='readonly', width=30)
        self.outputEntry_3.grid(row=9, column=2, sticky=tk.N+tk.S)

        # второй столбец (элементы управления)
        self.addPagebtn = tk.Button(self.mainWindow, text='Добавить', width=14, command=self.addInputData)
        self.addPagebtn.grid(row=2, column=1, rowspan=2, sticky=tk.N+tk.S)

        self.exportToCSVbtn = tk.Button(self.mainWindow, text='Экспортировать', width=14, command=self.exportDataToCSV)
        self.exportToCSVbtn.grid(row=5, column=1, rowspan=2, sticky=tk.N+tk.S)

        self.clearAllDatabtn = tk.Button(self.mainWindow, text='Очистить всё', width=14, command=self.clearAllData)
        self.clearAllDatabtn.grid(row=8, column=1, rowspan=2, sticky=tk.N+tk.S)

    
    # запуск графического приложения
    def __start(self):
        self.mainWindow.mainloop()
        
    
    # методы, вызываемые при активации элементов управления (UI)

    def prevPage(self):
        if self.selectedYearPage != 1:
            self.selectedYearPage -= 1
            self.statusLabelField.set(f'год {self.selectedYearPage} из {self.Service.getYearsCounter()}')
            dataInput = self.Service.getInputDataForTheOneYear(self.selectedYearPage)
            if dataInput.get('error'):
                return
            dataOutput = self.Service.getOutputData(self.selectedYearPage)
            if dataOutput.get('error'):
                return
            
            self.netProfitEntryField.set(str(dataInput[schemaData.inputData[0]]))
            self.depreciationDeductionsField.set(str(dataInput[schemaData.inputData[1]]))
            self.investmentsField.set(str(dataInput[schemaData.inputData[2]]))
            self.koefDiscountField.set(str(dataInput[schemaData.inputData[3]]))

            self.cashFlowField.set(str(dataOutput[schemaData.outputData[0]]))
            self.discountCashFlowField.set(str(dataOutput[schemaData.outputData[1]]))
            self.risingDiscountCashFlowField.set(str(dataOutput[schemaData.outputData[2]]))

            

    def nextPage(self):
        if self.selectedYearPage != self.limitPages and self.selectedYearPage != self.Service.getYearsCounter():
            self.selectedYearPage += 1
            self.statusLabelField.set(f'год {self.selectedYearPage} из {self.Service.getYearsCounter()}')
            dataInput = self.Service.getInputDataForTheOneYear(self.selectedYearPage)
            if dataInput.get('error'):
                return
            dataOutput = self.Service.getOutputData(self.selectedYearPage)
            if dataOutput.get('error'):
                return
            
            self.netProfitEntryField.set(str(dataInput[schemaData.inputData[0]]))
            self.depreciationDeductionsField.set(str(dataInput[schemaData.inputData[1]]))
            self.investmentsField.set(str(dataInput[schemaData.inputData[2]]))
            self.koefDiscountField.set(str(dataInput[schemaData.inputData[3]]))

            self.cashFlowField.set(str(dataOutput[schemaData.outputData[0]]))
            self.discountCashFlowField.set(str(dataOutput[schemaData.outputData[1]]))
            self.risingDiscountCashFlowField.set(str(dataOutput[schemaData.outputData[2]]))
            

    # копирование и вставка
    def _onKeyRelease(self, event):
        ctrl  = (event.state & 0x4) != 0
        if event.keycode==88 and  ctrl and event.keysym.lower() != "x": 
            event.widget.event_generate("<<Cut>>")

        if event.keycode==86 and  ctrl and event.keysym.lower() != "v": 
            event.widget.event_generate("<<Paste>>")

        if event.keycode==67 and  ctrl and event.keysym.lower() != "c":
            event.widget.event_generate("<<Copy>>")


    # методы, вызываемые при активации элементов управления (бизнес-логика)

    # экспорт данных в csv
    def exportDataToCSV(self):
        self.Service.exportDataToCSV()

    # изменение входных полей данных
    def changeInputData(self, event):
        data = dict()
        data[schemaData.inputData[0]] = self.netProfitEntryField.get()
        data[schemaData.inputData[1]] = self.depreciationDeductionsField.get()
        data[schemaData.inputData[2]] = self.investmentsField.get()
        data[schemaData.inputData[3]] = self.koefDiscountField.get()
        
        response = self.Service.changeInputDataForTheOneYear(self.selectedYearPage, data)
        if response:
            response = self.Service.calcOutputData()
        if response:
            outputData = self.Service.getOutputData(self.selectedYearPage)
            self.cashFlowField.set(str(outputData[schemaData.outputData[0]]))
            self.discountCashFlowField.set(str(outputData[schemaData.outputData[1]]))
            self.risingDiscountCashFlowField.set(str(outputData[schemaData.outputData[2]]))
    
    # добавление входных данных
    def addInputData(self):
        if self.Service.getYearsCounter() < self.limitPages:
            success = self.Service.addElemsToDataList(0, 0, 0, 0)
            if success:
                success = self.Service.calcOutputData()
            if success:
                self.selectedYearPage = self.Service.getYearsCounter()
                outputData = self.Service.getOutputData(self.selectedYearPage)
                self.cashFlowField.set(str(outputData[schemaData.outputData[0]]))
                self.discountCashFlowField.set(str(outputData[schemaData.outputData[1]]))
                self.risingDiscountCashFlowField.set(str(outputData[schemaData.outputData[2]]))

                self.netProfitEntryField.set('0')
                self.depreciationDeductionsField.set('0')
                self.investmentsField.set('0')
                self.koefDiscountField.set('0')

                self.statusLabelField.set(f'год {self.selectedYearPage} из {self.Service.getYearsCounter()}')

    # очистить все хранимые данные
    def clearAllData(self):
        self.Service.clearAllData()
        self.selectedYearPage = self.Service.getYearsCounter()
        self.statusLabelField.set(f'год {self.selectedYearPage} из {self.Service.getYearsCounter()}')

        dataInput = self.Service.getInputDataForTheOneYear(self.selectedYearPage)
        if dataInput.get('error'):
            return
        dataOutput = self.Service.getOutputData(self.selectedYearPage)
        if dataOutput.get('error'):
            return
        
        self.netProfitEntryField.set(str(dataInput[schemaData.inputData[0]]))
        self.depreciationDeductionsField.set(str(dataInput[schemaData.inputData[1]]))
        self.investmentsField.set(str(dataInput[schemaData.inputData[2]]))
        self.koefDiscountField.set(str(dataInput[schemaData.inputData[3]]))

        self.cashFlowField.set(str(dataOutput[schemaData.outputData[0]]))
        self.discountCashFlowField.set(str(dataOutput[schemaData.outputData[1]]))
        self.risingDiscountCashFlowField.set(str(dataOutput[schemaData.outputData[2]]))


        

