# デジタル芳名帳

## ユーザーのQrコードを作成する

1. `create_qr_code.py`のname_listにqr code化したい文字列を入力
   - 入力形式: "name,address"という形式で入力
2. `python3 create_qr_code.py`を実行
3. `qr_code_image`ディレクトリにQrコードが生成される
4. ユーザーへ配布する

## ユーザーのQrコードを読み取る

1. `python3 ./app/read_qr_code/read_web_camer_qr_code.py`を実行
2. カメラが起動し、Qrコードを読み取る
3. Qrコードに書かれた文字列が`sample_houmeityou/test_houmeityou.csv`に保存される
   - 重複は排除される
   - ユニークな文字列だとcsvに保存される
4. 出席者を管理するのにしようしたりする予定
# digital-guest-book
