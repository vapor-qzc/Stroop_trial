#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.3),
    on 七月 07, 2024, at 19:44
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2024.1.3')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.1.3'
expName = 'Stroop程序'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': '',
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1646, 1029]
_loggingLevel = logging.getLevel('exp')
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # override logging level
    _loggingLevel = logging.getLevel(
        prefs.piloting['pilotLoggingLevel']
    )

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='D:\\vapor\\Desktop\\新建文件夹\\Psychopy files\\Stroop2\\Stroop程序_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(_loggingLevel)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=_loggingLevel)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0.0039, 0.0039, 0.0039], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0.0039, 0.0039, 0.0039]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.mouseVisible = False
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('instructions_key_resp') is None:
        # initialise instructions_key_resp
        instructions_key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='instructions_key_resp',
        )
    if deviceManager.getDevice('practice_key_resp') is None:
        # initialise practice_key_resp
        practice_key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='practice_key_resp',
        )
    if deviceManager.getDevice('rest_key_resp') is None:
        # initialise rest_key_resp
        rest_key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='rest_key_resp',
        )
    if deviceManager.getDevice('trial_key_resp') is None:
        # initialise trial_key_resp
        trial_key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='trial_key_resp',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Instructions" ---
    instructions_text = visual.TextStim(win=win, name='instructions_text',
        text='您好！欢迎参加本次实验，在实验中您会看到一个“+”注视点。\n提示您需要将注意力集中在屏幕中央。\n随后会出现一个颜色字，需要您判断字的颜色：\n如果字为红色，则按“D”键；如果字为黄色，则按“F”键；\n如果字为蓝色，则按“J”键；如果字为绿色，则按“K”键。\n您有3秒钟的时间进行按键反应，请快速准确地进行判断。\n完全理解后，请按空格键开始练习。',
        font='Arial',
        pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    instructions_key_resp = keyboard.Keyboard(deviceName='instructions_key_resp')
    
    # --- Initialize components for Routine "practice" ---
    practice_text1 = visual.TextStim(win=win, name='practice_text1',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    practice_text2 = visual.TextStim(win=win, name='practice_text2',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    practice_key_resp = keyboard.Keyboard(deviceName='practice_key_resp')
    
    # --- Initialize components for Routine "feedback" ---
    feedback_text = visual.TextStim(win=win, name='feedback_text',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "rest" ---
    rest_text = visual.TextStim(win=win, name='rest_text',
        text='恭喜完成练习阶段！\n按空格键开始正式实验。',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    rest_key_resp = keyboard.Keyboard(deviceName='rest_key_resp')
    
    # --- Initialize components for Routine "trial" ---
    trial_text1 = visual.TextStim(win=win, name='trial_text1',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    trial_text2 = visual.TextStim(win=win, name='trial_text2',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    trial_key_resp = keyboard.Keyboard(deviceName='trial_key_resp')
    
    # --- Initialize components for Routine "feedback1" ---
    feedback_text1 = visual.TextStim(win=win, name='feedback_text1',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "endings" ---
    endings_text = visual.TextStim(win=win, name='endings_text',
        text='感谢参与本次实验！',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "Instructions" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instructions.started', globalClock.getTime(format='float'))
    instructions_key_resp.keys = []
    instructions_key_resp.rt = []
    _instructions_key_resp_allKeys = []
    # keep track of which components have finished
    InstructionsComponents = [instructions_text, instructions_key_resp]
    for thisComponent in InstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instructions" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_text* updates
        
        # if instructions_text is starting this frame...
        if instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_text.frameNStart = frameN  # exact frame index
            instructions_text.tStart = t  # local t and not account for scr refresh
            instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instructions_text.started')
            # update status
            instructions_text.status = STARTED
            instructions_text.setAutoDraw(True)
        
        # if instructions_text is active this frame...
        if instructions_text.status == STARTED:
            # update params
            pass
        
        # *instructions_key_resp* updates
        waitOnFlip = False
        
        # if instructions_key_resp is starting this frame...
        if instructions_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_key_resp.frameNStart = frameN  # exact frame index
            instructions_key_resp.tStart = t  # local t and not account for scr refresh
            instructions_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instructions_key_resp.started')
            # update status
            instructions_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instructions_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instructions_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instructions_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = instructions_key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _instructions_key_resp_allKeys.extend(theseKeys)
            if len(_instructions_key_resp_allKeys):
                instructions_key_resp.keys = _instructions_key_resp_allKeys[-1].name  # just the last key pressed
                instructions_key_resp.rt = _instructions_key_resp_allKeys[-1].rt
                instructions_key_resp.duration = _instructions_key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions" ---
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instructions.stopped', globalClock.getTime(format='float'))
    # check responses
    if instructions_key_resp.keys in ['', [], None]:  # No response was made
        instructions_key_resp.keys = None
    thisExp.addData('instructions_key_resp.keys',instructions_key_resp.keys)
    if instructions_key_resp.keys != None:  # we had a response
        thisExp.addData('instructions_key_resp.rt', instructions_key_resp.rt)
        thisExp.addData('instructions_key_resp.duration', instructions_key_resp.duration)
    thisExp.nextEntry()
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practices = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Practice_conditions.xlsx'),
        seed=None, name='practices')
    thisExp.addLoop(practices)  # add the loop to the experiment
    thisPractice = practices.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice:
            globals()[paramName] = thisPractice[paramName]
    
    for thisPractice in practices:
        currentLoop = practices
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
        if thisPractice != None:
            for paramName in thisPractice:
                globals()[paramName] = thisPractice[paramName]
        
        # --- Prepare to start Routine "practice" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('practice.started', globalClock.getTime(format='float'))
        practice_text2.setColor(color, colorSpace='rgb')
        practice_text2.setText(word)
        practice_key_resp.keys = []
        practice_key_resp.rt = []
        _practice_key_resp_allKeys = []
        # keep track of which components have finished
        practiceComponents = [practice_text1, practice_text2, practice_key_resp]
        for thisComponent in practiceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "practice" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 3.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *practice_text1* updates
            
            # if practice_text1 is starting this frame...
            if practice_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practice_text1.frameNStart = frameN  # exact frame index
                practice_text1.tStart = t  # local t and not account for scr refresh
                practice_text1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_text1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'practice_text1.started')
                # update status
                practice_text1.status = STARTED
                practice_text1.setAutoDraw(True)
            
            # if practice_text1 is active this frame...
            if practice_text1.status == STARTED:
                # update params
                pass
            
            # if practice_text1 is stopping this frame...
            if practice_text1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_text1.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_text1.tStop = t  # not accounting for scr refresh
                    practice_text1.tStopRefresh = tThisFlipGlobal  # on global time
                    practice_text1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'practice_text1.stopped')
                    # update status
                    practice_text1.status = FINISHED
                    practice_text1.setAutoDraw(False)
            
            # *practice_text2* updates
            
            # if practice_text2 is starting this frame...
            if practice_text2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                practice_text2.frameNStart = frameN  # exact frame index
                practice_text2.tStart = t  # local t and not account for scr refresh
                practice_text2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_text2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'practice_text2.started')
                # update status
                practice_text2.status = STARTED
                practice_text2.setAutoDraw(True)
            
            # if practice_text2 is active this frame...
            if practice_text2.status == STARTED:
                # update params
                pass
            
            # if practice_text2 is stopping this frame...
            if practice_text2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_text2.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_text2.tStop = t  # not accounting for scr refresh
                    practice_text2.tStopRefresh = tThisFlipGlobal  # on global time
                    practice_text2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'practice_text2.stopped')
                    # update status
                    practice_text2.status = FINISHED
                    practice_text2.setAutoDraw(False)
            
            # *practice_key_resp* updates
            waitOnFlip = False
            
            # if practice_key_resp is starting this frame...
            if practice_key_resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                practice_key_resp.frameNStart = frameN  # exact frame index
                practice_key_resp.tStart = t  # local t and not account for scr refresh
                practice_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'practice_key_resp.started')
                # update status
                practice_key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(practice_key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(practice_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if practice_key_resp is stopping this frame...
            if practice_key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_key_resp.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_key_resp.tStop = t  # not accounting for scr refresh
                    practice_key_resp.tStopRefresh = tThisFlipGlobal  # on global time
                    practice_key_resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'practice_key_resp.stopped')
                    # update status
                    practice_key_resp.status = FINISHED
                    practice_key_resp.status = FINISHED
            if practice_key_resp.status == STARTED and not waitOnFlip:
                theseKeys = practice_key_resp.getKeys(keyList=['d','f','j','k'], ignoreKeys=["escape"], waitRelease=False)
                _practice_key_resp_allKeys.extend(theseKeys)
                if len(_practice_key_resp_allKeys):
                    practice_key_resp.keys = _practice_key_resp_allKeys[-1].name  # just the last key pressed
                    practice_key_resp.rt = _practice_key_resp_allKeys[-1].rt
                    practice_key_resp.duration = _practice_key_resp_allKeys[-1].duration
                    # was this correct?
                    if (practice_key_resp.keys == str(answer)) or (practice_key_resp.keys == answer):
                        practice_key_resp.corr = 1
                    else:
                        practice_key_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practice" ---
        for thisComponent in practiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('practice.stopped', globalClock.getTime(format='float'))
        # check responses
        if practice_key_resp.keys in ['', [], None]:  # No response was made
            practice_key_resp.keys = None
            # was no response the correct answer?!
            if str(answer).lower() == 'none':
               practice_key_resp.corr = 1;  # correct non-response
            else:
               practice_key_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for practices (TrialHandler)
        practices.addData('practice_key_resp.keys',practice_key_resp.keys)
        practices.addData('practice_key_resp.corr', practice_key_resp.corr)
        if practice_key_resp.keys != None:  # we had a response
            practices.addData('practice_key_resp.rt', practice_key_resp.rt)
            practices.addData('practice_key_resp.duration', practice_key_resp.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.500000)
        
        # --- Prepare to start Routine "feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('feedback.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code
        message=''
        message_color=''
        if practice_key_resp.corr:
            message='回答正确!'
            message_color='green'
        else:
            message='回答错误!'
            message_color='red'
        feedback_text.setColor(message_color, colorSpace='rgb')
        feedback_text.setText(message)
        # keep track of which components have finished
        feedbackComponents = [feedback_text]
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
        frameN = -1
        
        # --- Run Routine "feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_text* updates
            
            # if feedback_text is starting this frame...
            if feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_text.frameNStart = frameN  # exact frame index
                feedback_text.tStart = t  # local t and not account for scr refresh
                feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_text.started')
                # update status
                feedback_text.status = STARTED
                feedback_text.setAutoDraw(True)
            
            # if feedback_text is active this frame...
            if feedback_text.status == STARTED:
                # update params
                pass
            
            # if feedback_text is stopping this frame...
            if feedback_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_text.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_text.tStop = t  # not accounting for scr refresh
                    feedback_text.tStopRefresh = tThisFlipGlobal  # on global time
                    feedback_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_text.stopped')
                    # update status
                    feedback_text.status = FINISHED
                    feedback_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('feedback.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'practices'
    
    
    # --- Prepare to start Routine "rest" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('rest.started', globalClock.getTime(format='float'))
    rest_key_resp.keys = []
    rest_key_resp.rt = []
    _rest_key_resp_allKeys = []
    # keep track of which components have finished
    restComponents = [rest_text, rest_key_resp]
    for thisComponent in restComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "rest" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rest_text* updates
        
        # if rest_text is starting this frame...
        if rest_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rest_text.frameNStart = frameN  # exact frame index
            rest_text.tStart = t  # local t and not account for scr refresh
            rest_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'rest_text.started')
            # update status
            rest_text.status = STARTED
            rest_text.setAutoDraw(True)
        
        # if rest_text is active this frame...
        if rest_text.status == STARTED:
            # update params
            pass
        
        # *rest_key_resp* updates
        waitOnFlip = False
        
        # if rest_key_resp is starting this frame...
        if rest_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rest_key_resp.frameNStart = frameN  # exact frame index
            rest_key_resp.tStart = t  # local t and not account for scr refresh
            rest_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'rest_key_resp.started')
            # update status
            rest_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(rest_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(rest_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if rest_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = rest_key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _rest_key_resp_allKeys.extend(theseKeys)
            if len(_rest_key_resp_allKeys):
                rest_key_resp.keys = _rest_key_resp_allKeys[-1].name  # just the last key pressed
                rest_key_resp.rt = _rest_key_resp_allKeys[-1].rt
                rest_key_resp.duration = _rest_key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "rest" ---
    for thisComponent in restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('rest.stopped', globalClock.getTime(format='float'))
    # check responses
    if rest_key_resp.keys in ['', [], None]:  # No response was made
        rest_key_resp.keys = None
    thisExp.addData('rest_key_resp.keys',rest_key_resp.keys)
    if rest_key_resp.keys != None:  # we had a response
        thisExp.addData('rest_key_resp.rt', rest_key_resp.rt)
        thisExp.addData('rest_key_resp.duration', rest_key_resp.duration)
    thisExp.nextEntry()
    # the Routine "rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Stroop_conditions.xlsx'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('trial.started', globalClock.getTime(format='float'))
        trial_text2.setColor(color, colorSpace='rgb')
        trial_text2.setText(word)
        trial_key_resp.keys = []
        trial_key_resp.rt = []
        _trial_key_resp_allKeys = []
        # keep track of which components have finished
        trialComponents = [trial_text1, trial_text2, trial_key_resp]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 3.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *trial_text1* updates
            
            # if trial_text1 is starting this frame...
            if trial_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial_text1.frameNStart = frameN  # exact frame index
                trial_text1.tStart = t  # local t and not account for scr refresh
                trial_text1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_text1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_text1.started')
                # update status
                trial_text1.status = STARTED
                trial_text1.setAutoDraw(True)
            
            # if trial_text1 is active this frame...
            if trial_text1.status == STARTED:
                # update params
                pass
            
            # if trial_text1 is stopping this frame...
            if trial_text1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trial_text1.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    trial_text1.tStop = t  # not accounting for scr refresh
                    trial_text1.tStopRefresh = tThisFlipGlobal  # on global time
                    trial_text1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'trial_text1.stopped')
                    # update status
                    trial_text1.status = FINISHED
                    trial_text1.setAutoDraw(False)
            
            # *trial_text2* updates
            
            # if trial_text2 is starting this frame...
            if trial_text2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                trial_text2.frameNStart = frameN  # exact frame index
                trial_text2.tStart = t  # local t and not account for scr refresh
                trial_text2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_text2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_text2.started')
                # update status
                trial_text2.status = STARTED
                trial_text2.setAutoDraw(True)
            
            # if trial_text2 is active this frame...
            if trial_text2.status == STARTED:
                # update params
                pass
            
            # if trial_text2 is stopping this frame...
            if trial_text2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trial_text2.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    trial_text2.tStop = t  # not accounting for scr refresh
                    trial_text2.tStopRefresh = tThisFlipGlobal  # on global time
                    trial_text2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'trial_text2.stopped')
                    # update status
                    trial_text2.status = FINISHED
                    trial_text2.setAutoDraw(False)
            
            # *trial_key_resp* updates
            waitOnFlip = False
            
            # if trial_key_resp is starting this frame...
            if trial_key_resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                trial_key_resp.frameNStart = frameN  # exact frame index
                trial_key_resp.tStart = t  # local t and not account for scr refresh
                trial_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_key_resp.started')
                # update status
                trial_key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(trial_key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(trial_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if trial_key_resp is stopping this frame...
            if trial_key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trial_key_resp.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    trial_key_resp.tStop = t  # not accounting for scr refresh
                    trial_key_resp.tStopRefresh = tThisFlipGlobal  # on global time
                    trial_key_resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'trial_key_resp.stopped')
                    # update status
                    trial_key_resp.status = FINISHED
                    trial_key_resp.status = FINISHED
            if trial_key_resp.status == STARTED and not waitOnFlip:
                theseKeys = trial_key_resp.getKeys(keyList=['d','j','f','k'], ignoreKeys=["escape"], waitRelease=False)
                _trial_key_resp_allKeys.extend(theseKeys)
                if len(_trial_key_resp_allKeys):
                    trial_key_resp.keys = _trial_key_resp_allKeys[-1].name  # just the last key pressed
                    trial_key_resp.rt = _trial_key_resp_allKeys[-1].rt
                    trial_key_resp.duration = _trial_key_resp_allKeys[-1].duration
                    # was this correct?
                    if (trial_key_resp.keys == str(answer)) or (trial_key_resp.keys == answer):
                        trial_key_resp.corr = 1
                    else:
                        trial_key_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('trial.stopped', globalClock.getTime(format='float'))
        # check responses
        if trial_key_resp.keys in ['', [], None]:  # No response was made
            trial_key_resp.keys = None
            # was no response the correct answer?!
            if str(answer).lower() == 'none':
               trial_key_resp.corr = 1;  # correct non-response
            else:
               trial_key_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('trial_key_resp.keys',trial_key_resp.keys)
        trials.addData('trial_key_resp.corr', trial_key_resp.corr)
        if trial_key_resp.keys != None:  # we had a response
            trials.addData('trial_key_resp.rt', trial_key_resp.rt)
            trials.addData('trial_key_resp.duration', trial_key_resp.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.500000)
        
        # --- Prepare to start Routine "feedback1" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('feedback1.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code_2
        message=''
        message_color=''
        if trial_key_resp.corr:
            message='回答正确!'
            message_color='green'
        else:
            message='回答错误!'
            message_color='red'
        feedback_text1.setColor(message_color, colorSpace='rgb')
        feedback_text1.setText(message)
        # keep track of which components have finished
        feedback1Components = [feedback_text1]
        for thisComponent in feedback1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "feedback1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_text1* updates
            
            # if feedback_text1 is starting this frame...
            if feedback_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_text1.frameNStart = frameN  # exact frame index
                feedback_text1.tStart = t  # local t and not account for scr refresh
                feedback_text1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_text1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_text1.started')
                # update status
                feedback_text1.status = STARTED
                feedback_text1.setAutoDraw(True)
            
            # if feedback_text1 is active this frame...
            if feedback_text1.status == STARTED:
                # update params
                pass
            
            # if feedback_text1 is stopping this frame...
            if feedback_text1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_text1.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_text1.tStop = t  # not accounting for scr refresh
                    feedback_text1.tStopRefresh = tThisFlipGlobal  # on global time
                    feedback_text1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_text1.stopped')
                    # update status
                    feedback_text1.status = FINISHED
                    feedback_text1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedback1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback1" ---
        for thisComponent in feedback1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('feedback1.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials'
    
    
    # --- Prepare to start Routine "endings" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('endings.started', globalClock.getTime(format='float'))
    # keep track of which components have finished
    endingsComponents = [endings_text]
    for thisComponent in endingsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "endings" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *endings_text* updates
        
        # if endings_text is starting this frame...
        if endings_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            endings_text.frameNStart = frameN  # exact frame index
            endings_text.tStart = t  # local t and not account for scr refresh
            endings_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endings_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'endings_text.started')
            # update status
            endings_text.status = STARTED
            endings_text.setAutoDraw(True)
        
        # if endings_text is active this frame...
        if endings_text.status == STARTED:
            # update params
            pass
        
        # if endings_text is stopping this frame...
        if endings_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > endings_text.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                endings_text.tStop = t  # not accounting for scr refresh
                endings_text.tStopRefresh = tThisFlipGlobal  # on global time
                endings_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'endings_text.stopped')
                # update status
                endings_text.status = FINISHED
                endings_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in endingsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "endings" ---
    for thisComponent in endingsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('endings.stopped', globalClock.getTime(format='float'))
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
