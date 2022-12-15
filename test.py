from datetime import datetime

import pytz


def is_dst(dt=None, timezone="UTC"):
    if dt is None:
        dt = datetime.utcnow()
    timezone = pytz.timezone(timezone)
    timezone_aware_date = timezone.localize(dt, is_dst=None)
    return timezone_aware_date.tzinfo._dst.seconds != 0


print(f"is_dst: {is_dst()}")
print(f"is_dst: {is_dst(datetime(2019, 1, 1), timezone='US/Eastern')}")
print(f"is_dst: {is_dst(datetime(2019, 4, 1), timezone='US/Eastern')}")
print(f"is_dst: {is_dst(datetime.now(), timezone='US/Eastern')}")
