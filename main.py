import uuid
from tkinter.messagebox import showinfo, showerror

check_0 = uuid.getnode()
check_1 = uuid.getnode()

if check_0 == check_1:
    showinfo("Hardware ID", str(check_0))
else:
    showerror("An Error Occured", "Failed to get hardware ID")
