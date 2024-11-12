from playwright.sync_api import sync_playwright

def test_installation():
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto('https://www.google.com')
            print("Playwright 安装成功并可以正常运行!")
            browser.close()
    except Exception as e:
        print(f"安装可能有问题: {e}")

test_installation()