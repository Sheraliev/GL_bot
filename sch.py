import schedule
import time
def job():
    print("Работаю")

schedule.every(1).seconds.do(job)
# нужно иметь свой цикл для запуска планировщика с периодом в 1 секунду:
while True:
    schedule.run_pending()
    time.sleep(1)