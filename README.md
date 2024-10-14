# Подготовка к работе
Установка и активация окружения

``` python3 -m venv .venv_my_proj ```
``` source .venv_my_proj/bin/activate ```

Связь с репозиторием на Github

``` git config user.name "neolex118" ```
``` git config user.email "gardov1182001@gmail.com" ```
``` git remote add origin https://github.com/neolex118/neolex.git ```
``` git branch -M main ```
``` git push -u origin main ```

Установка необходимых библиотек

``` pip install matplotlib ```
``` pip install pandas ```
``` pip install seaborn ```
``` pip install numpy ```
``` pip install pickle4 ```

# Описание проекта
Проект посвящён решению задачи классификации цен на мобильные телефоны

Исходные данные: https://www.kaggle.com/datasets/vijayaadithyanvg/car-price-predictionused-cars?resource=download

# Запуск
Для запуска проекта необходимо выполнить следующие команды:

``` git clone https://github.com/neolex118/neolex.git ```

Открыть папку через функцию "Open Folder" в разделе File

Создать виртуальное окружение:
``` python3 -m venv .venv_lr1 ```

Активировать виртуальное окружение:
``` source .venv_lr1/bin/activate ```

Установка зависимостей:
``` pip install -r requirments.txt ```

Установить исходные данные и загрузить в папку ` ./data `

# Исследование данных
Находится в ``` ./eda/eda.ipynb ```

В ходе исследования были проведены действия:

- Признаки, описывающие наличие или отсутствие параметра, переведы в категориальный тип. Например:
``` df['blue'] = df['blue'].astype('category') ```
- Числовые признаки, содержащие небольшой диапазон чисел, получили меньший по объёму тип данных. Например:
``` df['fc'] = df['fc'].astype('int8') ```


В ходе анализа были выявлены следующие закономерности:

Дизельные автомобили пользуются большим спросом чем другие, а также они долговечные. (см график ```./eda/graph1.png```)

Автоматическая коробка передач больше востребована, чем механическая. (см график ```./eda/graph2.png```)
Новые машины, у которых 0 владельцев, дороже чем которые были уже в эксплуатации. (см график ```./eda/graph3.png```)

Машины с автоматической коробкой передачи дороже, чем с механической. (см график ```./eda/graph4.png```)