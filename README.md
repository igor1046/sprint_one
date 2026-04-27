# UI Practice: Playwright + Selenium

Проект содержит два независимых UI-трека с Page Object Model:

- `tests/playwright` + `pages/playwright`
- `tests/selenium` + `pages/selenium`

Все тесты помечены маркером `ui`.

## Как запустить

1. Установите зависимости:

```bash
poetry install --with dev,playwright,selenium
```

2. Для Playwright установите браузеры:

```bash
poetry run playwright install
```

3. Запуск всех UI-тестов:

```bash
poetry run pytest -m ui
```

4. Запуск только Playwright:

```bash
poetry run pytest tests/playwright -m ui
```

5. Запуск только Selenium:

```bash
poetry run pytest tests/selenium -m ui
```

6. Allure-результаты пишутся в `reports/allure-results` через `pytest.ini`.

## Переменные окружения

Для теста успешной авторизации GitHub используйте `.env` в корне проекта:

```env
GH_USER=your_github_login
GH_PASS=your_github_password
```

Если `GH_USER` или `GH_PASS` отсутствуют, позитивный тест логина будет пропущен.

Рекомендуется хранить секреты только в `.env` и не коммитить его в репозиторий.

#Правка
