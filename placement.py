from psychopy import visual, core, event

"""Creates window"""
mywin= visual.Window((800,600),monitor="testMonitor",units="deg",fullscr=True)
mouse=event.Mouse(visible=True,newPos=(0,0),win=mywin)
obclk=False

"""Draws the lines"""
line1 = visual.Line(
    win=mywin,
    units="deg",
    lineColor=[-1, -1, -1])

line1.start = [-12, -10]
line1.end = [-12, 10]


line2 = visual.Line(
    win=mywin,
    units="deg",
    lineColor=[-1, -1, -1])

line2.start = [-12, -10]
line2.end = [10, -10]


"""Labels"""
text1=visual.TextStim(mywin, text='Popularity', pos=(-1, -10.5), color=[1.0, 1.0, 1.0],ori=0)
text1.draw()

text2=visual.TextStim(mywin, text='Competence', pos=(-13,0), color=[1.0,1.0,1.0],ori=-90)
text2.draw()

text3=visual.TextStim(mywin, text='Low', pos=(-13,-10.5), color=[1.0,1.0,1.0],ori=0)
text3.draw()

text4=visual.TextStim(mywin, text='High', pos=(9,-10.5), color=[1.0,1.0,1.0],ori=0)
text4.draw()

text5=visual.TextStim(mywin, text='High', pos=(-13,9), color=[1.0,1.0,1.0],ori=-90)
text5.draw()

"""Places IMG"""
img1 = visual.ImageStim(mywin,image="face1.jpg",\
                    color=(1,1,1), size=[2.5, 2.5], \
                    pos = (-15, 8.5))

img2 = visual.ImageStim(mywin,image="face2.jpg",\
                    color=(1,1,1), size=[2.5, 2.5], \
                    pos = (-15, 6))

img3 = visual.ImageStim(mywin,image="face3.jpg",\
                    color=(1,1,1), size=[2.5, 2.5], \
                    pos = (-15, 3.5))

img4 = visual.ImageStim(mywin,image="face4.jpg",\
                    color=(1,1,1), size=[2.5, 2.5], \
                    pos = (-15, 1))

img5 = visual.ImageStim(mywin,image="face5.jpg",\
                    color=(1,1,1), size=[2.5, 2.5], \
                    pos = (-15, -1.5))
                    
img6 = visual.ImageStim(mywin,image="face6.jpg",\
                    color=(1,1,1), size=[2.5, 2.5], \
                    pos = (-15, -4))

img7 = visual.ImageStim(mywin,image="face7.jpg",\
                    color=(1,1,1), size=[2.5, 2.5], \
                    pos = (-15, -6.5))

img8 = visual.ImageStim(mywin,image="face8.jpg",\
                    color=(1,1,1), size=[2.5, 2.5], \
                    pos = (-15, -9))

img9 = visual.ImageStim(mywin,image="face9.jpg",\
                    color=(1,1,1), size=[2.5, 2.5], \
                    pos = (-17, 8.5))

img10 = visual.ImageStim(mywin,image="face10.jpg",\
                    color=(1,1,1), size=[2.5, 2.5], \
                    pos = (-17, 6))
                    
img11 = visual.ImageStim(mywin,image="face11.jpg",\
                    color=(1,1,1), size=[2.5, 2.5], \
                    pos = (-17, 3.5))

img12 = visual.ImageStim(mywin,image="face12.jpg",\
                    color=(1,1,1), size=[2.5, 2.5], \
                    pos = (-17, 1))

img13 = visual.ImageStim(mywin,image="face13.jpg",\
                    color=(1,1,1), size=[2.5, 2.5], \
                    pos = (-17, -1.5))

img14 = visual.ImageStim(mywin,image="face14.jpg",\
                    color=(1,1,1), size=[2.5, 2.5], \
                    pos = (-17, -4))

img15 = visual.ImageStim(mywin,image="face15.jpg",\
                    color=(1,1,1), size=[2.5, 2.5], \
                    pos = (-17, -6.5))
                    
img16 = visual.ImageStim(mywin,image="face16.jpg",\
                    color=(1,1,1), size=[2.5, 2.5], \
                    pos = (-17, -9))
img1.draw()
img2.draw()
img3.draw()
img4.draw()
img5.draw()
img6.draw()
img7.draw()
img8.draw()
img9.draw()
img10.draw()
img11.draw()
img12.draw()
img13.draw()
img14.draw()
img15.draw()
img16.draw()

obs = [img1,img2,img3,img4,img5,img6,img7,img8,img9,img10,img11,img12,img13,img14,img15,img16]
"""Move Img"""

def draw_list(l):
    for thing in l:
        thing.draw()

while True:
    if event.getKeys(['q', 'space']):
        break
    
    
    
    m1,m2,m3= mouse.getPressed()
    
    print m1
    

    #draw statements
    draw_list(obs)
    
    line1.draw()
    line2.draw()
    text1.draw()
    text2.draw()
    text3.draw()
    text4.draw()
    text5.draw()
    
    mywin.flip()
    
    if m1:
        clicked=[ob for ob in obs if ob.contains(mouse)]
        if len(clicked)>0:
            mouse.clickReset()

            img=clicked[-1]
            
            while True:
                j,k,l=mouse.getPressed()
                if j:
                    img.pos=mouse.getPos()
                    
                    break 
    
    
    event.clearEvents()
    mouse.clickReset()
    