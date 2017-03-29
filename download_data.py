from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys


profile = webdriver.FirefoxProfile()

profile.set_preference("browser.download.panel.shown", False)
profile.set_preference("browser.download.dir", "D:\\GitRepos\\SchoolDistricts\\data_download")
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-msexcel,application/excel,application/x-excel,application/vnd.ms-excel")
profile.update_preferences()

driver = webdriver.Firefox(firefox_profile=profile)

driver.get("https://nces.ed.gov/programs/edge/tables.aspx?ds=acs&y=2011")
# geo_select = driver.find_element_by_id("ddlGeoType")
geo_select = driver.find_element_by_xpath("//select[@id='ddlGeoType']/option[text()='All School Districts by State']")
geo_select.click()


# sleep(1)
state_select = driver.find_element_by_id('ddlUSSchoolDistrictAllState')#"//select[@id='ddlUSStateForDistrict']")#/option[text()='Pennsylvania']")
WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.ID, "ddlUSSchoolDistrictAllState")))
state_select.click()
count = 0
for s in state_select.find_elements_by_tag_name("option"):

    if state_select.is_displayed():
        pass
    else:
        open_geo = driver.find_element_by_xpath("//*[@id='accordionGeography']/h3")
        hov = ActionChains(driver).move_to_element(open_geo)
        hov.perform()
        sleep(1)
        driver.find_element_by_xpath("//*[@id='titleGeography']").click()

    if s.text == "- Select State -":
        pass
    else:
        if count == 1:
            s.click()
            select_pop = driver.find_element_by_xpath("//*[@id='ddlEnrollmentType']/option[5]")
            select_pop.click()
            WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='B02001']/div[2]")))
            select_char = driver.find_element_by_xpath("//*[@id='B02001']/div[2]")
            select_char.click()
        else:
            WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.ID, "ddlUSSchoolDistrictAllState")))
            state_select.click()
            s.click()

        WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.ID, "btnTableExportToExcel")))
        down_excel = driver.find_element_by_xpath("//*[@id='btnTableExportToExcel']/span[2]")
        down_excel.click()

        WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='divMessageBody']/a")))
        confirm_down = driver.find_element_by_xpath("//*[@id='divMessageBody']/a")
        confirm_down.click()

        WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[11]/div/button/span")))
        done = driver.find_element_by_xpath("/html/body/div[2]/div[11]/div/button/span")
        done.click()

    count += 1