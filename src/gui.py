import tkinter as tk
import service
from tkinter.ttk import Style

class GUI:

    selectedYearPage = 1
    weight = 600
    height = 350

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
        self.statusLabelField.set(f'стр. {self.selectedYearPage} из {self.Service.getYearsCounter()}')

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

    # добавление и настройка виджетов
    def __addWidgets(self):

        # первая строка

        self.prevbtn = tk.Button(self.mainWindow, text='назад', command=self.__prevPage)
        self.prevbtn.grid(row=0, column=0, sticky=tk.W+tk.E+tk.N+tk.S)

        self.statusLabel = tk.Label(self.mainWindow, textvariable=self.statusLabelField)
        self.statusLabel.grid(row=0, column=1, sticky=tk.W+tk.E+tk.N+tk.S)

        self.nextbtn = tk.Button(self.mainWindow, text='далее', command=self.__nextPage)
        self.nextbtn.grid(row=0, column=2, sticky=tk.W+tk.E+tk.N+tk.S)

        # вторая строка

        self.inputFieldLabel = tk.Label(self.mainWindow, text='Входные данные:')
        self.inputFieldLabel.grid(row=1, column=0, sticky=tk.W+tk.E+tk.N+tk.S)

        self.outputFieldLabel = tk.Label(self.mainWindow, text='Выходные данные:')
        self.outputFieldLabel.grid(row=1, column=2, sticky=tk.W+tk.E+tk.N+tk.S)

        # первый столбец (Вводимые данные)

        self.inputLabel_1 = tk.Label(self.mainWindow, text='', width=30)
        self.inputLabel_1.grid(row=2, column=0, sticky=tk.N+tk.S)

        self.inputEntry_1 = tk.Entry(self.mainWindow, textvariable='', width=30)
        self.inputEntry_1.grid(row=3, column=0, sticky=tk.N+tk.S)

        self.inputLabel_2 = tk.Label(self.mainWindow, text='', width=30)
        self.inputLabel_2.grid(row=4, column=0, sticky=tk.N+tk.S)

        self.inputEntry_2 = tk.Entry(self.mainWindow, textvariable='', width=30)
        self.inputEntry_2.grid(row=5, column=0, sticky=tk.N+tk.S)

        self.inputLabel_3 = tk.Label(self.mainWindow, text='', width=30)
        self.inputLabel_3.grid(row=6, column=0, sticky=tk.N+tk.S)

        self.inputEntry_3 = tk.Entry(self.mainWindow, textvariable='', width=30)
        self.inputEntry_3.grid(row=7, column=0, sticky=tk.N+tk.S)

        self.inputLabel_4 = tk.Label(self.mainWindow, text='', width=30)
        self.inputLabel_4.grid(row=8, column=0, sticky=tk.N+tk.S)

        self.inputEntry_4 = tk.Entry(self.mainWindow, textvariable='', width=30)
        self.inputEntry_4.grid(row=9, column=0, sticky=tk.N+tk.S)

        # третий столбец (Выводимые данные)

        self.outputLabel_1 = tk.Label(self.mainWindow, text='', width=30)
        self.outputLabel_1.grid(row=2, column=2, sticky=tk.N+tk.S)

        self.outputEntry_1 = tk.Entry(self.mainWindow, textvariable='', state='readonly', width=30)
        self.outputEntry_1.grid(row=3, column=2, sticky=tk.N+tk.S)

        self.outputLabel_2 = tk.Label(self.mainWindow, text='', width=30)
        self.outputLabel_2.grid(row=4, column=2, sticky=tk.N+tk.S)

        self.outputEntry_2 = tk.Entry(self.mainWindow, textvariable='', state='readonly', width=30)
        self.outputEntry_2.grid(row=5, column=2, sticky=tk.N+tk.S)

        self.outputLabel_3 = tk.Label(self.mainWindow, text='', width=30)
        self.outputLabel_3.grid(row=6, column=2, sticky=tk.N+tk.S)

        self.outputEntry_3 = tk.Entry(self.mainWindow, textvariable='', state='readonly', width=30)
        self.outputEntry_3.grid(row=7, column=2, sticky=tk.N+tk.S)

        # второй столбец (элементы управления)
        self.addPagebtn = tk.Button(self.mainWindow, text='Добавить', width=14, command=self.__addInputData)
        self.addPagebtn.grid(row=4, column=1, rowspan=2, sticky=tk.N+tk.S)

        pass
    
    # запуск графического приложения
    def __start(self):
        self.mainWindow.mainloop()
        pass
    
    # методы, вызываемые при активации элементов управления (UI)

    def __prevPage(self):
        if self.selectedYearPage != 1:
            self.selectedYearPage -= 1
            self.statusLabelField.set(f'стр. {self.selectedYearPage} из {self.Service.getYearsCounter()}')
            pass

    def __nextPage(self):
        if self.selectedYearPage != 100 and self.selectedYearPage != self.Service.getYearsCounter():
            self.selectedYearPage += 1
            self.statusLabelField.set(f'стр. {self.selectedYearPage} из {self.Service.getYearsCounter()}')
            pass

    # методы, вызываемые при активации элементов управления (бизнес-логика)

    # изменение входных полей данных
    def __changeInputData(self):
        pass

    # добавление входных данных
    def __addInputData(self):
        pass
    
    # рассчитать выходные данные
    def __calcOutputData(self):
        pass
    
    # получить входные данные по году
    def __getInputDataByYear(self):
        pass
    
    # получить выходные данные по году
    def __getOutputDataByYear(self):
        pass

    # очистить все хранимые данные
    def __clearAllData(self):
        pass

    # получить счётчик числа лет
    def __getYearsCounter(self):
        pass