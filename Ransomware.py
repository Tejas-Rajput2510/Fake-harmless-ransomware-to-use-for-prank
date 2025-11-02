import tkinter as tk
import time
import threading

# Secret key
DECRYPT_KEY = "Lol!Youwereprankedverybadly@hahahaha!"
remaining_seconds = 60 * 60  # 1 hour

def launch_ransom_gui():
    terms_window.destroy()

    # Create main window
    global root, entry
    root = tk.Tk()
    root.title("Decrypter 2.1")
    root.attributes("-fullscreen", True)
    root.configure(bg="red")

    # Disable close, minimize, and escape
    root.protocol("WM_DELETE_WINDOW", lambda: None)
    root.bind("<Alt-F4>", lambda e: "break")
    root.bind("<Escape>", lambda e: "break")
    root.bind("<Control-KeyPress-w>", lambda e: "break")

    # Fake title bar
    title_bar = tk.Frame(root, bg="blue", height=30)
    title_bar.pack(fill="x")
    title_label = tk.Label(title_bar, text="Decrypter 2.1", bg="blue", fg="white", font=("Helvetica", 12, "bold"))
    title_label.pack(side="left", padx=10)

    # Dread banner
    banner = tk.Label(
        root,
        text="Bad news, all your files have been encrypted!",
        bg="red",
        fg="white",
        font=("Helvetica", 28, "bold")
    )
    banner.pack(pady=(10, 0))

    # Main layout frame
    main_frame = tk.Frame(root, bg="red")
    main_frame.pack(fill="both", expand=True)

    # Left timer frame
    timer_frame = tk.Frame(main_frame, bg="red", width=200)
    timer_frame.pack(side="left", fill="y", padx=20, pady=20)
    timer_label = tk.Label(timer_frame, text="60:00", bg="red", fg="white", font=("Helvetica", 32, "bold"))
    timer_label.pack(anchor="n")

    # Center content frame
    content_frame = tk.Frame(main_frame, bg="red")
    content_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

    text = """
What Happened To This Computer?
All your personal data, photos, videos, work files, including your operating system have been encrypted and can be accessed again if you pay a ransom. You can't access anything on this machine but this screen.

You have one hour to pay the prize, otherwise you will no longer be able to decrypt them. Powering off or restarting your computer will also destroy your files.

What Can You Do?
You might be looking for a way to recover your files but don't waste your time. We use an unbreakable encryption so nobody can restore your files without a decryption key.

You can purchase your key using one of the payment methods listed below. You will get a code to paste in the input field and click Decrypt. After this you should be restored in a couple of minutes.

Is This Legal?
Someone who has access to this computer has recently installed one of our free applications and agreed for the files to be encrypted by accepting the terms and conditions. This procedure is absolutely legal, we are a certified and awarded company specialized in computer viruses and digital identity theft. We will send you an invoice for your payment.

How Do You Pay?
We offer many payment methods to make the transaction smooth and easy to make you a satisfied but not a returning customer:

Send $399 + Tax worth of Monopoly Money to this address:
    ʞuɐɹԀ∀ʇsnſsIsᴉɥ┴#payment
Send the fee with PayDude:
    ransomware?!infected==__decryption?-key@decrypt.com
We now accept kidneys!
Call now to request kidney transplant: +1 804 TAKE MY KIDNEY
"""

    label = tk.Label(content_frame, text=text, bg="red", fg="white", font=("Helvetica", 12, "bold"), justify="left", wraplength=1000)
    label.pack(pady=10)

    # Entry + Button side by side
    entry_button_frame = tk.Frame(content_frame, bg="red")
    entry_button_frame.pack(pady=10)

    entry = tk.Entry(entry_button_frame, font=("Helvetica", 14), width=40)
    entry.pack(side="left", padx=(0, 10))

    button = tk.Button(entry_button_frame, text="Decrypt", font=("Helvetica", 14, "bold"), command=attempt_decrypt)
    button.pack(side="left")

    # Start the timer
    def update_timer():
        global remaining_seconds
        if remaining_seconds >= 0:
            mins, secs = divmod(remaining_seconds, 60)
            timer_label.config(text=f"{mins:02d}:{secs:02d}")
            remaining_seconds -= 1
            root.after(1000, update_timer)
    update_timer()

    root.mainloop()

def attempt_decrypt():
    if entry.get() == DECRYPT_KEY:
        for widget in root.winfo_children():
            widget.destroy()
        root.config(bg="green")
        success_label = tk.Label(
            root,
            text="Your files were restored successfully!",
            font=("Helvetica", 24, "bold"),
            fg="white",
            bg="green"
        )
        success_label.place(relx=0.5, rely=0.5, anchor="center")
        threading.Thread(target=exit_after_delay).start()

def exit_after_delay():
    global root
    time.sleep(5)
    root.destroy()
    exit()

# Stage 1: Terms and Conditions Window
terms_window = tk.Tk()
terms_window.title("Terms and conditions")
terms_window.geometry("600x300")
terms_window.configure(bg="white")

terms_text = """Terms and conditions

To use this application, you have to accept these terms and conditions to continue. You have to accept that this application can encrypt your files and it can also decide when to decrypt files and when not. And it can access your all files including system files, work files, photos, videos, audios, compressed, scripts and every type of file your computer contains. You have to accept these terms and conditions to continue."""

terms_label = tk.Label(terms_window, text=terms_text, bg="white", fg="black", font=("Helvetica", 10), justify="left", wraplength=580)
terms_label.pack(padx=10, pady=20)

accept_button = tk.Button(terms_window, text="Accept terms and conditions", font=("Helvetica", 12, "bold"), command=launch_ransom_gui)
accept_button.pack(pady=10)

terms_window.mainloop()
