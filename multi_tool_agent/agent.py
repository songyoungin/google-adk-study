import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent


def get_weather(city: str) -> dict[str, str]:
    """입력으로 들어온 도시에 대해서 날씨 정보를 반환하는 함수

    Args:
        city (str): 날씨 정보를 조회할 도시 이름 ("new york"만 지원) (예: "new york")

    Returns:
        dict[str, str]: 상태와 결과 또는 에러 메시지
    """
    if city.lower() == "new york":
        return {
            "status": "success",
            "report": (
                "The weather in New York is sunny with a temperature of 25 degrees"
                " Celsius (77 degrees Fahrenheit)."
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available.",
        }


def get_current_time(city: str) -> dict[str, str]:
    """입력으로 들어온 도시에 대해서 현재 시간을 반환하는 함수

    Args:
        city (str): 현재 시간을 조회할 도시 이름 ("new york"만 지원) (예: "new york")

    Returns:
        dict[str, str]: 상태와 결과 또는 에러 메시지
    """

    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": (f"Sorry, I don't have timezone information for {city}."),
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = f"The current time in {city} is {now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"
    return {"status": "success", "report": report}


root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash",
    description=("Agent to answer questions about the time and weather in a city."),
    instruction=(
        "You are a helpful agent who can answer user questions about the time and weather in a city."
    ),
    tools=[get_weather, get_current_time],
)
