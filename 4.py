from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

app = Flask(__name__)

@app.route('/scrape')
def scrape_data():
    # ChromeOptions 설정
    chrome_options = webdriver.ChromeOptions()

    # HTML 코드
    html_content = '''
    <div class="swiper-slide swiper-slide-next" data-swiper-slide-index="4" style="margin-right: 10px;">
        <a href="https://cu.bgfretail.com/brand_info/news_view.do?category=brand_info&amp;depth2=5&amp;idx=1024" title="VIP 고객님을 위한 4월 특별 혜택관" target=""> <!-- 이미지 링크 변경 필요 -->
            <picture>
            <source media="(max-width: 767px)" srcset="https://cdn2.bgfretail.com/bgfbrand/files/newmainImage/74CCA257408B4B1CA3FCB0E5EDD9928C.jpg">
            <source media="(min-width: 768px)" srcset="https://cdn2.bgfretail.com/bgfbrand/files/newmainImage/0A9C46355A514FDD80E805BB3C96EBF4.jpg">
            <img src="https://cdn2.bgfretail.com/bgfbrand/files/newmainImage/0A9C46355A514FDD80E805BB3C96EBF4.jpg" alt="관리자 등록 이미지"> </picture>
        </a>
    </div>
    '''

    # Chrome 브라우저 초기화
    driver = webdriver.Chrome(options=chrome_options)

    # HTML 코드를 로드하여 파싱
    driver.get("data:text/html;charset=utf-8,{html_content}".format(html_content=html_content))

    # 이미지 URL 가져오기
    img_element = driver.find_element(By.CSS_SELECTOR, 'img')
    img_url = img_element.get_attribute('src')

    # 웹 브라우저 종료
    driver.quit()

    # JSON 형식으로 결과 반환
    return jsonify({'image_url': img_url})

if __name__ == '__main__':
    app.run(debug=True, port=8000)
