# tv.py file
# class definition
class TV:
  def __init__(self):
    self.is_on = False
    self.chanel_no = 1
    self.channels = []
    self.volume = 0

  def turn_off(self):
    self.is_on = False
  def turn_on(self):
    self.is_on = True
    
    
  def show_status(self):
    if self.is_on == True and self.chanel_no > 0 and self.chanel_no < len(self.channels)+1:
      print(f"TV on: {self.is_on}, chanel {self.chanel_no} ({self.channels[self.chanel_no-1]})")
    elif self.is_on == True:
      print(f"TV on: {self.is_on}, volume: {self.volume}")
    else:
      print(f"TV on: {self.is_on}")
    
  def set_chanel(self, new_chanel_no):
    self.chanel_no= new_chanel_no     

  def set_channels(self, channels_list):
    self.channels = channels_list
  
  def show_channels(self):
    print("Channel list:")
    for index, name in enumerate(self.channels, start=1):
      print(f"{index}. {name}")
      
  def inc_vol(self):
    if self.volume < 10:
      self.volume += 1
  def dec_vol(self):
    if self.volume > 0:
      self.volume -= 1
    
  