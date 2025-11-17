def convert_year(model):
    if model > 1950:
        return model-621
    return model

def normalize(model):
    return model/1403
