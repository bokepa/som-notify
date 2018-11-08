import pystray
import PIL.Image

def configure(icon):
    print("configure")
	
def exitTrayIcon(icon):
    icon.stop()
	
def trayRunner(icon):    
    icon.visible = True
	
theMenu = pystray.Menu(pystray.MenuItem(text="Configura", action=configure, default=True),
                       pystray.MenuItem(text="Surt", action=exitTrayIcon),
					   pystray.Text(text="Hola"))
					   
trayIcon = pystray.Icon(name="Som Monitor", icon=PIL.Image.open('./index.jpg'),
                        title="Som Monitor", menu=theMenu)
trayIcon.warnings = True


trayIcon.run(trayRunner)
