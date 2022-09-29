Assignment: C.A.7
Class: BMES 202
Team: C03
      -> Tony Kabilan Okeke
      -> Vrigav Narra
      -> Ankit Patel
      -> Deep Patel

FUNCTONS:
-> Only the @liveFeed function can run directly from the command line.
-> @startCapture & @stopCapture are callback functions that allow the 
   buttons in the liveFeed figure to work. As such, the can not be run from
   the command window.
-> @dotFilter filters colored dots from images, and can be run from the 
   command window if desired.

RECCOMENDED USAGE:
-> Run the liveFeed function in the command window.
-> The filtering works best in a bright room, but not in direct sunlight.
-> To test if function works, hold up a red marker, or similar object.
   Move it around the frame, and matlab will identify its position using 
   a yellow circle.

NOTE:
-> Since the program is based on a long while loop, sometimes, the 'Stop 
   Capture' button takes a couple of seconds to execute.
