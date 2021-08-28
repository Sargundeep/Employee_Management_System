from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import matplotlib. pyplot as plt
import requests
import bs4

# ------------------------------------------Quote of the Day---------------------------------------------------------------------


try:
	web_address = "https://www.brainyquote.com/quote_of_the_day"
	response = requests.get(web_address)
	
	data = bs4.BeautifulSoup(response.text, 'html.parser')
	#print(data)

	info = data.find('img', {'class' : 'p-qotd'})
	#print(info)

	qotd = info['alt']
	#print(qotd)	
except Exception as e:
	print(e)
#-----------------------------------------Add Function------------------------------------------------------------------------------
def add_open():
	add_window.deiconify()
	main_window.withdraw()
def add_student():
	if (aw_ent_id.get() == "" or aw_ent_name.get() == "" or aw_ent_esal.get() == ""):
		showerror("OOPS!", "Please fill all the details")
	elif (aw_ent_id.get().isdigit() == False):
		showerror("OOPS!", "Id can have integers only")
		aw_ent_id.delete(0, END)
		aw_ent_name.delete(0, END)
		aw_ent_esal.delete(0, END)
	elif (int(aw_ent_id.get()) <= 0) :
		showerror("OOPS!", "Id can't be negative")
		aw_ent_id.delete(0, END)
		aw_ent_name.delete(0, END)
		aw_ent_esal.delete(0, END)
	elif (len(aw_ent_name.get()) < 2):
		showerror("OOPS!", "Name can't consist of only one alphabet")
		aw_ent_id.delete(0, END)
		aw_ent_name.delete(0, END)
		aw_ent_esal.delete(0, END)
	elif ((((aw_ent_name.get()).replace(" ","")).isalpha()) == False):
		showerror("OOPS!", "Name can't consist of digits")
		aw_ent_id.delete(0, END)
		aw_ent_name.delete(0, END)
		aw_ent_esal.delete(0, END)
	elif (aw_ent_esal.get().isdigit() == False):
		showerror("OOPS!", "Salary can be in integer only")
		aw_ent_id.delete(0, END)
		aw_ent_name.delete(0, END)
		aw_ent_esal.delete(0, END)
	elif int(aw_ent_esal.get()) < 0:
		showerror("OOPS!", "Salary can't be negative")
		aw_ent_id.delete(0, END)
		aw_ent_name.delete(0, END)
		aw_ent_esal.delete(0, END)
	elif int(aw_ent_esal.get()) < 8000:
		showerror("OOPS!", "Salary can't be less than 8000")
		aw_ent_id.delete(0, END)
		aw_ent_name.delete(0, END)
		aw_ent_esal.delete(0, END)
	else:
		con=None
		try:
			con=connect('employee1.db')
			cursor=con.cursor()
			sql="insert into emp values('%d','%s','%d')"
			id=int(aw_ent_id.get())
			name=aw_ent_name.get()
			esal=int(aw_ent_esal.get())
			cursor.execute(sql%(id,name,esal))
			con.commit()
			showinfo("Summit","record added")
			aw_ent_id.delete(0,END)
			aw_ent_name.delete(0,END)
			aw_ent_esal.delete(0,END)
		except Exception:
			showerror("Failure","Id Already Exists")
			aw_ent_id.delete(0,END)
			aw_ent_name.delete(0,END)
			aw_ent_esal.delete(0,END)
			con.rollback()
		finally:
			if con is not None:
				con.close()
def add_close():
	main_window.deiconify()
	add_window.withdraw()
#-----------------------------------------View Function------------------------------------------------------------------------------
def view_open():
	view_window.deiconify()
	main_window.withdraw()
	vw_emp_data.delete(1.0,END)
	info=""
	con=None
	try:
		con=connect('employee1.db')
		cursor=con.cursor()
		sql="select * from emp"
		cursor.execute(sql)
		data=cursor.fetchall()
		if data == []:
			showinfo("Message", "No record available")
			if con is not None:
				con.close()
			main_window.deiconify()
			view_window.withdraw()					
		else:	
			for d in data:
				info=info + "id: " + str(d[0])+"  " + "name: " + str(d[1])+"  "+"salary: "+ str(d[2])+"\n"
		vw_emp_data.insert(INSERT,info)
	except Exception as e :
		showerror("Failure",e)
	finally:
		if con is not None:
			con.close()
