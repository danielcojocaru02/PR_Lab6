import ntplib
from datetime import datetime, timedelta, timezone

def get_time_in_timezone(timezone_offset):
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request('pool.ntp.org')

    current_time_utc = datetime.fromtimestamp(response.tx_timestamp, tz=timezone.utc)
    current_time_timezone = current_time_utc + timedelta(hours=timezone_offset)

    return current_time_timezone

def main():
    try:
        timezone_str = input("Introduceți zona geografică (în format 'GMT+X' sau 'GMT-X'): ")
        if timezone_str.startswith("GMT+") or timezone_str.startswith("GMT-"):
            time_zone = int(timezone_str[4:])
        else:
            raise ValueError("Formatul zonei geografice nu este valid.")
        
        exact_time = get_time_in_timezone(time_zone)
        print(f"Ora exactă în zona {timezone_str} este: {exact_time.strftime('%Y-%m-%d %H:%M:%S')}")
    except ValueError as ve:
        print(f"Eroare: {ve}")

if __name__ == "__main__":
    main()