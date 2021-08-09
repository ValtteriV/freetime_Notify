import sched, time as tim
from win10toast import ToastNotifier
from threading import Thread
class Notification:
    def __init__(self, event, time=0):
        self.event = event
        self.time = time

notifier = ToastNotifier()
counter = 0

s = sched.scheduler(tim.time, tim.sleep)

def Notify():
    global counter, s
    print("I have been notified ", counter, " times so far")
    counter += 1
    s.enter(1,1,Notify)
    #notifier.show_toast(notif.event,threaded=True)


def loop(scheduler):
    while True:
        scheduler.run(blocking=False)

s.enter(1,1,Notify)

thr = Thread(target=loop,args=(s,))

thr.start()

tim.sleep(10)
print("this thread is still going strong")

# saa = "a"

# while saa!="":
#     saa = input()
#     aa = Notification(saa)
#     s.enter(5,1,Notify,(aa,))
#     s.run(blocking=False)


# while True:
#     event_name = input("give a name for the event you want to be notified of \n")
#     event_time = input("how long do you want to wait for the notification? (valid inputs seconds/minutes:seconds/hours:minutes:seconds) \n")
#     split_time = event_time.split(":")
#     try:
#         split_time = [int(x) for x in split_time]
#     except:
#         print("Are you inputting numbers?")
#         exit()
#     print("your split time is ", split_time)

#     time_in_seconds = 0
#     time_in_seconds += split_time[-1]
#     time_in_seconds += 60*split_time[-2] if len(split_time)>1 else 0
#     time_in_seconds += 60**2*split_time[0] if len(split_time)>2 else 0

#     print("your thing happens in ", time_in_seconds, " seconds")