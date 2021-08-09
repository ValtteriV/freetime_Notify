from domain.notifications import Notifications
from gui.gui import GUI
from threading import Thread
from notifier import Notifier


if __name__ == "__main__":
    notif = Notifications()
    notifier = Notifier(notif)
    thread = Thread(target=notifier.start_scheduler)
    gui = GUI(notif)
    gui.run()