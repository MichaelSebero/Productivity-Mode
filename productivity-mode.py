import psutil
import time

def close_app(app_name):
    running_apps = psutil.process_iter(['pid', 'name'])
    found = False
    for app in running_apps:
        sys_app = app.info.get('name').split('.')[0].lower()

        if sys_app in app_name.split() or app_name in sys_app:
            pid = app.info.get('pid')

            try:
                app_pid = psutil.Process(pid)
                app_pid.terminate()
                found = True
            except:
                pass

        else:
            pass
    if not found:
        print(app_name + " not found running")
    else:
        print(app_name + '(' + sys_app + ')' + ' closed')

application = input('Which application do you want to restrict?  ')

t_end = time.time() + 60 * 120
while time.time() < t_end:
    close_app(application)
    time.sleep(1)
