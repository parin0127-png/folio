from datetime import datetime
import pytz

def timezone_check(timezone: str):
    """get current time, date, and timezone information for any city or location worldwide"""
    try:
        tz = pytz.timezone(timezone)
        time = datetime.now(tz)
        return {
            "timezone": timezone,
            "time" : time.strftime("%Y-%m-%d %H:%M:%S"),
            "utc_offset": str(time.utcoffset())
        }
    except Exception as e:
        return f"> Timezone convert failed: {str(e)}"


