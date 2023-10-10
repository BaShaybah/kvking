from kivy.factory import Factory
from kvdesign.tools.hotreloader import App

class Main(App):
	CLASSES    = [
		"AppBar",
		"Icon",
		"IconButton",
		"NavDrawer",
		"Slide",
		"UIButton",
		"UIFile",
		"UILoading",
	]
	
	main_folder = "Collection"
	KVROOT      = "kvroot.kv"
	
if __name__ == "__main__":	
	Main().run()