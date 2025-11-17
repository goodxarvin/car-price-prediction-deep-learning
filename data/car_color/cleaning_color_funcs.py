def fix_half_space(text):
    if text is None:
        return text
    text = str(text)
    text = text.replace("\u200c", " ")
    text = text.replace("\u200b", " ")
    text = text.replace("\u00A0", " ")
    
    import re
    text = re.sub(r"\s+", " ", text).strip()
    return text


def merge_same_colors(color):
    if color == "طلائی":
        return "طلایی"
    elif color == "بادمجونی":
        return "بادمجانی"
    elif color == "سفید صدفی":
        return "سفید"
    elif color == "عدسی":
        return "نوک مدادی"
    elif color == "نقرآبی":
        return "آبی"
    elif any([color == "گیلاسی",color == "زرشکی",color == "عنابی"]):
        return "آلبالویی"
    elif any([color == "امبر بلک",color == "ذغالی",color == "کربن بلک"]):
        return "مشکی"
    elif any([color == "شتری",color == "موکا",color == "خاکی"]):
        return "قهوع ای"
    
    return color
    