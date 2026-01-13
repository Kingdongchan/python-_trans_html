# <html><head><title>제목</title></head><body><h1>내용</h1></body></html>

# html = open + "html" + close 
# head = open + "head" + close
# tilte = open + "title" + close
# body = open + "body" + close
# h1 = open + "h1" + close

# slash_html = open + slash + "html" + close
# slash_head = open + slash + "head" + close
# slash_title = open + slash + "title" + close
# slash_body = open + slash + "body" + close
# slash_h1 = open + slash + "h1" + close


def mark_up(isopen ,content):
    bracket = ["<", ">", "/"]
    
    if isopen == "open":
        def open_mark_up():
            keyword = bracket[0] + content + bracket[1]
            
            return keyword
    else:
        def close_mark_up():
            keyword = bracket[0] + bracket[2] + content + bracket[0]
            
            return keyword
        
