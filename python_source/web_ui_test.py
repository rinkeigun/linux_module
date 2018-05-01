from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import sys

# ブラウザの起動
#driver = webdriver.Firefox(u'C:\\Users\\linhu\\AppData\\Local\\Programs\\Python\\Python36\\selenium\\webdriver\\firefox\\amd64')
# chromedriver のダウンロード、パス指定が必要
driver = webdriver.Chrome("C:\\Users\\linhu\\AppData\\Local\\Programs\\Python\\Python36\\chromedriver.exe")

# ウィンドウの最大化
driver.maximize_window()

# Web サイトへのアクセス

driver.get("https://www.shufti.jp/users/login")
#driver.get("https://github.com")

# Web サイトのタイトルを取得
driver.title


# "q" という名前を持つエレメントを指定する
# ここでは，リポジトリ検索用のキーワード入力フォームのこと

#form_textfield = driver.find_element_by_name("user[login]")
#form_textfield.send_keys("hoge")
form_textfield = driver.find_element_by_id("UserEmail")
form_textfield.send_keys("huiqun.lin@gmail.com")
form_textfield = driver.find_element_by_id("UserPassword")
form_textfield.send_keys(sys.argv[1])
form_submit = driver.find_element_by_class_name('submit')
form_submit.submit()
'''
#form_textfield = driver.find_element_by_name("q")
# 入力フォームに，”hoge”と入力する
form_textfield.send_keys("hoge")
# 入力した内容を削除する
form_textfield.clear()
# 入力したキーワード("hoge")を送信し，検索を実行する
form_textfield.submit()
# 入力フォームの場所を調べる
form_textfield.location
# 入力フォームのサイズを調べる
form_textfield.size
# 入力フォームのタグ名を調べる
form_textfield.tag
# エレメントの(HTMLソース上の)テキストを調べる
form_textfield.text

# エレメントを xpath で指定する
# ここでは，ページ下部の1, 2, ..., n と書いてあるボタンのうち，2と書いてあるボタンを指す
next_button = driver.find_element_by_xpath("//*[@id=\"container\"]/div[2]/div/div[2]/div[2]/div/a[1]")
# このエレメントはクリックできるので，クリックしてみる
next_button.click()

# エレメントを xpath で指定する
# ここでは，python を使ったリポジトリに絞って再検索してみる．
refined_search_python = driver.find_element_by_xpath("//*[@id=\"container\"]/div[2]/div/div[1]/ul/li[9]/a")
refined_search_python.click()
'''
# タイムアウト時間を設定する(ページ遷移) <- まだ試していない
driver.set_page_load_timeout(1)

# タイムアウト時間を設定する(スクリプトの実行) <- まだ試していない
driver.set_page_script_timeout(1)

# ページを一つ戻す
# やりかたその1
#ActionChains(driver).key_down(Keys.BACKSPACE).send_keys('').keys_up(Keys.BACKSPACE).send_keys('').perform()
# やりかたその2
driver.back()

# ページを一つ進める
driver.forward()

# スクリーンショットをとる
driver.get_screenshot_as_file("./hogehoge.png")
'''
# ウィンドウの位置を調べる
driver.get_window_position()

# ウィンドウのサイズを調べる
driver.get_window_size()

# ページの更新
driver.refresh()

# url の取得
driver.current_url

# 現在使用しているブラウザの種類を調べる
driver.name

# 現在開いているページのソースを取得する
driver.page_source

# ブラウザを閉じる
# やりかたその1
driver.quit()
# やりかたその2
driver.close()
'''