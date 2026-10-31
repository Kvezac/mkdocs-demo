# Настройка терминала: Powerlevel10k и шрифты

Эта заметка — шпаргалка по установке и настройке красивой темы для терминала **Powerlevel10k (p10k)** на macOS. 
---
## Шаг 1. Установка темы через Homebrew

Откройте терминал и выполните команду:
```bash
brew install romkatv/powerlevel10k/powerlevel10k
```
---
## 2 Установка шрифтов (MesloLGS NF)
Без специального шрифта вместо красивых иконок (ветки Git, папки, часы) вы будете видеть квадратики. Powerlevel10k использует MesloLGS NF (Nerd Font).

Скачайте все 4 файла (это нужно для поддержки обычного, жирного и курсивного текста в терминале):

* [MesloLGS NF Regular.ttf](https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Regular.ttf)
* [MesloLGS NF Bold.ttf](https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold.ttf)
* [MesloLGS NF Italic.ttf](https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Italic.ttf)
* [MesloLGS NF Bold Italic.ttf](https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold%20Italic.ttf)

Установка:

Дважды кликните по каждому скачанному файлу .ttf.

В открывшемся окне нажмите кнопку «Установить шрифт» (Install Font).

Настройка терминала:

В стандартном Terminal.app: Нажмите ⌘ + , (Настройки) → вкладка Профили → выберите ваш профиль → блок «Шрифт» → нажмите «Изменить» → выберите MesloLGS NF (размер 12–14 пт).

В iTerm2: Settings → Profiles → Text → выберите MesloLGS NF в поле Font.

## Шаг 3. Подключение темы в конфиг
Добавьте строку запуска темы в ваш файл ~/.zshrc. Выполните в терминале:

```bash
echo 'source /opt/homebrew/share/powerlevel10k/powerlevel10k.zsh-theme' >> ~/.zshrc
```

Затем примените изменения:

bash
source ~/.zshrc
Шаг 4. Быстрая настройка (Визард)
При первом запуске темы или при вводе команды 
```bash
p10k configure
``` 
запускается мастер настройки.

!!! tip "Рекомендуемые ответы для современного вида (стиль Lean)"

- Diamond (ромб): y (если шрифт установлен, вы увидите ромб).

- Prompt Style: 1 (Lean — минималистичный).

- Unicode: 1 (Unicode — красивые иконки).

- Prompt Height: 2 (Two lines — две строки, чтобы длинные команды не ломали верстку).

- Prompt Connection: 2 (Dotted — пунктирная линия).

- Prompt Frame: 1 (No frame — без рамок).

- Prompt Spacing: 2 (Sparse — пустая строка между командами).

- Icons: 2 (Many icons — используем все возможности шрифта).

- Prompt Flow: 1 (Concise — лаконично, только иконки).

- Transient Prompt: y (Yes — прячет длинное приглашение в истории).

- Instant Prompt: 1 (Verbose — мгновенная загрузка терминала).

## 4 Полезные команды

---
- :material-cog:{ .lg .middle } **`p10k configure`** <br>
  Запустить визард настройки заново (сменить тему/иконки).
  
- :material-refresh:{ .lg .middle } **`p10k reload`** <br>
  Применить изменения из `~/.p10k.zsh` без перезапуска терминала.
  
- :material-monitor-dashboard:{ .lg .middle } **`p10k display -a`** <br>
  Показать все текущие настройки и размеры сегментов.

!!! info "Где хранятся настройки?"
    Ваши ответы из визарда сохраняются в скрытый файл `~/.p10k.zsh`. 

    Если вы вручную захотите что-то подкрутить (например, цвета), ищите конфигурацию там. В `~/.zshrc` должна остаться только одна строка `source ...`.

