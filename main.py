
tag_name = "h1"
angle_bracket = ["<", ">"]
content = "공욱재"


tag_jolib_open = angle_bracket[0] + tag_name + angle_bracket[1]
tag_jolib_close = angle_bracket[0] + "/" + tag_name + angle_bracket[1]

result = tag_jolib_open + content + tag_jolib_close