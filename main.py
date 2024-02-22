import tkinter
import customtkinter
from VirtualMachine import *

def main():
    inputs_from_keyboard = []


    #Sets light or dark mode
    customtkinter.set_appearance_mode("default")
    #Sets color of buttons
    customtkinter.set_default_color_theme("green")
    #Initalizes tkinter
    root = customtkinter.CTk()

    #Sets screen size
    root.geometry("500x600")
    root.title("UVSimulator")

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    label = customtkinter.CTkLabel(master=frame, text="UVSim")
    label.pack(pady=12, padx=10)

    entry1 = customtkinter.CTkEntry(master=frame, width = 200, placeholder_text="Enter File Name")
    entry1.pack(pady=12, padx=10)

    def run():  # Use nonlocal to modify the outer scope variable
        file_text = entry1.get()
        VM = VirtualMachine(file_text, inputs_from_keyboard)
        VM.run()
        
        label2.configure(text = VM.get_output())
        label3.configure(text = VM)
        #root.destroy()

    def store_inputs(): #will store inputs into a list of strings
        one_input = entry2.get()
        inputs_from_keyboard.append(one_input)
        entry2.delete(0, len(one_input))

    
    #Another entry if there is any input values asked for
    entry2 = customtkinter.CTkEntry(master = frame, width = 200, placeholder_text="Enter a 4 digit instruction")
    entry2.pack(pady=12, padx=10)

    #input button stores button
    input_button = customtkinter.CTkButton(master=frame, width = 200, text="Store Instruction", command=store_inputs)
    input_button.pack(pady=12, padx=10)

    # button 1 is a "run" button that will execute the "run" function.
    button = customtkinter.CTkButton(master=frame, width = 200, text="Run", command=run)
    button.pack(pady=12, padx=10)

    # button 2 is a quit button. The text="Quit" displays the button and the "command" terminates the gui
    button2 = customtkinter.CTkButton(master=frame, width = 200, text="Quit", command=root.destroy)
    button2.pack(pady=12, padx=10)

    frame2 = customtkinter.CTkScrollableFrame(frame, orientation="vertical", width=200, height=300)
    frame2.pack(pady=40)

    label2 = customtkinter.CTkLabel(frame2, text="")
    label2.pack()

    label3 = customtkinter.CTkLabel(frame2, text="")
    label3.pack()

    # entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Output")
    # entry2.pack(pady=12, padx=10)
    root.mainloop()


if __name__ == "__main__":
    main()
