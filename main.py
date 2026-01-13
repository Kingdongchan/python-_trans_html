
tag_name = "h1"
angle_bracket = ["<", ">"]
content = "공욱재"

## 매겨변수 설정하는 것이 많이 어렵다 -> 많이 해봐야 함
def make_tag(isOpen):
    if isOpen == True:
        open = angle_bracket[0] + tag_name + angle_bracket[1]
        return open 
    else:
        close = angle_bracket[0] + "/" + tag_name + angle_bracket[1]
        return  close
    

result = make_tag(True) + content + make_tag(False)


print(result)