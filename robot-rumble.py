# nothing here yet!
x = 0
target_id = '114'
def init_target(state):
    global target_id
    target = state.objs_by_team(state.other_team)[0]
    #print(target.id)
    target_id =  target.id
    
    dis = []
    for unit in state.objs_by_team(state.other_team):
        dis_per = [[]]
        dis_per.append(unit.id)
        for bot in state.objs_by_team(state.our_team):
            dis_per[0].append(bot.coords.walking_distance_to(unit.coords))
            
        dis.append(dis_per)    
    
    means = []
    for entry in dis:
        row = 0
        for value in entry[0]:
            row += value
        row = row / len(entry)
        means.append(row)
    print(dis)
    print(means)
      
def robot(state, unit):
    global target_id
    if state.obj_by_id(target_id) == None:
        init_target(state)
    opponent = state.obj_by_id(target_id)
    #print(f'Opponent Coordinates: {opponent.coords}')
    #print(f'Friendly Coordinates: {unit.coords}')
    dir = unit.coords.direction_to(opponent.coords)
    #print(dir)
    dis = unit.coords.walking_distance_to(opponent.coords)
   # print(dis)
    global x
    
    if dis <= 1:
        return Action.attack(Direction.East)
    else:
        
        return Action.move(dir)
    
