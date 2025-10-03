from win10toast import ToastNotifier

toast = ToastNotifier()
toast.show_toast(
    "Hello Khalid",
    "I am your notification bar. It's time to study!",
    duration=10
)
