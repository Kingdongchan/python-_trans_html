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


def mark_up(content):
    open = "<"
    close = ">"
    slash = "/"
            
    def open_mark_up(content):
        keyword = open + content + close
        print(keyword)

    def close_mark_up(content):
        keyword = open + slash + content + close
        print(keyword)