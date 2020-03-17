from tkinter import *
import tkinter.font as tkfont
from display import *
from internet import *
from app import new, last

class GUI():
	def __init__(self, item):
		self.root = Tk()

		self.liked = False
		self.item = item
		self.name = "Windows Spotlight"
		self.author = "made with ❤ by Shikher Srivastava"
		self.bg = '#000000'
		self.fg = '#eeeeee'

		self.root.like = PhotoImage(file='icons/heart.png')
		self.root.dislike = PhotoImage(file='icons/broken-heart.png')
		self.root.author = PhotoImage(file='icons/author.png')
		self.root.next = PhotoImage(file='icons/arrow-right.png')
		self.root.previous = PhotoImage(file='icons/arrow-left.png')
		self.root.outline = PhotoImage(file='icons/camera.png')
		self.root.bing = PhotoImage(file='icons/bing.png')

		self.root.overrideredirect(True)
		# self.root.attributes('-topmost', True)
		self.root.wm_attributes("-transparentcolor", "yellow")
		# self.root.config(bg=self.bg)
		self.root.attributes('-alpha', 0.75)
		
		self.frame1 = Frame((self.root), bg='yellow', width=70)
		self.frame2 = Frame((self.root), bg=self.bg)
		self.like_buttons = Frame(self.frame2, bg=self.bg)
		self.navigation_buttons = Frame(self.frame2, bg=self.bg)
		self.link_buttons = Frame(self.frame2, bg=self.bg)
		
		self.title_font = tkfont.Font(family='Helvetica',size=20,weight='bold')
		self.copyright_font = tkfont.Font(family='Helvetica',size=8,weight='bold')
		self.font = tkfont.Font(family='Helvetica',size=12,weight='bold')
		
		self.title = Label(self.frame2, text=self.name, bg=self.bg, fg=self.fg, font=self.title_font)
		# self.shikhersrivastava = Label( self.frame2,text=self.author , bg=self.bg, fg=self.fg, font=self.font)

		self.copyright = Label(self.frame2, bg=self.bg, fg=self.fg, font=self.font)
		self.copyright = Label(self.frame2, bg=self.bg, fg=self.fg, font=self.copyright_font)

		self.outline = Button((self.frame1), image=self.root.outline, bg='#ffff00', fg='black', width=280, cursor='hand2', font=self.title_font, command=lambda: self.like(), borderwidth=0)
		
		
		self.like_button = Button((self.like_buttons), text="Like", image=self.root.like, bg=self.bg, fg='black', cursor='hand2',font=self.font, command=lambda: self.like())

		self.dislike_button = Button((self.like_buttons), text='Dislike', image=self.root.dislike, bg=self.bg, fg='black', cursor='hand2',font=self.font, command=lambda: self.dislike())

		self.prev_button = Button((self.navigation_buttons), text='Previous', image=self.root.previous, bg=self.bg, fg='black', cursor='hand2',font=self.font, command=lambda: self.previous())
		self.next_button = Button((self.navigation_buttons), text='Next', image=self.root.next, bg=self.bg, fg='black', cursor='hand2',font=self.font, command=lambda: self.next())
		
		self.bing_button = Button((self.link_buttons), text='Bing', image=self.root.bing, bg=self.bg, fg=self.fg, cursor='hand2',font=self.font, command=lambda: self.link(self.item["url"]))
		self.shikhersrivastava = Button((self.link_buttons), text=self.author, image=self.root.author, bg=self.bg, fg=self.fg, cursor='hand2', font=self.font, command=lambda: self.link("https://www.shikhersrivastava.com/windows-spotlight"))
		
		self.exit_button = Button((self.frame2), text='EXIT', bg="#000000", fg=self.fg, cursor='hand2',font=self.font, command=lambda: self.exit())
		
		self.outline.pack(side=TOP, fill=BOTH)

		# Hover Event
		self.frame1.bind('<Enter>', lambda event: self.enter(event))
		self.frame2.bind('<Leave>', lambda event: self.leave(event))

		
		self.width, self.height, self.y = get_resolution()
		self.title_width = self.title_font.measure(self.name)
		self.author_width = self.font.measure(self.author)
		self.root.geometry("%dx%d+%d+%d" % (40, 40, (self.width-41), self.y))

		self.title.pack(side=TOP, fill=BOTH)
		self.copyright.pack(side=TOP, fill=BOTH)
		self.like_button.pack(side=LEFT)
		self.dislike_button.pack(side=RIGHT)
		self.like_buttons.pack(side=TOP, fill=BOTH)
		self.navigation_buttons.pack(side=TOP, fill=BOTH)
		self.link_buttons.pack(side=TOP, fill=BOTH)
		self.bing_button.pack(side=LEFT, fill=BOTH)
		self.shikhersrivastava.pack(side=RIGHT, fill=BOTH)
		self.exit_button.pack(side=BOTTOM, fill=BOTH)

		self.prev_button.pack(side=LEFT, fill=BOTH)
		self.next_button.pack(side=RIGHT, fill=BOTH)

		self.outline.pack()
		self.frame1.pack()

		self.root.mainloop()

	# Utility Functions 
	def set_text(self):
		title= self.item['title']
		self.title.config(text=self.item['title'])
		self.title_width = self.title_font.measure(title)	
		copyright= self.item['copyright']
		self.copyright.config(text=copyright)
		self.copyright_width = self.copyright_font.measure(copyright)
	
	# Callback functions
	def link(self, url):
		print("LINK")
		open_link(url)
	
	def like(self):
		print("LIKE")
		# self.like_button.config(state="disabled")
		# self.dislike_button.config(state="normal")
		like(self.item)
		self.liked = True
		self.update()

	def dislike(self):
		print("DISLIKE")
		# self.dislike_button.config(image=self.root.dislike)
		dislike(self.item)
		self.liked = False
		# self.like_button.config(state="normal")
		# self.dislike_button.config(state="disabled")
		item = self.next()
		self.update()
		# self.item = item
		# self.set_text()
		# self.root.destroy()

	def previous(self):
		print("PREVIOUS")
		self.item = last()
		self.set_text()
		self.update()

	def next(self):
		print('NEXT')
		self.item = new()
		self.set_text()
		self.liked = False
		self.update()

	def exit(self):
		self.root.destroy()

	# Hover Effects	
	def enter(self, event):
		# on Hover display like and dislike buttons
		self.frame1.pack_forget()
		self.set_text()
		self.frame2.pack()
		self.update()
		# self.root.geometry("%dx%d+%d+%d" % (280, 230, (self.width-m_len), self.y))
		# self.root.winfo_toplevel().wm_geometry("")


	def leave(self, event):
		# on Hover Stop hide like and dislike buttons
		self.frame2.pack_forget()
		self.frame1.pack()
		self.root.geometry("%dx%d+%d+%d" % (40, 40, (self.width-41), self.y))
		# self.root.winfo_toplevel().wm_geometry("")

	def update(self):
		if self.liked:
			self.like_button.config(state="disabled")
		else:
			self.like_button.config(state="normal")
		net_width = max([self.copyright_width, self.title_width, self.author_width]) + 20
		self.like_button.config(width=net_width/2)
		self.dislike_button.config(width=net_width/2)
		self.prev_button.config(width=net_width/2)
		self.next_button.config(width=net_width/2)
		self.bing_button.config(width=net_width/2)
		self.shikhersrivastava.config(width=net_width/2)
		self.root.geometry("%dx%d+%d+%d" % (net_width, 300, (self.width-net_width), self.y))

# item = {
# 		"copyright_text": {"tx": "Michael Jackson, Mississipi"}, 
# 		"copyright_text": {"tx": "\u00a9 Kevin Carden / Adobe Stock"},
# 			"copyright_destination_url": {"t": "url", "u": "https://www.bing.com/search?q=triple+falls+north+carolina&filters=IsConversation%3a%22True%22+BTEPKey:%22Encyclo_WL_TripleFallsNCarolina%22&FORM=EMSDS0"}
# 		}
# GUI(item, item)