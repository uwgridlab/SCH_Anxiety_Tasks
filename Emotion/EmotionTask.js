/******************** 
 * Emotiontask Test *
 ********************/

import { PsychoJS } from './lib/core-2020.2.js';
import * as core from './lib/core-2020.2.js';
import { TrialHandler } from './lib/data-2020.2.js';
import { Scheduler } from './lib/util-2020.2.js';
import * as visual from './lib/visual-2020.2.js';
import * as sound from './lib/sound-2020.2.js';
import * as util from './lib/util-2020.2.js';
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([1, 1, 1]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'EmotionTask';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// Start code blocks for 'Before Experiment'

        // add-on: list(s: string): string[]
        function list(s) {
            // if s is a string, we return a list of its characters
            if (typeof s === 'string')
                return s.split('');
            else
                // otherwise we return s:
                return s;
        }

        import * as pd from 'pandas';
import * as serial from 'serial';
var cats, cz, df_sm, numruns, numruns_opts, nums, numtrls_per, numtrls_tot, numtrls_tot_opts, z;
df_sm = pd.read_excel("stimuli.xlsx");
cats = df_sm.Category.unique();
nums = list(range(cats.length));
cz = df_sm.Num.unique().length;
z = round((cz / cats.length));
if ((cz !== df_sm.length)) {
    console.log("Warning: more spreadsheet entries than unique image indices");
}
numtrls_tot_opts = [(cz * 4), (cz * 8), (cz * 12), (cz * 16)];
numruns_opts = [z, (z * 2), (z * 4)];
numruns = numruns_opts[1];
numtrls_tot = numtrls_tot_opts[3];
numtrls_per = round((numtrls_tot / numruns));

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(settingsRoutineBegin());
flowScheduler.add(settingsRoutineEachFrame());
flowScheduler.add(settingsRoutineEnd());
flowScheduler.add(instructionsRoutineBegin());
flowScheduler.add(instructionsRoutineEachFrame());
flowScheduler.add(instructionsRoutineEnd());
const blocksLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(blocksLoopBegin, blocksLoopScheduler);
flowScheduler.add(blocksLoopScheduler);
flowScheduler.add(blocksLoopEnd);
flowScheduler.add(overall_completedRoutineBegin());
flowScheduler.add(overall_completedRoutineEachFrame());
flowScheduler.add(overall_completedRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'Images/fix_cross.png', 'path': 'Images/fix_cross.png'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.DEBUG);

function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.2.10';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

function experimentInit() {
  // Initialize components for Routine "settings"
  settingsClock = new util.Clock();
  tot_trials = new visual.Slider({
    win: psychoJS.window, name: 'tot_trials',
    size: [1.0, 0.05], pos: [0, 0.25], units: 'height',
    labels: 
          // add-on: list(s: string): string[]
          function list(s) {
              // if s is a string, we return a list of its characters
              if (typeof s === 'string')
                  return s.split('');
              else
                  // otherwise we return s:
                  return s;
          }
  
          function () {
      var _pj_a = [], _pj_b = list(range(4));
      for (var _pj_c = 0, _pj_d = _pj_b.length; (_pj_c < _pj_d); _pj_c += 1) {
          var i = _pj_b[_pj_c];
          _pj_a.push(numtrls_tot_opts[i].toString());
      }
      return _pj_a;
  }
  .call(this), ticks: [0, 1, 2, 3],
    granularity: 1, style: [visual.Slider.Style.RATING],
    color: new util.Color('black'), 
    fontFamily: 'HelveticaBold', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  exp_blocks = new visual.Slider({
    win: psychoJS.window, name: 'exp_blocks',
    size: [1.0, 0.05], pos: [0, 0], units: 'height',
    labels: 
          // add-on: list(s: string): string[]
          function list(s) {
              // if s is a string, we return a list of its characters
              if (typeof s === 'string')
                  return s.split('');
              else
                  // otherwise we return s:
                  return s;
          }
  
          function () {
      var _pj_a = [], _pj_b = list(range(3));
      for (var _pj_c = 0, _pj_d = _pj_b.length; (_pj_c < _pj_d); _pj_c += 1) {
          var i = _pj_b[_pj_c];
          _pj_a.push(numruns_opts[i].toString());
      }
      return _pj_a;
  }
  .call(this), ticks: [0, 1, 2],
    granularity: 1, style: [visual.Slider.Style.RADIO],
    color: new util.Color('black'), 
    fontFamily: 'HelveticaBold', bold: true, italic: false, depth: -2, 
    flip: false,
  });
  
  trl_label = new visual.TextStim({
    win: psychoJS.window,
    name: 'trl_label',
    text: (("# of Trials (default " + numtrls_tot_opts[3].toString()) + ")"),
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.31], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  block_label = new visual.TextStim({
    win: psychoJS.window,
    name: 'block_label',
    text: (("# of Blocks (default " + numruns_opts[1].toString()) + ")"),
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.06], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  report_label = new visual.TextStim({
    win: psychoJS.window,
    name: 'report_label',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
  done = new visual.TextStim({
    win: psychoJS.window,
    name: 'done',
    text: 'DONE',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.35)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('red'),  opacity: 1,
    depth: -6.0 
  });
  
  done_click = new core.Mouse({
    win: psychoJS.window,
  });
  done_click.mouseClock = new util.Clock();
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  instructions_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions_text',
    text: 'Press the space bar when you see a house.\n\nClick anywhere when ready.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  // Initialize components for Routine "pre"
  preClock = new util.Clock();
  fix_cross = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fix_cross', units : undefined, 
    image : 'Images/fix_cross.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.05, 0.05],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "test"
  testClock = new util.Clock();
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  sound_1 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 0.1,
    });
  sound_1.setVolume(1);
  // Initialize components for Routine "post"
  postClock = new util.Clock();
  post_jittered_break = new visual.TextStim({
    win: psychoJS.window,
    name: 'post_jittered_break',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "block_completed"
  block_completedClock = new util.Clock();
  completed_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'completed_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  cont = new core.Mouse({
    win: psychoJS.window,
  });
  cont.mouseClock = new util.Clock();
  // Initialize components for Routine "overall_completed"
  overall_completedClock = new util.Clock();
  complete_and_exit = new visual.TextStim({
    win: psychoJS.window,
    name: 'complete_and_exit',
    text: 'Thank you, you have finished the task!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function settingsRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'settings'-------
    t = 0;
    settingsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    tot_trials.markerPos = numtrls_tot;
    exp_blocks.markerPos = 2;
    
    tot_trials.reset()
    exp_blocks.reset()
    // setup some python lists for storing info about the done_click
    done_click.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    settingsComponents = [];
    settingsComponents.push(tot_trials);
    settingsComponents.push(exp_blocks);
    settingsComponents.push(trl_label);
    settingsComponents.push(block_label);
    settingsComponents.push(report_label);
    settingsComponents.push(done);
    settingsComponents.push(done_click);
    
    for (const thisComponent of settingsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function settingsRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'settings'-------
    // get current time
    t = settingsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    if ((exp_blocks.getRating() !== null)) {
        numruns = numruns_opts[exp_blocks.getRating()];
    }
    if ((tot_trials.getRating() !== null)) {
        numtrls_tot = round(numtrls_tot_opts[tot_trials.getRating()]);
        numtrls_per = round((numtrls_tot / numruns));
    }
    
    
    // *tot_trials* updates
    if (t >= 0.0 && tot_trials.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tot_trials.tStart = t;  // (not accounting for frame time here)
      tot_trials.frameNStart = frameN;  // exact frame index
      
      tot_trials.setAutoDraw(true);
    }

    
    // *exp_blocks* updates
    if (t >= 0.0 && exp_blocks.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      exp_blocks.tStart = t;  // (not accounting for frame time here)
      exp_blocks.frameNStart = frameN;  // exact frame index
      
      exp_blocks.setAutoDraw(true);
    }

    
    // *trl_label* updates
    if (t >= 0.0 && trl_label.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trl_label.tStart = t;  // (not accounting for frame time here)
      trl_label.frameNStart = frameN;  // exact frame index
      
      trl_label.setAutoDraw(true);
    }

    
    // *block_label* updates
    if (t >= 0.0 && block_label.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      block_label.tStart = t;  // (not accounting for frame time here)
      block_label.frameNStart = frameN;  // exact frame index
      
      block_label.setAutoDraw(true);
    }

    
    // *report_label* updates
    if (t >= 0.0 && report_label.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      report_label.tStart = t;  // (not accounting for frame time here)
      report_label.frameNStart = frameN;  // exact frame index
      
      report_label.setAutoDraw(true);
    }

    
    if (report_label.status === PsychoJS.Status.STARTED){ // only update if being drawn
      report_label.setText((((((numtrls_tot.toString() + " total trials split among ") + numruns.toString()) + " blocks for ") + numtrls_per.toString()) + " trials per block."), false);
    }
    
    // *done* updates
    if (t >= 0.0 && done.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      done.tStart = t;  // (not accounting for frame time here)
      done.frameNStart = frameN;  // exact frame index
      
      done.setAutoDraw(true);
    }

    // *done_click* updates
    if (t >= 0.0 && done_click.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      done_click.tStart = t;  // (not accounting for frame time here)
      done_click.frameNStart = frameN;  // exact frame index
      
      done_click.status = PsychoJS.Status.STARTED;
      done_click.mouseClock.reset();
      prevButtonState = done_click.getPressed();  // if button is down already this ISN'T a new click
      }
    if (done_click.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = done_click.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [done]) {
            if (obj.contains(done_click)) {
              gotValidClick = true;
              done_click.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of settingsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function settingsRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'settings'-------
    for (const thisComponent of settingsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    
            // add-on: list(s: string): string[]
            function list(s) {
                // if s is a string, we return a list of its characters
                if (typeof s === 'string')
                    return s.split('');
                else
                    // otherwise we return s:
                    return s;
            }
    
            split_list = function () {
        var _pj_a = [], _pj_b = list(range(numruns));
        for (var _pj_c = 0, _pj_d = _pj_b.length; (_pj_c < _pj_d); _pj_c += 1) {
            var _ = _pj_b[_pj_c];
            _pj_a.push([]);
        }
        return _pj_a;
    }
    .call(this);
    df = pd.concat(([df_sm] * round((numtrls_tot / df_sm.length))));
    for (var x, _pj_c = 0, _pj_a = nums, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        x = _pj_a[_pj_c];
        loc = cats[x];
        subs = df[df.Category.str.match(loc)];
        numsubs = subs.length;
        div = round((numsubs / numruns));
        subsn = list(subs.index);
        shuffle(subsn);
        loclist = function () {
        var _pj_d = [], _pj_e = list(range(numruns));
        for (var _pj_f = 0, _pj_g = _pj_e.length; (_pj_f < _pj_g); _pj_f += 1) {
            var i = _pj_e[_pj_f];
            _pj_d.push(subsn.slice((div * i), (div * (i + 1))));
        }
        return _pj_d;
    }
    .call(this);
        for (var n, _pj_f = 0, _pj_d = list(range(numruns)), _pj_e = _pj_d.length; (_pj_f < _pj_e); _pj_f += 1) {
            n = _pj_d[_pj_f];
            split_list[n].extend(loclist[n]);
        }
    }
    for (var n, _pj_c = 0, _pj_a = list(range(numruns)), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        n = _pj_a[_pj_c];
        shuffle(split_list[n]);
    }
    
    psychoJS.experiment.addData('tot_trials.response', tot_trials.getRating());
    psychoJS.experiment.addData('tot_trials.rt', tot_trials.getRT());
    psychoJS.experiment.addData('exp_blocks.response', exp_blocks.getRating());
    psychoJS.experiment.addData('exp_blocks.rt', exp_blocks.getRT());
    // store data for thisExp (ExperimentHandler)
    // the Routine "settings" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function instructionsRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instructions'-------
    t = 0;
    instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    instructionsComponents = [];
    instructionsComponents.push(instructions_text);
    instructionsComponents.push(mouse);
    
    for (const thisComponent of instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function instructionsRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instructions'-------
    // get current time
    t = instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructions_text* updates
    if (t >= 0.0 && instructions_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_text.tStart = t;  // (not accounting for frame time here)
      instructions_text.frameNStart = frameN;  // exact frame index
      
      instructions_text.setAutoDraw(true);
    }

    // *mouse* updates
    if (t >= 0.0 && mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse.tStart = t;  // (not accounting for frame time here)
      mouse.frameNStart = frameN;  // exact frame index
      
      mouse.status = PsychoJS.Status.STARTED;
      mouse.mouseClock.reset();
      prevButtonState = mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // abort routine on response
          continueRoutine = false;
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function instructionsRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instructions'-------
    for (const thisComponent of instructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for thisExp (ExperimentHandler)
    _mouseXYs = mouse.getPos();
    _mouseButtons = mouse.getPressed();
    psychoJS.experiment.addData('mouse.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouse.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouse.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouse.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouse.rightButton', _mouseButtons[2]);
    // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function blocksLoopBegin(blocksLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  blocks = new TrialHandler({
    psychoJS: psychoJS,
    nReps: numruns, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'blocks'
  });
  psychoJS.experiment.addLoop(blocks); // add the loop to the experiment
  currentLoop = blocks;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisBlock of blocks) {
    const snapshot = blocks.getSnapshot();
    blocksLoopScheduler.add(importConditions(snapshot));
    const trialsLoopScheduler = new Scheduler(psychoJS);
    blocksLoopScheduler.add(trialsLoopBegin, trialsLoopScheduler);
    blocksLoopScheduler.add(trialsLoopScheduler);
    blocksLoopScheduler.add(trialsLoopEnd);
    blocksLoopScheduler.add(block_completedRoutineBegin(snapshot));
    blocksLoopScheduler.add(block_completedRoutineEachFrame(snapshot));
    blocksLoopScheduler.add(block_completedRoutineEnd(snapshot));
    blocksLoopScheduler.add(endLoopIteration(blocksLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}

function trialsLoopBegin(trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: numtrls_per, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials'
  });
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrial of trials) {
    const snapshot = trials.getSnapshot();
    trialsLoopScheduler.add(importConditions(snapshot));
    trialsLoopScheduler.add(preRoutineBegin(snapshot));
    trialsLoopScheduler.add(preRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(preRoutineEnd(snapshot));
    trialsLoopScheduler.add(testRoutineBegin(snapshot));
    trialsLoopScheduler.add(testRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(testRoutineEnd(snapshot));
    trialsLoopScheduler.add(postRoutineBegin(snapshot));
    trialsLoopScheduler.add(postRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(postRoutineEnd(snapshot));
    trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}

function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}

function blocksLoopEnd() {
  psychoJS.experiment.removeLoop(blocks);

  return Scheduler.Event.NEXT;
}

function preRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'pre'-------
    t = 0;
    preClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    rand_t = ((random() * 0.2) + 1.4);
    loc_sub = split_list[blocks.thisRepN];
    
    // keep track of which components have finished
    preComponents = [];
    preComponents.push(fix_cross);
    
    for (const thisComponent of preComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function preRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'pre'-------
    // get current time
    t = preClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fix_cross* updates
    if (t >= 0.0 && fix_cross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix_cross.tStart = t;  // (not accounting for frame time here)
      fix_cross.frameNStart = frameN;  // exact frame index
      
      fix_cross.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((fix_cross.status === PsychoJS.Status.STARTED || fix_cross.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      fix_cross.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of preComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function preRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'pre'-------
    for (const thisComponent of preComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}

function testRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'test'-------
    t = 0;
    testClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    image.setImage(df_sm.ImageFile[loc_sub[trials.thisRepN]]);
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    sound_1.secs=0.1;
    sound_1.setVolume(1);
    /* Syntax Error: Fix Python code */
    // keep track of which components have finished
    testComponents = [];
    testComponents.push(image);
    testComponents.push(key_resp);
    testComponents.push(sound_1);
    
    for (const thisComponent of testComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function testRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'test'-------
    // get current time
    t = testClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image* updates
    if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index
      
      image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((image.status === PsychoJS.Status.STARTED || image.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      image.setAutoDraw(false);
    }
    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((key_resp.status === PsychoJS.Status.STARTED || key_resp.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      key_resp.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys.map((key) => key.name);  // storing all keys
        key_resp.rt = _key_resp_allKeys.map((key) => key.rt);
      }
    }
    
    // start/stop sound_1
    if (t >= 0.0 && sound_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_1.tStart = t;  // (not accounting for frame time here)
      sound_1.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_1.play(); });  // screen flip
      sound_1.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0.0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((sound_1.status === PsychoJS.Status.STARTED || sound_1.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      if (0.1 > 0.5) {  sound_1.stop();  // stop the sound (if longer than duration)
        sound_1.status = PsychoJS.Status.FINISHED;
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of testComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function testRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'test'-------
    for (const thisComponent of testComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        }
    
    key_resp.stop();
    sound_1.stop();  // ensure sound has stopped at end of routine
    /* Syntax Error: Fix Python code */
    return Scheduler.Event.NEXT;
  };
}

function postRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'post'-------
    t = 0;
    postClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    postComponents = [];
    postComponents.push(post_jittered_break);
    
    for (const thisComponent of postComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function postRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'post'-------
    // get current time
    t = postClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *post_jittered_break* updates
    if (t >= 0.0 && post_jittered_break.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      post_jittered_break.tStart = t;  // (not accounting for frame time here)
      post_jittered_break.frameNStart = frameN;  // exact frame index
      
      post_jittered_break.setAutoDraw(true);
    }

    frameRemains = 0.0 + rand_t - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((post_jittered_break.status === PsychoJS.Status.STARTED || post_jittered_break.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      post_jittered_break.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of postComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function postRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'post'-------
    for (const thisComponent of postComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    loc_idx = loc_sub[trials.thisRepN];
    thisExp.addData("ImageFile", df_sm.ImageFile[loc_idx]);
    thisExp.addData("Category", df_sm.Category[loc_idx]);
    thisExp.addData("Num", df_sm.Num[loc_idx]);
    corr = 0;
    if ((key_resp.rt.length > 0)) {
        if ((df_sm.Category[loc_idx] === "house")) {
            corr = 1;
        } else {
            corr = 0;
        }
    } else {
        if ((df_sm.Category[loc_idx] === "house")) {
            corr = 0;
        } else {
            corr = 1;
        }
    }
    thisExp.addData("CorrectButton", corr);
    
    // the Routine "post" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function block_completedRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'block_completed'-------
    t = 0;
    block_completedClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    completed_text.setText((((("Completed block " + (blocks.thisRepN + 1).toString()) + " out of ") + numruns.toString()) + ". Click anywhere to continue."));
    // setup some python lists for storing info about the cont
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    block_completedComponents = [];
    block_completedComponents.push(completed_text);
    block_completedComponents.push(cont);
    
    for (const thisComponent of block_completedComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function block_completedRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'block_completed'-------
    // get current time
    t = block_completedClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *completed_text* updates
    if (t >= 0.0 && completed_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      completed_text.tStart = t;  // (not accounting for frame time here)
      completed_text.frameNStart = frameN;  // exact frame index
      
      completed_text.setAutoDraw(true);
    }

    // *cont* updates
    if (t >= 0.0 && cont.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cont.tStart = t;  // (not accounting for frame time here)
      cont.frameNStart = frameN;  // exact frame index
      
      cont.status = PsychoJS.Status.STARTED;
      cont.mouseClock.reset();
      prevButtonState = cont.getPressed();  // if button is down already this ISN'T a new click
      }
    if (cont.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = cont.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // abort routine on response
          continueRoutine = false;
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of block_completedComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function block_completedRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'block_completed'-------
    for (const thisComponent of block_completedComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for thisExp (ExperimentHandler)
    _mouseXYs = cont.getPos();
    _mouseButtons = cont.getPressed();
    psychoJS.experiment.addData('cont.x', _mouseXYs[0]);
    psychoJS.experiment.addData('cont.y', _mouseXYs[1]);
    psychoJS.experiment.addData('cont.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('cont.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('cont.rightButton', _mouseButtons[2]);
    // the Routine "block_completed" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function overall_completedRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'overall_completed'-------
    t = 0;
    overall_completedClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(10.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    overall_completedComponents = [];
    overall_completedComponents.push(complete_and_exit);
    
    for (const thisComponent of overall_completedComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function overall_completedRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'overall_completed'-------
    // get current time
    t = overall_completedClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *complete_and_exit* updates
    if (t >= 0.0 && complete_and_exit.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      complete_and_exit.tStart = t;  // (not accounting for frame time here)
      complete_and_exit.frameNStart = frameN;  // exact frame index
      
      complete_and_exit.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((complete_and_exit.status === PsychoJS.Status.STARTED || complete_and_exit.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      complete_and_exit.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of overall_completedComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function overall_completedRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'overall_completed'-------
    for (const thisComponent of overall_completedComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}

function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}

function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
