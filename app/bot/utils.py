

def is_valid_imei(imei: str) -> bool:
    if len(imei) != 15 or not imei.isdigit():
        return False
    
    total = 0
    for i in range(14, -1, -1):
        digit = int(imei[i])
        if (14 - i) % 2 == 1: 
            digit *= 2
            if digit > 9:
                digit -= 9 

        total += digit
    return total % 10 == 0