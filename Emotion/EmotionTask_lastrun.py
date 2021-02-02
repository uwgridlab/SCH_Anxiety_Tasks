#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on Thu Jan 28 14:56:21 2021
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

# need pandas for dataframe functionality
import pandas as pd
# need serial for TTL generation
import serial
# excel file with image filenames and categories
df_sm = pd.read_excel('stimuli.xlsx')
# setup variables
cats = df_sm.Category.unique();
nums = list(range(len(cats)));
## calculate numtrls_tot and numruns options
cz = len(df_sm.Num.unique());
z = round(cz/len(cats));
if cz != len(df_sm):
    print('Warning: more spreadsheet entries than unique image indices');
numtrls_tot_opts = [cz*4, cz*8, cz*12, cz*16];
numruns_opts = [z, z*2, z*4];
# set defaults
numruns = numruns_opts[1];
numtrls_tot = numtrls_tot_opts[3];
numtrls_per = round(numtrls_tot/numruns);
# open serial port
ser = serial.Serial('/dev/tty.usbserial-AG0JFT5C', 19200, timeout = 1);


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'EmotionTask'  # from the Builder filename that created this script
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
    originPath='/Users/llevinson/Documents/SCH_Anxiety_Tasks/Emotion/EmotionTask_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1, 1, 1], colorSpace='rgb',
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

# Initialize components for Routine "settings"
settingsClock = core.Clock()
tot_trials = visual.Slider(win=win, name='tot_trials',
    size=(1.0, 0.05), pos=(0, 0.25), units=None,
    labels=[str(numtrls_tot_opts[i]) for i in list(range(4))], ticks=[0, 1, 2, 3],
    granularity=1, style=['rating'],
    color='black', font='HelveticaBold',
    flip=False, depth=-1)
exp_blocks = visual.Slider(win=win, name='exp_blocks',
    size=(1.0, 0.05), pos=(0, 0), units=None,
    labels=[str(numruns_opts[i]) for i in list(range(3))], ticks=[0, 1, 2],
    granularity=1, style=['radio'],
    color='black', font='HelveticaBold',
    flip=False, depth=-2)
