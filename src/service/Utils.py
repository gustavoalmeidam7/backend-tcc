from playhouse.shortcuts import model_to_dict

def bulk_convert_to_dict(modelList) -> dict:
    return list(
        map(
            model_to_dict,
            modelList
        ))

def unmask_number(number: str | None) -> str | None:
    if number is None:
        return None
    
    return filter(str.isdigit, number)