# Расширенный калькулятор

Расширенный калькулятор с математическими операциями, статистическими вычислениями, геометрическими расчетами и тригонометрическими функциями, написанный на Python для демонстрации тестирования программного обеспечения.

## Функциональность

### Базовые операции
- Арифметические операции (+, -, *, /)
- Возведение в степень
- Извлечение квадратного корня

### Статистика
- Среднее, медиана, мода
- Стандартное отклонение, дисперсия
- Размах, процентили

### Геометрия
- Площади и периметры кругов, прямоугольников, треугольников
- Объемы и поверхности сфер
- Расстояния между точками

### Тригонометрия
- Синус, косинус, тангенс
- Арксинус, арккосинус, арктангенс
- Законы синусов и косинусов

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/MikhailChernyshev2003/testing-course.git
cd testing-course
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Использование

### Базовый калькулятор (тестируется)
```python
from src.calculator import Calculator

calc = Calculator()

# Базовые операции
result = calc.add(2, 3)        # 5.0
result = calc.subtract(10, 4)  # 6.0
result = calc.multiply(3, 7)   # 21.0
result = calc.divide(15, 3)    # 5.0
result = calc.power(2, 3)      # 8.0
result = calc.sqrt(9)          # 3.0
```

### Расширенный калькулятор (не тестируется)
```python
from src.advanced_calculator import AdvancedCalculator

calc = AdvancedCalculator()

# Статистика
result = calc.mean([1, 2, 3, 4, 5])  # 3.0
result = calc.standard_deviation([1, 2, 3, 4, 5])  # 1.581

# Геометрия
result = calc.circle_area(5)    # 78.54
result = calc.rectangle_area(4, 3)  # 12.0

# Тригонометрия
result = calc.sin(90)           # 1.0
result = calc.cos(0)            # 1.0
```

## Тестирование

Запуск тестов:
```bash
pytest
```

Запуск тестов с покрытием:
```bash
pytest --cov=src
```

## Результаты тестирования

- **Количество тестов**: 11
- **Покрытие кода важных модулей**: 75-79%
- **Статус**: Все тесты проходят успешно

## Компиляция отчета

Для компиляции отчета в PDF:
```bash
./compile_report.sh
```

Или вручную:
```bash
pdflatex report.tex
pdflatex report.tex
```

## Структура проекта

```
testing-course/
├── src/
│   ├── __init__.py
│   ├── calculator.py           
│   ├── operations.py         
│   ├── validators.py        
│   ├── statistics.py         
│   ├── geometry.py           
│   ├── trigonometry.py        
│   └── advanced_calculator.py 
├── tests/
│   ├── test_calculator.py     
│   ├── test_operations.py    
│   └── test_validators.py     
├── .github/workflows/
│   └── test.yml              
├── requirements.txt
├── pytest.ini             
├── .gitignore               
└── README.md                
```

## Автор

Чернышев Михаил Павлович