from playhouse.shortcuts import model_to_dict

def bulk_convert_to_dict(modelList) -> dict:
    return list(
        map(
            model_to_dict,
            modelList
        ))

def unmask_number(number: str) -> str:
    finalNumber = ""
    for char in number:
        if char.isnumeric():
            finalNumber += char

    return str(finalNumber)