__author__ = 'trunghieu11'


def dfs(html, begin, end, type):
    if html == "":
        return ""
    for i in range(3):
        if html.find(begin[i]) == 0:
            html = html[len(begin[i]):]
            return type[i] + "([" + dfs(html, begin, end, type)
    if html.find("<img />") == 0:
        html = html[len("<img />"):]
        return "IMG({})" + dfs(html, begin, end, type)
    for i in range(3):
        if html.find(end[i]) == 0:
            html = html[len(end[i]):]
            return "])" + dfs(html, begin, end, type)


def htmlToLuna(html):
    begin = ["<div>", "<p>", "<b>"]
    end = ["</div>", "</p>", "</b>"]
    type = ["DIV", "P", "B"]
    return dfs(html, begin, end, type)


if __name__ == '__main__':
    html = "<div><p><img /></p><b></b></div>"
    print htmlToLuna(html)