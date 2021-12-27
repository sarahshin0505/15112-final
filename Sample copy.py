################################################################################
# Copyright (C) 2012-2013 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################

#this file gets the leap motion working, and links it back to the main 

import Leap, sys, thread, time
sys.path.insert(0, "../lib/x86")
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
import pygame
import pygame.display
from tp_main import *
from tp_fruits import *
from tp_sword import *

pygame.init()
pygame.display.init()

class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE); 

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()
        # Get hands
        for hand in frame.hands:
            handType = "Left hand" if hand.is_left else "Right hand"
            x = (hand.palm_position)[0]
            y = (hand.palm_position)[1]
            print(x,y)
        # for gesture in frame.gestures():
        #     if gesture.type == Leap.Gesture.TYPE_SWIPE:
        #         swipe = SwipeGesture(gesture)
        #         print(swipe.position, swipe.direction)
        #         x = swipe.position[0] + swipe.direction[0]
        #         y = swipe.position[1] + swipe.direction[1]
        #         # return (swipe.position, swipe.direction)
    
def main():
    game = PygameGame()
    game.run()
    # Create a sample listener and controller
    listener = SampleListener()   
    controller = Leap.Controller()
    # Have the sample listener receive events from the controller
    controller.add_listener(listener)
    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()


