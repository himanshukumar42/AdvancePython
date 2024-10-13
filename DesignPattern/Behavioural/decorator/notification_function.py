def notify_on_completion(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            print("Send email and push notification")
            return result
        except Exception as e:
            print(f"Exception Occurred: {str(e)}")

    return wrapper


@notify_on_completion
def generate_report():
    print("Report generated successfully")


def main() -> None:
    generate_report()


if __name__ == '__main__':
    main()
