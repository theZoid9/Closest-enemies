def closest_enemies(matrix):
    enemies_pos = []
    rows = len(matrix)
    columns = len(matrix[0])
    
    for i in range(columns):
        for x in range(rows):
            if matrix[i][x] == "1":
                player_pos = [i,x]
            if matrix[i][x] == "2":
                enemies_pos.append((i,x))
       
    distance = []  
    if len(enemies_pos)  == 0:
        return 0
    for enemies in enemies_pos:
        distance_height = abs(player_pos[1] - enemies[1])
        wrapped_h = columns - distance_height
        height_min = min(wrapped_h,distance_height)
        
        distance_vertical = abs(player_pos[0] - enemies[0])
        wrapped_v = columns - distance_vertical
        vertical_min = min(wrapped_v,distance_vertical)
        
        total_distance = height_min + vertical_min
        distance.append(total_distance)    
        
    return min(distance)
    
    

closest_enemies([
 "0000", 
 "2010",
 "0000", 
 "2002"])