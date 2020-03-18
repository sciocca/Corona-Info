from tkinter import *
from PIL import ImageTk, Image
import xlsxwriter

#Setup

root =Tk()
root.title("Corona Info")
root.iconbitmap("C:/GitHub/Corona-Info/medical_icon.ico")
root.geometry("600x400")

#Main Page

rating = IntVar()
rating_string = StringVar()

#DATA HUB
def goto_data_hub():
    data_hub=Toplevel()
    data_hub_title = Label(data_hub,text="Data Hub",font=("Helvetica", 72))
    data_hub_title.pack()
    return
#NEWS HUB
def goto_news_hub():
    news_hub=Toplevel()
    news_hub_title = Label(news_hub,text="News Hub",font=("Helvetica", 72))
    news_hub_title.pack()
    return

def clicked_rating_button(var,string):
    rating_workbook = xlsxwriter.Workbook('C:/GitHub/Corona-Info/AppRatings.xlsx')
    ratings = rating_workbook.add_worksheet()
    rating_list=[rating.get(),rating_string.get()]
    for col_num, data in enumerate(rating_list):
        ratings.write(0, col_num, data)
    rating_workbook.close()
    #RESET
    b_rating = Button(rating_system_frame,state=DISABLED, text="Send",padx=5,pady=5,command=lambda: clicked_rating_button(rating.get(),rating_string.get()))
    rating_text.delete(0,END)
    rating_text.insert(0, "Thank you for your feedback!")
    b_rating.grid(row=3, columnspan=2)
    return


coronainfo_label = Label(root,text="Corona Info",font=("Helvetica", 72), padx=50)
main_page_button_frame = LabelFrame(root,padx=89,pady=10)
main_page_label = Label(main_page_button_frame, text="Click Here To Go To Modules",font=("Helvetica", 11))
datahub_button = Button(main_page_button_frame,text="Data Hub",padx=5,pady=5,command=goto_data_hub)
newshub_button = Button(main_page_button_frame,text="News Hub",padx=5,pady=5,command=goto_news_hub )

#App rating system

rating_system_frame = LabelFrame(root,padx=60,pady=10)
rating_label = Label(rating_system_frame,text="How Do You Like This App?",font=("Helvetica", 11))
rb_good = Radiobutton(rating_system_frame, text="Good", variable=rating, value=0, state=NORMAL)
rb_bad = Radiobutton(rating_system_frame, text="Bad", variable=rating, value=1, state=NORMAL)
rating_text = Entry(rating_system_frame,width=40,textvariable=rating_string,relief=SUNKEN)
b_rating = Button(rating_system_frame, text="Send",padx=5,pady=5,command=lambda: clicked_rating_button(rating.get(),rating_string.get()))



#Main Page Display

coronainfo_label.grid(row=0,column=0,columnspan=2)
main_page_button_frame.grid(row=1,columnspan=2)
main_page_label.grid(row=0,column=0, columnspan=2)
datahub_button.grid(row=1,column=0)
newshub_button.grid(row=1,column=1)

rating_system_frame.grid(row=2,columnspan=2)
rating_label.grid(row=0,columnspan=2)
rb_good.grid(row=1, column=0)
rb_bad.grid(row=1, column=1)
rating_text.grid(row=2,column=0,columnspan=2,padx=5,pady=10,ipady=3)
rating_text.insert(0, "Suggestions?")
b_rating.grid(row=3, columnspan=2)




root.mainloop()