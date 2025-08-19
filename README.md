# Algorithms Capsule

Небольшая коллекция задач по алгоритмам и их решениям.

## Структура
```
algorithms/<category>/<problem>/
    task.md        # условие и примеры
    solution.py    # сигнатура функции и TODO
    tests.py       # тесты на pytest
    explanation.md # идея решения и сложность

scripts/new_problem.py # генератор шаблонов задач
common/utils.py        # вспомогательные утилиты
```

Доступные категории: `arrays`, `strings`, `hashing`, `sliding_window`, `dp`.

## Запуск тестов
```bash
pytest
```

## Добавление новой задачи
1. Сгенерируйте шаблон:
   ```bash
   python scripts/new_problem.py <category> <problem_name>
   ```
2. Заполните файлы в созданной папке и реализуйте решение.
3. Проверьте стиль:
   ```bash
   pre-commit run --files <изменённые файлы>
   ```
4. Запустите тесты и закоммитьте изменения.

Пример:
```bash
python scripts/new_problem.py arrays two_sum
```
