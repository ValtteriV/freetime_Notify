from domain.notifications import Notifications
import sched, time
from win10toast import ToastNotifier


class Notifier:
    def __init__(self, notifications: Notifications):
        self.toaster = ToastNotifier()
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.notifications = notifications

    def notify(self):
        next_notification_time = self.notifications.next_timer()
        print("current time is {}".format(time.time))
        print("next notification is {}".format(next_notification_time))
        if (next_notification_time != -1 and next_notification_time < time.time):
            notif = self.notifications.give_notification()
            self.toaster.show_toast(notif.name, threaded=True)
        self.scheduler.enter(5,1,self.notify)

    def start_scheduler(self):
        self.scheduler.enter(5,1,self.notify)
        while True:
            self.scheduler.run(blocking=False)
