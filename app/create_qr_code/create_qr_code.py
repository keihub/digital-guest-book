import qrcode

name_list = ["hoge,hoge県hoge市", "fuga,fuga県fuga市", "piyo,piyo県piyo市"]


for name in name_list:
    try:
        img = qrcode.make(name.encode())
        n = name.split(",")[0]
        img.save(f"./app/create_qr_code/qr_code_image/{n}.png")
        print(f"{n}のqrcodeを作成しました")
    except:
        print(f"{n}のQrcodeの作成に失敗しました")
