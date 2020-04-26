import tkinter as tk
import requests
import re
import os

def get_html(url):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    try:
        html = requests.get(url,headers = headers)
        html.encoding = html.apparent_encoding
        if html.status_code == 200:
            print('成功获取源代码')
    except Exception as e:
        print('获取源代码失败:%s' % e)

    return html.text

def parse_html(html):

    urls = re.findall('"objURL":"(.*?)"',html,re.S)

    return urls

def downloadimg(urls,name):

    if name in os.listdir():
        pass
    else:
        os.mkdir(name)
    os.chdir(name)

    i = 0
    for url in urls:
        time.sleep(random.randint(1, 3) + random.random())
        imag = requests.get(url,timeout = 10).content

        if imag:
            with open(str(i) + '.jpg','wb')as f:
                print('正在下载第%d张照片：%s' % (i + 1,url))
                f.write(imag)
            i += 1
        else:
            print('图片下载失败，连接超时')

    print('图片下载完成')

    return None


def setwindow(root):
    root.title("图片下载器")
    root.geometry("600x300")

def download():
    html = get_html()


if __name__ == '__main__':
    root = tk.Tk()

    setwindow(root)

    entry = tk.Entry(root)
    entry.grid(row=0, column=4, padx=10)

    btn = tk.Button(root, text="下载", command=download, font="楷体", bg="red", fg="white")
    btn.grid(row=0, column=6, )

    text = tk.Text(root, width=150, height=50)
    text.grid(row=2, column=0, rowspan=6, columnspan=6)



    root.mainloop()