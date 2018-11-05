# Video_handling

## Creating a video using OpenCV 2.4.0 in python
https://stackoverflow.com/questions/14440400/creating-a-video-using-opencv-2-4-0-in-python
```pytnon


```


[이미지 reading과 writing](http://sams.epaiai.com/220499281999)

[비디오 reading과 writing](http://sams.epaiai.com/220500854338)



## 파일을 steam으로 전달 


```python 

vs = cv2.VideoCapture('exmaple_01.mp4')
while True:

	# read the next frame from the video stream and resize it

	frame = vs.read() #파일 읽기
```