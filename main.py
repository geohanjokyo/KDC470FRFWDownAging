import unittest
import os
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
import time
import datetime
import pandas as pd




class aging(unittest.TestCase):

    def setUp(self):
        # Set up appium
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4723/wd/hub',
            desired_capabilities={
                "platformName": "Android",
                "platformVersion": "12",# 실행할 폰에 맞추어 정보 수정 필요
                "deviceName": "GTA3",# 실행할 폰에 맞추어 정보 수정 필요
                "automationName": "Appium",
                "newCommandTimeout": 3000,
                "appPackage": "com.koamtac.ktsimplebledemofw",
                "appActivity": "com.koamtac.ktsimplebledemofw.MainActivity",
                "udid": "R54R1029CWB",# 실행할 폰에 맞추어 정보 수정 필요
                "noReset": "true"  # app 데이터 유지
            })

    def test_search_field(self):
        # appiun의 webdriver를 초기화 합니다.
        driver = self.driver
        # 테스트 시나리오에 따라 selenium 작성
        sleep(10)

        #fw 다운로드 aging
        cycle = 0
        kdc_fw_up_ok = 0
        kdc_fw_up_ng = 0
        kdc_fw_dn_ok = 0
        kdc_fw_dn_ng = 0
        ble_fw_up_ok = 0
        ble_fw_up_ng = 0
        ble_fw_dn_ok = 0
        ble_fw_dn_ng = 0
        uhf_fw_up_ok = 0
        uhf_fw_up_ng = 0
        uhf_fw_dn_ok = 0
        uhf_fw_dn_ng = 0

        # 연결 상태 확인 후 미연결 시 연결
        con = driver.find_element(By.XPATH,
                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.TextView[2]").text
        conn = con[-9:]
        if conn != "Connected":
            # 햄버거 메뉴 클릭
            driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
            sleep(3)
            # Connect Bonded Device 클릭
            driver.find_element(By.XPATH,
                                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView").click()
            sleep(3)
            # Device 선택(클릭)
            driver.find_element(By.XPATH,
                                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]").click()
            sleep(3)
            # OK 클릭
            driver.find_element(By.XPATH,
                                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]").click()

        # 연결 상태이면 다른 조작 하지 않음
        else:
            pass
        print("연결 성공 Aging 시작")

        sleep(10)

        while True:
            #연결된 device 판단
            #device name으,로 470(475) / A40 구분
            connn = driver.find_element(By.XPATH,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.TextView[2]").text
            conn_d = connn[:6]
            #print(conn_d)
            if conn_d == "KDC470":
                #name이 KDC470이면 uhf fw 벚전으로 470/475 구분
                #log clear
                driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                sleep(3)
                driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.TextView").click()
                sleep(3)
                # Get Firmware Version
                driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                sleep(3)
                driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[12]/android.widget.RelativeLayout/android.widget.TextView").click()
                sleep(3)
                version = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.ListView/android.widget.TextView").text
                version_list = version.split("\n")
                fw_version_uhf = version_list[3][22:]
                # print(fw_version_uhf)
                if fw_version_uhf != "8.2":
                    #uhf fw 버전이 8.3이 아니면 0.5W가 장착된 470
                    fw_version_ble = version_list[2][28:30]
                    # print(fw_version_ble)
                    if fw_version_ble == "05":
                        #ble fw 버전이 05로 시작하면 BLE5.0 기기
                        #A710 & 050024 & 3.3.6 다운로드
                        #470 fw A710 선택
                        driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                        sleep(3)
                        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[4]/android.widget.RelativeLayout/android.widget.TextView").click()
                        sleep(3)
                        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[12]").click()
                        sleep(3)
                        #ble fw 050024 선택
                        driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                        sleep(3)
                        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[6]/android.widget.RelativeLayout/android.widget.TextView").click()
                        sleep(3)
                        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]").click()
                        sleep(3)
                        #uhf fw 3.3.6 선택
                        driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                        sleep(3)
                        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[7]/android.widget.RelativeLayout/android.widget.TextView").click()
                        sleep(3)
                        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[4]").click()
                        sleep(3)
                        #download all
                        driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                        sleep(3)
                        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[11]/android.widget.RelativeLayout/android.widget.TextView").click()
                        sleep(3)
                        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]").click()
                        sleep(3)
                        #fw 업데이트 대기(7분)
                        sleep(430)
                        #재연결
                        driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView").click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]").click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]").click()
                        sleep(10)
                        #버전 확인
                        driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                        sleep(3)
                        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.TextView").click()
                        sleep(3)
                        driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                        sleep(3)
                        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[12]/android.widget.RelativeLayout/android.widget.TextView").click()
                        sleep(3)
                        version = driver.find_element(By.XPATH,
                                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.ListView/android.widget.TextView").text
                        version_list = version.split("\n")
                        kdc_fw = version_list[1][28:]
                        ble_fw = version_list[2][28:]
                        uhf_fw = version_list[3][22:]
                        if kdc_fw == "A710":
                            kdc_fw_up_ok = kdc_fw_up_ok + 1
                        else:
                            kdc_fw_up_ng = kdc_fw_up_ng + 1
                        if ble_fw == "050024":
                            ble_fw_up_ok = ble_fw_up_ok + 1
                        else:
                            ble_fw_up_ng = ble_fw_up_ng + 1
                        if uhf_fw == "RED4S_v1.3.3__AIS_v0.3.6_U":
                            uhf_fw_up_ok = uhf_fw_up_ok + 1
                        else:
                            uhf_fw_up_ng = uhf_fw_up_ng + 1

                        # A704 & 050022 & 3.3.2 다운그레이드
                        # 연결 상태 확인 후 미연결 시 연결
                        con = driver.find_element(By.XPATH,
                                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.TextView[2]").text
                        conn = con[-9:]
                        if conn != "Connected":
                            # 햄버거 메뉴 클릭
                            driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                            sleep(3)
                            # Connect Bonded Device 클릭
                            driver.find_element(By.XPATH,
                                                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView").click()
                            sleep(3)
                            # Device 선택(클릭)
                            driver.find_element(By.XPATH,
                                                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]").click()
                            sleep(3)
                            # OK 클릭
                            driver.find_element(By.XPATH,
                                                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]").click()
                            sleep(10)
                        # 연결 상태이면 다른 조작 하지 않음
                        # 470 fw A704 선택
                        driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[4]/android.widget.RelativeLayout/android.widget.TextView").click()
                        sleep(3)
                        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[7]").click()
                        sleep(3)
                        # ble fw 050022 선택
                        driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                        sleep(3)
                        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[6]/android.widget.RelativeLayout/android.widget.TextView").click()
                        sleep(3)
                        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[1]").click()
                        sleep(3)
                        # uhf fw 3.3.2 선택
                        driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[7]/android.widget.RelativeLayout/android.widget.TextView").click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[3]").click()
                        sleep(3)
                        # download all
                        driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[11]/android.widget.RelativeLayout/android.widget.TextView").click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]").click()
                        sleep(3)
                        # fw 업데이트 대기(7분)
                        sleep(430)
                        # 재연결
                        driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView").click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]").click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]").click()
                        sleep(10)
                        # 버전 확인
                        driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.TextView").click()
                        sleep(3)
                        driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[12]/android.widget.RelativeLayout/android.widget.TextView").click()
                        sleep(3)
                        version = driver.find_element(By.XPATH,
                                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.ListView/android.widget.TextView").text
                        version_list = version.split("\n")
                        kdc_fw = version_list[1][28:]
                        ble_fw = version_list[2][28:]
                        uhf_fw = version_list[3][22:]
                        if kdc_fw == "A704":
                            kdc_fw_dn_ok = kdc_fw_dn_ok + 1
                        else:
                            kdc_fw_dn_ng = kdc_fw_dn_ng + 1
                        if ble_fw == "050022":
                            ble_fw_dn_ok = ble_fw_dn_ok + 1
                        else:
                            ble_fw_dn_ng = ble_fw_dn_ng + 1
                        if uhf_fw == "RED4S_v1.3.3__AIS_v0.3.2_U":
                            uhf_fw_dn_ok = uhf_fw_dn_ok + 1
                        else:
                            uhf_fw_dn_ng = uhf_fw_dn_ng + 1
                        #결과 출력
                        cycle = cycle + 1
                        print("fw 다운로드 테스트" + str(cycle) + " 회 수행")
                        print("KDC(BLE5.0) FW : " + "업그레이드 성공 : " + str(kdc_fw_up_ok) + "회" + " ," + "업그레이드 실패 : " + str(kdc_fw_up_ng) + "회" + "/" +  "다운그레이드 성공 : " + str(kdc_fw_dn_ok) + "회" + " ," + "다운그레이드 실패 : " + str(kdc_fw_dn_ng) + "회")
                        print("ble FW : " + "업그레이드 성공 : " + str(ble_fw_up_ok) + "회" + " ," + "업그레이드 실패 : " + str(ble_fw_up_ng) + "회" + "/" + "다운그레이드 성공 : " + str(ble_fw_dn_ok) + "회" + " ," + "다운그레이드 실패 : " + str(ble_fw_dn_ng) + "회")
                        print("UHF FW : " + "업그레이드 성공 : " + str(uhf_fw_up_ok) + "회" + " ," + "업그레이드 실패 : " + str(uhf_fw_up_ng) + "회" + "/" + "다운그레이드 성공 : " + str(uhf_fw_dn_ok) + "회" + " ," + "다운그레이드 실패 : " + str(uhf_fw_dn_ng) + "회")

                    else:
                        # ble fw 버전이 05가 아니면 BLE4.1 기기
                        # A710 & 040012 & 3.3.6 다운로드
                        # 470 fw A710 선택
                        driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[4]/android.widget.RelativeLayout/android.widget.TextView").click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[12]").click()
                        sleep(3)
                        # uhf fw 3.3.6 선택
                        driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[7]/android.widget.RelativeLayout/android.widget.TextView").click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[4]").click()
                        sleep(3)
                        # download all
                        driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[11]/android.widget.RelativeLayout/android.widget.TextView").click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]").click()
                        sleep(3)
                        # fw 업데이트 대기(12분)
                        sleep(7230)
                        # 재연결
                        driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView").click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]").click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]").click()
                        sleep(10)
                        # 버전 확인
                        driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.TextView").click()
                        sleep(3)
                        driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[12]/android.widget.RelativeLayout/android.widget.TextView").click()
                        sleep(3)
                        version = driver.find_element(By.XPATH,
                                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.ListView/android.widget.TextView").text
                        version_list = version.split("\n")
                        kdc_fw = version_list[1][28:]
                        uhf_fw = version_list[3][22:]
                        if kdc_fw == "A710":
                            kdc_fw_up_ok = kdc_fw_up_ok + 1
                        else:
                            kdc_fw_up_ng = kdc_fw_up_ng + 1
                        if uhf_fw == "RED4S_v1.3.3__AIS_v0.3.6_U":
                            uhf_fw_up_ok = uhf_fw_up_ok + 1
                        else:
                            uhf_fw_up_ng = uhf_fw_up_ng + 1

                        # A704 & 040012 & 3.3.2 다운로드
                        # 470 fw A704 선택
                        driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[4]/android.widget.RelativeLayout/android.widget.TextView").click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[7]").click()
                        sleep(3)
                        # uhf fw 3.3.2 선택
                        driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[7]/android.widget.RelativeLayout/android.widget.TextView").click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[3]").click()
                        sleep(3)
                        # download all
                        driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[11]/android.widget.RelativeLayout/android.widget.TextView").click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]").click()
                        sleep(3)
                        # fw 업데이트 대기(12분)
                        sleep(7230)
                        # 재연결
                        driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView").click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]").click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]").click()
                        sleep(10)
                        # 버전 확인
                        driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.TextView").click()
                        sleep(3)
                        driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                        sleep(3)
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[12]/android.widget.RelativeLayout/android.widget.TextView").click()
                        sleep(3)
                        version = driver.find_element(By.XPATH,
                                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.ListView/android.widget.TextView").text
                        version_list = version.split("\n")
                        kdc_fw = version_list[1][28:]
                        uhf_fw = version_list[3][22:]
                        if kdc_fw == "A704":
                            kdc_fw_dn_ok = kdc_fw_dn_ok + 1
                        else:
                            kdc_fw_dn_ng = kdc_fw_dn_ng + 1
                        if uhf_fw == "RED4S_v1.3.3__AIS_v0.3.2_U":
                            uhf_fw_dn_ok = uhf_fw_dn_ok + 1
                        else:
                            uhf_fw_dn_ng = uhf_fw_dn_ng + 1
                        # 결과 출력
                        cycle = cycle + 1
                        print("fw 다운로드 테스트" + str(cycle) + " 회 수행")
                        print("KDC(BLE4.1) FW : " + "업그레이드 성공 : " + str(kdc_fw_up_ok) + "회" + " ," + "업그레이드 실패 : " + str(kdc_fw_up_ng) + "회" + "/" + "다운그레이드 성공 : " + str(kdc_fw_dn_ok) + "회" + " ," + "다운그레이드 실패 : " + str(kdc_fw_dn_ng) + "회")
                        print("UHF FW : " + "업그레이드 성공 : " + str(uhf_fw_up_ok) + "회" + " ," + "업그레이드 실패 : " + str(uhf_fw_up_ng) + "회" + "/" + "다운그레이드 성공 : " + str(uhf_fw_dn_ok) + "회" + " ," + "다운그레이드 실패 : " + str(uhf_fw_dn_ng) + "회")


                else:
                    #uhf fw 버전이 8.3이면 1.0W가 장착된 475
                    #A710 & 050024 다운로드(uhf는 다운로드 하지 않음)
                    # 470 fw A710 선택
                    driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                    sleep(3)
                    driver.find_element(By.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[4]/android.widget.RelativeLayout/android.widget.TextView").click()
                    sleep(3)
                    driver.find_element(By.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[12]").click()
                    sleep(3)
                    # ble fw 050024 선택
                    driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                    sleep(3)
                    driver.find_element(By.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[6]/android.widget.RelativeLayout/android.widget.TextView").click()
                    sleep(3)
                    driver.find_element(By.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]").click()
                    sleep(3)
                    # download all
                    driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                    sleep(3)
                    driver.find_element(By.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[11]/android.widget.RelativeLayout/android.widget.TextView").click()
                    sleep(3)
                    #uhf 체크박스 해제
                    uhf_checked = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[3]").get_attribute("checked")
                    if uhf_checked == "true":
                        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[3]").click()
                        sleep(3)
                    else:
                        pass
                    driver.find_element(By.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]").click()
                    sleep(3)
                    # fw 업데이트 대기(7분)
                    sleep(430)
                    # 재연결
                    driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                    sleep(3)
                    driver.find_element(By.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView").click()
                    sleep(3)
                    driver.find_element(By.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]").click()
                    sleep(3)
                    driver.find_element(By.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]").click()
                    sleep(10)
                    # 버전 확인
                    driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                    sleep(3)
                    driver.find_element(By.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.TextView").click()
                    sleep(3)
                    driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                    sleep(3)
                    driver.find_element(By.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[12]/android.widget.RelativeLayout/android.widget.TextView").click()
                    sleep(3)
                    version = driver.find_element(By.XPATH,
                                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.ListView/android.widget.TextView").text
                    version_list = version.split("\n")
                    kdc_fw = version_list[1][28:]
                    ble_fw = version_list[2][28:]
                    uhf_fw = version_list[3][22:]
                    if kdc_fw == "A710":
                        kdc_fw_up_ok = kdc_fw_up_ok + 1
                    else:
                        kdc_fw_up_ng = kdc_fw_up_ng + 1
                    if ble_fw == "050024":
                        ble_fw_up_ok = ble_fw_up_ok + 1
                    else:
                        ble_fw_up_ng = ble_fw_up_ng + 1

                    #A704 & 050022 다운로드(uhf는 다운로드 하지 않음)
                    # 470 fw A704 선택
                    driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                    sleep(3)
                    driver.find_element(By.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[4]/android.widget.RelativeLayout/android.widget.TextView").click()
                    sleep(3)
                    driver.find_element(By.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[7]").click()
                    sleep(3)
                    # ble fw 050022 선택
                    driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                    sleep(3)
                    driver.find_element(By.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[6]/android.widget.RelativeLayout/android.widget.TextView").click()
                    sleep(3)
                    driver.find_element(By.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[1]").click()
                    sleep(3)
                    # download all
                    driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                    sleep(3)
                    driver.find_element(By.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[11]/android.widget.RelativeLayout/android.widget.TextView").click()
                    sleep(3)
                    # uhf 체크박스 해제
                    uhf_checked = driver.find_element(By.XPATH,
                                                      "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[3]").get_attribute(
                        "checked")
                    if uhf_checked == "true":
                        driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[3]").click()
                        sleep(3)
                    else:
                        pass
                    driver.find_element(By.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]").click()
                    sleep(3)
                    # fw 업데이트 대기
                    sleep(430)
                    # 재연결
                    driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                    sleep(3)
                    driver.find_element(By.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView").click()
                    sleep(3)
                    driver.find_element(By.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]").click()
                    sleep(3)
                    driver.find_element(By.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]").click()
                    sleep(10)
                    # 버전 확인
                    driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                    sleep(3)
                    driver.find_element(By.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.TextView").click()
                    sleep(3)
                    driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                    sleep(3)
                    driver.find_element(By.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[12]/android.widget.RelativeLayout/android.widget.TextView").click()
                    sleep(3)
                    version = driver.find_element(By.XPATH,
                                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.ListView/android.widget.TextView").text
                    version_list = version.split("\n")
                    kdc_fw = version_list[1][28:]
                    ble_fw = version_list[2][28:]
                    if kdc_fw == "A704":
                        kdc_fw_dn_ok = kdc_fw_dn_ok + 1
                    else:
                        kdc_fw_dn_ng = kdc_fw_dn_ng + 1
                    if ble_fw == "050022":
                        ble_fw_dn_ok = ble_fw_dn_ok + 1
                    else:
                        ble_fw_dn_ng = ble_fw_dn_ng + 1
                    # 결과 출력
                    cycle = cycle + 1
                    print("fw 다운로드 테스트" + str(cycle) + " 회 수행")
                    print("KDC475 FW : " + "업그레이드 성공 : " + str(kdc_fw_up_ok) + "회" + " ," + "업그레이드 실패 : " + str(kdc_fw_up_ng) + "회" + "/" + "다운그레이드 성공 : " + str(kdc_fw_dn_ok) + "회" + " ," + "다운그레이드 실패 : " + str(kdc_fw_dn_ng) + "회")
                    print("ble FW : " + "업그레이드 성공 : " + str(ble_fw_up_ok) + "회" + " ," + "업그레이드 실패 : " + str(ble_fw_up_ng) + "회" + "/" + "다운그레이드 성공 : " + str(ble_fw_dn_ok) + "회" + " ," + "다운그레이드 실패 : " + str(ble_fw_dn_ng) + "회")

            else:
                #A40 fw 다운로드 Aging
                # A710 & 050024 & 3.3.6 다운로드
                # 470 fw A710 선택
                driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                sleep(3)
                driver.find_element(By.XPATH,
                                    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[4]/android.widget.RelativeLayout/android.widget.TextView").click()
                sleep(3)
                driver.find_element(By.XPATH,
                                    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[12]").click()
                sleep(3)
                # ble fw 050024 선택
                driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                sleep(3)
                driver.find_element(By.XPATH,
                                    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[6]/android.widget.RelativeLayout/android.widget.TextView").click()
                sleep(3)
                driver.find_element(By.XPATH,
                                    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]").click()
                sleep(3)
                # uhf fw 3.3.6 선택
                driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                sleep(3)
                driver.find_element(By.XPATH,
                                    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[7]/android.widget.RelativeLayout/android.widget.TextView").click()
                sleep(3)
                driver.find_element(By.XPATH,
                                    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[4]").click()
                sleep(3)
                # download all
                driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                sleep(3)
                driver.find_element(By.XPATH,
                                    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[11]/android.widget.RelativeLayout/android.widget.TextView").click()
                sleep(3)
                driver.find_element(By.XPATH,
                                    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]").click()
                sleep(3)
                # fw 업데이트 대기(7분)
                sleep(430)
                # 재연결
                driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                sleep(3)
                driver.find_element(By.XPATH,
                                    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView").click()
                sleep(3)
                driver.find_element(By.XPATH,
                                    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]").click()
                sleep(3)
                driver.find_element(By.XPATH,
                                    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]").click()
                sleep(10)
                # 버전 확인
                driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                sleep(3)
                driver.find_element(By.XPATH,
                                    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.TextView").click()
                sleep(3)
                driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                sleep(3)
                driver.find_element(By.XPATH,
                                    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[12]/android.widget.RelativeLayout/android.widget.TextView").click()
                sleep(3)
                version = driver.find_element(By.XPATH,
                                              "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.ListView/android.widget.TextView").text
                version_list = version.split("\n")
                kdc_fw = version_list[1][28:]
                ble_fw = version_list[2][28:]
                uhf_fw = version_list[3][22:]
                if kdc_fw == "A710":
                    kdc_fw_up_ok = kdc_fw_up_ok + 1
                else:
                    kdc_fw_up_ng = kdc_fw_up_ng + 1
                if ble_fw == "050024":
                    ble_fw_up_ok = ble_fw_up_ok + 1
                else:
                    ble_fw_up_ng = ble_fw_up_ng + 1
                if uhf_fw == "RED4S_v1.3.3__AIS_v0.3.6_U":
                    uhf_fw_up_ok = uhf_fw_up_ok + 1
                else:
                    uhf_fw_up_ng = uhf_fw_up_ng + 1

                # A704 & 050022 & 3.3.2 다운그레이드
                # 연결 상태 확인 후 미연결 시 연결
                con = driver.find_element(By.XPATH,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.TextView[2]").text
                conn = con[-9:]
                if conn != "Connected":
                    # 햄버거 메뉴 클릭
                    driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                    sleep(3)
                    # Connect Bonded Device 클릭
                    driver.find_element(By.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView").click()
                    sleep(3)
                    # Device 선택(클릭)
                    driver.find_element(By.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]").click()
                    sleep(3)
                    # OK 클릭
                    driver.find_element(By.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]").click()
                    sleep(10)
                # 연결 상태이면 다른 조작 하지 않음
                # 470 fw A704 선택
                driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                sleep(3)
                driver.find_element(By.XPATH,
                                    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[4]/android.widget.RelativeLayout/android.widget.TextView").click()
                sleep(3)
                driver.find_element(By.XPATH,
                                    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[7]").click()
                sleep(3)
                # ble fw 050022 선택
                driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                sleep(3)
                driver.find_element(By.XPATH,
                                    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[6]/android.widget.RelativeLayout/android.widget.TextView").click()
                sleep(3)
                driver.find_element(By.XPATH,
                                    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[1]").click()
                sleep(3)
                # uhf fw 3.3.2 선택
                driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                sleep(3)
                driver.find_element(By.XPATH,
                                    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[7]/android.widget.RelativeLayout/android.widget.TextView").click()
                sleep(3)
                driver.find_element(By.XPATH,
                                    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[3]").click()
                sleep(3)
                # download all
                driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                sleep(3)
                driver.find_element(By.XPATH,
                                    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[11]/android.widget.RelativeLayout/android.widget.TextView").click()
                sleep(3)
                driver.find_element(By.XPATH,
                                    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]").click()
                sleep(3)
                # fw 업데이트 대기(7분)
                sleep(430)
                # 재연결
                driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                sleep(3)
                driver.find_element(By.XPATH,
                                    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView").click()
                sleep(3)
                driver.find_element(By.XPATH,
                                    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]").click()
                sleep(3)
                driver.find_element(By.XPATH,
                                    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]").click()
                sleep(10)
                # 버전 확인
                driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                sleep(3)
                driver.find_element(By.XPATH,
                                    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.TextView").click()
                sleep(3)
                driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="옵션 더보기"]').click()
                sleep(3)
                driver.find_element(By.XPATH,
                                    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[12]/android.widget.RelativeLayout/android.widget.TextView").click()
                sleep(3)
                version = driver.find_element(By.XPATH,
                                              "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.ListView/android.widget.TextView").text
                version_list = version.split("\n")
                kdc_fw = version_list[1][28:]
                ble_fw = version_list[2][28:]
                uhf_fw = version_list[3][22:]
                if kdc_fw == "A704":
                    kdc_fw_dn_ok = kdc_fw_dn_ok + 1
                else:
                    kdc_fw_dn_ng = kdc_fw_dn_ng + 1
                if ble_fw == "050022":
                    ble_fw_dn_ok = ble_fw_dn_ok + 1
                else:
                    ble_fw_dn_ng = ble_fw_dn_ng + 1
                if uhf_fw == "RED4S_v1.3.3__AIS_v0.3.2_U":
                    uhf_fw_dn_ok = uhf_fw_dn_ok + 1
                else:
                    uhf_fw_dn_ng = uhf_fw_dn_ng + 1
                # 결과 출력
                cycle = cycle + 1
                print("fw 다운로드 테스트" + str(cycle) + " 회 수행")
                print("SKXA40 FW : " + "업그레이드 성공 : " + str(kdc_fw_up_ok) + "회" + " ," + "업그레이드 실패 : " + str(
                    kdc_fw_up_ng) + "회" + "/" + "다운그레이드 성공 : " + str(kdc_fw_dn_ok) + "회" + " ," + "다운그레이드 실패 : " + str(
                    kdc_fw_dn_ng) + "회")
                print(
                    "ble FW : " + "업그레이드 성공 : " + str(ble_fw_up_ok) + "회" + " ," + "업그레이드 실패 : " + str(
                        ble_fw_up_ng) + "회" + "/" + "다운그레이드 성공 : " + str(
                        ble_fw_dn_ok) + "회" + " ," + "다운그레이드 실패 : " + str(ble_fw_dn_ng) + "회")
                print(
                    "UHF FW : " + "업그레이드 성공 : " + str(uhf_fw_up_ok) + "회" + " ," + "업그레이드 실패 : " + str(
                        uhf_fw_up_ng) + "회" + "/" + "다운그레이드 성공 : " + str(
                        uhf_fw_dn_ok) + "회" + " ," + "다운그레이드 실패 : " + str(uhf_fw_dn_ng) + "회")


def tearDown(self):
    self.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(aging)
    unittest.TextTestRunner(verbosity=2).run(suite)