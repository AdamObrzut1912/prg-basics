# tv_show.py file
# main program
import tv

def main():
   # object creation
   tele = tv.TV()

   # object usage
   tele.show_status()
   tele.turn_on()
   tele.set_chanel()
   tele.show_status()
   tele.turn_off()
   tele.show_status()

if __name__ == "__main__":
   main() 