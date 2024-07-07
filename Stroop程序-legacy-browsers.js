/***************** 
 * Stroop程序 *
 *****************/


// store info about the experiment session:
let expName = 'Stroop程序';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([-0.1765, -0.1765, -0.1765]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
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
flowScheduler.add(InstructionsRoutineBegin());
flowScheduler.add(InstructionsRoutineEachFrame());
flowScheduler.add(InstructionsRoutineEnd());
const practicesLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practicesLoopBegin(practicesLoopScheduler));
flowScheduler.add(practicesLoopScheduler);
flowScheduler.add(practicesLoopEnd);



flowScheduler.add(restRoutineBegin());
flowScheduler.add(restRoutineEachFrame());
flowScheduler.add(restRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);



flowScheduler.add(endingsRoutineBegin());
flowScheduler.add(endingsRoutineEachFrame());
flowScheduler.add(endingsRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'Practice_conditions.xlsx', 'path': 'Practice_conditions.xlsx'},
    {'name': 'Stroop_conditions.xlsx', 'path': 'Stroop_conditions.xlsx'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.1.3';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var InstructionsClock;
var instructions_text;
var instructions_key_resp;
var practiceClock;
var practice_text1;
var practice_text2;
var practice_key_resp;
var feedbackClock;
var feedback_text;
var restClock;
var rest_text;
var rest_key_resp;
var trialClock;
var trial_text1;
var trial_text2;
var trial_key_resp;
var feedback1Clock;
var feedback_text1;
var endingsClock;
var endings_text;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "Instructions"
  InstructionsClock = new util.Clock();
  instructions_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions_text',
    text: '您好！欢迎参加本次实验，在实验中您会看到一个“+”注视点。\n提示您需要将注意力集中在屏幕中央。\n随后会出现一个颜色字，需要您判断字的颜色：\n如果字为红色，则按“D”键；如果字为黄色，则按“F”键；\n如果字为蓝色，则按“J”键；如果字为绿色，则按“K”键。\n您有3秒钟的时间进行按键反应，请快速准确地进行判断。\n完全理解后，请按空格键开始练习。',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  instructions_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practice"
  practiceClock = new util.Clock();
  practice_text1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'practice_text1',
    text: '+',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  practice_text2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'practice_text2',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  practice_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  feedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "rest"
  restClock = new util.Clock();
  rest_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'rest_text',
    text: '恭喜完成练习阶段！\n按空格键开始正式实验。',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  rest_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  trial_text1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'trial_text1',
    text: '+',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  trial_text2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'trial_text2',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  trial_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback1"
  feedback1Clock = new util.Clock();
  feedback_text1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text1',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "endings"
  endingsClock = new util.Clock();
  endings_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'endings_text',
    text: '感谢参与本次实验！',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _instructions_key_resp_allKeys;
var InstructionsComponents;
function InstructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instructions' ---
    t = 0;
    InstructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Instructions.started', globalClock.getTime());
    instructions_key_resp.keys = undefined;
    instructions_key_resp.rt = undefined;
    _instructions_key_resp_allKeys = [];
    // keep track of which components have finished
    InstructionsComponents = [];
    InstructionsComponents.push(instructions_text);
    InstructionsComponents.push(instructions_key_resp);
    
    InstructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function InstructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instructions' ---
    // get current time
    t = InstructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructions_text* updates
    if (t >= 0.0 && instructions_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_text.tStart = t;  // (not accounting for frame time here)
      instructions_text.frameNStart = frameN;  // exact frame index
      
      instructions_text.setAutoDraw(true);
    }
    
    
    // *instructions_key_resp* updates
    if (t >= 0.0 && instructions_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_key_resp.tStart = t;  // (not accounting for frame time here)
      instructions_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instructions_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instructions_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instructions_key_resp.clearEvents(); });
    }
    
    if (instructions_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = instructions_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _instructions_key_resp_allKeys = _instructions_key_resp_allKeys.concat(theseKeys);
      if (_instructions_key_resp_allKeys.length > 0) {
        instructions_key_resp.keys = _instructions_key_resp_allKeys[_instructions_key_resp_allKeys.length - 1].name;  // just the last key pressed
        instructions_key_resp.rt = _instructions_key_resp_allKeys[_instructions_key_resp_allKeys.length - 1].rt;
        instructions_key_resp.duration = _instructions_key_resp_allKeys[_instructions_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
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
    InstructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instructions' ---
    InstructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Instructions.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(instructions_key_resp.corr, level);
    }
    psychoJS.experiment.addData('instructions_key_resp.keys', instructions_key_resp.keys);
    if (typeof instructions_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('instructions_key_resp.rt', instructions_key_resp.rt);
        psychoJS.experiment.addData('instructions_key_resp.duration', instructions_key_resp.duration);
        routineTimer.reset();
        }
    
    instructions_key_resp.stop();
    // the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practices;
function practicesLoopBegin(practicesLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    practices = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Practice_conditions.xlsx',
      seed: undefined, name: 'practices'
    });
    psychoJS.experiment.addLoop(practices); // add the loop to the experiment
    currentLoop = practices;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    practices.forEach(function() {
      snapshot = practices.getSnapshot();
    
      practicesLoopScheduler.add(importConditions(snapshot));
      practicesLoopScheduler.add(practiceRoutineBegin(snapshot));
      practicesLoopScheduler.add(practiceRoutineEachFrame());
      practicesLoopScheduler.add(practiceRoutineEnd(snapshot));
      practicesLoopScheduler.add(feedbackRoutineBegin(snapshot));
      practicesLoopScheduler.add(feedbackRoutineEachFrame());
      practicesLoopScheduler.add(feedbackRoutineEnd(snapshot));
      practicesLoopScheduler.add(practicesLoopEndIteration(practicesLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function practicesLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(practices);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function practicesLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Stroop_conditions.xlsx',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials.forEach(function() {
      snapshot = trials.getSnapshot();
    
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsLoopScheduler.add(trialRoutineEachFrame());
      trialsLoopScheduler.add(trialRoutineEnd(snapshot));
      trialsLoopScheduler.add(feedback1RoutineBegin(snapshot));
      trialsLoopScheduler.add(feedback1RoutineEachFrame());
      trialsLoopScheduler.add(feedback1RoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var _practice_key_resp_allKeys;
var practiceComponents;
function practiceRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice' ---
    t = 0;
    practiceClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.500000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('practice.started', globalClock.getTime());
    practice_text2.setColor(new util.Color(color));
    practice_text2.setText(word);
    practice_key_resp.keys = undefined;
    practice_key_resp.rt = undefined;
    _practice_key_resp_allKeys = [];
    // keep track of which components have finished
    practiceComponents = [];
    practiceComponents.push(practice_text1);
    practiceComponents.push(practice_text2);
    practiceComponents.push(practice_key_resp);
    
    practiceComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function practiceRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice' ---
    // get current time
    t = practiceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *practice_text1* updates
    if (t >= 0.0 && practice_text1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practice_text1.tStart = t;  // (not accounting for frame time here)
      practice_text1.frameNStart = frameN;  // exact frame index
      
      practice_text1.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (practice_text1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      practice_text1.setAutoDraw(false);
    }
    
    
    // *practice_text2* updates
    if (t >= 0.5 && practice_text2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practice_text2.tStart = t;  // (not accounting for frame time here)
      practice_text2.frameNStart = frameN;  // exact frame index
      
      practice_text2.setAutoDraw(true);
    }
    
    frameRemains = 0.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (practice_text2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      practice_text2.setAutoDraw(false);
    }
    
    
    // *practice_key_resp* updates
    if (t >= 0.5 && practice_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practice_key_resp.tStart = t;  // (not accounting for frame time here)
      practice_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { practice_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { practice_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { practice_key_resp.clearEvents(); });
    }
    
    frameRemains = 0.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (practice_key_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      practice_key_resp.status = PsychoJS.Status.FINISHED;
        }
      
    if (practice_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = practice_key_resp.getKeys({keyList: ['d', 'f', 'j', 'k'], waitRelease: false});
      _practice_key_resp_allKeys = _practice_key_resp_allKeys.concat(theseKeys);
      if (_practice_key_resp_allKeys.length > 0) {
        practice_key_resp.keys = _practice_key_resp_allKeys[_practice_key_resp_allKeys.length - 1].name;  // just the last key pressed
        practice_key_resp.rt = _practice_key_resp_allKeys[_practice_key_resp_allKeys.length - 1].rt;
        practice_key_resp.duration = _practice_key_resp_allKeys[_practice_key_resp_allKeys.length - 1].duration;
        // was this correct?
        if (practice_key_resp.keys == answer) {
            practice_key_resp.corr = 1;
        } else {
            practice_key_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
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
    practiceComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practiceRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice' ---
    practiceComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('practice.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (practice_key_resp.keys === undefined) {
      if (['None','none',undefined].includes(answer)) {
         practice_key_resp.corr = 1;  // correct non-response
      } else {
         practice_key_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(practice_key_resp.corr, level);
    }
    psychoJS.experiment.addData('practice_key_resp.keys', practice_key_resp.keys);
    psychoJS.experiment.addData('practice_key_resp.corr', practice_key_resp.corr);
    if (typeof practice_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('practice_key_resp.rt', practice_key_resp.rt);
        psychoJS.experiment.addData('practice_key_resp.duration', practice_key_resp.duration);
        routineTimer.reset();
        }
    
    practice_key_resp.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var message;
var message_color;
var feedbackComponents;
function feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback' ---
    t = 0;
    feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('feedback.started', globalClock.getTime());
    // Run 'Begin Routine' code from code
    message = "";
    message_color = "";
    if (practice_key_resp.corr) {
        message = "\u56de\u7b54\u6b63\u786e!";
        message_color = "green";
    } else {
        message = "\u56de\u7b54\u9519\u8bef!";
        message_color = "red";
    }
    
    feedback_text.setColor(new util.Color(message_color));
    feedback_text.setText(message);
    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(feedback_text);
    
    feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback' ---
    // get current time
    t = feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_text* updates
    if (t >= 0.0 && feedback_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_text.tStart = t;  // (not accounting for frame time here)
      feedback_text.frameNStart = frameN;  // exact frame index
      
      feedback_text.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedback_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_text.setAutoDraw(false);
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
    feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback' ---
    feedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('feedback.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _rest_key_resp_allKeys;
var restComponents;
function restRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'rest' ---
    t = 0;
    restClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('rest.started', globalClock.getTime());
    rest_key_resp.keys = undefined;
    rest_key_resp.rt = undefined;
    _rest_key_resp_allKeys = [];
    // keep track of which components have finished
    restComponents = [];
    restComponents.push(rest_text);
    restComponents.push(rest_key_resp);
    
    restComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function restRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'rest' ---
    // get current time
    t = restClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rest_text* updates
    if (t >= 0.0 && rest_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rest_text.tStart = t;  // (not accounting for frame time here)
      rest_text.frameNStart = frameN;  // exact frame index
      
      rest_text.setAutoDraw(true);
    }
    
    
    // *rest_key_resp* updates
    if (t >= 0.0 && rest_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rest_key_resp.tStart = t;  // (not accounting for frame time here)
      rest_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { rest_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { rest_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { rest_key_resp.clearEvents(); });
    }
    
    if (rest_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = rest_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _rest_key_resp_allKeys = _rest_key_resp_allKeys.concat(theseKeys);
      if (_rest_key_resp_allKeys.length > 0) {
        rest_key_resp.keys = _rest_key_resp_allKeys[_rest_key_resp_allKeys.length - 1].name;  // just the last key pressed
        rest_key_resp.rt = _rest_key_resp_allKeys[_rest_key_resp_allKeys.length - 1].rt;
        rest_key_resp.duration = _rest_key_resp_allKeys[_rest_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
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
    restComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function restRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'rest' ---
    restComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('rest.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(rest_key_resp.corr, level);
    }
    psychoJS.experiment.addData('rest_key_resp.keys', rest_key_resp.keys);
    if (typeof rest_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('rest_key_resp.rt', rest_key_resp.rt);
        psychoJS.experiment.addData('rest_key_resp.duration', rest_key_resp.duration);
        routineTimer.reset();
        }
    
    rest_key_resp.stop();
    // the Routine "rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _trial_key_resp_allKeys;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial' ---
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.500000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('trial.started', globalClock.getTime());
    trial_text2.setColor(new util.Color(color));
    trial_text2.setText(word);
    trial_key_resp.keys = undefined;
    trial_key_resp.rt = undefined;
    _trial_key_resp_allKeys = [];
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(trial_text1);
    trialComponents.push(trial_text2);
    trialComponents.push(trial_key_resp);
    
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial' ---
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *trial_text1* updates
    if (t >= 0.0 && trial_text1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial_text1.tStart = t;  // (not accounting for frame time here)
      trial_text1.frameNStart = frameN;  // exact frame index
      
      trial_text1.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (trial_text1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      trial_text1.setAutoDraw(false);
    }
    
    
    // *trial_text2* updates
    if (t >= 0.5 && trial_text2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial_text2.tStart = t;  // (not accounting for frame time here)
      trial_text2.frameNStart = frameN;  // exact frame index
      
      trial_text2.setAutoDraw(true);
    }
    
    frameRemains = 0.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (trial_text2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      trial_text2.setAutoDraw(false);
    }
    
    
    // *trial_key_resp* updates
    if (t >= 0.5 && trial_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial_key_resp.tStart = t;  // (not accounting for frame time here)
      trial_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { trial_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { trial_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { trial_key_resp.clearEvents(); });
    }
    
    frameRemains = 0.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (trial_key_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      trial_key_resp.status = PsychoJS.Status.FINISHED;
        }
      
    if (trial_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = trial_key_resp.getKeys({keyList: ['d', 'j', 'f', 'k'], waitRelease: false});
      _trial_key_resp_allKeys = _trial_key_resp_allKeys.concat(theseKeys);
      if (_trial_key_resp_allKeys.length > 0) {
        trial_key_resp.keys = _trial_key_resp_allKeys[_trial_key_resp_allKeys.length - 1].name;  // just the last key pressed
        trial_key_resp.rt = _trial_key_resp_allKeys[_trial_key_resp_allKeys.length - 1].rt;
        trial_key_resp.duration = _trial_key_resp_allKeys[_trial_key_resp_allKeys.length - 1].duration;
        // was this correct?
        if (trial_key_resp.keys == answer) {
            trial_key_resp.corr = 1;
        } else {
            trial_key_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
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
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial' ---
    trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('trial.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (trial_key_resp.keys === undefined) {
      if (['None','none',undefined].includes(answer)) {
         trial_key_resp.corr = 1;  // correct non-response
      } else {
         trial_key_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(trial_key_resp.corr, level);
    }
    psychoJS.experiment.addData('trial_key_resp.keys', trial_key_resp.keys);
    psychoJS.experiment.addData('trial_key_resp.corr', trial_key_resp.corr);
    if (typeof trial_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('trial_key_resp.rt', trial_key_resp.rt);
        psychoJS.experiment.addData('trial_key_resp.duration', trial_key_resp.duration);
        routineTimer.reset();
        }
    
    trial_key_resp.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedback1Components;
function feedback1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback1' ---
    t = 0;
    feedback1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('feedback1.started', globalClock.getTime());
    // Run 'Begin Routine' code from code_2
    message = "";
    message_color = "";
    if (trial_key_resp.corr) {
        message = "\u56de\u7b54\u6b63\u786e!";
        message_color = "green";
    } else {
        message = "\u56de\u7b54\u9519\u8bef!";
        message_color = "red";
    }
    
    feedback_text1.setColor(new util.Color(message_color));
    feedback_text1.setText(message);
    // keep track of which components have finished
    feedback1Components = [];
    feedback1Components.push(feedback_text1);
    
    feedback1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function feedback1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback1' ---
    // get current time
    t = feedback1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_text1* updates
    if (t >= 0.0 && feedback_text1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_text1.tStart = t;  // (not accounting for frame time here)
      feedback_text1.frameNStart = frameN;  // exact frame index
      
      feedback_text1.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedback_text1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_text1.setAutoDraw(false);
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
    feedback1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedback1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback1' ---
    feedback1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('feedback1.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var endingsComponents;
function endingsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'endings' ---
    t = 0;
    endingsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('endings.started', globalClock.getTime());
    // keep track of which components have finished
    endingsComponents = [];
    endingsComponents.push(endings_text);
    
    endingsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function endingsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'endings' ---
    // get current time
    t = endingsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *endings_text* updates
    if (t >= 0.0 && endings_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endings_text.tStart = t;  // (not accounting for frame time here)
      endings_text.frameNStart = frameN;  // exact frame index
      
      endings_text.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (endings_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      endings_text.setAutoDraw(false);
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
    endingsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endingsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'endings' ---
    endingsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('endings.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
