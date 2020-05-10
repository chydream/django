import threading

from django.db.models import F

from weibo.models import WeiboUser


class ChangeThread(threading.Thread):
    def __init__(self, max_count=100, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_count = max_count

    def run(self):
        count = 0
        user = WeiboUser.objects.get(pk=3)
        while True:
            if count >= self.max_count:
                break
            print(self.getName(), count)
            user.status = F('status') + 1
            user.save()
            count += 1

def main():
    t1 = ChangeThread(max_count=800)
    t2 = ChangeThread(max_count=500)
    t1.start()
    t2.start()
    t1.join()
    t2.join()