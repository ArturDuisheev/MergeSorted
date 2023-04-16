import tkinter as tk


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def sort_button_clicked():
    input_str = input_box.get()
    input_arr = [int(x) for x in input_str.split()]
    merge_sort(input_arr)
    result_box.delete('1.0', tk.END)
    result_box.insert(tk.END, ' '.join([str(x) for x in input_arr]))


window = tk.Tk()
window.title("Сортировка слиянием")

input_label = tk.Label(window, text="Входные числа (разделенные пробелом):")
input_label.pack()

input_box = tk.Entry(window)
input_box.pack()

sort_button = tk.Button(window, text="Сортировать", command=sort_button_clicked)
sort_button.pack()

result_label = tk.Label(window, text="Сортитруемые значения: ")
result_label.pack()

result_box = tk.Text(window)
result_box.pack()

window.mainloop()
