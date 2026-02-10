from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)
driver.get("http://www.scrapethissite.com/pages/ajax-javascript/")

years = ["2012", "2013", "2014", "2015"]

for year in years:
    butn = driver.find_element(By.XPATH, f'//*[@id="{year}"]').click()
    table = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "table")))

    movies = [] #заметки для аиши: тут мы создаем пустой список
    rows = driver.find_elements(By.CSS_SELECTOR, ".table tbody tr")#заметки для аиши: тут проверяем все ряды
    
    for row in rows: #заметки для аиши: этот цикл перебирает каждый ряд  и проверяя ячейки присваивает им ID а потом к нему присваивает его содержимое 
    #после чего это содержимое сортируется
        cells = row.find_elements(By.TAG_NAME, "td")
        movie_data = {
            "year": year,
            "title": cells[0].text,
            "nominations": int(cells[1].text),
            "awards": int(cells[2].text)
        }
        movies.append(movie_data)
    
    filename = f"movies_{year}.json"# тут мы создаем файл. и открваем его, записываем данные сортируя их ииииии все 
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(movies, file, ensure_ascii=False, indent=4)

driver.quit()