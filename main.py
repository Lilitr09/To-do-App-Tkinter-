from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from PIL import Image, ImageTk


def add_task(entry, list):
    """Adds a task from the Entry box to the Listbox.

    Retrieves the text entered in the Entry,
    inserts it into the Listbox,
    and then clears the Entry.

    Args:
        entry (Entry): The Entry widget from which to get the task.
        list (Listbox): The Listbox widget to add the task to.

    Returns:
        None
    """
    task = entry.get()
    if task:
        list.insert(END, "• " + task)
        entry.delete(0, END)
    else:
        messagebox.showerror("Error", "Empty task")


def delete_task(list):
    """Deletes the selected task from the Listbox.

    Gets the index of the selected task in the Listbox and deletes it.
    If no task is selected, shows a warning message.

    Args:
        list (Listbox): The Listbox widget from which to delete the task.

    Returns:
        None
    """
    try:
        index = list.curselection()[0]
        list.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please, select a task to delete")


def main():
    """Color
    definition"""
    background_color = "#F5F5F5"  # Light grey
    text_color = "#212121"  # Dark grey
    primary_color = "#3498DB"  # Blue
    secondary_color = "#2980B9"  # Dark blue
    highlight_color = "#FFEB3B"  # Yellow
    red_button = "#E74C3C"
    red_button_hover = "#C0392B"

    # Window configuration
    window = Tk()
    window.title("To-do App")
    window.geometry("500x665")
    window.configure(bg=background_color)
    window.resizable(0, 0)

    icon = PhotoImage(file="icon.png")
    window.iconphoto(False, icon)

    # App layout

    # Image header
    try:
        image = Image.open("to-do-header.png")
        image_resized = image.resize((150, 90))
        image_tk = ImageTk.PhotoImage(image_resized)

        label_image = Label(window, image=image_tk, bg=background_color)
        label_image.image = image_tk
        label_image.pack()
    except FileNotFoundError:
        print("Error: image not found")

    # Tasks Entry
    task = Entry(
        window, bg=background_color, bd=4, fg=text_color, font=("calibre", 15, "bold")
    )
    task.pack(fill=X, padx=10, pady=10)
    # Add Task Button
    add_task_button = Button(
        window,
        text="Add Task",
        bg=primary_color,
        fg="white",
        padx=5,
        pady=5,
        cursor="hand2",
        activebackground=secondary_color,
        activeforeground="white",
        font=("calibre", 10, "bold"),
        command=lambda: add_task(task, tasks_area),
    )
    add_task_button.pack()
    # Tasks area
    tasks_area = Listbox(
        window,
        bg=background_color,
        activestyle="dotbox",
        fg=text_color,
        height=16,
        font=("Arial", 15),
    )
    tasks_area.pack(fill=X, padx=10, pady=10)
    # Delete task button
    delete_task_button = Button(
        window,
        text="Delete task",
        bg=red_button,
        fg="white",
        padx=5,
        pady=5,
        cursor="hand2",
        activebackground=red_button_hover,
        activeforeground="white",
        font=("calibre", 10, "bold"),
        command=lambda: delete_task(tasks_area),
    )
    delete_task_button.pack()

    # Footer
    message = Label(window, text="Made by Liliana Torres", bg=background_color)
    message.pack(padx=10, pady=10)

    # App execuition
    window.mainloop()


if __name__ == "__main__":
    main()
