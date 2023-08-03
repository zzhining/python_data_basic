menu = {"고구마": 200, "떡볶이": 600, "라면": 800}

def get_recommend_weight(height, man=True):
    weight = 0
    if man:
        weight = height - 100
    else:
        weight = (height - 100) * 0.9
    print("권장 체중은 {}kg 입니다".format(weight))
    return weight

def print_valid_menu():  
    for key, value in menu.items():
        if value > 500:
            print("{}:X".format(key))
        else:
            print("{}:O".format(key))
