# Подготовка к работе
Установка и активация окружения

``` python3 -m venv .venv_my_proj ```
``` source .venv_my_proj/bin/activate ```

Связь с репозиторием на Github

``` git config user.name "neolex118" ```
``` git config user.email "gradov1182001@gmail.com" ```
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

Был создан интерактивный график, показывающий: марку автомобивя, тип топлива, а также цену и год выпуска, что позволяет выявить закономерность в изменениях заданных переменных


## Запуск mlflow
**1. Перейти в с mlflow:**
```
cd .\mlflow\
```

**2. Выполнить скрипт**
```
source .\mlflow_runner.sh
```

## Результаты исследования

#### Лучший результат следующая модель
#### Preprocessor: 
- StandardScaler для преобразования числовых признаков
- OrdinalEncoder для преобразования категориальных признаков
- QuantileTransformer преобразует числовые признаки, чтобы они распределялись равномерно или нормально — так данные меньше подвергаются влиянию выбросов.
- PolynomialFeatures(создает полином степени degree=2 из указанных признаков - ['Selling_Price', 'Driven_kms']) в сочетании с StandardScaler
- SplineTransformer(Cоздаёт новую матрицу признаков, состоящую из сплайнов порядка degree=2)
  
#### RandomForestRegressor:
- максимальная глубина дерева = 3
- процент признаков, по которым ищется разбиение = 0.9
- число деревьев в «лесу» = 3 
#### Метрики:
mae
2.3761014311020556
mape
0.20944138779526347
mse
41.87649765074893
```
run_id = 6a4991b0933a4f8699cdcd3053657973
```

# Сервис классификации

Описание файлов в папке services:

- api_handler.py включает в себя функции, необходимые для работы модели в FastAPI (загрузка, обработка и т.п.)
- Dockerfile включает в себя необходимые команды для сборки контейнера с определёнными параметрами
- main.py содержит основные функции для создания предсказаний
- requirements.txt содержит необходимые для работы сервиса библиотеки
- файл get_model.py берёт необходимую модель из mlflow и записывает её в формат pickle
- model.pkl содержит модель, полученную при помощи get_model.py

Создание образа и запуск контейнера осуществляется по следующим командам:
```
docker build . --tag price_model:2
docker run -p 8001:8000 -v $(pwd)/../models:/models price_model:2
```

Проверить работоспособность сервиса можно следующей командой:
```
curl -X 'POST' \
  'http://127.0.0.1:8000/api/prediction?car_id=1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"Car_Name": "ritz", "Year": 2014,"Selling_Price": 3.35,"Driven_kms": 27000,"Fuel_Type": "Petrol","Selling_type": "Dealer","Transmission": "Manual","Owner": 0}'
```