def view_close():
	main_window.deiconify()
	view_window.withdraw()

#-----------------------------------------Update Function------------------------------------------------------------------------------
def update_open():
	update_window.deiconify()
	main_window.withdraw()
def update():
	if (uw_ent_id.get() == "" or uw_ent_name.get() == "" or uw_ent_esal.get() == ""):
		showerror("OOPS!", "Please fill all the details")
	elif (uw_ent_id.get().isdigit() == False):
		showerror("OOPS!", "Id can have integers only")
		uw_ent_id.delete(0, END)
		uw_ent_name.delete(0, END)
		uw_ent_esal.delete(0, END)
	elif (int(uw_ent_id.get()) <= 0) :
		showerror("OOPS!", "Id can't be negative")
		uw_ent_id.delete(0, END)
		uw_ent_name.delete(0, END)
		uw_ent_sal.delete(0, END)
	elif (len(uw_ent_name.get()) < 2):
		showerror("OOPS!", "Name can't consist of only one alphabet")
		uw_ent_id.delete(0, END)
		uw_ent_name.delete(0, END)
		uw_ent_esal.delete(0, END)
	elif ((((uw_ent_name.get()).replace(" ","")).isalpha()) == False):
		showerror("OOPS!", "Name can't consist of digits")
		uw_ent_id.delete(0, END)
		uw_ent_name.delete(0, END)
		uw_ent_esal.delete(0, END)
	elif (uw_ent_esal.get().isdigit() == False):
		showerror("OOPS!", "Salary can be in integer only")
		uw_ent_id.delete(0, END)
		uw_ent_name.delete(0, END)
		uw_ent_esal.delete(0, END)
	elif int(uw_ent_esal.get()) < 0:
		showerror("OOPS!", "Salary can't be negative")
		uw_ent_id.delete(0, END)
		uw_ent_name.delete(0, END)
		uw_ent_esal.delete(0, END)
	elif int(uw_ent_esal.get()) < 8000:
		showerror("OOPS!", "Salary can't be less than 8000")
		uw_ent_id.delete(0, END)
		uw_ent_name.delete(0, END)
		uw_ent_esal.delete(0, END)
	else:
		con=None
		try:
			con=connect('employee1.db')
			cursor=con.cursor()
			sql="update emp set name = '%s', esal = '%d' where id ='%d'"
			id=int(uw_ent_id.get())
			name=uw_ent_name.get()
			esal=int(uw_ent_esal.get())
			cursor.execute(sql % (name,esal,id))
			if cursor.rowcount > 0:
				con.commit()
				showinfo("Success", "Details updated successfully")
				uw_ent_id.delete(0, END)
				uw_ent_name.delete(0, END)
				uw_ent_esal.delete(0, END)
			else:
				showwarning("OOPS!", "Record does not exist")
				uw_ent_id.delete(0, END)
				uw_ent_name.delete(0, END)
				uw_ent_esal.delete(0, END)
		except Exception as e:
			showerror("Failure",e)
			uw_ent_id.delete(0, END)
			uw_ent_name.delete(0, END)
			uw_ent_esal.delete(0, END)
			con.rollback()
		finally:
			if con is not None:
				con.close()
def update_close():
	main_window.deiconify()
	update_window.withdraw()
#-----------------------------------------Delete Function------------------------------------------------------------------------------
def delete_open():
	delete_window.deiconify()
	main_window.withdraw()
