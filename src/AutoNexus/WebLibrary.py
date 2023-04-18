from webdriver_manager.chrome import ChromeDriverManager
from robot.api.deco import keyword
from robot.utils.robotpath import abspath
from selenium.webdriver.chrome.options import Options
import os,random,string,tempfile

class WebLibrary:

    @keyword("Install Webdriver")
    def install_webdriver(self, browser):
        exec_path = abspath('.')
        if browser == 'Chrome':
            return ChromeDriverManager(path = exec_path).install()

    @keyword("Create Chrome Options")
    def create_chrome_options(self,
                              is_headless=False,
                              is_incognito=False):
        chrome_options = Options()
        if is_headless:
            chrome_options.add_argument('--headless=new')
        if is_incognito:
            chrome_options.add_argument('--incognito')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-popup-blocking')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--ignore_certificate-errors')
        prefs = {'download.default_directory' : self._generate_download_directory()}
        chrome_options.add_experimental_option('prefs', prefs)
        return chrome_options

    def _generate_download_directory(self):
        character_set = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(character_set) for i in range(4))
        return os.path.join(abspath(tempfile.gettempdir()), random_string)
    
# if __name__ == "__main__":
#     library = WebLibrary()
#     options = library.create_chrome_options()
#     print(library.install_webdriver('Chrome'))
