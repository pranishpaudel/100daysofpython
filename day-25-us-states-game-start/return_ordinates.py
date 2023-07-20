import pandas



class Ordinates:

    def __init__(self):
        self.file= open("day-25-us-states-game-start/50_states.csv")
        self.data= pandas.read_csv(self.file)
        self.all_state= self.data["state"].to_list()

    
    def x_coordinate(self, ask_state):
        new_row= self.data[self.data["state"] == ask_state]
        new_x= int(new_row["x"])
        return new_x


    def y_coordinate(self, ask_state):
        new_row= self.data[self.data["state"] == ask_state]
        new_y= int(new_row["y"])
        return new_y

