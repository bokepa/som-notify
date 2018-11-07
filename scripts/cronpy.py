from crontab import CronTab

cron = CronTab(user='dhj')  
job = cron.new(command='python test.py >> socis.txt')  
job.minute.every(1)

cron.write()  