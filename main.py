
tag_name = "h1"
angle_bracket = ["<", ">"]
content = "공욱재"


tag_jolib_open = angle_bracket[0] + tag_name + angle_bracket[1]
tag_jolib_close = angle_bracket[0] + "/" + tag_name + angle_bracket[1]


## 매겨변수 설정하는 것이 많이 어렵다 -> 많이 해봐야 함
def make_tag(isOpen):
    if isOpen == True:
        open = tag_jolib_open
        return open 
    else:
        close = tag_jolib_close
        return  close
    

result = make_tag(True) + content + make_tag(False)


print(result)