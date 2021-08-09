class Notifications:

    def __init__(self):
        self.notificationlist = []
        
    def add_notification(self, name, timer):
        new_notification = Notification(name,timer)
        self.notificationlist.append(new_notification)
        self.sort_notifications()
        print("notification added, timer is {}".format(new_notification.timer))

    def sort_notifications(self): 
        self.notificationlist.sort(key=get_timer)

    def next_timer(self):
        return self.notificationlist[0].timer if len(self.notificationlist) > 0 else -1

    def give_notification(self):
        return self.notificationlist.pop(0)

class Notification:
    def __init__(self, name, timer):
        self.name = name
        self.timer = timer

def get_timer(notification):
        return notification.timer
