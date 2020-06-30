from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import xlrd
import xlwt

chrome_driver=r'C:\Users\算师妙\PycharmProjects\job\venv\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe'
browser = webdriver.Chrome(executable_path=chrome_driver)
chrome_options = webdriver.ChromeOptions()
# 使用headless无界面浏览器模式
chrome_options.add_argument('--headless') #增加无界面选项
chrome_options.add_argument('--disable-gpu') #如果不加这个选项，有时定位会出现问题
browser.implicitly_wait(30) #隐性等待,如等待时间过长，请使用显性等待
browser.get('http://www.offcn.com/sydw/kaoshi/zj/') #请将zj改成其他省份的缩写
str1 = browser.find_elements_by_class_name('lh_olistCatename')
lists1 = []
for i in str1:
    a = i.text
    lists1.append(a)
    print(a, i.get_attribute('textContent'))

str2 = browser.find_elements_by_class_name('dategwy')
lists2 = []
for i in str2:
    a = i.text
    lists2.append(a)
    print(a, i.get_attribute('textContent'))


#excelpath = r'C:\Users\算师妙\Desktop\工作簿1.xls' #请勿使用xlsx格式，会提示无效
#wtbook = xlwt.Workbook()
#sheet = wtbook.add_sheet('Sheet1',cell_overwrite_ok=True) #新增一个sheet工作表
#headlist = [u'时间',u'类型',u'标题']
#row = 0
#col = 0
#for head in headlist:
    #sheet.write(row,col,head)
    #col = col+1
#for i in range(1,60):