## Репозиторий группового проекта

### Рабочие ветки:
* project/back-end - все работают в ней, push делают в неё
* project/front-end - ветка для фронта, он разберётся

## Схема работы: 
### 1. Переключитесь на ветку project/back-end:

Убедитесь, что вы находитесь в ветке ```project/back-end```, так как разработка ведется именно в этой ветке.
Выполните команду для переключения на нужную ветку: 
```
git checkout project/back-end
```
### 2. Получите последние изменения:
Перед началом работы убедитесь, что у вас актуальная версия ветки ```project/back-end```, чтобы избежать конфликтов с кодом других разработчиков.
Выполните:
```
git pull origin project/back-end
```

### 3. Внесите изменения и зафиксируйте их:
Напишите код или внесите нужные изменения в проект.
Добавьте файлы в коммит с помощью git add . или укажите конкретные файлы.
Зафиксируйте изменения командой git commit -m "Описание изменений".

### 4. Отправьте изменения на удаленный сервер:
Отправьте ваши изменения в удаленную ветку ```project/back-end```.
Выполните:
```
git push origin project/back-end
```

### 5. Получите последние изменения из master (если необходимо):
Поскольку над проектом работают несколько человек, важно убедиться, что ```project/back-end``` актуальна относительно master, перед тем как сливать изменения.
Выполните данную команду: 
```
git pull origin master
```
, чтобы получить последние изменения из master. Разрешите конфликты, если они возникнут.

### 6. Тестирование и ревью:
Протестируйте ветку, чтобы убедиться, что все работает корректно. Если в вашей команде есть процесс ревью, создайте Pull Request (PR) или попросите коллегу проверить ваш код.

### 7. Слияние с ```master```:
После тестирования и проверки вашего кода можно сливать изменения из ```project/back-end``` в ```master```.
Переключитесь на ```master``` с помощью ```git checkout master ```и выполните: 
```
git pull origin master
```
, чтобы получить последние изменения.
Затем выполните: 
```
git merge project/back-end
```
, чтобы объединить ветку ```project/back-end``` с ```master```.

### 8. Отправьте master на удаленный сервер:
Отправьте обновленную ветку master на удаленный сервер.
Выполните:
```
git push origin master
```

### 9. Синхронизация с project/front-end (если нужно):
Если ветка ```project/front-end``` зависит от изменений в ```master```, слейте ```master``` в ```project/front-end```, чтобы актуализировать эту ветку.
