from flask import Flask, jsonify
from selenium import webdriver
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_image_url():
    # Chrome WebDriver 초기화
    driver = webdriver.Chrome()
    
    # 웹 페이지 로드
    driver.get("https://cu.bgfretail.com/brand_info/news_view.do?category=brand_info&depth2=5&idx=1024")
    
    # 페이지 소스 가져오기
    html_content = driver.page_source
    
    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(html_content, "html.parser")
    
    # 이미지 URL 찾기
    img_element = soup.find("img")
    img_url = img_element["src"]
    
    # WebDriver 종료
    driver.quit()
    
    return img_url

@app.route('/scrape')
def scrape_data():
    # 이미지 URL 가져오기
    img_url = get_image_url()
    
    # JSON 형식으로 결과 반환
    return jsonify({'image_url': img_url})

if __name__ == '__main__':
    app.run(debug=True, port=9000)
