from psychopy import visual, core, event, gui
import os, random

'''constants'''

#Subject Gui
subinfo={"Participant ID": ''}
        
if not gui.DlgFromDict(dictionary=subinfo, order=["Participant ID"]).OK:
    core.quit()

#window 
mywin= visual.Window((),monitor="testMonitor",units="deg",fullscr=True,)
#mouse
mouse=event.Mouse(visible=True,newPos=(0,0),win=mywin)

#fixation Cross
fixation = visual.GratingStim(win=mywin, size=0.15, pos=[0,0], units= 'deg', rgb=[.5])

#write/load paths
basepath=os.path.normpath(os.getcwd() + os.sep + os.pardir)
img_path=os.path.join(basepath, 'Images')+'\\'
data_path=os.path.join(basepath, 'Data')+'\\'

#lines
line1 = visual.Line(win=mywin,units="deg",lineColor=[-1, -1, -1],start=[-12,-10],end=[-12,10])
line2 = visual.Line(win=mywin,units="deg",lineColor=[-1, -1, -1],start=[-12,-10],end=[10,-10])

#labels Axis
text1=visual.TextStim(mywin, text='Popularity', pos=(-1, -10.5), color=[1.0, 1.0, 1.0],ori=0)
text2=visual.TextStim(mywin, text='Competence', pos=(-13,0), color=[1.0,1.0,1.0],ori=-90)
text3=visual.TextStim(mywin, text='Low', pos=(-13,-10.5), color=[1.0,1.0,1.0],ori=0)
text4=visual.TextStim(mywin, text='High', pos=(9,-10.5), color=[1.0,1.0,1.0],ori=0)
text5=visual.TextStim(mywin, text='High', pos=(-13,9), color=[1.0,1.0,1.0],ori=-90)

#load in faces and intialize positions 
picPos=[(-15, 8.5),(-15, 6),(-15, 3.5),(-15, 1),(-15, -1.5),(-15, -4),(-15, -6.5),(-15, -9),
(-17, 8.5),(-17, 6),(-17, 3.5),(-17, 1),(-17, -1.5),(-17, -4),(-17, -6.5),(-17, -9)]

#shuffle list for randomization
random.shuffle(picPos)
pics=[img_path+pic for pic in os.listdir(img_path) if str(pic).endswith('.jpg')]
faces=[visual.ImageStim(mywin,image=f[0],color=(1,1,1), size=[2.5, 2.5], pos =f[1], name=f[0][-6:-4]) for f in zip(pics,picPos)]


'''Functions'''
def draw_list(l):
    for item in l:
        item.draw()

def get_list_pos(x):
#save everything in x,y coors then name
    save_list=[]
    savFrac= open(data_path+subinfo['Participant ID']+'.txt', 'w')
    for item in x:
        save_list.append(str(item.pos[0]) +','+ str(item.pos[1]) + ',' + str(item.name))
    for t in save_list:
        savFrac.write("%s\n" % t)
    savFrac.close()


'''Call task'''
def Place_task():
    while True:
        if event.getKeys(['q', 'space']):
            break
        m1,m2,m3= mouse.getPressed()
# Draw Statements
        draw_list(faces)
        line1.draw()
        line2.draw()
        text1.draw()
        text2.draw()
        text3.draw()
        text4.draw()
        text5.draw()
        fixation.draw()
        
        mywin.flip()
        #Checks if image clicked then reset imgpos next click
        if m1:
            clicked=[ob for ob in faces if ob.contains(mouse)]
            if len(clicked)>0:
                event.mouseButtons=[0,0,0]
                img=clicked[-1]
                while True:
                    j,k,l=mouse.getPressed()
                    if j:
                        img.pos=mouse.getPos()
                        break 
                event.mouseButtons=[0,0,0]
                mouse.clickReset()

if __name__ == '__main__':
    Place_task()

get_list_pos(faces)