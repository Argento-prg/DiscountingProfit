import calculate as cl

class Service:

    # Входные данные

    # список чистой прибыли
    __netProfitList = []
    # список амортизационных отчислений
    __depreciationDeductionsList = []
    # список инвестиций
    __investmentsList = []
    # список коэффициентов дисконтирования
    __koefDiscountList = []
    # счётчик лет
    __yearsCounter = 0

    # Выходные данные

    # список денежного потока
    __cashFlowList = []
    # список дисконтированного денежного потока
    __discountCashFlowList = []
    # список дисконтированного денежного потока нарастающим итогом
    __risingDiscountCashFlowList = []
    
    
    # инициализация сервиса
    def __init__(self):
        self.__fillFirstPageData()
    
    # заполнение первой страницы элементов
    def __fillFirstPageData(self):
        self.addElemsToDataList(0, 0, 0, 0)
        self.calcOutputData()

    # добавление данных в списки
    def addElemsToDataList(self, netProfit: float, depreciationDeductions: float, investments: float, koefDiscount: float) -> bool:
        result = True
        try:
            self.__netProfitList.append(netProfit)
            self.__depreciationDeductionsList.append(depreciationDeductions)
            self.__investmentsList.append(investments)
            self.__koefDiscountList.append(koefDiscount)
            self.__yearsCounter += 1

            self.__cashFlowList.append(0)
            self.__discountCashFlowList.append(0)
            self.__risingDiscountCashFlowList.append(0)
        except(Exception):
            result = False
        
        return result

    # получение данных за один то 
    def getInputDataForTheOneYear(self, year: int) -> dict:
        if year > self.__yearsCounter or year < 1:
            return dict(error='Year is not valid')
        
        try:
            idx = year - 1
            data = dict(
                netProfit=self.__netProfitList[idx],
                depreciationDeductions=self.__depreciationDeductionsList[idx],
                investments=self.__investmentsList[idx],
                koefDiscount=self.__koefDiscountList[idx]
            )
            return data
        except(Exception):
            return dict(error='Fail')

    # изменение данных за один год
    def changeInputDataForTheOneYear(self, year: int, data: dict) -> bool:
        if year > self.__yearsCounter or year < 1:
            return dict(error='Year is not valid')
        
        try:
            idx = year - 1
            self.__netProfitList[idx] = data['netProfit'],
            self.__depreciationDeductionsList[idx] = data['depreciationDeductions'],
            self.__investmentsList[idx] = data['investments'],
            self.__koefDiscountList[idx] = data['koefDiscount']

            return True
        except(Exception):
            return False
    
    # сброс всех данных
    def clearAllData(self):
        self.__netProfitList.clear()
        self.__depreciationDeductionsList.clear()
        self.__investmentsList.clear()
        self.__koefDiscountList.clear()
        self.__yearsCounter = 0

        self.__cashFlowList.clear()
        self.__discountCashFlowList.clear()
        self.__risingDiscountCashFlowList.clear()

        self.__fillFirstPageData()

    # расчёт выходных данных
    def calcOutputData(self) -> bool:
        result = True
        try:
            for i in range(self.__yearsCounter):
                self.__cashFlowList[i] = cl.calcCashFlow(self.__netProfitList[i], self.__depreciationDeductionsList[i], self.__investmentsList[i])
                self.__discountCashFlowList[i] = cl.calcDiscountCashFlow(self.__cashFlowList[i], self.__koefDiscountList[i])
                # если это не первая итерация, то используем предыдущее значение дисконтированного денежного потока нарастающим итогом
                prev = 0
                if i != 0:
                    prev = self.__risingDiscountCashFlowList[i-1]
                self.__risingDiscountCashFlowList[i] = cl.calcRisingDiscountCashFlow(prev, self.__discountCashFlowList[i])
        except(Exception):
            result = False
        return result

    # получение выходных данных за один год
    def getOutputData(self, year: int) -> dict:
        if year > self.__yearsCounter or year < 1:
            return dict(error='Year is not valid')
        
        try:
            idx = year - 1
            data = dict(
                cashFlow=self.__cashFlowList[idx],
                discountCashFlow=self.__discountCashFlowList[idx],
                risingDiscountCashFlow=self.__risingDiscountCashFlowList[idx]
            )
            return data
        except(Exception):
            return dict(error='Fail')
    
    # получение счётчика числа лет
    def getYearsCounter(self):
        return self.__yearsCounter
        
