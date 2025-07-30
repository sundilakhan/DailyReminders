import time
import threading
from plyer import notification

# ========== Fixed Reminders ==========
def fixed_reminders():
    while True:
        # Hydration reminder every 1 hour
        notification.notify(
            title="💧 Time to Hydrate!",
            message="Drink a glass of water to stay healthy!",
            timeout=10
        )
        time.sleep(60 * 60)  # 1 hour

        # Study reminder (every 24 hours)
        notification.notify(
            title="📚 Study Time!",
            message="Get ready to seek some knowledge... Best of Luck!",
            timeout=10
        )
        time.sleep(60 * 60 * 24)  # 1 day

        # Break reminder (every 3 hours)
        notification.notify(
            title="☕ Break Time!",
            message="Take a short break and relax!",
            timeout=5
        )
        time.sleep(60 * 60 * 3)  # 3 hours


# ========== Custom User Reminder ==========
def custom_reminder():
    reminder_message = input("Enter your reminder message: ")
    interval_type = input("Set interval (m for minutes, h for hours): ").lower()
    interval_value = int(input("Enter the interval value: "))

    # Convert to seconds
    if interval_type == 'm':
        interval_seconds = interval_value * 60
    elif interval_type == 'h':
        interval_seconds = interval_value * 60 * 60
    else:
        print("Invalid type, defaulting to 1 hour.")
        interval_seconds = 3600

    print("\n🔔 Custom reminder system is running... Press Ctrl+C to stop.\n")

    while True:
        notification.notify(
            title="🔔 Custom Reminder",
            message=reminder_message,
            timeout=10
        )
        time.sleep(interval_seconds)


# ========== Run Both in Parallel ==========
if __name__ == "__main__":
    # Create threads
    fixed_thread = threading.Thread(target=fixed_reminders)
    custom_thread = threading.Thread(target=custom_reminder)

    # Start threads
    fixed_thread.start()
    custom_thread.start()

    # Keep main program alive
    fixed_thread.join()
    custom_thread.join()