def delete_record():
	con = None
	if (dw_ent_id.get() == ""):
		showerror("OOPS!", "Please enter Id")
	elif ((dw_ent_id.get()).isdigit() == False):
		showerror("OOPS!", "Id can consist of integers only")
		dw_ent_id.delete(0, END)
	elif (int(dw_ent_id.get()) <= 0):
		showerror("OOPS!", "Id can't be negative")
		dw_ent_id.delete(0, END)
	else:
		try:
			con=connect('employee1.db')
			cursor = con.cursor()
			sql = "delete from emp where id ='%d'"
			id = int(dw_ent_id.get())
			cursor.execute(sql % (id))
			if cursor.rowcount > 0:
				con.commit()
				showinfo("Success", "Employee deleted successfully :)")
				dw_ent_id.delete(0, END)
			else:
				showerror("Failure", "Employee does not exist")
				dw_ent_id.delete(0, END)
		except Exception as e:
			showerror("OOPS!", e)
			dw_ent_id.delete(0, END)
		finally:
			if con is not None:
				con.close()
def delete_close():
	main_window.deiconify()
	delete_window.withdraw()

#-----------------------------------------Chart function------------------------------------------------------------------------------
def chart_open():
	chart_window.deiconify()
	main_window.withdraw()
def chart():
	list_name = []	
	list_esal = []
	con=None
	try:
		con=connect('employee1.db')
		cursor=con.cursor()
		sql="select name from emp group by name order by esal desc limit 5"
		cursor.execute(sql)
		data=cursor.fetchall()
		for d in data:	
			list_name.append(str(d[0]))
			#print(list_name)
	except Exception as e:
		showerror("Error", e)
	finally:
		if con is not None:
			con.close()

	con=None
	try:
		con=connect('employee1.db')
		cursor=con.cursor()
		sql="select esal from emp group by esal order by esal desc limit 5"
		cursor.execute(sql)
		data=cursor.fetchall()
		for d in data:	
			list_esal.append(int(str(d[0])))
	except Exception as e:
		showerror("Error", e)
	finally:
		if con is not None:
			con.close()


	plt.bar(list_name, list_esal, width = 0.6, color = ['red', 'green', 'cyan', 'orange','blue'])
	plt.title("Top 5 Highest Salary Persons")
	plt.xlabel("Employees")
	plt.ylabel("Salary")

	plt.show()
		
def chart_close():
	main_window.deiconify()
	chart_window.withdraw()



	
#-----------------------------------------Main Window------------------------------------------------------------------------------	
f=("Arial",20,"bold")
main_window=Tk()
main_window.geometry("500x500")
main_window.title("E. M. S.")
main_window.configure(bg='#000028')


mw_btn_add  = Button(main_window,text = " Add ", font=f,bd=4, width=10,command=add_open)
mw_btn_view = Button(main_window,text = " View ", font=f,bd=4, width=10,command=view_open)
mw_btn_update=Button(main_window,text = " Update ", font=f,bd=4, width=10,command=update_open)
mw_btn_delete=Button(main_window,text = " Delete ", font=f,bd=4, width=10,command=delete_open)
mw_btn_chart=Button(main_window,text = " Charts ", font=f, bd=4,width=10,command=chart_open)
mw_lbl_quote=Label(main_window,text="QOTD:  "+qotd,font=f,bg='#4bf29c',wraplength = 500)

mw_btn_add.pack(pady=5)
mw_btn_view.pack(pady=5)
mw_btn_update.pack(pady=5)
mw_btn_delete.pack(pady=5)
mw_btn_chart.pack(pady=5)
mw_lbl_quote.pack(pady=5)

#-----------------------------------------Add Window------------------------------------------------------------------------------	
add_window = Toplevel(main_window)
add_window.geometry("500x500")
add_window.title("Add Emp.")
add_window.withdraw()
add_window.configure(bg='#000028')

