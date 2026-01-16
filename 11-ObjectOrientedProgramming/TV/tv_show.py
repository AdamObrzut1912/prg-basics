# tv_show.py file
# main program
import tv

def main():
   tv1 = tv.TV()

   # object usage
   tv1.show_status()
   tv1.turn_on()
   tv1.show_status()
   tv1.turn_off()
   tv1.show_status()

   tv2 = tv.TV()
   tv2.show_status()
   tv2.turn_on()
   tv2.show_status()
   tv2.set_chanel(5)
   tv2.show_status()
   tv2.turn_off()
   tv2.show_status()

   tv3 = tv.TV()
   tv3.show_status()
   tv3.turn_on()
   tv3.show_status()
   tv3.show_channels()
   chanels = ["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"]
   tv3.set_channels(chanels)
   tv3.show_channels()
   tv3.show_status()
   tv3.turn_off()


   tv4 = tv.TV()
   tv4.turn_on()
   tv4.set_channels(chanels)
   tv4.set_chanel(7)
   tv4.show_status()
   tv4.set_chanel(3)
   tv4.show_status()
   tv4.set_chanel(1)
   tv4.show_status()
   tv4.turn_off()


   tv5 = tv.TV()
   tv5.show_status()
   tv5.turn_on()
   tv5.inc_vol()
   tv5.inc_vol()
   tv5.inc_vol()
   tv5.inc_vol()
   tv5.show_status()
if __name__ == "__main__":
   main() 