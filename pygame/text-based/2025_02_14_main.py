class Game:
    def __init__(self):
        self.rooms =[
            ['','Break Room','Corridor','Intersection','Corridor','Data Center',       ''],
            ['','',          '',        'Corridor',     '',        '',                 ''],
            ['','',          '',         'Main',        '',        '',                 ''],
            ['','',          '',         'Intersection','Corridor','Sleeping Quarters',''],
            ['','Storage',   'Corridor', 'Corner',       '',       '',                 ''],
        ]
        self.current_room = 'Main'
        self.current_pos = self.get_pos(self.current_room)
        self.main()

    def get_pos(self, current_room):
        for i, row in enumerate(self.rooms):
            if current_room in row:
                return i, row.index(current_room)

    def move_room(self, current_room):
        pos = self.get_pos(self.current_room)
        choices = {'up': '', 'down': '', 'left': '', 'right': ''}
        print('You can move to: ')

        if self.rooms[pos[0]-1][pos[1]]: # UP
            print(f'[Up] {self.rooms[pos[0]-1][pos[1]]}')
            choices['up'] = self.rooms[pos[0]-1][pos[1]]

        if self.rooms[pos[0]+1][pos[1]]: # DOWN
            print(f'[Down] {self.rooms[pos[0]+1][pos[1]]}')
            choices['down'] = self.rooms[pos[0]+1][pos[1]]

        if self.rooms[pos[0]][pos[1]-1]: # LEFT
            print(f'[Left] {self.rooms[pos[0]][pos[1]-1]}')
            choices['left'] = self.rooms[pos[0]][pos[1]-1]

        if self.rooms[pos[0]][pos[1]+1]: # RIGHT
            print(f'[Right] {self.rooms[pos[0]+1][pos[1]+1]}')
            choices['right'] = self.rooms[pos[0]][pos[1]+1]

        while True:
            print(choices)
            choice = input('Enter choice: ')
            if choices[choice] and choices[choice != '']:
                self.current_room = choice
            else:
                print('Chose a valid path!')



    def main(self):
        print(f'You are currently in {self.current_room}.')
        self.move_room(self.current_room)






game = Game
game()
