import httpx
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://date.nager.at/api/v4"
mcp = FastMCP("nager-holidays")


async def _get(path: str):
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=15) as client:
        r = await client.get(path)
        r.raise_for_status()
        return r.json()


@mcp.tool()
async def get_available_countries() -> list[dict]:
    """List all countries supported by the Nager.Date API."""
    return await _get("/Countries/Available")


@mcp.tool()
async def get_country_info(country_code: str) -> dict:
    """Get details about a country (names, region, border countries).

    Args:
        country_code: ISO 3166-1 alpha-2 code, e.g. "FR".
    """
    return await _get(f"/Countries/{country_code.upper()}")


@mcp.tool()
async def get_public_holidays(country_code: str, year: int) -> list[dict]:
    """Get all public holidays for a country and year.

    Args:
        country_code: ISO 3166-1 alpha-2 code, e.g. "FR".
        year: Four-digit year, e.g. 2026.
    """
    return await _get(f"/Holidays/{country_code.upper()}/{year}")


@mcp.tool()
async def get_next_public_holidays(country_code: str) -> list[dict]:
    """Get upcoming public holidays for a country within the next 365 days.

    Args:
        country_code: ISO 3166-1 alpha-2 code, e.g. "IT".
    """
    return await _get(f"/Holidays/{country_code.upper()}/Next")


@mcp.tool()
async def is_today_public_holiday(iso_code: str, offset: int = 0) -> dict | bool:
    """Check whether today is a public holiday.

    Args:
        iso_code: Country code ("FR") or subdivision code ("DE-BY").
        offset: UTC offset in hours (e.g. 1 for CET) to decide what "today" is.
    """
    return await _get(f"/IotHolidays/{iso_code.upper()}/IsToday/{offset}")


@mcp.tool()
async def get_api_version() -> dict:
    """Return the Nager.Date library version information."""
    return await _get("/Versions")


if __name__ == "__main__":
    mcp.run()
