from tkinter import *


def main():
    """Color
    definition"""
    background_color = "#F5F5F5"  # Light grey
    text_color = "#212121"  # Dark grey
    primary_color = "#4CAF50"  # Green
    secondary_color = "#8BC34A"  # Light green
    highlight_color = "#FFEB3B"  # Yellow

    # Window configuration
    window = Tk()
    window.title("To-do App")
    window.geometry("500x500")
    window.configure(bg=background_color)

    # App layout

    # Tasks Entry
    task = Entry(
        window, bg=background_color, bd=4, fg=text_color, font=("calibre", 13, "bold")
    )
    task.pack(fill=X, padx=10, pady=10)
    # Add Task Button
    add_task_button = Button(
        window,
        text="Add Task",
        bg=secondary_color,
        fg=text_color,
        padx=5,
        pady=5,
        cursor="hand2",
        activebackground=primary_color,
        activeforeground="white",
    )
    add_task_button.pack()

    # App execuition
    window.mainloop()


if __name__ == "__main__":
    main()
