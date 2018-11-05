# Video_handling

## Creating a video using OpenCV 2.4.0 in python
https://stackoverflow.com/questions/14440400/creating-a-video-using-opencv-2-4-0-in-python
```pytnon


```


[이미지 reading과 writing](http://sams.epaiai.com/220499281999)

[비디오 reading과 writing](http://sams.epaiai.com/220500854338)



## 파일을 steam으로 전달 


```python 

from imutils.video import FileVideoStream


vs = FileVideoStream('/workspace/tutorial/people-counting-opencv/videos/exmaple_01.mp4').start()
time.sleep(1.0)


while vs.more():
	# read the next frame from the video stream and resize it
	print("2")
	frame = vs.read() #파일 읽기
	print("21")
#https://www.pyimagesearch.com/2017/02/06/faster-video-file-fps-with-cv2-videocapture-and-opencv/
```