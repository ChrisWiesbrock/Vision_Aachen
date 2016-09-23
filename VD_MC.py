 #!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Juli 06, 2016, at 09:18
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import glob

REPEATS=200

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'untitled.py'
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
 
expInfo['expName'] = expName
#imagedir=_thisDir+'\Stim1'
#imagedir=_thisDir+'\Stim2'
#imagedir=_thisDir+'\Stim3'
imagedir=_thisDir+'\Stim4'
image_list=glob.glob(imagedir+'\*.png')
#image_list=(0.6695,5.205,7)
print image_list
trialnumber=0
bias=np.zeros((REPEATS,4))
print len(bias)
last_choice=''
left=0
right=0
same=0
opposite=0
correct_trials=np.zeros((REPEATS,1))
reactiontime=np.zeros((REPEATS,1))
correctstim=''
orientation_difference=0
orientation=0
correct_trial=0
save_reactiontime=0
correct_orientation=0
orientation_range=8

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    )
win.mouseVisibile=False
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

image = visual.ImageStim(win=win, name='image',
    image=None, mask='circle',
    ori=0, pos=[-5, 0], units='cm', size=[7, 7],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image_2 = visual.ImageStim(win=win, name='image_2',
    image=None, mask='circle',
    ori=0, pos=[5, 0], units='cm', size=[7, 7],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
'''
image = visual.GratingStim(win=win, name='grating',
    tex=u'sin', mask='circle',
    ori=0, pos=[-5, 0], units='cm', size=[7, 7], sf=2.97, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
image_2 = visual.GratingStim(win=win, name='grating',
    tex=u'sin', mask='circle',
    ori=0, pos=[5, 0], units='cm', size=[7, 7], sf=2.97, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
'''
mouse = event.Mouse(win=win, visible=False)
x, y = [None, None]
cross = visual.ShapeStim(win=win, name='cross', units='cm',
    vertices=((0, -0.5), (0, 0.5), (0,0), (-0.5,0), (0.5, 0)),
    lineWidth=3,
    closeShape=False,
    lineColor='white'
)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=REPEATS, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(ISI)
    trialComponents.append(cross)
    trialComponents.append(image)
    trialComponents.append(image_2)
    trialComponents.append(mouse)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
            
    chosen_image=np.random.randint(0, high=len(image_list))
    #image.setSF(image_list[chosen_image])
    #image_2.setSF(image_list[chosen_image])
    image.setImage(image_list[chosen_image])
    image_2.setImage(image_list[chosen_image])
    trialnumber=trialnumber+1
    orientation_list=[0,45,90,135]
    orientation_list=(orientation_list)
    mouse.setPos((0,0))
    
    
    #bias correction
    
    
    if trialnumber<10:
        if np.random.uniform(0,high=100)<=50:
            orientation=orientation_list[np.random.randint(0,high=4,size=1)]
            image.setOri(orientation)
            orientation_difference=np.random.randint(0,high=orientation_range,size=1)
            correct_orientation=int(orientation+orientation_difference)
            image_2.setOri(correct_orientation)
            correctstim='right'
            
            
        if np.random.uniform(0,high=100)>50:
            orientation=orientation_list[np.random.randint(0,high=4,size=1)]
            image_2.setOri(orientation)
            orientation_difference=np.random.randint(0,high=orientation_range,size=1)
            correct_orientation=int(orientation+orientation_difference)
            image.setOri(correct_orientation)
            correctstim='left'
            
    
    if trialnumber>11:
        bias_left=np.abs(left)
        bias_right=np.abs(right)
        bias_same=np.abs(same)
        bias_opposite=np.abs(opposite)
        if np.abs(bias_left-bias_right)==np.abs(bias_same-bias_opposite):
            if np.random.uniform(0,high=100)<=50:
                orientation=orientation_list[np.random.randint(0,high=4,size=1)]
                image.setOri(orientation)
                orientation_difference=np.random.randint(0,high=orientation_range,size=1)
                correct_orientation=int(orientation+orientation_difference)
                image_2.setOri(correct_orientation)
                correctstim='right'
                
            
            if np.random.uniform(0,high=100)>50:
                orientation=orientation_list[np.random.randint(0,high=4,size=1)]
                image_2.setOri(orientation)
                orientation_difference=np.random.randint(0,high=orientation_range,size=1)
                correct_orientation=int(orientation+orientation_difference)
                image.setOri(correct_orientation)
                correctstim='left'
               
                
        if np.abs(bias_left-bias_right)>np.abs(bias_same-bias_opposite):
            if bias_left>bias_right:
                orientation=orientation_list[np.random.randint(0,high=4,size=1)]
                image.setOri(orientation)
                orientation_difference=np.random.randint(0,high=orientation_range,size=1)
                correct_orientation=int(orientation+orientation_difference)
                image_2.setOri(correct_orientation)
                correctstim='right'
                
            if bias_left<bias_right:
                orientation=orientation_list[np.random.randint(0,high=4,size=1)]
                image_2.setOri(orientation)
                orientation_difference=np.random.randint(0,high=orientation_range,size=1)
                correct_orientation=int(orientation+orientation_difference)
                image.setOri(correct_orientation)
                correctstim='left'
                
                
        if np.abs(bias_left-bias_right)<np.abs(bias_same-bias_opposite):
            if bias_same<bias_opposite:
                if last_choice=='left':
                    orientation=orientation_list[np.random.randint(0,high=4,size=1)]
                    image_2.setOri(orientation)
                    orientation_difference=np.random.randint(0,high=orientation_range,size=1)
                    correct_orientation=int(orientation+orientation_difference)
                    image.setOri(correct_orientation)
                    correctstim='left'
                    
                if last_choice=='right':
                    orientation=orientation_list[np.random.randint(0,high=4,size=1)]
                    image.setOri(orientation)
                    orientation_difference=np.random.randint(0,high=orientation_range,size=1)
                    correct_orientation=int(orientation+orientation_difference)
                    image_2.setOri(correct_orientation)
                    correctstim='right'
                   
            if bias_same>bias_opposite:
                if last_choice=='left':
                    orientation=int(orientation_list[np.random.randint(0,high=4,size=1)])
                    image.setOri(orientation)
                    orientation_difference=np.random.randint(0,high=orientation_range,size=1)
                    correct_orientation=int(orientation+orientation_difference)
                    image_2.setOri(correct_orientation)
                    correctstim='right'
                if last_choice=='right':
                    orientation=int(orientation_list[np.random.randint(0,high=4,size=1)])
                    image_2.setOri(orientation)
                    orientation_difference=np.random.randint(0,high=orientation_range,size=1)
                    correct_orientation=int(orientation+orientation_difference)
                    image.setOri(correct_orientation)
                    correctstim='left'
    
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        mouse.setPos((0,0))
        # update/draw components on each frame
        if image.contains(mouse)==True:
            bias[trialnumber-1,0]=1 #colloumnds in bias array: 0=left, 1=right, 2=same. 3=opposite
            bias[trialnumber-1,1]=0
            last_choice='left'
        if image_2.contains(mouse)==True:
            bias[trialnumber-1,0]=0
            bias[trialnumber-1,1]=1
            last_choice='right'
            
        # *cross* updates
        if t >= 0.5 and cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            cross.tStart = t  # underestimates by a little under one framef
            cross.frameNStart = frameN  # exact frame index
            cross.setAutoDraw(True)
        if cross.status == STARTED and t >= (0.5 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            cross.setAutoDraw(False)
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(0.5)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        # *image* updates
        if t >= 1.2 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        if image.status == STARTED and t >= (1 + (2-win.monitorFramePeriod*0.75)) or image.contains(mouse)==True or image_2.contains(mouse)==True: #most of one frame period left
            image.setAutoDraw(False)
            if image.contains(mouse):
                last_choice=='left'
                reactiontime[trialnumber-1]=0
                save_reactiontime=0
                if correctstim=='left' and trialnumber>0:
                    correct_trials[trialnumber-1]=1.
                    correct_trial=1.
                if correctstim=='right' and trialnumber>0:
                    correct_trial=0.

        # *image_2* updates
        if t >= 1.2 and image_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_2.tStart = t  # underestimates by a little under one frame
            image_2.frameNStart = frameN  # exact frame index
            image_2.setAutoDraw(True)
        if image_2.status == STARTED and t >= (1 + (2-win.monitorFramePeriod*0.75)) or image.contains(mouse)==True or image_2.contains(mouse)==True: #most of one frame period left
            image_2.setAutoDraw(False)
            if image_2.contains(mouse):
                last_choice=='right'
                reactiontime[trialnumber-1]=0
                save_reactiontime=0
                if correctstim=='right' and trialnumber>0:
                    correct_trials[trialnumber-1]=1.
                    correct_trial=1
                if correctstim=='left' and trialnumber>0:
                    correct_trial=0.
                    
        save_orientation=int(orientation)
        save_correct=int(correct_trial)
        save_difference=int(np.abs(correct_orientation-orientation))
        save_reactiontime=float(save_reactiontime)
           
        # *mouse* updates
        if t >= 0.0 and mouse.status == NOT_STARTED:
            # keep track of start time/frame for later
            mouse.tStart = t  # underestimates by a little under one frame
            mouse.frameNStart = frameN  # exact frame index
            mouse.status = STARTED
            mouse.setPos((0,0))
            event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'
        if mouse.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            mouse.status = STOPPED
        if mouse.status == STARTED:  # only update if started and not stopped!
            buttons = mouse.getPressed()
            if sum(buttons) > 0:  # ie if any button is pressed
                # abort routine on response
                continueRoutine = False
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(0.5)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    if bias[trialnumber-1,0]+bias[trialnumber-2,0]==2:
        bias[trialnumber-1,2]=1
    if bias[trialnumber-1,0]+bias[trialnumber-2,0]==1:
        bias[trialnumber-1,3]=1
    if bias[trialnumber-1,1]+bias[trialnumber-2,1]==2:
        bias[trialnumber-1,2]=1
    if bias[trialnumber-1,1]+bias[trialnumber-2,1]==1:
        bias[trialnumber-1,3]=1
    
    if trialnumber>10:
        left=np.sum(bias[trialnumber-11:trialnumber-1,0])
        right=np.sum(bias[trialnumber-11:trialnumber-1,1])
        same=np.sum(bias[trialnumber-11:trialnumber-1,2])
        opposite=np.sum(bias[trialnumber-11:trialnumber-1,3])
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('imagename', image_list[chosen_image])
    trials.addData('correct',save_correct)
    trials.addData('Difference',save_difference)
    trials.addData('reactiontime', save_reactiontime)
    trials.addData('orientation', save_orientation)
    thisExp.nextEntry()
    
# completed 5 repeats of 'trials'

win.close()
core.quit()
