import tkinter as tk


# Определяем функцию для сортировки слиянием
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Слияние двух отсортированных списков
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Добавление оставшихся элементов из левого и правого списка
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Определяем функцию, которая будет вызываться при нажатии кнопки "Сортировать"
def sort_button_clicked():
    # Получаем строку из ввода и преобразуем ее в список целых чисел
    input_str = input_box.get()
    input_arr = [int(x) for x in input_str.split()]

    # Сортируем список с помощью функции сортировки слиянием
    merge_sort(input_arr)

    # Очищаем текстовое поле результата и выводим отсортированный список
    result_box.delete('1.0', tk.END)
    result_box.insert(tk.END, ' '.join([str(x) for x in input_arr]))


# Создаем главное окно приложения
window = tk.Tk()
window.title("Сортировка слиянием")

# Создаем текстовую метку и поле ввода для входных чисел
input_label = tk.Label(window, text="Входные числа (разделенные пробелом):")
input_label.pack()
input_box = tk.Entry(window)
input_box.pack()

# Создаем кнопку "Сортировать"
sort_button = tk.Button(window, text="Сортировать", command=sort_button_clicked)
sort_button.pack()

# Создаем текстовую метку и текстовое поле для отображения результата сортировки
result_label = tk.Label(window, text="Сортируемые значения: ")
result_label.pack()
result_box = tk.Text(window)
result_box.pack()

# Запускаем главный цикл обработки событий
window.mainloop()
