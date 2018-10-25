```python 

def tracker_vialization(det,trk):
  img_height = 500
  img_width = 500

  code = long(-1)

  cv.namedWindow("Kalman")

  while True:
      # plot points
      def draw_cross(center, color, d):
          cv.line(img,
                    (center[0] - d, center[1] - d), (center[0] + d, center[1] + d),
                    color, 1, cv.LINE_AA, 0)
          cv.line(img,
                    (center[0] + d, center[1] - d), (center[0] - d, center[1] + d),
                    color, 1, cv.LINE_AA, 0)
      """          
      img – 그림을 그릴 이미지 파일
      start – 시작 좌표(ex; (0,0))
      end – 종료 좌표(ex; (500. 500))
      color – BGR형태의 Color(ex; (255, 0, 0) -> Blue)
      thickness (int) – 선의 두께. pixel
      """
      detss = convert_bbox_to_z(det)
      trkss = convert_bbox_to_z(trk)
    
      #det의 타입은 tuple

      img = np.zeros((img_height, img_width, 3), np.uint8)
      draw_cross(np.int32(det), (255, 255, 255), 3) #white
      draw_cross(np.int32(trk), (0, 0, 255), 3) #blue
      #cv.line(img, state_pt, measurement_pt, (0, 0, 255), 3, cv.LINE_AA, 0)
      #cv.line(img, state_pt, predict_pt, (0, 255, 255), 3, cv.LINE_AA, 0)

      cv.imshow("Kalman", img)

      code = cv.waitKey(100)
      if code != -1:
          break
  cv.destroyWindow("Kalman")  
  
```