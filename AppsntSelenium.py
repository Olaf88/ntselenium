#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException

browser = webdriver.Chrome()
browser.get('http://console.appsnt.com/front/login.html')
browser.implicitly_wait(5)

# Badia data for use
count = 1
user_email = "greg@appsnt.com"
login_passwd = "3Cu+8HNO3=3Cu(NO3)2+4H2O+2NO"
tracking = 'http://tracking.crobo.com/aff_c?offer_id=23968&aff_id=19867&aff_sub2={clickid}&aff_sub=64md9{networkid}3Dqs&aff_sub4={gaid}{idfa}'
tracking2 = 'http://apps.applift.com/aff_c?offer_id=56584&aff_id=26440&aff_unique4=1035015&aff_sub4=1035015&aff_sub={clickid}&source=eR3{networkid}_{sub_channel}&unid={gaid}&ios_ifa={idfa}'
cpaofferkpi = 'Non incentive traffic, iframe allowed'
wadiOffer = 'http://c.snnd.co/api/v4/click?campaign_id=10786950&publisher_id=1593&rt=180129233117&_po=0063ebb0eddfcc51f174b6052f1fce30&_mw=p&_c=500&_cw=p&_ad=1151&sub_1={clickid}&publisher_slot={networkid}-{sub_channel}&pub_gaid={gaid}&pub_idfa={idfa}'
audiobooks = 'http://c.snnd.co/api/v4/click?campaign_id=11468175&publisher_id=1593&rt=180129233117&_po=df7b90760fbe8c21cc74e27b0b5c87b5&_mw=p&_c=500&_cw=p&_ad=1523&sub_1={clickid}&publisher_slot={networkid}-{sub_channel}&pub_gaid={gaid}&pub_idfa={idfa}'
smartlink = 'https://bestperforming.site/c/a20265ba-12da-11e7-b975-06867f9fc2d7?clickid={clickid}&IDFA={IDFA}&GAID={GAID}&pubid={networkid}'


# Login to the website
ele = browser.find_element_by_xpath("//input[@class='d-user' and @type='text']").send_keys(user_email)
ele = browser.find_element_by_xpath("//input[@class='d-pwd' and @type='password']").send_keys(login_passwd)
ele = browser.find_element_by_xpath("//input[@class='s-loginBtn d-loginBtn' and @type='button']").click()
time.sleep(2)


def specialOffer():
    time.sleep(5)
    try:
        browser.get('http://console.appsnt.com/front/index.php#/offer-edit/13903280680229/229')
        time.sleep(8)
        browser.find_element_by_xpath("//textarea[@id='advTracking']").clear()
        browser.find_element_by_xpath("//textarea[@id='advTracking']").send_keys(tracking)
        time.sleep(1)
        browser.find_element_by_xpath("//input[@type='button' and @class='s-okBtn']").click()
    except StaleElementReferenceException:
        pass
    return


def changecpilink(url, cpiOfferUrl):
    time.sleep(5)
    try:
        browser.get(url)
        time.sleep(4)
        browser.find_element_by_xpath("//textarea[@id='advTracking']").clear()
        browser.find_element_by_xpath("//textarea[@id='advTracking']").send_keys(cpiOfferUrl)
        time.sleep(1)
        browser.find_element_by_xpath("//input[@type='button' and @class='s-okBtn']").click()
    except StaleElementReferenceException:
        pass
    return


def changelink(pageURL):
    time.sleep(5)
    try:
        browser.get(pageURL)
        time.sleep(8)
        browser.find_element_by_xpath("//textarea[@id='advTracking']").clear()
        browser.find_element_by_xpath("//textarea[@id='advTracking']").send_keys(smartlink)
        time.sleep(1)
        browser.find_element_by_xpath("//input[@type='button' and @class='s-okBtn']").click()
    except StaleElementReferenceException:
        pass
    return


def changecpalink(pageURL, cpaofferURL):
    time.sleep(5)
    try:
        browser.get(pageURL)
        time.sleep(4)
        browser.find_element_by_xpath("//textarea[@id='advTracking']").clear()
        browser.find_element_by_xpath("//textarea[@id='advTracking']").send_keys(cpaofferURL)
        browser.find_element_by_xpath("//textarea[@id='offerKpi']").send_keys(cpaofferkpi)
        time.sleep(1)
        browser.find_element_by_xpath("//input[@type='button' and @class='s-okBtn']").click()
    except StaleElementReferenceException:
        pass
    return


cpaoffer = 'http://console.appsnt.com/front/index.php#/cpa-offer-edit/19622464810287/287'
AndroidSmart = 'http://click.whatadis.com/smart_link?package_name=com.alibaba.aliexpresshd&affiliate_id=5639'
iOSSmart = 'http://click.whatadis.com/smart_link?package_name=id436672029&affiliate_id=5639'

while True:
    specialOffer()
    changecpilink('http://console.appsnt.com/front/index.php#/offer-edit/7184466510283/283', AndroidSmart)
    changecpilink('http://console.appsnt.com/front/index.php#/offer-edit/15534843160283/283', AndroidSmart)
    changecpilink('http://console.appsnt.com/front/index.php#/offer-edit/29209226320058/58', AndroidSmart)
    changecpilink('http://console.appsnt.com/front/index.php#/offer-edit/37219572550197/197', AndroidSmart)
    changecpilink('http://console.appsnt.com/front/index.php#/offer-edit/25394495510266/266', AndroidSmart)
    print count
    count += 1
    time.sleep(100)