aw_lbl_id=Label(add_window,text="enter Id: ",bg='#000028',fg='#00FFFF',font=f)
aw_ent_id=Entry(add_window,font=f,bd=4)
aw_lbl_name=Label(add_window,text="enter name: ",bg='#000028',fg='#00FFFF',font=f)
aw_ent_name=Entry(add_window,font=f,bd=4)
aw_lbl_esal=Label(add_window,text="enter salary: ",bg='#000028',fg='#00FFFF',font=f)
aw_ent_esal=Entry(add_window,font=f,bd=4)
aw_btn_save=Button(add_window,text="Save",width=10,bd=4,font=f,command=add_student)
aw_btn_back=Button(add_window,text="Back",width=10,bd=4,font=f,command=add_close)

aw_lbl_id.pack(pady=5)
aw_ent_id.pack(pady=5)
aw_lbl_name.pack(pady=5)
aw_ent_name.pack(pady=5)
aw_lbl_esal.pack(pady=5)
aw_ent_esal.pack(pady=5)
aw_btn_save.pack(pady=5)
aw_btn_back.pack(pady=5)

#-----------------------------------------View Window------------------------------------------------------------------------------
view_window = Toplevel(main_window)
view_window.geometry("500x500")
view_window.title("View Emp")
view_window.configure(bg='#000028')

vw_emp_data=ScrolledText(view_window,width=30,height=10,font=f)
vw_btn_back=Button(view_window,text="Back",width=10,bd=4,font=f,command=view_close)
vw_emp_data.pack(pady=5)
vw_btn_back.pack(pady=5)
view_window.withdraw()

#-----------------------------------------Update Window------------------------------------------------------------------------------
update_window = Toplevel(main_window)
update_window.geometry("500x500")
update_window.title("Update Emp")
update_window.configure(bg='#000028')

uw_lbl_id=Label(update_window,text="enter id: ",bg='#000028',fg='#00FFFF',font=f)
uw_ent_id=Entry(update_window,font=f,bd=4)
uw_lbl_name=Label(update_window,text="enter name: ",bg='#000028',fg='#00FFFF',font=f)
uw_ent_name=Entry(update_window,font=f,bd=4)
uw_lbl_esal=Label(update_window,text="enter salary: ",bg='#000028',fg='#00FFFF',font=f)
uw_ent_esal=Entry(update_window,font=f,bd=4)
uw_btn_save=Button(update_window,text="Save",width=10,bd=4,font=f,command=update)
uw_btn_back=Button(update_window,text="Back",width=10,bd=4,font=f,command=update_close)

uw_lbl_id.pack(pady=5)
uw_ent_id.pack(pady=5)
uw_lbl_name.pack(pady=5)
uw_ent_name.pack(pady=5)
uw_lbl_esal.pack(pady=5)
uw_ent_esal.pack(pady=5)
uw_btn_save.pack(pady=5)
uw_btn_back.pack(pady=5)
update_window.withdraw()

#-----------------------------------------Delete Window------------------------------------------------------------------------------
delete_window = Toplevel(main_window)
delete_window.geometry("500x500")
delete_window.title("Delete Emp")
delete_window.configure(bg='#000028')

dw_lbl_id=Label(delete_window,text="enter id:",bg='#000028',fg='#00FFFF',font=f)
dw_ent_id=Entry(delete_window,font=f,bd=4)
dw_btn_save=Button(delete_window,text="Save",width=10,bd=4,font=f,command=delete_record)
dw_btn_back=Button(delete_window,text="Back",width=10,bd=4,font=f,command=delete_close)

dw_lbl_id.pack(pady=5)
dw_ent_id.pack(pady=5)
dw_btn_save.pack(pady=5)
dw_btn_back.pack(pady=5)
delete_window.withdraw()

#-----------------------------------------Chart Window------------------------------------------------------------------------------
chart_window = Toplevel(main_window)
chart_window.geometry("500x500")
chart_window.title("Chart")
chart_window.configure(bg='#000028')

cw_btn_chart = Button(chart_window, text = 'Charts',bd=4, font=f, width = 10, command = chart)
cw_btn_chart.pack(pady = 5)
cw_btn_back=Button(chart_window,text="Back",bd=4,width=10,font=f,command=chart_close)
cw_btn_back.pack(pady=5)
chart_window.withdraw()

main_window.mainloop()