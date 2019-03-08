# txt line by line read

```python 
def parse_data(file_path):

  all_sensor_data = []
  all_ground_truths = []  

  with open(file_path) as f:
      
    for line in f:
      data = line.split() 
      
      if data[0]  == 'L':
        
        sensor_data = DataPoint({ 
          'timestamp': int(data[3]),
          'name': 'lidar',
          'x': float(data[1]), 
          'y': float(data[2])
        })
        
        g = {'timestamp': int(data[3]),
             'name': 'state',
             'x': float(data[4]),
             'y': float(data[5]),
             'vx': float(data[6]),
             'vy': float(data[7])
        }
          
        ground_truth = DataPoint(g)
                
      elif data[0] == 'R':
          
        sensor_data = DataPoint({ 
          'timestamp': int(data[4]),
          'name': 'radar',
          'rho': float(data[1]), 
          'phi': float(data[2]),
          'drho': float(data[3])
        })
       
        g = {'timestamp': int(data[4]),
             'name': 'state',
             'x': float(data[5]),
             'y': float(data[6]),
             'vx': float(data[7]),
             'vy': float(data[8])
        }
        ground_truth = DataPoint(g)  

      all_sensor_data.append(sensor_data)
      all_ground_truths.append(ground_truth)

  return all_sensor_data, all_ground_truths
```