import time
import schedule


def job_monday():
    print("Start your weekly goals")


def job_wednesday():
    print("Review your weekly progress")


def job_friday():
    print("Weekly work completed")


def main():
    schedule.every().monday.at("09:00").do(job_monday)
    schedule.every().wednesday.at("17:00").do(job_wednesday)
    schedule.every().friday.at("18:00").do(job_friday)

    print("Scheduler started...")
    print("Press Ctrl + C to stop.")

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nScheduler stopped.")


if __name__ == "__main__":
    main()