trl_label = visual.TextStim(win=win, name='trl_label',
    text='# of Trials (default ' + str(numtrls_tot_opts[3]) +')',
    font='Arial',
    pos=(0, .31), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
block_label = visual.TextStim(win=win, name='block_label',
    text='# of Blocks (default ' + str(numruns_opts[1]) + ')',
    font='Arial',
    pos=(0, 0.06), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
report_label = visual.TextStim(win=win, name='report_label',
    text='default text',
    font='Arial',
    pos=(0, -.2), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
done = visual.TextStim(win=win, name='done',
    text='DONE',
    font='Arial',
    pos=(0, -.35), height=0.05, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
done_click = event.Mouse(win=win)
x, y = [None, None]
done_click.mouseClock = core.Clock()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instructions_text = visual.TextStim(win=win, name='instructions_text',
    text='Press the space bar when you see a house.\n\nClick anywhere when ready.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "pre"
preClock = core.Clock()
fix_cross = visual.ImageStim(
    win=win,
    name='fix_cross', 
    image='Images/fix_cross.png', mask=None,
    ori=0, pos=(0, 0), size=(0.05, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)

# Initialize components for Routine "test"
testClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
key_resp = keyboard.Keyboard()
sound_1 = sound.Sound('A', secs=0.1, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1)

# Initialize components for Routine "post"
postClock = core.Clock()
post_jittered_break = visual.TextStim(win=win, name='post_jittered_break',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "block_completed"
block_completedClock = core.Clock()
completed_text = visual.TextStim(win=win, name='completed_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
cont = event.Mouse(win=win)
x, y = [None, None]
cont.mouseClock = core.Clock()

# Initialize components for Routine "overall_completed"
overall_completedClock = core.Clock()
complete_and_exit = visual.TextStim(win=win, name='complete_and_exit',
    text='Thank you, you have finished the task!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "settings"-------
continueRoutine = True
# update component parameters for each repeat
# set defaults
tot_trials.markerPos = numtrls_tot;
exp_blocks.markerPos = 2;
tot_trials.reset()
exp_blocks.reset()
# setup some python lists for storing info about the done_click
done_click.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
settingsComponents = [tot_trials, exp_blocks, trl_label, block_label, report_label, done, done_click]
for thisComponent in settingsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
settingsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "settings"-------
while continueRoutine:
    # get current time
    t = settingsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=settingsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # update numruns and numtrls based on input
    if exp_blocks.getRating() is not None:
        numruns = numruns_opts[exp_blocks.getRating()];
    if tot_trials.getRating() is not None:
        numtrls_tot = round(numtrls_tot_opts[tot_trials.getRating()])
        numtrls_per = round(numtrls_tot/numruns);
    
    # *tot_trials* updates
    if tot_trials.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tot_trials.frameNStart = frameN  # exact frame index
        tot_trials.tStart = t  # local t and not account for scr refresh
        tot_trials.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tot_trials, 'tStartRefresh')  # time at next scr refresh
        tot_trials.setAutoDraw(True)
    
    # *exp_blocks* updates
    if exp_blocks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        exp_blocks.frameNStart = frameN  # exact frame index
        exp_blocks.tStart = t  # local t and not account for scr refresh
        exp_blocks.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(exp_blocks, 'tStartRefresh')  # time at next scr refresh
        exp_blocks.setAutoDraw(True)
    
    # *trl_label* updates
    if trl_label.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trl_label.frameNStart = frameN  # exact frame index
        trl_label.tStart = t  # local t and not account for scr refresh
        trl_label.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trl_label, 'tStartRefresh')  # time at next scr refresh
        trl_label.setAutoDraw(True)
    
    # *block_label* updates
    if block_label.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        block_label.frameNStart = frameN  # exact frame index
        block_label.tStart = t  # local t and not account for scr refresh
        block_label.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(block_label, 'tStartRefresh')  # time at next scr refresh
        block_label.setAutoDraw(True)
    
    # *report_label* updates
    if report_label.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        report_label.frameNStart = frameN  # exact frame index
        report_label.tStart = t  # local t and not account for scr refresh
        report_label.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(report_label, 'tStartRefresh')  # time at next scr refresh
        report_label.setAutoDraw(True)
    if report_label.status == STARTED:  # only update if drawing
        report_label.setText(str(numtrls_tot) + ' total trials split among ' + str(numruns) + ' blocks for ' + str(numtrls_per) + ' trials per block.')
    
    # *done* updates
    if done.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        done.frameNStart = frameN  # exact frame index
        done.tStart = t  # local t and not account for scr refresh
        done.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(done, 'tStartRefresh')  # time at next scr refresh
        done.setAutoDraw(True)
    # *done_click* updates
    if done_click.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        done_click.frameNStart = frameN  # exact frame index
        done_click.tStart = t  # local t and not account for scr refresh
        done_click.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(done_click, 'tStartRefresh')  # time at next scr refresh
        done_click.status = STARTED
        done_click.mouseClock.reset()
        prevButtonState = done_click.getPressed()  # if button is down already this ISN'T a new click
    if done_click.status == STARTED:  # only update if started and not finished!
        buttons = done_click.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [done]:
                    if obj.contains(done_click):
                        gotValidClick = True
                        done_click.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in settingsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "settings"-------
for thisComponent in settingsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# randomly split stimuli for blocks with even representation of categories per block
split_list = [[] for _ in list(range(numruns))] # empty list of lists, where each list will ultimately represent a block
df = pd.concat([df_sm]*round(numtrls_tot/len(df_sm))); # repeat the dataframe so the number of trials is correct
for x in nums: # for each category
    loc = cats[x];
    subs = df[df.Category.str.match(loc)]; # subset of data in this category
    numsubs = len(subs); # number of stimuli in this category
    div = round(numsubs/numruns) # number of stimuli in this category to be put in each block
    subsn = list(subs.index) # just get the image indices
    shuffle(subsn); # randomize order
    loclist = [subsn[div*i:div*(i+1)] for i in list(range(numruns))]; # split evenly in numruns lists with div values each
    for n in list(range(numruns)): # for each block, add these stimuli to the list
        split_list[n].extend(loclist[n])
for n in list(range(numruns)): # after lists are constructed for each block, shuffle order of stimuli within each block
    shuffle(split_list[n]);
thisExp.addData('tot_trials.response', tot_trials.getRating())
thisExp.addData('tot_trials.rt', tot_trials.getRT())
thisExp.addData('tot_trials.started', tot_trials.tStartRefresh)
thisExp.addData('tot_trials.stopped', tot_trials.tStopRefresh)
thisExp.addData('exp_blocks.response', exp_blocks.getRating())
thisExp.addData('exp_blocks.rt', exp_blocks.getRT())
thisExp.addData('exp_blocks.started', exp_blocks.tStartRefresh)
thisExp.addData('exp_blocks.stopped', exp_blocks.tStopRefresh)
thisExp.addData('trl_label.started', trl_label.tStartRefresh)
thisExp.addData('trl_label.stopped', trl_label.tStopRefresh)
thisExp.addData('block_label.started', block_label.tStartRefresh)
thisExp.addData('block_label.stopped', block_label.tStopRefresh)
thisExp.addData('report_label.started', report_label.tStartRefresh)
thisExp.addData('report_label.stopped', report_label.tStopRefresh)
thisExp.addData('done.started', done.tStartRefresh)
thisExp.addData('done.stopped', done.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('done_click.started', done_click.tStart)
thisExp.addData('done_click.stopped', done_click.tStop)
thisExp.nextEntry()
# the Routine "settings" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse
gotValidClick = False  # until a click is received
# keep track of which components have finished
instructionsComponents = [instructions_text, mouse]
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
    
    # *instructions_text* updates
    if instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_text.frameNStart = frameN  # exact frame index
        instructions_text.tStart = t  # local t and not account for scr refresh
        instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_text, 'tStartRefresh')  # time at next scr refresh
        instructions_text.setAutoDraw(True)
    # *mouse* updates
    if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse.frameNStart = frameN  # exact frame index
        mouse.tStart = t  # local t and not account for scr refresh
        mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        mouse.status = STARTED
        mouse.mouseClock.reset()
        prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
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
thisExp.addData('instructions_text.started', instructions_text.tStartRefresh)
thisExp.addData('instructions_text.stopped', instructions_text.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse.getPos()
buttons = mouse.getPressed()
thisExp.addData('mouse.x', x)
thisExp.addData('mouse.y', y)
thisExp.addData('mouse.leftButton', buttons[0])
thisExp.addData('mouse.midButton', buttons[1])
thisExp.addData('mouse.rightButton', buttons[2])
thisExp.addData('mouse.started', mouse.tStart)
thisExp.addData('mouse.stopped', mouse.tStop)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=numruns, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=numtrls_per, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "pre"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        rand_t = (random()*0.2)+1.4;
        loc_sub = split_list[blocks.thisRepN];
        # keep track of which components have finished
        preComponents = [fix_cross]
        for thisComponent in preComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        preClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "pre"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = preClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=preClock)
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
                if tThisFlipGlobal > fix_cross.tStartRefresh + 0.5-frameTolerance:
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
            for thisComponent in preComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "pre"-------
        for thisComponent in preComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('fix_cross.started', fix_cross.tStartRefresh)
        trials.addData('fix_cross.stopped', fix_cross.tStopRefresh)
        
        # ------Prepare to start Routine "test"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        image.setImage(df_sm.ImageFile[loc_sub[trials.thisRepN]])
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        sound_1.setSound('A', secs=0.1, hamming=True)
        sound_1.setVolume(1, log=False)
        # keep track of which components have finished
        testComponents = [image, key_resp, sound_1]
        for thisComponent in testComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "test"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = testClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=testClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image* updates
            if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                image.setAutoDraw(True)
            if image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    image.tStop = t  # not accounting for scr refresh
                    image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                    image.setAutoDraw(False)
            
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
                if tThisFlipGlobal > key_resp.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = [key.name for key in _key_resp_allKeys]  # storing all keys
                    key_resp.rt = [key.rt for key in _key_resp_allKeys]
            # start/stop sound_1
            if sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sound_1.frameNStart = frameN  # exact frame index
                sound_1.tStart = t  # local t and not account for scr refresh
                sound_1.tStartRefresh = tThisFlipGlobal  # on global time
                sound_1.play(when=win)  # sync with win flip
            if sound_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_1.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_1.tStop = t  # not accounting for scr refresh
                    sound_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
                    sound_1.stop()
            ser.dtr = not ser.dtr
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in testComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "test"-------
        for thisComponent in testComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('image.started', image.tStartRefresh)
        trials.addData('image.stopped', image.tStopRefresh)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        trials.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            trials.addData('key_resp.rt', key_resp.rt)
        trials.addData('key_resp.started', key_resp.tStartRefresh)
        trials.addData('key_resp.stopped', key_resp.tStopRefresh)
        sound_1.stop()  # ensure sound has stopped at end of routine
        trials.addData('sound_1.started', sound_1.tStartRefresh)
        trials.addData('sound_1.stopped', sound_1.tStopRefresh)
        
        # ------Prepare to start Routine "post"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        postComponents = [post_jittered_break]
        for thisComponent in postComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        postClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "post"-------
        while continueRoutine:
            # get current time
            t = postClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=postClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *post_jittered_break* updates
            if post_jittered_break.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                post_jittered_break.frameNStart = frameN  # exact frame index
                post_jittered_break.tStart = t  # local t and not account for scr refresh
                post_jittered_break.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(post_jittered_break, 'tStartRefresh')  # time at next scr refresh
                post_jittered_break.setAutoDraw(True)
            if post_jittered_break.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > post_jittered_break.tStartRefresh + rand_t-frameTolerance:
                    # keep track of stop time/frame for later
                    post_jittered_break.tStop = t  # not accounting for scr refresh
                    post_jittered_break.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(post_jittered_break, 'tStopRefresh')  # time at next scr refresh
                    post_jittered_break.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in postComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "post"-------
        for thisComponent in postComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('post_jittered_break.started', post_jittered_break.tStartRefresh)
        trials.addData('post_jittered_break.stopped', post_jittered_break.tStopRefresh)
        loc_idx = loc_sub[trials.thisRepN];
        thisExp.addData('ImageFile', df_sm.ImageFile[loc_idx]);
        thisExp.addData('Category', df_sm.Category[loc_idx]);
        thisExp.addData('Num', df_sm.Num[loc_idx]);
        corr = 0; 
        if len(key_resp.rt) > 0:
            if df_sm.Category[loc_idx] == 'house':
                corr = 1;
            else:
                corr = 0;
        else:
            if df_sm.Category[loc_idx] == 'house':
                corr = 0;
            else:
                corr = 1;
        thisExp.addData('CorrectButton', corr);
        # the Routine "post" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed numtrls_per repeats of 'trials'
    
    
    # ------Prepare to start Routine "block_completed"-------
    continueRoutine = True
    # update component parameters for each repeat
    completed_text.setText('Completed block ' + str(blocks.thisRepN + 1) + ' out of ' + str(numruns) + '. Click anywhere to continue.')
    # setup some python lists for storing info about the cont
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    block_completedComponents = [completed_text, cont]
    for thisComponent in block_completedComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    block_completedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "block_completed"-------
    while continueRoutine:
        # get current time
        t = block_completedClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=block_completedClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *completed_text* updates
        if completed_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            completed_text.frameNStart = frameN  # exact frame index
            completed_text.tStart = t  # local t and not account for scr refresh
            completed_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(completed_text, 'tStartRefresh')  # time at next scr refresh
            completed_text.setAutoDraw(True)
        # *cont* updates
        if cont.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cont.frameNStart = frameN  # exact frame index
            cont.tStart = t  # local t and not account for scr refresh
            cont.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cont, 'tStartRefresh')  # time at next scr refresh
            cont.status = STARTED
            cont.mouseClock.reset()
            prevButtonState = cont.getPressed()  # if button is down already this ISN'T a new click
        if cont.status == STARTED:  # only update if started and not finished!
            buttons = cont.getPressed()
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
        for thisComponent in block_completedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "block_completed"-------
    for thisComponent in block_completedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blocks.addData('completed_text.started', completed_text.tStartRefresh)
    blocks.addData('completed_text.stopped', completed_text.tStopRefresh)
    # store data for blocks (TrialHandler)
    x, y = cont.getPos()
    buttons = cont.getPressed()
    blocks.addData('cont.x', x)
    blocks.addData('cont.y', y)
    blocks.addData('cont.leftButton', buttons[0])
    blocks.addData('cont.midButton', buttons[1])
    blocks.addData('cont.rightButton', buttons[2])
    blocks.addData('cont.started', cont.tStart)
    blocks.addData('cont.stopped', cont.tStop)
    # the Routine "block_completed" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed numruns repeats of 'blocks'


# ------Prepare to start Routine "overall_completed"-------
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
overall_completedComponents = [complete_and_exit]
for thisComponent in overall_completedComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
overall_completedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "overall_completed"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = overall_completedClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=overall_completedClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *complete_and_exit* updates
    if complete_and_exit.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        complete_and_exit.frameNStart = frameN  # exact frame index
        complete_and_exit.tStart = t  # local t and not account for scr refresh
        complete_and_exit.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(complete_and_exit, 'tStartRefresh')  # time at next scr refresh
        complete_and_exit.setAutoDraw(True)
    if complete_and_exit.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > complete_and_exit.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            complete_and_exit.tStop = t  # not accounting for scr refresh
            complete_and_exit.frameNStop = frameN  # exact frame index
            win.timeOnFlip(complete_and_exit, 'tStopRefresh')  # time at next scr refresh
            complete_and_exit.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in overall_completedComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "overall_completed"-------
for thisComponent in overall_completedComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('complete_and_exit.started', complete_and_exit.tStartRefresh)
thisExp.addData('complete_and_exit.stopped', complete_and_exit.tStopRefresh)

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
