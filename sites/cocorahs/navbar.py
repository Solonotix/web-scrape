from selenium.webdriver.remote.webelement import WebElement

from selenium_pom import BasePage, Locator


class NavBar(BasePage):
    url = 'https://www.cocorahs.org'

    @property
    def links(self) -> dict[str, WebElement]:
        # Must be re-computed everytime to avoid stale element references
        links = dict()
        # for each link in the top-nav
        for locator in (Locator.css('ul.MenuPanelList a'), Locator.css('td.header_menubar a')):
            for element in self.find_elements(locator):
                text = element.text.strip()
                if text:
                    links[text] = element

        return links

    def navbar_link(self, contains: str):
        for link, element in self.links.items():
            if contains in link:
                element.click()
            else:
                print(f'Unable to click navbar link with text "{contains}"')

'''
Home
Countries
States
View Data
Maps
My Data Entry
Login
Daily Precip Reports
Daily Comments Reports
Significant Weather Reports
Multiple Day Reports
Condition Monitoring Reports
Condition Monitoring Charts
Soil Moisture
ET Reports
Days with Hail
Search Hail Reports
Station Hail Reports
Station Precip Summary
Water Year Summary
Station Snow Summary
Rainy Days Report
Total Precip Summary
Station Water Balance
Water Balance Summary
Water Balance Charts
List Stations
Frost
Optics
Snowflake
Thunder
About Us
Join CoCoRaHS
Contact Us
Donate
FAQ / Help
Education
Training Slide-Shows
Videos
Condition Monitoring
Evapotranspiration
NCEI Normals
Volunteer Coordinators
Hail Pad
Distribution/Drop-off
Help Needed
Printable Forms
The Catch
Message of the Day
Publications
CoCoRaHS Blog
Web Groups
State Newsletters
Master Gardener Guide
State Climate Series
March Madness
WxTalk Webinars
Sponsors
Links
CoCoRaHS Store
Daily Precipitation Reports
Multiple Day Accumulation Reports
Condition Monitoring Summary Charts
Evapotranspiration Reports
Soil Moisture Reports
Days With Hail Reports
Water Year Summary Reports
Station Precipitation Summary Report
Station Snow Summary Report
Station Water Balance Summary Report
Station Water Balance Chart
Total Precipitation Summary
Frost Reports
Optics Reports
Snowflake Reports
Thunder Reports
info@cocorahs.org
Creative Commons Attribution 3.0 License
Privacy Policy
Data Usage Policy
'''