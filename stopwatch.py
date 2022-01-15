import tkinter as tk
import time

LABEL_FONT = "Helvetica 18 bold"
BUTTON_FONT = "Helvetica 14 bold"
BUTTON_WIDTH = 6
BUTTON_HEIGHT = 2
BUTTON_BG = "white"
BUTTON_ACTIVEFOREGROUND = "green"
PAD_X_Y = 8

startTime = time.time()  # стартовое время первого круга
lastTime = startTime
lapNum = 1  # номер круга

IS_RUNNING = False


def start_stop_button():
    global startTime, lastTime, lapNum, IS_RUNNING
    if start_stop_button_text.get() == "Старт":
        start_stop_button_text.set("Стоп")
        lap_button["state"] = "normal"

        startTime = time.time()  # стартовое время первого круга
        lastTime = startTime
        lapNum = 1  # номер круга

        IS_RUNNING = True
        time_refresher()

        # text_box.delete("1.0", tk.END)  # Очистить вывод
        if len(text_box.get("1.0", 'end-1c')) == 0:  # Пустой вывод, тогда выводим шапку
            text_box.insert(tk.END, 'Круг #№: Всего (Время круга)\n')

        reset_button.grid_forget()
    else:  # if button = Стоп
        start_stop_button_text.set("Старт")
        lap_button["state"] = "disabled"

        IS_RUNNING = False
        time_refresher()

        # text_box.delete("1.0", tk.END)  # Очистить вывод

        reset_button.grid(row=1, column=0,
                    padx=PAD_X_Y, pady=PAD_X_Y)


def lap_button():
    global startTime, lastTime, lapNum
    lapTime = round(time.time() - lastTime, 2)
    totalTime = round(time.time() - startTime, 2)
    lap = f"Круг #{lapNum}: {totalTime} ({lapTime})"
    lapNum += 1
    lastTime = time.time()  # сброс времени последнего круга

    text_box.insert(tk.END, f'{lap}\n')  # Добавить в вывод


def reset_button():
    global startTime, lastTime, lapNum

    # НУЖЕН СКОРЕЕ ВСЕГО КАКОЙ ТО ФЛАГ

    startTime = time.time()  # стартовое время первого круга
    lastTime = startTime
    lapNum = 1  # номер круга

    text_box.delete("1.0", tk.END)  # Очистить вывод


def time_refresher():
    current_diff_time = time.time() - startTime
    current_diff_time_formatted = round(current_diff_time, 2)
    if IS_RUNNING:
        label.configure(text=current_diff_time_formatted)
        window.after(100, time_refresher)  # 1000 = 1 second
    else:
        label.configure(text="00.00")


"""
1) install python
2) pip install tk
"""

"""
открыть терминал
cd Downloads/stopwatch/
source venv/bin/activate
python stopwatch.py
deactivate
"""


if __name__ == '__main__':
    window = tk.Tk()
    window.title('Секундомер')

    label = tk.Label(
        text="00.00",
        font=LABEL_FONT,
    )
    label.grid(row=0, column=0, columnspan=2,
               padx=PAD_X_Y, pady=PAD_X_Y)

    lap_button_text = tk.StringVar()
    lap_button = tk.Button(
        textvariable=lap_button_text,
        font=BUTTON_FONT,
        width=BUTTON_WIDTH,
        height=BUTTON_HEIGHT,
        bg=BUTTON_BG,
        activeforeground=BUTTON_ACTIVEFOREGROUND,
        command=lap_button,
        state="disabled"
    )
    lap_button_text.set("Круг")
    lap_button.grid(row=1, column=0,
                    padx=PAD_X_Y, pady=PAD_X_Y)

    reset_button_text = tk.StringVar()
    reset_button = tk.Button(
        textvariable=reset_button_text,
        font=BUTTON_FONT,
        width=BUTTON_WIDTH,
        height=BUTTON_HEIGHT,
        bg=BUTTON_BG,
        activeforeground=BUTTON_ACTIVEFOREGROUND,
        command=reset_button,
    )
    reset_button_text.set("Сброс")
    reset_button.grid(row=1, column=0,
                    padx=PAD_X_Y, pady=PAD_X_Y)

    start_stop_button_text = tk.StringVar()
    start_stop_button = tk.Button(
        textvariable=start_stop_button_text,
        font=BUTTON_FONT,
        width=BUTTON_WIDTH,
        height=BUTTON_HEIGHT,
        bg=BUTTON_BG,
        activeforeground=BUTTON_ACTIVEFOREGROUND,
        command=start_stop_button
    )
    start_stop_button_text.set("Старт")
    start_stop_button.grid(row=1, column=1,
                           padx=PAD_X_Y, pady=PAD_X_Y)

    bottom_frame = tk.Frame()
    bottom_frame.grid(row=2, column=0, columnspan=2,
                      padx=PAD_X_Y, pady=PAD_X_Y)

    text_box = tk.Text(
        master=bottom_frame,
        bg="grey90",
        width=30,
    )
    text_box.pack(side="left")

    sb = tk.Scrollbar(
        master=bottom_frame,
        orient="vertical",
        width=5,
    )
    sb.pack(side="right", anchor="ne", fill="y", pady=4)
    text_box.config(yscrollcommand=sb.set)
    sb.config(command=text_box.yview)

    window.mainloop()
