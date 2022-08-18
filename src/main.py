import gui
import service

def main():
    gui.GUI()

def test():
    Service = service.Service()
    success = Service.addElemsToDataList(260000, 0, 305000, 0.97)
    if success:
        print('data was added')
    success = Service.addElemsToDataList(368500, 0, 0, 0.95)
    if success:
        print('data was added')

    success = Service.calcOutputData()
    if success:
        print('data was calced')
    data = Service.getOutputData(2)
    print("Data:")
    for key in data.keys():
        print(data[key])
    data = Service.getYearsCounter()
    print(data)
    data = Service.getInputDataForTheOneYear(1)
    print(data)
    


if __name__ == '__main__':
    main()
    #test()