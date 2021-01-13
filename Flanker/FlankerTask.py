#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on Tue Jan 12 15:23:47 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

prac_rat = [0.25, 0.25, 0.25, 0.25];
prac_trls = 24;
prac_thresh = 11;
fast_thresh = 4;
prac_errors = 0;

# RC, RI, LC, LI
stim_nums = [0, 1, 2, 3];
stim_names = ['Flanker_white_congruent_right', 'Flanker_white_incongruent_right', 'Flanker_white_congruent_left', 'Flanker_white_incongruent_left'];

# feedback
feedback_names = ['Incorrect_Frowny', 'Correct_Smiley'];
feedback_times = [0.69, 1];

# slow or fast
#stim_lens = [0.25, 0.3];
#resp_lens = [0.5, 0.6];
stim_lens = [1, 2];
resp_lens = [1, 2];
fs = 1; # 0 for fast, 1 for slow


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'FlankerTask'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/llevinson/Documents/SCH_Anxiety_Tasks/Flanker/FlankerTask.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instr = visual.TextStim(win=win, name='instr',
    text='Press the right button if the middle fish is pointing right and the left button if the middle fish is pointing left.\n\n(click anywhere to continue)',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
cont_instr = event.Mouse(win=win)
x, y = [None, None]
cont_instr.mouseClock = core.Clock()

# Initialize components for Routine "practice_go"
practice_goClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text="Let's practice!\n\n(click anywhere to continue)",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
cont_prac = event.Mouse(win=win)
x, y = [None, None]
cont_prac.mouseClock = core.Clock()

# Initialize components for Routine "fix"
fixClock = core.Clock()
fix_cross = visual.TextStim(win=win, name='fix_cross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "blank_pre"
blank_preClock = core.Clock()
blank1 = visual.TextStim(win=win, name='blank1',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "stimulus_pres"
stimulus_presClock = core.Clock()
prac_ord_n = [[stim_nums[i]]*round(prac_rat[i]*prac_trls) for i in list(range(4))];
prac_ord = [];
for sublist in prac_ord_n:
    for item in sublist:
        prac_ord.append(item)
shuffle(prac_ord);
stimulus = visual.ImageStim(
    win=win,
    name='stimulus', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, 0.23),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "blank_post"
blank_postClock = core.Clock()
blank3 = visual.TextStim(win=win, name='blank3',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
feedback_image = visual.ImageStim(
    win=win,
    name='feedback_image', 
    image='Images/' + feedback_names[fnum] + '.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# Initialize components for Routine "blank_post_2"
blank_post_2Clock = core.Clock()
blank4 = visual.TextStim(win=win, name='blank4',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the cont_instr
gotValidClick = False  # until a click is received
# keep track of which components have finished
instructionsComponents = [instr, cont_instr]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr* updates
    if instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr.frameNStart = frameN  # exact frame index
        instr.tStart = t  # local t and not account for scr refresh
        instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr, 'tStartRefresh')  # time at next scr refresh
        instr.setAutoDraw(True)
    # *cont_instr* updates
    if cont_instr.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cont_instr.frameNStart = frameN  # exact frame index
        cont_instr.tStart = t  # local t and not account for scr refresh
        cont_instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cont_instr, 'tStartRefresh')  # time at next scr refresh
        cont_instr.status = STARTED
        cont_instr.mouseClock.reset()
        prevButtonState = cont_instr.getPressed()  # if button is down already this ISN'T a new click
    if cont_instr.status == STARTED:  # only update if started and not finished!
        buttons = cont_instr.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # abort routine on response
                continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr.started', instr.tStartRefresh)
thisExp.addData('instr.stopped', instr.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = cont_instr.getPos()
buttons = cont_instr.getPressed()
thisExp.addData('cont_instr.x', x)
thisExp.addData('cont_instr.y', y)
thisExp.addData('cont_instr.leftButton', buttons[0])
thisExp.addData('cont_instr.midButton', buttons[1])
thisExp.addData('cont_instr.rightButton', buttons[2])
thisExp.addData('cont_instr.started', cont_instr.tStart)
thisExp.addData('cont_instr.stopped', cont_instr.tStop)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practice_go"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the cont_prac
gotValidClick = False  # until a click is received
# keep track of which components have finished
practice_goComponents = [text, cont_prac]
for thisComponent in practice_goComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice_goClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practice_go"-------
while continueRoutine:
    # get current time
    t = practice_goClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice_goClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    # *cont_prac* updates
    if cont_prac.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cont_prac.frameNStart = frameN  # exact frame index
        cont_prac.tStart = t  # local t and not account for scr refresh
        cont_prac.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cont_prac, 'tStartRefresh')  # time at next scr refresh
        cont_prac.status = STARTED
        cont_prac.mouseClock.reset()
        prevButtonState = cont_prac.getPressed()  # if button is down already this ISN'T a new click
    if cont_prac.status == STARTED:  # only update if started and not finished!
        buttons = cont_prac.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # abort routine on response
                continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_goComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_go"-------
for thisComponent in practice_goComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = cont_prac.getPos()
buttons = cont_prac.getPressed()
thisExp.addData('cont_prac.x', x)
thisExp.addData('cont_prac.y', y)
thisExp.addData('cont_prac.leftButton', buttons[0])
thisExp.addData('cont_prac.midButton', buttons[1])
thisExp.addData('cont_prac.rightButton', buttons[2])
thisExp.addData('cont_prac.started', cont_prac.tStart)
thisExp.addData('cont_prac.stopped', cont_prac.tStop)
thisExp.nextEntry()
# the Routine "practice_go" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice = data.TrialHandler(nReps=24, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='practice')
thisExp.addLoop(practice)  # add the loop to the experiment
thisPractice = practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
if thisPractice != None:
    for paramName in thisPractice:
        exec('{} = thisPractice[paramName]'.format(paramName))

for thisPractice in practice:
    currentLoop = practice
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice:
            exec('{} = thisPractice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fix"-------
    continueRoutine = True
    routineTimer.add(0.190000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixComponents = [fix_cross]
    for thisComponent in fixComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fix"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_cross* updates
        if fix_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_cross.frameNStart = frameN  # exact frame index
            fix_cross.tStart = t  # local t and not account for scr refresh
            fix_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_cross, 'tStartRefresh')  # time at next scr refresh
            fix_cross.setAutoDraw(True)
        if fix_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_cross.tStartRefresh + .190-frameTolerance:
                # keep track of stop time/frame for later
                fix_cross.tStop = t  # not accounting for scr refresh
                fix_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_cross, 'tStopRefresh')  # time at next scr refresh
                fix_cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fix"-------
    for thisComponent in fixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice.addData('fix_cross.started', fix_cross.tStartRefresh)
    practice.addData('fix_cross.stopped', fix_cross.tStopRefresh)
    
    # ------Prepare to start Routine "blank_pre"-------
    continueRoutine = True
    routineTimer.add(0.040000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank_preComponents = [blank1]
    for thisComponent in blank_preComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank_preClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank_pre"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank_preClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank_preClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank1* updates
        if blank1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank1.frameNStart = frameN  # exact frame index
            blank1.tStart = t  # local t and not account for scr refresh
            blank1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank1, 'tStartRefresh')  # time at next scr refresh
            blank1.setAutoDraw(True)
        if blank1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank1.tStartRefresh + .04-frameTolerance:
                # keep track of stop time/frame for later
                blank1.tStop = t  # not accounting for scr refresh
                blank1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank1, 'tStopRefresh')  # time at next scr refresh
                blank1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank_preComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank_pre"-------
    for thisComponent in blank_preComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice.addData('blank1.started', blank1.tStartRefresh)
    practice.addData('blank1.stopped', blank1.tStopRefresh)
    
    # ------Prepare to start Routine "stimulus_pres"-------
    continueRoutine = True
    # update component parameters for each repeat
    trl_num = prac_ord[practice.thisRepN];
    if trl_num < 2:
        corans = 'right';
    else:
        corans = 'left';
    stimulus.setImage('Images/' + stim_names[prac_ord[practice.thisRepN]] + '.jpg')
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    stimulus_presComponents = [stimulus, key_resp]
    for thisComponent in stimulus_presComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stimulus_presClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "stimulus_pres"-------
    while continueRoutine:
        # get current time
        t = stimulus_presClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stimulus_presClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimulus* updates
        if stimulus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stimulus.frameNStart = frameN  # exact frame index
            stimulus.tStart = t  # local t and not account for scr refresh
            stimulus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimulus, 'tStartRefresh')  # time at next scr refresh
            stimulus.setAutoDraw(True)
        if stimulus.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimulus.tStartRefresh + stim_lens[fs]-frameTolerance:
                # keep track of stop time/frame for later
                stimulus.tStop = t  # not accounting for scr refresh
                stimulus.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimulus, 'tStopRefresh')  # time at next scr refresh
                stimulus.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + stim_lens[fs] + resp_lens[fs]-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[0].name  # just the first key pressed
                key_resp.rt = _key_resp_allKeys[0].rt
                # was this correct?
                if (key_resp.keys == str(corans)) or (key_resp.keys == corans):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimulus_presComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimulus_pres"-------
    for thisComponent in stimulus_presComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if not key_resp.keys:
        fnum = 0;
    elif key_resp.corr:
        fnum = 1;
    else:
        fnum = 0;
    practice.addData('stimulus.started', stimulus.tStartRefresh)
    practice.addData('stimulus.stopped', stimulus.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(corans).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for practice (TrialHandler)
    practice.addData('key_resp.keys',key_resp.keys)
    practice.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        practice.addData('key_resp.rt', key_resp.rt)
    practice.addData('key_resp.started', key_resp.tStartRefresh)
    practice.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "stimulus_pres" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank_post"-------
    continueRoutine = True
    routineTimer.add(0.640000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank_postComponents = [blank3]
    for thisComponent in blank_postComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank_postClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank_post"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank_postClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank_postClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank3* updates
        if blank3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank3.frameNStart = frameN  # exact frame index
            blank3.tStart = t  # local t and not account for scr refresh
            blank3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank3, 'tStartRefresh')  # time at next scr refresh
            blank3.setAutoDraw(True)
        if blank3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank3.tStartRefresh + 0.64-frameTolerance:
                # keep track of stop time/frame for later
                blank3.tStop = t  # not accounting for scr refresh
                blank3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank3, 'tStopRefresh')  # time at next scr refresh
                blank3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank_postComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank_post"-------
    for thisComponent in blank_postComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice.addData('blank3.started', blank3.tStartRefresh)
    practice.addData('blank3.stopped', blank3.tStopRefresh)
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    feedbackComponents = [feedback_image]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_image* updates
        if feedback_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_image.frameNStart = frameN  # exact frame index
            feedback_image.tStart = t  # local t and not account for scr refresh
            feedback_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_image, 'tStartRefresh')  # time at next scr refresh
            feedback_image.setAutoDraw(True)
        if feedback_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_image.tStartRefresh + feedback_times[fnum]-frameTolerance:
                # keep track of stop time/frame for later
                feedback_image.tStop = t  # not accounting for scr refresh
                feedback_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback_image, 'tStopRefresh')  # time at next scr refresh
                feedback_image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice.addData('feedback_image.started', feedback_image.tStartRefresh)
    practice.addData('feedback_image.stopped', feedback_image.tStopRefresh)
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank_post_2"-------
    continueRoutine = True
    routineTimer.add(0.090000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank_post_2Components = [blank4]
    for thisComponent in blank_post_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank_post_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank_post_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank_post_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank_post_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank4* updates
        if blank4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank4.frameNStart = frameN  # exact frame index
            blank4.tStart = t  # local t and not account for scr refresh
            blank4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank4, 'tStartRefresh')  # time at next scr refresh
            blank4.setAutoDraw(True)
        if blank4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank4.tStartRefresh + 0.09-frameTolerance:
                # keep track of stop time/frame for later
                blank4.tStop = t  # not accounting for scr refresh
                blank4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank4, 'tStopRefresh')  # time at next scr refresh
                blank4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank_post_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank_post_2"-------
    for thisComponent in blank_post_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice.addData('blank4.started', blank4.tStartRefresh)
    practice.addData('blank4.stopped', blank4.tStopRefresh)
# completed 24 repeats of 'practice'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
