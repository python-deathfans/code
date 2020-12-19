import itchat
import PIL.Image as Image
import os


def make_avatar_path():

    if "avatar" not in os.listdir():
        os.mkdir("avatar")
        os.chdir("avatar")

        save_avatar()
    else:
        merge_avatar()


def save_avatar():

    num = 0

    for f in friends:
        img = itchat.get_head_img(userName=f['UserName'])
        img_name = str(num) + ".png"

        try:
            with open(img_name, 'wb') as f:
                f.write(img)
                print("正在保存第%d张图片" % num)

                num += 1
        except Exception as e:
            print(e)

    os.chdir("../")


def merge_avatar():

    each_line = 15
    size = 60
    new_image = Image.new('RGBA', (900, 900), 'white')

    x = 0
    y = 0

    for i in range(15*15+2):
        try:
            img = Image.open('./avatar/' + str(i) + ".png")
        except IOError:
            print("图片没法打开, %s.png" % i)
        else:
            img = img.resize((size, size), Image.ANTIALIAS)
            new_image.paste(img, (x*size, y*size))

            x += 1

            if x == each_line:
                x = 0
                y += 1

    new_image.save("all.png")
    new_image.show()


if __name__ == '__main__':

    # 登录微信
    itchat.auto_login(hotReload=True)

    friends = itchat.get_friends(update=True)[1:]

    print(friends)

    make_avatar_path()

