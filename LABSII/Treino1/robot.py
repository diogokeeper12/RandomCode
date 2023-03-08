def robot(comandos):
    pos = {0:(0,1), 1:(-1,0), 2:(0,-1), 3:(1,0)}

    res = []
    
    if comandos[-1] != 'H':
      com = comandos.split('H')
    
    else:
      com = comandos.split('H')
      com.pop()
    
    for instruction in com:
      direcao = 0
      cord = [(0,0)]
      val = {'x':0, 'y':0}
      for char in instruction:
        
        if char == 'E':
          direcao = (direcao+1)%4
        
        elif char == 'D':
          direcao = (direcao-1)%4
        
        elif char == 'A':
          val['x'] += (pos[direcao])[0]
          val['y'] += (pos[direcao])[1]
          cord.append((val['x'],val['y']))
      
      min_x = sorted(cord,key=lambda x: x[0])[0][0]
      min_y = sorted(cord,key=lambda x: x[1])[0][1]
      max_x = sorted(cord,key=lambda x: x[0],reverse=True)[0][0]
      max_y = sorted(cord,key=lambda x: x[1],reverse=True)[0][1]
      res.append(tuple((min_x,min_y,max_x,max_y)))
    return res