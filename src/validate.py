import schemaData

def validateInputData(data: dict) -> dict:
    for i in schemaData.inputData:
        try:
            data[i] = float(data[i])
        except Exception as exc:
            return dict(error='Valid Fail, not number')
            
    if data[schemaData.inputData[3]] < 0 or data[schemaData.inputData[3]] > 1:
        return dict(error='Valid Fail')
    
    return data
    