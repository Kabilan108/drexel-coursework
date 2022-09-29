outVid = VideoWriter('shuttle_out.avi');
outVid.FrameRate = 10;
open(outVid)

cam = webcam;

for i = 1:500
	I = snapshot(cam);
	writeVideo(outVid,I)
end

close(outVid)
clear cam