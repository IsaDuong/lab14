#########################################
#
#    100pt - Putting it together!
#
#########################################

# Animate the target area to bounce from left to right.
# Add in buttons for movement left, right, up and down
# Add in boundary detection for the edges (don't let the player move off screen)
# Add in colision detection - and STOP the target when you catch it!

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="red")
player = drawpad.create_rectangle(240,240,260,260, fill="white")
targetMove = True

class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1)
		self.button1.configure(text="Up", background= "white")
		self.button1.grid(row=0,column=1)
		
		self.button2 = Button(self.myContainer1)
		self.button2.configure(text="Down", background= "white")
		self.button2.grid(row=3,column=1)
		
		self.button3 = Button(self.myContainer1)
		self.button3.configure(text="Left", background= "white")
		self.button3.grid(row=1,column=0)
		
		self.button4 = Button(self.myContainer1)
		self.button4.configure(text="Right", background= "white")
		self.button4.grid(row=1,column=2)
		
					
		# "Bind" an action to the first button												
		self.button1.bind("<Button-1>", self.button1Click)
		self.button2.bind("<Button-1>", self.button2Click)
		self.button3.bind("<Button-1>", self.button3Click)
		self.button4.bind("<Button-1>", self.button4Click)
		  
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		self.animate()
		
	def animate(self):
	    global target
	    global direction
	    targetx1,targety1,targetx2,targety2 = drawpad.coords(target)
	    
            if targetx1 < -2:
		direction = -5
            elif targetx2 > drawpad.winfo_width():
                direction = 5
            drawpad.move(target,direction,0)
            drawpad.after(10,self.animate)
		
	def button1Click(self, event):   
                # "global" makes sure that we can access our oval and our drawpad
		global oval
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
                if y1<320:
                    drawpad.move(player,0,-10)
                elif y1>320:
                    drawpad.move(player,0,0)
                
        def button2Click(self, event):   
		global oval
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
                drawpad.move(player,0,10)
                
        def button3Click(self, event):
		global oval
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
                drawpad.move(player,-10,0)
                
        def button4Click(self, event):
		global oval
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
                drawpad.move(player,10,0)
                
		# Get the coords of our target


		# Ensure that we are doing our collision detection
		# After we move our object!
                didWeHit = collisionDetect()
                if(didWeHit == True):
                    # We made contact! Stop our animation!
                    print "Do something"
	# Use a function to do our collision detection
	# This way we only have to write it once, and call it from
	# every button click function.
	def collisionDetect(self):
                global target
		global drawpad
		global player
                x1,y1,x2,y2 = drawpad.coords(player)
                targetx1,targety1,targetx2,targety2 = drawpad.coords(target)
                if (playerx1>targetx1 and playerx2<targetx2) and (playery1>targety1 and playery2<targety2):
                    targetMove = False
                else:
                    targetMove = True

                # Do your if statement - remember to return True if successful!
                
	    
		
myapp = MyApp(root)

root.mainloop()