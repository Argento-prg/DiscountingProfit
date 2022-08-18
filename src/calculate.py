# расчёт денежного потока
def calcCashFlow(netProfit: float, depreciationDeductions: float, investments: float) -> float:
    return netProfit + depreciationDeductions - investments

# расчёт дисконтированного денежного потока
def calcDiscountCashFlow(cashFlow: float, koefDiscount: float) -> float:
    return cashFlow * koefDiscount

# расчёт дисконтированного денежного потока нарастающим итогом
def calcRisingDiscountCashFlow(prev: float, current: float) -> float:
    return prev + current