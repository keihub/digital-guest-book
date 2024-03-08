import pathlib
import cv2
import pandas as pd


camera_id = 0
delay = 1
window_name = "OpenCV QR Code"

qcd = cv2.QRCodeDetector()
cap = cv2.VideoCapture(camera_id)

path = pathlib.Path("./app/read_qr_code/sample_houmeityou/test_houmeityou.csv")

print(path)

while True:
    ret, frame = cap.read()

    if ret:
        ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(frame)
        if ret_qr:
            for s, p in zip(decoded_info, points):
                if s:
                    # FIXME: 1度の読み込みで何度もprintを出力してしまう
                    try:
                        color = (0, 255, 0)
                        csv_df = pd.read_csv(path)
                        csv_df = csv_df.append(
                            pd.Series(s.split(","), index=["name", "address"]),
                            ignore_index=True,
                        )
                        csv_df = csv_df.drop_duplicates().reset_index()[
                            ["name", "address"]
                        ]
                        csv_df.to_csv(path, index=False, encoding="utf-8-sig")
                        print(f"{s}を追加しました")
                    except:
                        print(f"{s}の追加に失敗しました")

                    # 動画を停止
                    # cv2.cap_cam.release()

                else:
                    color = (0, 0, 255)
                frame = cv2.polylines(frame, [p.astype(int)], True, color, 8)
        cv2.imshow(window_name, frame)

    if cv2.waitKey(delay) & 0xFF == ord("q"):
        break


cv2.destroyWindow(window_name)
