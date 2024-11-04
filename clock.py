# -*- coding: utf-8 -*-
"""修正ユリウス日で表示する時計
"""
from astropy.time import Time
import math
import tkinter
import threading
import time


class MJDClock:
    """表示時計クラス

    時計と，その表示に関する処理を扱うためのクラス．
    """

    def __init__(self):
        """コンストラクタ

        GUI表示に関する初期化処理を実行する
        """
        self.root = tkinter.Tk()
        self.root.title("MJD Clock")

        self.canvas = tkinter.Canvas(master=self.root, width=270, height=40)

    def tick(self):
        """時計表示処理

        現在時刻を修正ユリウス日で取得し，表示するという処理を0.1秒間隔で続ける．
        """
        old_text = ""
        while True:
            # 現在時刻を修正ユリウス日の文字列に変換
            f, i = math.modf(Time.now().mjd)
            text = "{:05d}".format(int(i)) + "." + "{:.05f}".format(f)[2:]

            # 前回と違う場合に表示を更新
            if old_text != text:
                self.canvas.delete("all")
                self.canvas.create_text(
                    5, 14, text="MJD", font=("Terminal", 14), anchor="nw"
                )
                self.canvas.create_text(
                    40, 4, text=text, font=("Terminal", 36), anchor="nw"
                )
                old_text = text

            time.sleep(0.01)

    def start(self):
        """開始処理

        時計を表示し，時刻表示の処理をスレッド化して呼び出す
        """
        self.canvas.pack()

        thread = threading.Thread(target=self.tick, daemon=True)
        thread.start()

        self.canvas.mainloop()


if __name__ == "__main__":
    clock = MJDClock()
    clock.start()
