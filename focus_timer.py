import time
import winsound

def focus_timer(focus_minutes, break_minutes):
    print(f"开始专注 {focus_minutes} 分钟")
    time.sleep(focus_minutes * 60)
    winsound.Beep(440, 1000)  # 播放提示音，可选
    print(f"专注结束，休息 {break_minutes} 分钟")
    time.sleep(break_minutes * 60)
    winsound.Beep(440, 1000)  # 播放提示音，可选
    print("休息结束")

if __name__ == "__main__":
    focus_time = 25  # 专注时间 25 分钟
    break_time = 5   # 休息时间 5 分钟

    while True:
        focus_timer(focus_time, break_time)
        continue_working = input("是否继续工作？(y/n): ")
        if continue_working.lower() != 'y':
            break
