import tkinter as tk
import akinator

# configure the window
root = tk.Tk()
root.title("Loading..")
root.geometry("400x100")
root.iconphoto(False, tk.PhotoImage(file="./img/aki_ico.png"))
root.configure(background="#286afa")

root.lift()
root.attributes('-topmost', True)
root.after_idle(root.attributes, '-topmost', False)

def start():
  global aki, q
  aki = akinator.Akinator()
  q = aki.start_game(language="id", child_mode=False)
  root.title("Akinator")

start()

question_frame = tk.LabelFrame(
    root,
    text='Question',
    background='#286afa',
    foreground="#ffffff",
    font=(20)
)
question_frame.pack()

button_frame = tk.Frame(root, background='#286afa')
button_frame.pack(pady=5)

def answer_call(answer):
    if answer == "b":
      try:
        q = aki.back()

        question.config(text=q, font="Helvestica 10 bold")
      except akinator.CantGoBackAnyFurther:
        pass
    elif aki.progression >= 80:
        aki.answer(answer)

        yes.pack_forget()
        no.pack_forget()
        idk.pack_forget()
        probably.pack_forget()
        probablynot.pack_forget()
        back.pack_forget()

        aki.win()

        question_frame.config(
            text=f"i'm {format(aki.progression)}% Sure Your Character is")
        question.config(
            text=aki.first_guess['name'], font="Helvestica 10 bold")
    else:
        q = aki.answer(answer)
        question.config(text=q, font="Helvestica 10 bold")


question = tk.Label(question_frame, text=q,
                    background="#286afa", font="Helvestica 10 bold", cursor="xterm", foreground="#ffffff")
question.pack()

yes = tk.Button(button_frame, text="Yes",
                command=lambda: answer_call("y"), cursor="hand2", font="Calibri 10 bold", fg="green")
no = tk.Button(button_frame, text="No",
               command=lambda: answer_call("n"), cursor="hand2", font="Calibri 10 bold", fg="red")
idk = tk.Button(button_frame, text="Idk",
                command=lambda: answer_call("idk"), cursor="hand2", font="Calibri 10 bold", fg="#ad9f1c")
probably = tk.Button(button_frame, text="Probably",
                     command=lambda: answer_call("p"), cursor="hand2", font="Calibri 10 bold", fg="orange")
probablynot = tk.Button(button_frame, text="Probably Not",
                        command=lambda: answer_call("pn"), cursor="hand2", font="Calibri 10 bold")
back = tk.Button(button_frame, text="Back",
                 command=lambda: answer_call("b"), cursor="hand2", font="Calibri 10 bold", bg="red", fg="white")

yes.pack(side=tk.LEFT, padx=2)
no.pack(side=tk.LEFT, padx=2)
idk.pack(side=tk.LEFT, padx=2)
probably.pack(side=tk.LEFT, padx=2)
probablynot.pack(side=tk.LEFT, padx=2)
back.pack()

root.mainloop()