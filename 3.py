from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By

app = Flask(__name__)

@app.route('/scrape')
def scrape_data():
    # Firefox를 사용하기 위한 WebDriver 설정
    driver = webdriver.Firefox()

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

    # HTML 코드를 로드하여 파싱
    driver.get("data:text/html;charset=utf-8,{html_content}".format(html_content=html_content))

    # 요소 찾기
    element = driver.find_element(By.CLASS_NAME, 'swiper-slide')

    # 결과 출력
    outerHTML = element.get_attribute('outerHTML')

    # 브라우저 종료
    driver.quit()

    # JSON 형식으로 결과 반환
    return jsonify({'result': outerHTML})

if __name__ == '__main__':
    app.run(debug=True)
