# tv.py file
# class definition
class TV:
    def __init__(self):
      self.is_on = False
    def turn_off(self):
      self.is_on = False
    def turn_on(self):
      self.is_on = True
    def chanel_no(self, chanel):
       self.chanel = chanel
    def set_chanel(new_chanel_no):
       new_chanel_no = input("podaj nowy kanał")
       print(f"Change TV chanel to {new_chanel_no}")
    def show_status(self):
        if self.is_on == True:
          print(f"Tv is on, chanel {new_chanel_no}")
        else:
          print("TV is off")
   
    