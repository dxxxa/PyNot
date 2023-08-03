https://starper55plys.ru/shpargalki/
https://webref.ru/html/a
http://htmlbook.ru/html/value/script
https://htmlbase.ru/html/a
https://html5css.ru/tags/ref_byfunc.php



### HTML
HTML (HyperText Markup Language, язык разметки гипертекста) — это система вёрстки, которая определяет, как и какие элементы должны располагаться на веб-странице 
(это язык для описания структуры веб-страниц… С помощью HTML описывают структуру страниц с помощью разметки. Элементы языка обозначают части контента, такие как абзац, список, таблица и так далее). 
Информация на сайте, способ её представления и оформления зависят исключительно от разработчика и тех целей, которые он перед собой ставит.
(Стандартизированный язык разметки документов для просмотра веб-страниц в браузере.)



### CSS
Стилем или CSS (Cascading Style Sheets, каскадные таблицы стилей) называется набор параметров форматирования, который применяется к элементам документа, чтобы изменить их внешний вид.
(CSS используется для определения стилей (правил) оформления документов — включая дизайн, вёрстку, цвет, шрифты и вариации макета для различных устройств и размеров экрана)

Что такое синтаксис CSS?
Синтаксис CSS состоит из селектора и блока декларации.
Селектор определяет HTML-элемент, который нужно стилизовать, а блок декларации содержит одно или несколько деклараций или пар CSS — имя свойства и значение с двоеточием между ними.
Декларации разделяются точкой с запятой, а блоки деклараций всегда заключаются в фигурные скобки.
Например, если вы хотите изменить внешний вид заголовка 1, синтаксис CSS будет выглядеть примерно так: 
h1 {color:red; font-size:16pc;}



### В чем разница между HTML и CSS?
Хотя HTML и CSS — это языки разметки, используемые для создания веб-страниц и приложений, у них разные функции.
HTML — формирует структуру и содержание, которое будет отображаться на веб-странице.
CSS — модифицирует веб-дизайн или стиль элементов HTML на веб-странице (включая макет, визуальные эффекты и цвет фона).
Вместе HTML и CSS создают веб-страницу.



### Что такое PHP?
PHP — это аббревиатура от Hypertext Preprocessor, популярного языка сценариев с открытым исходным кодом, 
встроенного в HTML и используемого для разработки динамических веб-сайтов, веб-приложений или статических веб-сайтов.

Поскольку PHP является серверным языком, его скрипты выполняются на сервере (а не в браузере), а результатом является обычный HTML.

PHP — это широко используемый скриптовый язык общего назначения с открытым исходным кодом, который особенно 
подходит для веб-разработки и может быть внедрен в HTML.



### В чем разница между PHP и HTML?
Хотя оба языка имеют решающее значение для веб-разработки, PHP и HTML отличаются друг от друга по нескольким параметрам.

Ключевое различие заключается в том, для чего используются эти два языка:
HTML используется для разработки на стороне клиента (или frontend), а PHP — для разработки на стороне сервера.

HTML — это язык, который разработчики используют для организации контента на сайте, например, для вставки текста,
изображений, таблиц и гиперссылок, форматирования текста и задания цветов.
PHP используется для хранения и извлечения данных из базы данных, выполнения логических операций, отправки и ответов 
на электронные письма, загрузки и скачивания файлов, разработки настольных приложений и т.д.

С точки зрения типа кода, HTML является статическим, а PHP — динамическим. Код HTML всегда один и тот же при каждом 
открытии, в то время как результаты PHP меняются в зависимости от браузера пользователя.





# Справочник CSS
Стилем или CSS (Cascading Style Sheets, каскадные таблицы стилей) называется набор параметров форматирования, который применяется к элементам документа, чтобы изменить их внешний вид.
(CSS используется для определения стилей (правил) оформления документов — включая дизайн, вёрстку, цвет, шрифты и вариации макета для различных устройств и размеров экрана)


### Что такое синтаксис CSS?
Синтаксис CSS состоит из селектора и блока декларации.
Селектор определяет HTML-элемент, который нужно стилизовать, а блок декларации содержит одно или несколько деклараций или пар CSS — имя свойства и значение с двоеточием между ними.
Декларации разделяются точкой с запятой, а блоки деклараций всегда заключаются в фигурные скобки.
Например, если вы хотите изменить внешний вид заголовка 1, синтаксис CSS будет выглядеть примерно так: 
h1 {color:red; font-size:16pc;}





# Справочник HTML
HTML (HyperText Markup Language, язык разметки гипертекста) — это система вёрстки, которая определяет, как и какие элементы должны располагаться на веб-странице 
(это язык для описания структуры веб-страниц… С помощью HTML описывают структуру страниц с помощью разметки. Элементы языка обозначают части контента, такие как абзац, список, таблица и так далее). 
Информация на сайте, способ её представления и оформления зависят исключительно от разработчика и тех целей, которые он перед собой ставит.
(Стандартизированный язык разметки документов для просмотра веб-страниц в браузере.)

Этот язык разметки состоит из ряда элементов, которые используются для придания контенту определенного вида или функциональности, и является основной частью внешнего вида каждого веб-сайта.

Каркас HTML документа по версии HTML5
```
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8" />
<title>Документ без названия</title>
</head>
<body>
Контент
</body>
</html>
```
Всем тегам HTML в браузерах, по умолчанию, присвоено свойство `display:`, результатом чего существует разделение элементов на блочные и встроенные или строчные.




### Служебные теги
<details> 
  <summary>Служебные теги </summary>

- #### `<!DOCTYPE>`	Определяет тип документа	`none`
- #### `<head></head>`	Контейнер в начале страницы для служебных тегов и подгружаемых функций	`none`
- #### `<title></title>`	Заголовок документа отображаемый во вкладке браузера	`none`
- #### `<meta>`	Метаданные страницы	`none`
- #### `<link>`	Подключает внешние сервисы и таблицы стилей	`none`
- #### `<script></script>`	Подключает скрипты к станице	`none`
- #### `<style></style>`	Подключает глобальные стили к странице	`none`
- #### `<base>`	Базовый URL-адрес — домен	`none`
- #### `<noscript></noscrip>`	Блок не поддерживающий скрипты	`block`
</details>


### Структурные блоки
<details> 
  <summary>Структурные блоки </summary>

- #### `<body></body>`	Тело html документа	`block`
- #### `<main><main>`	Контейнер для всего содержимого страницы	`block`
- #### `<nav></nav>`	Контейнер для навигационного меню	`block`
- #### `<header><header>`	Шапка сайта	`block`
- #### `<article></article>`	Блок основного контента, обычно статья	`block`
- #### `<section></section>`	Часть контента с заголовком	`block`
- #### `<aside></aside>`	Часть контента, имеющая косвенное отношение к основному	`block`
- #### `<footer></footer>`	Подвал страницы	`block`
- #### `<div>`	Применяется для создания блочных контейнеров	`block`
- #### `<span></span>`	Применяется для создания встроенных контейнеров	`block`
- #### `<figure></figure>`	Независимый контейнер. Преимущественно для изображений	`block`
- #### `<figcaption></figcaption>`	Заголовок для figure	`block`
- #### `<details></details>`	Контейнер с дополнительной информацией, который можно свернуть или развернуть	`block`
- #### `<summary></summary>`	Заголовок для details, по которому можно щёлкать, чтоб свернуть или развернуть блок	`block`
</details>


### Текст
<details> 
  <summary>Текст </summary>

- #### `<h1></h1>…<h6></h6>`	Заголовки шесть уровней	`block`
- #### `<p></p>`	Абзац	`block`
- #### `<br>`	Перенос строки	`block`
- #### `<wbr>`	Возможное место разрыва строки	`none`
- #### `<hr>`	Прямая линия	`none`
- #### `<blockquote></blockquote>`	Цитата	`block`
- #### `<q></q>`	Краткая цитата	`inline`
- #### `<cite></cite>`	Источник цитирования	`inline`
- #### `<code></code>`	Фрагмент кода	`inline`
- #### `<pre></pre>`	Неформатированнй код	`block`
- #### `<kbd></kbd>`	Текст моноширным шрифтом	`inline`
- #### `<samp></samp>`	Результат выполнения скрипта	`inline`
- #### `<var></var>`	Выделяет переменные из программ	`inline`
- #### `<del></del>`	Зачёркнутый текст помечается как удалённый	`inline`
- #### `<s></s>`	Зачёркнутый текст	`block`
- #### `<ins><ins>`	Подчёркивает изменения в тексте	`inline`
- #### `<u></u>`	Подчёркнутый текст	`inline`
- #### `<dfn></dfn>`	Выделяет термин курсивом	`inline`
- #### `<em></em>`	Выделяет курсивом важные фрагменты текста	`inline`
- #### `<i></i>`	Выделяет текст курсивом	`inline`
- #### `<strong></strong>`	Выделяет важный текст полужирным	`inline`
- #### `<b></b>`	Выделяет текст полужирным	`inline`
- #### `<mark></mark>`	Выделяет фрагмент текста жёлтым фоном	`inline`
- #### `<small></small>`	Уменьшает размер шрифта	`inline`
- #### `<sub></sub>`	Подстрочное написание H2O	`inline`
- #### `<sup></sup>`	Надстрочное написание R2	`inline`
- #### `<time><time>`	Дата, время выпуска статьи	`inline`
- #### `<abbr></abbr>`	Аббревиатура	`inline`
- #### `<address></address>`	Адрес автора статьи	`inline`
- #### `<bdi></bdi>`	Изолирует текст читаемый справа на лево. Применяется в текстах написанных на двух языках	`inline`
- #### `<bdo></bdo>`	Задаёт направление написания текста	`inline`
- #### `<ruby></ruby>`	Контейнер для Восточно-Азиатских символов	`inline`
- #### `<rp></rp>`	Используется для вывода текста в браузерах, которые не поддерживают тег . В остальных браузерах текст, заключенный в контейнер	`none`
- #### `<rt></rt>`	Расшифровка символов	`block`
</details>


### Таблицы
<details> 
  <summary>Таблицы </summary>

- #### `<table></table>`	Таблица HTML	`table`
- #### `<tr></tr>`	Строка таблицы	`table-row`
- #### `<th></th>`	Ячейки заголовков столбцов таблицы	`table-cell`
- #### `<td></td>`	Ячейки таблицы	`table-cell`
- #### `<thead></thead>`	Группа верхних строк таблицы. Применяется для общего оформления	`table-header-group`
- #### `<tfoot></tfoot>`	Группа нижних строк таблицы. Применяется для общего оформления	`table-footer-group`
- #### `<tbody></tbody>`	Группа строк в середине таблицы. Применяется для общего оформления	`table-row-group`
- #### `<col>`	Выделяет столбец таблицы	`table-column`
- #### `<colgroup></colgroup>`	Группирует несколько столбцов таблицы для общего оформления	`table-column-group`
- #### `<caption></caption>`	Описание таблицы	`table-caption`
</details>


### Списки
<details> 
  <summary>Списки </summary>

- #### `<ol></ol>`	Упорядоченный нумерованный список	`block`
- #### `<ul></ul>`	Маркированный список	`block`
- #### `<li></li>`	Элемент списка	list-item
- #### `<dl></dl>`	Список с описаниями	`block`
- #### `<dt></dt>`	Строка списка с описаниями	`block`
- #### `<dd></dd>`	Описание строки, списка с описаниями	`block`
</details>


### Изображения
<details> 
  <summary>Изображения </summary>

- #### `<img>`	Изображение html	`inline`
    <details> 
      <summary>Описание </summary>
  
      Элемент <img> (от англ. image — изображение) предназначен для отображения на веб-странице изображений в графическом формате GIF, JPEG, SVG или PNG. Адрес файла с картинкой задаётся через атрибут src. Если необходимо, то рисунок можно сделать ссылкой на другой файл, поместив <img> в контейнер <a>.

      Рисунки также могут применяться в качестве карт-изображений, когда картинка содержит активные области, выступающие в качестве ссылок. Такая карта по внешнему виду ничем не отличается от обычного изображения, но при этом оно может быть разбито на невидимые зоны разной формы, где каждая из областей служит ссылкой.
    </details> 
    <details> 
      <summary>Синтаксис </summary>

      <img src="<адрес>" alt="<текст>">
    </details> 
    <details> 
      <summary>Атрибуты </summary>

    - `align` - Определяет, как рисунок будет выравниваться по краю и способ обтекания текстом. 
    - `alt` - Альтернативный текст для изображения. 
    - `border` - Толщина рамки вокруг изображения. 
    - `height` - Высота изображения.
    - `hspace` - Горизонтальный отступ от изображения до окружающего контента. 
    - `ismap` - Говорит браузеру, что картинка является серверной картой-изображением.
    - `longdesc` - Указывает адрес документа, где содержится аннотация к картинке. 
    - `sizes` - Задаёт размеры изображения для разных макетов страницы. 
    - `src` - Путь к графическому файлу. 
    - `srcset` - Путь к графическим файлам с учётом размера изображения и устройств. 
    - `vspace` - Вертикальный отступ от изображения до окружающего контента. 
    - `width` - Ширина изображения.
    - `usemap` - Ссылка на элемент <map>, содержащий координаты для клиентской карты-изображения.
    Также для этого элемента доступны универсальные атрибуты и события.
    </details> 
    <details> 
      <summary>Примеры </summary>
          
          <!DOCTYPE HTML>
          <html>
           <head>
            <meta charset="utf-8">
            <title>IMG</title>
           </head>
           <body> 
            <p><a href="page/lorem.html"><img src="image/girl.jpg" 
            width="120" height="120" alt="Девочка с муфтой"></a></p>
           </body>
          </html>

    <!DOCTYPE HTML>
    <html>
     <head>
      <meta charset="utf-8">
      <title>IMG</title>
     </head>
     <body> 
      <p><a href="page/lorem.html"><img src="image/girl.jpg" 
      width="120" height="120" alt="Девочка с муфтой"></a></p>
     </body>
    </html>
  
    </details>
  
    - #### `<>map</map>`	Активные области на карте	`inline`
      <details> 
        <summary>Описание </summary>
    
        Элемент <map> (от англ. map — карта) служит контейнером для элементов <area>, которые определяют активные области для карт-изображений. Такие области устанавливают невидимые зоны на изображении, являющиеся ссылками на HTML-документы. Цель использования <map> — в связывании элемента <img> с клиентской картой-изображением. Эта связь определяется применением единого идентификатора как в <img>, задаваемого атрибутом usemap, так и в <map>, устанавливаемого атрибутом name.
      </details>
      <details> 
        <summary>Синтаксис </summary>

          <map name="<имя>">
            <area>
          </map>
      </details>
      <details> 
        <summary>Атрибуты </summary>
  
      - `name` - Имя карты-изображения.
      </details> 
      <details> 
        <summary>Примеры </summary>
      
          <!DOCTYPE html>
          <html>
           <head>
            <meta charset="utf-8">
            <title>MAP</title>
            <style>
             #title {
              line-height: 0; /* Изменяем межстрочное расстояние */
             }
             #title img {
              border: none; /* Убираем рамку вокруг изображения */
             }
            </style>
           </head>
           <body> 
            <div id="title"><img src="image/ecctitle.png" width="640" height="158" 
              alt="Детский образовательный центр"><br>
             <img src="image/navigate.png" width="640" height="30" alt="Навигация по сайту"
              usemap="#Navigation"></div>
             <p><map name="Navigation">
              <area shape="poly" coords="113,24,211,24,233,0,137,0" href="page/inform.html" alt="Информация">
              <area shape="poly" coords="210,24,233,0,329,0,307,24" href="page/activity.html" alt="Мероприятия">
              <area shape="poly" coords="304,24,385,24,407,0,329,0" href="page/depart.html" alt="Отделения">
              <area shape="poly" coords="384,24,449,24,473,0,406,0" href="page/techinfo.html" alt="Техническая информация">
              <area shape="poly" coords="449,24,501,24,525,0,473,0" href="page/study.html" alt="Обучение">
              <area shape="poly" coords="501,24,560,24,583,0,525,0" href="page/work.html" alt="Работа">
              <area shape="poly" coords="560,24,615,24,639,0,585,0" href="page/misk.html" alt="Разное">
             </map></p>
           </body>
          </html>

      <!DOCTYPE html>
      <html>
       <head>
        <meta charset="utf-8">
        <title>MAP</title>
        <style>
         #title {
          line-height: 0; /* Изменяем межстрочное расстояние */
         }
         #title img {
          border: none; /* Убираем рамку вокруг изображения */
         }
        </style>
       </head>
       <body> 
        <div id="title"><img src="image/ecctitle.png" width="640" height="158" 
          alt="Детский образовательный центр"><br>
         <img src="image/navigate.png" width="640" height="30" alt="Навигация по сайту"
          usemap="#Navigation"></div>
         <p><map name="Navigation">
          <area shape="poly" coords="113,24,211,24,233,0,137,0" href="page/inform.html" alt="Информация">
          <area shape="poly" coords="210,24,233,0,329,0,307,24" href="page/activity.html" alt="Мероприятия">
          <area shape="poly" coords="304,24,385,24,407,0,329,0" href="page/depart.html" alt="Отделения">
          <area shape="poly" coords="384,24,449,24,473,0,406,0" href="page/techinfo.html" alt="Техническая информация">
          <area shape="poly" coords="449,24,501,24,525,0,473,0" href="page/study.html" alt="Обучение">
          <area shape="poly" coords="501,24,560,24,583,0,525,0" href="page/work.html" alt="Работа">
          <area shape="poly" coords="560,24,615,24,639,0,585,0" href="page/misk.html" alt="Разное">
         </map></p>
       </body>
      </html>

      </details>

    - #### `<area></area>`	Активная область с гиперссылкой на карте	`inline`
      <details> 
        <summary>Описание </summary>
      
          Каждый элемент <area> (от англ. area — область, регион) определяет активные области изображения, которые являются ссылками. Рисунок с привязанными к нему активными областями называется в совокупности картой-изображением. Такая карта по внешнему виду ничем не отличается от обычного изображения, но при этом оно может быть разбито на невидимые зоны разной формы, где каждая из областей служит ссылкой. Элемент <area> задаёт форму области, её размеры, устанавливает адрес документа, на который следует сделать ссылку. <area> всегда располагается в контейнере <map>, который связывает координаты областей с изображением.
        
          Несколько областей могут перекрывать друг друга, сверху будет та, которая в коде HTML располагается выше.
      </details>
      <details> 
        <summary>Синтаксис </summary>

          <map>
            <area href="<адрес>">
          </map>
              <details> 
                <summary>Атрибуты </summary>
      </details>
      <details> 
        <summary>Атрибуты </summary>
  
      - `alt` - Альтернативный текст для области изображения.
      - `coords` - Координаты активной области.
      - `href` - Задаёт адрес документа, на который следует перейти.
      - `hreflang` - Указывает язык документа, на который ведёт ссылка. 
      - `nohref` - Область без ссылки на другой документ. 
      - `shape` - Форма области.
      - `target` - Имя фрейма, куда браузер будет загружать документ.
      - `type` - Устанавливает MIME-тип документа, на который ведёт ссылка.
  
          Также для этого элемента доступны универсальные атрибуты и события.
      </details> 
      <details> 
        <summary>Примеры </summary>
  
          <!DOCTYPE HTML>
          <html>
           <head>
            <meta charset="utf-8">
            <title>AREA</title>
            <style>
             #title {
              line-height: 0; /* Изменяем межстрочное расстояние */
             }
             #title img {
              border: none; /* Убираем рамку вокруг изображения */
             }
            </style>
           </head>
           <body> 
           <div id="title"><img src="image/ecctitle.png" width="640" height="158" 
                          alt="Детский образовательный центр"><br>
            <img src="image/navigate.png" width="640" height="30" 
                          alt="Навигация по сайту" usemap="#Navigation"></div>
            <p><map name="Navigation">
            <area shape="poly" coords="113,24,211,24,233,0,137,0" href="page/inform.html" alt="Информация">
            <area shape="poly" coords="210,24,233,0,329,0,307,24" href="page/activity.html" alt="Мероприятия">
            <area shape="poly" coords="304,24,385,24,407,0,329,0" href="page/depart.html" alt="Отделения">
            <area shape="poly" coords="384,24,449,24,473,0,406,0" href="page/techinfo.html" alt="Техническая информация">
            <area shape="poly" coords="449,24,501,24,525,0,473,0" href="page/study.html" alt="Обучение">
            <area shape="poly" coords="501,24,560,24,583,0,525,0" href="page/work.html" alt="Работа">
            <area shape="poly" coords="560,24,615,24,639,0,585,0" href="page/misk.html" alt="Разное">
            </map></p>
           </body>
          </html>
  
        <!DOCTYPE HTML>
        <html>
         <head>
          <meta charset="utf-8">
          <title>AREA</title>
          <style>
           #title {
            line-height: 0; /* Изменяем межстрочное расстояние */
           }
           #title img {
            border: none; /* Убираем рамку вокруг изображения */
           }
          </style>
         </head>
         <body> 
         <div id="title"><img src="image/ecctitle.png" width="640" height="158" 
                        alt="Детский образовательный центр"><br>
          <img src="image/navigate.png" width="640" height="30" 
                        alt="Навигация по сайту" usemap="#Navigation"></div>
          <p><map name="Navigation">
          <area shape="poly" coords="113,24,211,24,233,0,137,0" href="page/inform.html" alt="Информация">
          <area shape="poly" coords="210,24,233,0,329,0,307,24" href="page/activity.html" alt="Мероприятия">
          <area shape="poly" coords="304,24,385,24,407,0,329,0" href="page/depart.html" alt="Отделения">
          <area shape="poly" coords="384,24,449,24,473,0,406,0" href="page/techinfo.html" alt="Техническая информация">
          <area shape="poly" coords="449,24,501,24,525,0,473,0" href="page/study.html" alt="Обучение">
          <area shape="poly" coords="501,24,560,24,583,0,525,0" href="page/work.html" alt="Работа">
          <area shape="poly" coords="560,24,615,24,639,0,585,0" href="page/misk.html" alt="Разное">
          </map></p>
         </body>
        </html>
    
      </details> 

    - #### `<canvas></canvas>`	Холст контейнер для динамического отображения изображений созданных с помощью JavaScript	`inline`-`block`
      <details> 
        <summary>Описание </summary>
      
          Элемент <canvas> (от англ. canvas — холст, полотно) создаёт область, в которой при помощи JavaScript можно рисовать разные объекты, выводить изображения, трансформировать их и менять свойства. При помощи <canvas> можно создавать рисунки, анимацию, игры и др.
      </details>
      <details> 
        <summary>Синтаксис </summary>

            <canvas id="<идентификатор>">
            </canvas>
      </details>
      <details> 
        <summary>Атрибуты </summary>
    
        - `height` -         Задаёт высоту холста. По умолчанию 300 пикселей.
        - `width` -         Задаёт ширину холста. По умолчанию 150 пикселей.

        Также для этого элемента доступны универсальные атрибуты и события.
      </details> 
      <details> 
        <summary>Примеры </summary>
    
            <!DOCTYPE html>
            <html>
             <head>
              <title>canvas</title>
              <meta charset="utf-8">
             </head>
             <body>
              <canvas id="smile" width="200" height="200">
                <p>Ваш браузер не поддерживает рисование.</p>
              </canvas>
              <script> 
                var drawingCanvas = document.getElementById('smile');
                if(drawingCanvas && drawingCanvas.getContext) {
                 var context = drawingCanvas.getContext('2d');
                 // Рисуем окружность 
                 context.strokeStyle = "#000";
                 context.fillStyle = "#fc0";
                 context.beginPath();
                 context.arc(100,100,50,0,Math.PI*2,true);
                 context.closePath();
                 context.stroke();
                 context.fill();
                 // Рисуем левый глаз 
                 context.fillStyle = "#fff";
                 context.beginPath();
                 context.arc(84,90,8,0,Math.PI*2,true);
                 context.closePath();
                 context.stroke();
                 context.fill();
                 // Рисуем правый глаз 
                 context.beginPath();
                 context.arc(116,90,8,0,Math.PI*2,true);
                 context.closePath();
                 context.stroke();
                 context.fill();
                 // Рисуем рот
                 context.beginPath();
                 context.moveTo(70,115);
                 context.quadraticCurveTo(100,130,130,115);
                 context.quadraticCurveTo(100,150,70,115); 
                 context.closePath();
                 context.stroke();
                 context.fill();
                }
              </script>
             </body>
            </html>

        <!DOCTYPE html>
        <html>
         <head>
          <title>canvas</title>
          <meta charset="utf-8">
         </head>
         <body>
          <canvas id="smile" width="200" height="200">
            <p>Ваш браузер не поддерживает рисование.</p>
          </canvas>
          <script> 
            var drawingCanvas = document.getElementById('smile');
            if(drawingCanvas && drawingCanvas.getContext) {
             var context = drawingCanvas.getContext('2d');
             // Рисуем окружность 
             context.strokeStyle = "#000";
             context.fillStyle = "#fc0";
             context.beginPath();
             context.arc(100,100,50,0,Math.PI*2,true);
             context.closePath();
             context.stroke();
             context.fill();
             // Рисуем левый глаз 
             context.fillStyle = "#fff";
             context.beginPath();
             context.arc(84,90,8,0,Math.PI*2,true);
             context.closePath();
             context.stroke();
             context.fill();
             // Рисуем правый глаз 
             context.beginPath();
             context.arc(116,90,8,0,Math.PI*2,true);
             context.closePath();
             context.stroke();
             context.fill();
             // Рисуем рот
             context.beginPath();
             context.moveTo(70,115);
             context.quadraticCurveTo(100,130,130,115);
             context.quadraticCurveTo(100,150,70,115); 
             context.closePath();
             context.stroke();
             context.fill();
            }
          </script>
         </body>
        </html>

      </details> 



### Формы HTML
<details> 
  <summary>Формы HTML </summary>

- #### `<form></form>`	Формы HTML	`block`
- #### `<input></input>`	Многофункциональные поля формы	`inline-block`
- #### `<textarea></textarea>`	Многострочное поле формы	`inline-block`
- #### `<label></label>`	Обычно текст формы	`inline`
- #### `<datalist></datalist>`	Создаёт список вариантов, из которых можно сделать выбор.	`none`
- #### `<option></option>`	Опция в раскрывающемся списке	`block`
- #### `<optgroup></optgroup>`	Контейнер с заголовком для группы `<option>`	`block`
- #### `<select></select>`	Контейнер для создания раскрывающегося списка	`inline-block`
- #### `<fieldset></fieldset>`	Группирует связанные элементы формы	`block`
- #### `<legend></legend>`	Заголовок элементов формы, связанных `<fieldset>`	`block`
- #### `<button></button>`	Интерактивная кнопка	`inline-block`
- #### `<keygen></keygen>`	Генератор ключей	`inline-block`
- #### `<progress></progress>`	Отображает процесс выполнения в числовых значениях	`inline-block`
- #### `<meter></meter>`	Используется для отображения числовых значений таких показателей как количество посетителей, величина давления и т.п.	`inline-block`
- #### `<output></output>`	Поле для вывода результатов вычислений	`inline`
</details>


## Встраиваемые элементы
- #### `<audio></audio>`	Аудио файл	`inline-block`
    <details> 
      <summary>Описание </summary>
  
      Элемент <audio> (от англ. audio — звук) добавляет, воспроизводит и управляет настройками аудиозаписи на веб-странице. Путь к файлу задаётся через атрибут src или вложенный элемент <source>. Внутри контейнера <audio> можно написать текст, который будет выводиться в браузерах, не работающих с этим элементом.

      Для универсального воспроизведения в указанных браузерах аудио кодируют с помощью разных кодеков и добавляют файлы одновременно через элемент <source>.
      
      Управление воспроизведением аудио различается между браузерами по своему виду, но основные элементы совпадают. Это кнопка воспроизведения/паузы, длина трека, прошедшее и суммарное время звучания, а также уровень громкости.
    </details>
    <details> 
      <summary>Синтаксис </summary>

      <audio src="<адрес>"></audio>
      <audio>
       <source src="<адрес>">
      </audio>
    </details>
    <details> 
      <summary>Атрибуты </summary>
  
  - `autoplay` - Звук начинает играть сразу после загрузки страницы.
  - `controls` - Добавляет панель управления к аудиофайлу.
  - `loop` - Повторяет воспроизведение звука с начала после его завершения.
  - `muted` - Отключает звук при воспроизведении музыки.
  - `preload` - Используется для предварительной загрузки аудиофайла или его данных вместе с загрузкой веб-страницы.
  - `src` - Указывает путь к воспроизводимому файлу.
    </details>
    <details> 
      <summary>Примеры </summary>
  
        <!DOCTYPE html>
        <html>
         <head>
          <meta charset="utf-8">
          <title>audio</title>
         </head>
         <body>
          <p>Александр Клименков - Четырнадцать</p>
          <audio controls>
            <source src="audio/music.ogg" type="audio/ogg; codecs=vorbis">
            <source src="audio/music.mp3" type="audio/mpeg">
            Тег audio не поддерживается вашим браузером. 
            <a href="audio/music.mp3">Скачайте музыку</a>.
          </audio>
         </body>
        </html>
    
    <!DOCTYPE html>
    <html>
     <head>
      <meta charset="utf-8">
      <title>audio</title>
     </head>
     <body>
      <p>Александр Клименков - Четырнадцать</p>
      <audio controls>
        <source src="audio/music.ogg" type="audio/ogg; codecs=vorbis">
        <source src="audio/music.mp3" type="audio/mpeg">
        Тег audio не поддерживается вашим браузером. 
        <a href="audio/music.mp3">Скачайте музыку</a>.
      </audio>
     </body>
    </html>
    </details>
  
  - #### `<video></video>`	Видео файл	`inline-block`
    <details> 
      <summary>Описание </summary>
  
        Добавляет, воспроизводит и управляет настройками видеоролика на веб-странице. Путь к файлу задаётся через атрибут src или вложенный элемент <source>. Список поддерживаемых браузерами аудио и видеокодеков ограничен и приведён в табл. 1.
        Firefox поддерживает AAC частично — только в контейнере MP4 и когда операционная система поддерживает этот формат.
      
        Для универсального воспроизведения в указанных браузерах видео кодируют с помощью разных кодеков и добавляют файлы одновременно (см. пример).
    </details>
    <details> 
      <summary>Синтаксис </summary>
      
        <video>
         <source src="<адрес>">
        </video>
    </details>

    <details> 
      <summary>Атрибуты </summary>
    
    - `autoplay` - Видео начинает воспроизводиться автоматически после загрузки страницы.
    - `controls` - Добавляет панель управления к видеоролику.
    - `height` - Задаёт высоту области для воспроизведения видеоролика.
    - `loop` - Повторяет воспроизведение видео с начала после его завершения.
    - `poster` - Указывает адрес картинки, которая будет отображаться, пока видео не доступно или не воспроизводится.
    - `preload` - Используется для загрузки видео вместе с загрузкой веб-страницы.
    - `src` - Указывает путь к воспроизводимому видеоролику.
    - `width` - Задаёт ширину области для воспроизведения видеоролика.
    </details>
    <details> 
      <summary>Примеры </summary>
      
        <!DOCTYPE html>
        <html>
         <head>
          <meta charset="utf-8">
          <title>video</title>
         </head>
         <body>
          <video width="400" height="300" controls="controls" poster="video/duel.jpg">
           <source src="video/duel.ogv" type='video/ogg; codecs="theora, vorbis"'>
           <source src="video/duel.mp4" type='video/mp4; codecs="avc1.42E01E, mp4a.40.2"'>
           <source src="video/duel.webm" type='video/webm; codecs="vp8, vorbis"'>
           Элемент video не поддерживается вашим браузером. 
           <a href="video/duel.mp4">Скачайте видео</a>.
          </video>
         </body>
        </html>

      <!DOCTYPE html>
      <html>
       <head>
        <meta charset="utf-8">
        <title>video</title>
       </head>
       <body>
        <video width="400" height="300" controls="controls" poster="video/duel.jpg">
         <source src="video/duel.ogv" type='video/ogg; codecs="theora, vorbis"'>
         <source src="video/duel.mp4" type='video/mp4; codecs="avc1.42E01E, mp4a.40.2"'>
         <source src="video/duel.webm" type='video/webm; codecs="vp8, vorbis"'>
         Элемент video не поддерживается вашим браузером. 
         <a href="video/duel.mp4">Скачайте видео</a>.
        </video>
       </body>
      </html>
    </details>
      
  - #### `<source></source>`	указывает местоположение и тип альтернативных файлов для `<video> и <audio>`	`none`
    <details> 
      <summary>Описание </summary>
  
        Вставляет звуковой или видеофайл для элементов <audio> и <video>. Обобщённо такие файлы называются медийными. Также применяется для добавления изображений в контейнере <picture>
    
        Когда располагается внутри <audio> или <video>, элемент <source> (от англ. source — исходник) должен идти после медийных файлов, но до <track>. Внутри <picture> он должен идти перед <img>.
    </details> 
    <details> 
      <summary>Синтаксис </summary>
    
        <audio>
         <source src="<адрес>">
        </audio>
          
        <video>
         <source src="<адрес>">
        </video>
          
        <picture>
         <source srcset="...">
        </picture>
    </details>
    <details> 
      <summary>Атрибуты </summary>
  
      - `media` - Определяет устройство, для которого будет воспроизводиться файл.
      - `sizes` - Задаёт размеры изображений для разных макетов страницы.
      - `src` - Адрес медиа-файла.
      - `srcset` - Изображения, которые используются в разных ситуациях (для экранов планшетов, для экранов ретина и др.).
      - `type` - MIME-тип медийного источника.
    </details>
    <details> 
      <summary>Примеры </summary>
    
        <!DOCTYPE html>
        <html>
         <head>
          <meta charset="utf-8">
          <title>source</title>
         </head>
         <body>
          <video width="400" height="300" controls="controls">
           <source src="video/duel.ogv" type='video/ogg; codecs="theora, vorbis"'>
           <source src="video/duel.mp4" type='video/mp4; codecs="avc1.42E01E, mp4a.40.2"'>
           <source src="video/duel.webm" type='video/webm; codecs="vp8, vorbis"'>
           Элемент video не поддерживается вашим браузером. 
           <a href="video/duel.mp4">Скачайте видео</a>.
          </video>
         </body>
        </html>
    
    <!DOCTYPE html>
    <html>
     <head>
      <meta charset="utf-8">
      <title>source</title>
     </head>
     <body>
      <video width="400" height="300" controls="controls">
       <source src="video/duel.ogv" type='video/ogg; codecs="theora, vorbis"'>
       <source src="video/duel.mp4" type='video/mp4; codecs="avc1.42E01E, mp4a.40.2"'>
       <source src="video/duel.webm" type='video/webm; codecs="vp8, vorbis"'>
       Элемент video не поддерживается вашим браузером. 
       <a href="video/duel.mp4">Скачайте видео</a>.
      </video>
     </body>
    </html>
      </details>

  - #### `<track></track>`	Субтитры	`none`
    <details> 
      <summary>Описание </summary>
    
        Элемент <track> (от англ. track — дорожка) позволяет авторам указать текстовую дорожку для медийных элементов <audio> и <video>. Такая дорожка обычно содержит субтитры на разных языках, комментарии, заголовки и др.



        Содержимое файла jane.ru.vtt в формате субтитров VTT приведено ниже.
  
        WEBVTT FILE
        00:00.360 --> 00:01.240
          Солдат Джейн.
  
        00:01.240 --> 00:02.240
          Спасаюсь от радиации.
  
        00:02.240 --> 00:04.000
          Арбуз - лучшее средство.
    </details>
    <details>
      <summary>Синтаксис </summary>
        
        <audio>
          <track kind | src | srclang | label | default>
        </audio>
        <video>
          <track kind | src | srclang | label | default>
        </video>
    </details>
    <details> 
      <summary>Атрибуты </summary>
  
    - `kind` - Указывает тип дорожки, возможные варианты перечислены
      <details>
        <summary>Значения атрибута kind </summary>
        
        - Значение:`subtitles`	/	Предназначение:Субтитры	/	Описание:Предназначены для дублирования звуковой дорожки фильма в виде текста на языке оригинала для глухих людей. Также могут содержать перевод на другие языки для тех, кто не знаком с языком оригинала. Текст субтитров выводится поверх видео.
        - Значение:`captions`	/	Предназначение:Заголовки	/	Описание:Дублирование диалогов, звуковых эффектов, музыкального сопровождения в виде текста для тех случаев, когда звук недоступен или для глухих пользователей. Выводится поверх видео, при этом помечается, что подходит для плохо слышащих людей.
        - Значение:`descriptions`	/	Предназначение:Описание	/	Описание:Звуковое описание происходящего в видео для тех случаев, когда изображение недоступно или для слепых людей.
        - Значение:`chapters`	/	Предназначение:Главы	/	Описание:Названия глав используемые для быстрой навигации по видео или аудио. Отображаются в виде списка.
        - Значение:`metadata`	/	Предназначение:Метаданные	/	Описание:Предназначены для использования скриптами и не отображаются в браузере.
      </details>
    - `src` - Путь к файлу с дорожкой.
    - `srclang` - Язык дорожки. См. коды языков.
    - `label` - Отображаемое название дорожки. Если этот атрибут не указан, браузер станет использовать значение, которое применяется у него по умолчанию, например «untitled1».
    - `default` - Наличие этого атрибута указывает, что данная дорожка предпочтительна и должна быть выбрана по умолчанию. Только одна дорожка может иметь атрибут default.
    </details>
    <details> 
     <summary>Примеры </summary>
        
         <!DOCTYPE html>
         <html>
          <head>
           <meta charset="utf-8">
           <title>track</title>
          </head>
          <body>
           <video width="500" height="400" controls>
             <source src="video/jane.ogv" type='video/ogg; codecs="theora, vorbis"'>
             <source src="video/jane.mp4" type='video/mp4; codecs="avc1.42E01E, mp4a.40.2"'>
             <source src="video/jane.webm" type='video/webm; codecs="vp8, vorbis"'>
             <track kind="subtitles" src="video/jane.en.vtt" srclang="en" label="English">
             <track kind="subtitles" src="video/jane.ua.vtt" srclang="uk" label="Українська">
             <track kind="subtitles" src="video/jane.ru.vtt" srclang="ru" label="Русский" default>
              Элемент video не поддерживается вашим браузером.
           </video>
          </body>
         </html>
      
    <!DOCTYPE html>
    <html>
    <head>
     <meta charset="utf-8">
     <title>track</title>
    </head>
    <body>
     <video width="500" height="400" controls>
       <source src="video/jane.ogv" type='video/ogg; codecs="theora, vorbis"'>
       <source src="video/jane.mp4" type='video/mp4; codecs="avc1.42E01E, mp4a.40.2"'>
       <source src="video/jane.webm" type='video/webm; codecs="vp8, vorbis"'>
       <track kind="subtitles" src="video/jane.en.vtt" srclang="en" label="English">
       <track kind="subtitles" src="video/jane.ua.vtt" srclang="uk" label="Українська">
       <track kind="subtitles" src="video/jane.ru.vtt" srclang="ru" label="Русский" default>
        Элемент video не поддерживается вашим браузером.
     </video>
    </body>
    </html>
    </details>
  
  - #### `<embed></embed>`	Встроенный внешний элемент	`inline-block`
    <details> 
      <summary>Описание </summary>
  
        Элемент <embed> (от англ. embed — вставить, внедрить) используется для загрузки и отображения объектов (например, видеофайлов, флэш-роликов, некоторых звуковых файлов и т. д.), которые исходно браузер не понимает. Как правило, такие объекты требуют подключения к браузеру специального модуля, который называется плагин, или запуска вспомогательной программы.
    
        Вид внедрённого объекта зависит от установленных в браузере плагинов, типа загружаемого файла, а также от атрибутов элемента <embed>.
    </details>
    <details>
      <summary>Синтаксис </summary>

        <embed></embed>
    </details>
    <details> 
      <summary>Атрибуты </summary>

    - `align` - Определяет, как объект будет выравниваться на странице и способ его обтекания текстом. 
    - `height` - Высота объекта.
    - `hidden` - Указывает, скрыть объект на странице или нет.
    - `hspace` - Горизонтальный отступ от объекта до окружающего контента. 
    - `pluginspage` - Адрес страницы в Интернете, откуда можно скачать и установить плагин к браузеру.
    - `src` - Путь к файлу.
    - `type` - MIME-тип объекта.
    - `vspace` - Вертикальный отступ от объекта до окружающего контента. 
    - `width` - Ширина объекта.
    </details>
    <details> 
      <summary>Примеры </summary>
         
        <!DOCTYPE html>
        <html>
          <head>
            <meta charset="utf-8">
            <title>EMBED</title>
          </head>
          <body> 
            <embed src="flash/mouse.swf" width="400" height="300" 
                   type="application/x-shockwave-flash"
                   pluginspage="https://get.adobe.com/flashplayer">  
          </body>
        </html>
      
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="utf-8">
        <title>EMBED</title>
      </head>
      <body> 
        <embed src="flash/mouse.swf" width="400" height="300"
                type="application/x-shockwave-flash"
                pluginspage="https://get.adobe.com/flashplayer">
      </body>
    </html>
    </details>
      
  - #### `<object></object>`	Контейнер для встраиваемого внешнего элемента	`inline-block`
      <details>
        <summary>Описание </summary>
  
          Элемент <object> (от англ. object — объект) сообщает браузеру, как загружать и отображать объекты, которые исходно браузер не понимает. Как правило, такие объекты требуют подключения к браузеру специального модуля, который называется плагин, или запуска вспомогательной программы.

          Дополнительно внутрь контейнера <object> можно поместить элемент <param>, который передаёт дополнительные параметры для отображения объекта.
      </details>
      <details>
        <summary>Синтаксис </summary>
  
          <object></object>
      </details>
      <details>
        <summary>Атрибуты </summary>
  
    - `align` - Определяет, как объект будет выравниваться на странице и способ его обтекания текстом. 
    - `archive` - Устанавливает путь к файлам, необходимым для работы объекта. 
    - `classid` - Адрес программы (приложения или плагина), которая работает с данным объектом, и будет запускать его. 
    - `code` - Имя объекта для его выполнения. 
    - `codebase` - Путь к папке с объектом, который указан атрибутом code или classid. 
    - `codetype` - Указывает на тип объекта, который задан атрибутом classid. 
    - `data` - Адрес файла для его отображения в окне браузера. 
    - `height` - Высота объекта.
    - `hspace` - Горизонтальный отступ от объекта до окружающего контента. 
    - `type` - MIME-тип объекта. 
    - `vspace` - Вертикальный отступ от объекта до окружающего контента. 
    - `width` - Ширина объекта.

          Также для этого элемента доступны универсальные атрибуты и события.

      </details>
      <details>
        <summary>Примеры </summary>
    
          <!DOCTYPE html>
          <html>
            <head>
              <meta charset="utf-8">
              <title>OBJECT</title>
            </head>
            <body> 
             <p><object type="application/x-shockwave-flash" 
                data="flash/mouse.swf" width="400" height="300">
              <param name="quality" value="high">
              <param name="wmode" value="opaque">
             </object></p>
            </body>
          </html>
              
      <!DOCTYPE html>
      <html>
        <head>
          <meta charset="utf-8">
          <title>OBJECT</title>
        </head>
        <body> 
        <p><object type="application/x-shockwave-flash" 
            data="flash/mouse.swf" width="400" height="300">
          <param name="quality" value="high">
          <param name="wmode" value="opaque">
        </object></p>
       </body>
      </html>
        
      </details>
  
    - #### `<param>`	Параметры встраиваемого внешнего элемента	`none`
        <details> 
          <summary>Описание </summary>
          
          Элемент <param> (от англ. parameter — параметр) предназначен для передачи значений параметров Java-апплетам или объектам веб-страницы, созданным с помощью элементов <applet> или <object>. Такой подход позволяет прямо в коде HTML-документа изменять характеристики объекта без его дополнительной компиляции. Количество одновременно используемых элементов <param> может быть больше одного и для каждого из них задаётся пара «имя=значение» через атрибуты name и value.
        </details>
        <details> 
          <summary>Синтаксис </summary>
          
          <param name="<имя>" value="<значение>">
        </details>
        <details> 
          <summary>Атрибуты </summary>
          
      - `name` - Имя параметра.
      - `type` - MIME-тип объекта. 
      - `value` - Значение параметра.
      - `valuetype` - Тип значения параметра. 
        </details>
        <details> 
          <summary>Примеры </summary>
  
            <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" 
              "http://www.w3.org/TR/html4/strict.dtd">
            <html>
              <head>
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
                <title>PARAM</title>
              </head>
              <body>  
               <p><object classid="animation.class" width="500" height="200">
                <param name="bgcolor" value="#000000">
                <param name="delay" value="1000">
                <param name="loop" value="5">
               </object></p>
              </body>
            </html>

        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" 
          "http://www.w3.org/TR/html4/strict.dtd">
        <html>
          <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            <title>PARAM</title>
          </head>
          <body>  
           <p><object classid="animation.class" width="500" height="200">
            <param name="bgcolor" value="#000000">
            <param name="delay" value="1000">
            <param name="loop" value="5">
           </object></p>
          </body>
        </html>
        </details>
          
      - #### `<iframe></iframe>`	Встроенный фрейм	`block`
          <details> 
            <summary>Описание </summary>
  
              Элемент <iframe> (от англ. inline frame — встроенный фрейм) создаёт встроенный фрейм, который находится внутри обычного документа, он позволяет загружать в область заданных размеров любые другие независимые документы.

              <iframe> является контейнером, содержание которого игнорируется браузерами, не поддерживающими данный элемент. Для таких браузеров можно указать альтернативный текст, который увидят пользователи. Он должен располагаться между тегами <iframe> и </iframe>.

          </details>
          <details> 
            <summary>Синтаксис </summary>
  
              <iframe>...</iframe>
          </details>
          <details> 
            <summary>Атрибуты </summary>
  
        - `align` - Определяет, как фрейм будет выравниваться по краю, а также способ обтекания его текстом. 
        - `allowfullscreen` - Разрешает для фрейма полноэкранный режим.
        - `frameborder` - Устанавливает, отображать границу вокруг фрейма или нет. 
        - `height` - Высота фрейма.
        - `hspace` - Горизонтальный отступ от фрейма до окружающего контента. 
        - `marginheight` - Отступ сверху и снизу от содержания до границы фрейма. 
        - `marginwidth` - Отступ слева и справа от содержимого до границы фрейма. 
        - `name` - Имя фрейма.
        - `sandbox` - Позволяет задать ряд ограничений на контент загружаемый во фрейме. 
        - `scrolling` - Способ отображения полосы прокрутки во фрейме.
        - `seamless` - Определяет, что содержимое фрейма должно отображаться так, словно оно является частью документа. 
        - `src` - Путь к файлу, содержимое которого будет загружаться во фрейм.
        - `srcdoc` - Хранит содержимое фрейма непосредственно в атрибуте. 
        - `vspace` - Вертикальный отступ от фрейма до окружающего контента. 
        - `width` - Ширина фрейма.
          </details>
          <details> 
            <summary>Примеры </summary>
    
              <!DOCTYPE HTML>
              <html>
               <head>
                <meta charset="utf-8">
                <title>IFRAME</title>
               </head>
               <body>  
               <iframe src="page/banner.html" width="468" height="60" align="left">
                  Ваш браузер не поддерживает встроенные фреймы!
               </iframe>
               </body>
              </html>
          
            <!DOCTYPE HTML>
            <html>
              <head>
                <meta charset="utf-8">
                <title>IFRAME</title>
              </head>
              <body>  
              <iframe src="page/banner.html" width="468" height="60" align="left">
                Ваш браузер не поддерживает встроенные фреймы!
              </iframe>
              </body>
              </html>
            
          </details>
  
  
  
### Ссылка
- #### `<a></a>`	Гипер ссылка		`inline`
    <details> 
      <summary>Описание </summary>
  
        Элемент <a> (от англ. anchor — якорь) является одним из важных в HTML и предназначен для создания ссылок. 
        Для этого необходимо сообщить браузеру, что является ссылкой, а также указать адрес документа, на который 
        следует сделать ссылку. В качестве значения атрибута href используется адрес документа, на который происходит 
        переход. Адрес ссылки может быть абсолютным и относительным. Абсолютные адреса работают везде и всюду 
        независимо от имени сайта или веб-страницы, где прописана ссылка. Относительные ссылки, как следует из 
        их названия, построены относительно текущего документа или корня сайта.
    </details>
    <details> 
      <summary>Синтаксис </summary>
  
        <a href="<адрес>">...</a>
    </details>
    <details> 
      <summary>Атрибуты </summary>
  
  - `coords` - Устанавливает координаты активной области. 
  - `download` - Предлагает скачать указанный по ссылке файл. 
  - `href` - Задаёт адрес документа, на который следует перейти.
  - `hreflang` - Идентифицирует язык текста по ссылке.
  - `name` - Устанавливает имя якоря внутри документа. 
  - `rel` - Отношения между ссылаемым и текущим документами.
  - `rev` - Отношения между текущим и ссылаемым документами. 
  - `shape` - Задаёт форму активной области ссылки для изображений. 
  - `target` - Имя окна или фрейма, куда браузер будет загружать документ.
  - `type` - Указывает MIME-тип документа, на который ведёт ссылка.
  
          Также для этого элемента доступны универсальные атрибуты и события.
    </details>
    <details> 
      <summary>Примеры </summary>
    
        <!DOCTYPE HTML>
        <html>
         <head>
           <meta charset="utf-8">
          <title>А</title>
         </head>
         <body>
          <p><a href="image/xxx.jpg">Посмотрите на мою фотографию!</a></p>
          <p><a href="page/tip.html">Как сделать такое же фото?</a></p> 
        </body>
        </html>
  
    <!DOCTYPE HTML>
    <html>
      <head>
        <meta charset="utf-8">
        <title>А</title>
      </head>
      <body>
        <p><a href="image/xxx.jpg">Посмотрите на мою фотографию!</a></p>
        <p><a href="page/tip.html">Как сделать такое же фото?</a></p> 
      </body>
      </html>
    
    </details>
  </details>







# Шпаргалки спецсимволы

## Знаки валют

<table style="width:100%;">
<tbody><tr>
<td>&amp;nbsp;</td>
<td> &nbsp;</td>
<td> неразрывный пробел</td>
</tr>
<tr>
<td>&amp;ndash;</td>
<td> –</td>
<td> тире</td>
</tr>
<tr>
<td>&amp;mdash;</td>
<td> —</td>
<td> длинное тире</td>
</tr>
<tr>
<td>&amp;brvbar;</td>
<td> ¦</td>
<td> вертикальное тире</td>
</tr>
<tr>
<td>&amp;quot;</td>
<td> "</td>
<td> двойная кавычка</td>
</tr>
<tr>
<td>&amp;lsquo;</td>
<td> ‘</td>
<td> левая одиночная кавычка</td>
</tr>
<tr>
<td>&amp;rsquo;</td>
<td> ’</td>
<td> правая одиночная кавычка</td>
</tr>
<tr>
<td>&amp;sbquo;</td>
<td> ‚</td>
<td> нижняя одиночная кавычка</td>
</tr>
<tr>
<td>&amp;ldquo;</td>
<td> “</td>
<td> левая двойная кавычка</td>
</tr>
<tr>
<td>&amp;rdquo;</td>
<td> ”</td>
<td> правая двойная кавычка</td>
</tr>
<tr>
<td>&amp;bdquo;</td>
<td> „</td>
<td> нижняя двойная кавычка</td>
</tr>
<tr>
<td>&amp;laquo;</td>
<td> «</td>
<td> левая двойная угловая скобка</td>
</tr>
<tr>
<td>&amp;raquo;</td>
<td> »</td>
<td> правая двойная угловая скобка</td>
</tr>
<tr>
<td>&amp;deg;</td>
<td> °</td>
<td> градус</td>
</tr>
<tr>
<td>&amp;acute;</td>
<td> ´</td>
<td> ударение</td>
</tr>
<tr>
<td>&amp;plusmn;</td>
<td> ±</td>
<td> плюс-минус</td>
</tr>
<tr>
<td>&amp;asymp;</td>
<td> ≈</td>
<td> приблизительно</td>
</tr>
<tr>
<td>&amp;ne;</td>
<td> ≠</td>
<td> не равно</td>
</tr>
<tr>
<td>&amp;radic;</td>
<td> √</td>
<td> квадратный корень</td>
</tr>
<tr>
<td>&amp;infin;</td>
<td> ∞</td>
<td> бесконечность</td>
</tr>
<tr>
<td>&amp;frac14;</td>
<td> ¼</td>
<td> дробь одна четверть</td>
</tr>
<tr>
<td>&amp;frac12;</td>
<td> ½</td>
<td> дробь одна вторая</td>
</tr>
<tr>
<td>&amp;frac34;</td>
<td> ¾</td>
<td> дробь три четверти</td>
</tr>
<tr>
<td>&amp;times;</td>
<td> ×</td>
<td> знак умножения</td>
</tr>
<tr>
<td>&amp;divide;</td>
<td> ÷</td>
<td> знак деления</td>
</tr>
<tr>
<td>&amp;#216;</td>
<td> Ø</td>
<td> диаметр</td>
</tr>
<tr>
<td>&amp;otimes;</td>
<td> ⊗</td>
<td> лампочка</td>
</tr>
<tr>
<td>&amp;lt;</td>
<td> &lt;</td>
<td> знак «меньше»</td>
</tr>
<tr>
<td>&amp;gt;</td>
<td> &gt;</td>
<td> знак «больше»</td>
</tr>
<tr>
<td>&amp;hellip;</td>
<td> …</td>
<td> многоточие</td>
</tr>
<tr>
<td>&amp;amp;</td>
<td> &amp;</td>
<td> амперсанд</td>
</tr>
<tr>
<td>&amp;#64;</td>
<td> @</td>
<td> собака</td>
</tr>
<tr>
<td>&amp;#93;</td>
<td> ]</td>
<td> правая квадратная скобка</td>
</tr>
<tr>
<td>&amp;#91;</td>
<td> [</td>
<td> левая квадратная скобка</td>
</tr>
<tr>
<td>&amp;#125;</td>
<td> }</td>
<td> правая фигурная скобка</td>
</tr>
<tr>
<td>&amp;#123;</td>
<td> {</td>
<td> левая фигурная скобка</td>
</tr>
<tr>
<td>&amp;micro;</td>
<td> µ</td>
<td> микро</td>
</tr>
<tr>
<td>&amp;para;</td>
<td> ¶</td>
<td> абзац</td>
</tr>
<tr>
<td>&amp;sect;</td>
<td> §</td>
<td> параграф</td>
</tr>
<tr>
<td>&amp;permil;</td>
<td> ‰</td>
<td> промиле</td>
</tr>
<tr>
<td>&amp;ang;</td>
<td> ∠</td>
<td> угол</td>
</tr>
<tr>
<td>&amp;perp;</td>
<td> ⊥</td>
<td> перпендикуляр</td>
</tr>
<tr>
<td>&amp;#8251;</td>
<td> ※</td>
<td> сноска</td>
</tr>
<tr>
<td>&amp;int;</td>
<td> ∫</td>
<td> интеграл</td>
</tr>
</tbody></table>



## Знаки валют

<table style="width:100%;">
<tbody><tr>
<td>&amp;pound;</td>
<td> £</td>
<td> фунт стерлингов</td>
</tr>
<tr>
<td>&amp;cent;</td>
<td> ¢</td>
<td> цент</td>
</tr>
<tr>
<td>&amp;yen;</td>
<td> ¥</td>
<td> йена</td>
</tr>
<tr>
<td>&amp;#36;</td>
<td> $</td>
<td> доллар</td>
</tr>
<tr>
<td>&amp;#8372;</td>
<td> ₴</td>
<td> гривна</td>
</tr>
<tr>
<td>&amp;#22291;</td>
<td> 圓</td>
<td> юань</td>
</tr>
<tr>
<td>&amp;#8376;</td>
<td> ₸</td>
<td> теньге</td>
</tr>
<tr>
<td>&amp;euro;</td>
<td> €</td>
<td> знак евро</td>
</tr>
</tbody></table>



## Стрелки

<table style="width:100%;">
<tbody><tr>
<td>&amp;larr;</td>
<td> ←</td>
<td> стрелка влево</td>
</tr>
<tr>
<td>&amp;rarr;</td>
<td> →</td>
<td> стрелка вправо</td>
</tr>
<tr>
<td>&amp;uarr;</td>
<td> ↑</td>
<td> стрелка вверх</td>
</tr>
<tr>
<td>&amp;darr;</td>
<td> ↓</td>
<td> стрелка вниз</td>
</tr>
<tr>
<td>&amp;harr;</td>
<td> ↔</td>
<td> стрелка влево-вправо</td>
</tr>
<tr>
<td>&amp;crarr;</td>
<td> ↵</td>
<td> стрелка возврата</td>
</tr>
<tr>
<td>&amp;lArr;</td>
<td> ⇐</td>
<td> двойная стрелка влево</td>
</tr>
<tr>
<td>&amp;rArr;</td>
<td> ⇒</td>
<td> двойная стрелка вправо</td>
</tr>
<tr>
<td>&amp;uArr;</td>
<td> ⇑</td>
<td> двойная стрелка вверх</td>
</tr>
<tr>
<td>&amp;dArr;</td>
<td> ⇓</td>
<td> двойная стрелка вниз</td>
</tr>
<tr>
<td>&amp;hArr;</td>
<td> ⇔</td>
<td> двойная стрелка влево-вправо</td>
</tr>
<tr>
<td>&amp;#10144;</td>
<td> ➠</td>
<td> стрелка</td>
</tr>
<tr>
<td>&amp;#10148;</td>
<td> ➤</td>
<td> стрелка</td>
</tr>
<tr>
<td>&amp;#10149;</td>
<td> ➥</td>
<td> стрелка</td>
</tr>
<tr>
<td>&amp;#10150;</td>
<td> ➦</td>
<td> стрелка</td>
</tr>
<tr>
<td>&amp;#10163;</td>
<td> ➳</td>
<td> стрела с оперением</td>
</tr>
<tr>
<td>&amp;#8634;</td>
<td> ↺</td>
<td> круглая стрелка</td>
</tr>
<tr>
<td>&amp;#8635;</td>
<td> ↻</td>
<td> круглая стрелка</td>
</tr>
<tr>
<td>&amp;#8679;</td>
<td> ⇧</td>
<td> стрелка</td>
</tr>
<tr>
<td>&amp;#8617;</td>
<td> <img draggable="false" role="img" class="emoji" alt="↩" src="https://s.w.org/images/core/emoji/14.0.0/svg/21a9.svg"></td>
<td> стрелка</td>
</tr>
<tr>
<td>&amp;#10155;</td>
<td> ➫</td>
<td> стрелка</td>
</tr>
</tbody></table>



## Знаки портфилио

<table style="width:100%;">
<tbody><tr>
<td>&amp;#9731;</td>
<td> <img draggable="false" role="img" class="emoji" alt="☃" src="https://s.w.org/images/core/emoji/14.0.0/svg/2603.svg"></td>
<td> снеговик</td>
</tr>
<tr>
<td>&amp;#8224;</td>
<td> †</td>
<td> крестик</td>
</tr>
<tr>
<td>&amp;#10006;</td>
<td> <img draggable="false" role="img" class="emoji" alt="✖" src="https://s.w.org/images/core/emoji/14.0.0/svg/2716.svg"></td>
<td> крест</td>
</tr>
<tr>
<td>&amp;#10008;</td>
<td> ✘</td>
<td> крест</td>
</tr>
<tr>
<td>&amp;#10010;</td>
<td> ✚</td>
<td> крест</td>
</tr>
<tr>
<td>&amp;#9766;</td>
<td> <img draggable="false" role="img" class="emoji" alt="☦" src="https://s.w.org/images/core/emoji/14.0.0/svg/2626.svg"></td>
<td> православный крест</td>
</tr>
<tr>
<td>&amp;#9875;</td>
<td> <img draggable="false" role="img" class="emoji" alt="⚓" src="https://s.w.org/images/core/emoji/14.0.0/svg/2693.svg"></td>
<td> якорь</td>
</tr>
<tr>
<td>&amp;#9990;</td>
<td> ✆</td>
<td> телефон</td>
</tr>
<tr>
<td>&amp;#9742;</td>
<td> <img draggable="false" role="img" class="emoji" alt="☎" src="https://s.w.org/images/core/emoji/14.0.0/svg/260e.svg"></td>
<td> телефон</td>
</tr>
<tr>
<td>&amp;#9749;</td>
<td> <img draggable="false" role="img" class="emoji" alt="☕" src="https://s.w.org/images/core/emoji/14.0.0/svg/2615.svg"></td>
<td> горячие напитки</td>
</tr>
<tr>
<td>&amp;#10001;</td>
<td> ✑</td>
<td> перо</td>
</tr>
<tr>
<td>&amp;#10002;</td>
<td> <img draggable="false" role="img" class="emoji" alt="✒" src="https://s.w.org/images/core/emoji/14.0.0/svg/2712.svg"></td>
<td> перо</td>
</tr>
<tr>
<td>&amp;#9884;</td>
<td> <img draggable="false" role="img" class="emoji" alt="⚜" src="https://s.w.org/images/core/emoji/14.0.0/svg/269c.svg"></td>
<td> геральдическая лилия</td>
</tr>
<tr>
<td>&amp;#10084;</td>
<td> <img draggable="false" role="img" class="emoji" alt="❤" src="https://s.w.org/images/core/emoji/14.0.0/svg/2764.svg"></td>
<td> сердце</td>
</tr>
<tr>
<td>&amp;#9728;</td>
<td> <img draggable="false" role="img" class="emoji" alt="☀" src="https://s.w.org/images/core/emoji/14.0.0/svg/2600.svg"></td>
<td> солнце</td>
</tr>
<tr>
<td>&amp;#9729;</td>
<td> <img draggable="false" role="img" class="emoji" alt="☁" src="https://s.w.org/images/core/emoji/14.0.0/svg/2601.svg"></td>
<td> облако</td>
</tr>
<tr>
<td>&amp;#9730;</td>
<td> <img draggable="false" role="img" class="emoji" alt="☂" src="https://s.w.org/images/core/emoji/14.0.0/svg/2602.svg"></td>
<td> зонт</td>
</tr>
<tr>
<td>&amp;#10004;</td>
<td> <img draggable="false" role="img" class="emoji" alt="✔" src="https://s.w.org/images/core/emoji/14.0.0/svg/2714.svg"></td>
<td> галочка</td>
</tr>
<tr>
<td>&amp;#9745;</td>
<td> <img draggable="false" role="img" class="emoji" alt="☑" src="https://s.w.org/images/core/emoji/14.0.0/svg/2611.svg"></td>
<td> чекбокс с галочкой</td>
</tr>
<tr>
<td>&amp;#9746;</td>
<td> ☒</td>
<td> чекбокс с крестиком</td>
</tr>
<tr>
<td>&amp;#9773;</td>
<td> ☭</td>
<td> серп и молот</td>
</tr>
<tr>
<td>&amp;#9873;</td>
<td> ⚑</td>
<td> флаг</td>
</tr>
<tr>
<td>&amp;#9872;</td>
<td> ⚐</td>
<td> флаг</td>
</tr>
<tr>
<td>&amp;#10047;</td>
<td> ✿</td>
<td> цветок</td>
</tr>
<tr>
<td>&amp;#10048;</td>
<td> ❀</td>
<td> цветок</td>
</tr>
<tr>
<td>&amp;#10046;</td>
<td> ✾</td>
<td> цветок</td>
</tr>
<tr>
<td>&amp;#10049;</td>
<td> ❁</td>
<td> цветок</td>
</tr>
<tr>
<td>&amp;#10050;</td>
<td> ❂</td>
<td> цветок</td>
</tr>
<tr>
<td>&amp;#9993;</td>
<td> <img draggable="false" role="img" class="emoji" alt="✉" src="https://s.w.org/images/core/emoji/14.0.0/svg/2709.svg"></td>
<td> конверт</td>
</tr>
<tr>
<td>&amp;#10086;</td>
<td> ❦</td>
<td> вишня</td>
</tr>
<tr>
<td>&amp;#8967;</td>
<td> ⌇</td>
<td> волнистая линия</td>
</tr>
<tr>
<td>&amp;#9883;</td>
<td> <img draggable="false" role="img" class="emoji" alt="⚛" src="https://s.w.org/images/core/emoji/14.0.0/svg/269b.svg"></td>
<td> атом</td>
</tr>
<tr>
<td>&amp;#9000;</td>
<td> <img draggable="false" role="img" class="emoji" alt="⌨" src="https://s.w.org/images/core/emoji/14.0.0/svg/2328.svg"></td>
<td> клавиатура</td>
</tr>
<tr>
<td>&amp;#9850;</td>
<td> ♺</td>
<td> переработка</td>
</tr>
<tr>
<td>&amp;#10065;</td>
<td> ❑</td>
<td> квадрат с тенью</td>
</tr>
<tr>
<td>&amp;#10066;</td>
<td> ❒</td>
<td> квадрат с тенью</td>
</tr>
<tr>
<td>&amp;#9672;</td>
<td> ◈</td>
<td> алмаз в оправе</td>
</tr>
<tr>
<td>&amp;#9680;</td>
<td> ◐</td>
<td> круг с тенью</td>
</tr>
<tr>
<td>&amp;#9681;</td>
<td> ◑</td>
<td> круг с тенью</td>
</tr>
<tr>
<td>&amp;copy;</td>
<td> ©</td>
<td> знак copyright</td>
</tr>
<tr>
<td>&amp;reg;</td>
<td> ®</td>
<td> знак зарегистрированной торговой марки</td>
</tr>
<tr>
<td>&amp;trade;</td>
<td> ™</td>
<td> знак торговой марки</td>
</tr>
<tr>
<td>&amp;fnof;</td>
<td> ƒ</td>
<td> знак функции</td>
</tr>
<tr>
<td>&amp;#9997;</td>
<td> <img draggable="false" role="img" class="emoji" alt="✍" src="https://s.w.org/images/core/emoji/14.0.0/svg/270d.svg"></td>
<td> рука</td>
</tr>
<tr>
<td>&amp;#9998;</td>
<td> ✎</td>
<td> карандаш вниз</td>
</tr>
<tr>
<td>&amp;#10000;</td>
<td> ✐</td>
<td> карандаш вверх</td>
</tr>
<tr>
<td>&amp;#9674;</td>
<td> ◊</td>
<td> ромб</td>
</tr>
</tbody></table>



## Цифры

<table style="width:100%;">
<tbody><tr>
<td>&amp;#10102;</td>
<td> ❶</td>
<td> один</td>
</tr>
<tr>
<td>&amp;#10103;</td>
<td> ❷</td>
<td> два</td>
</tr>
<tr>
<td>&amp;#10104;</td>
<td> ❸</td>
<td> три</td>
</tr>
<tr>
<td>&amp;#10105;</td>
<td> ❹</td>
<td> четыре</td>
</tr>
<tr>
<td>&amp;#10106;</td>
<td> ❺</td>
<td> пять</td>
</tr>
<tr>
<td>&amp;#10107;</td>
<td> ❻</td>
<td> шесть</td>
</tr>
<tr>
<td>&amp;#10108;</td>
<td> ❼</td>
<td> семь</td>
</tr>
<tr>
<td>&amp;#10109;</td>
<td> ❽</td>
<td> восемь</td>
</tr>
<tr>
<td>&amp;#10130;</td>
<td> ➒</td>
<td> девять</td>
</tr>
<tr>
<td>&amp;#10131;</td>
<td> ➓</td>
<td> десять</td>
</tr>
</tbody></table>





## Звёздочки и снежинки

<table style="width:100%;">
<tbody><tr>
<td>&amp;#9885;</td>
<td> ⚝</td>
<td> звезда</td>
</tr>
<tr>
<td>&amp;#9733;</td>
<td> ★</td>
<td> звезда</td>
</tr>
<tr>
<td>&amp;#9734;</td>
<td> ☆</td>
<td> звезда</td>
</tr>
<tr>
<td>&amp;#10026;</td>
<td> ✪</td>
<td> звезда</td>
</tr>
<tr>
<td>&amp;#10027;</td>
<td> ✫</td>
<td> звезда</td>
</tr>
<tr>
<td>&amp;#10031;</td>
<td> ✯</td>
<td> звезда</td>
</tr>
<tr>
<td>&amp;#9055;</td>
<td> ⍟</td>
<td> звезда</td>
</tr>
<tr>
<td>&amp;#10052;</td>
<td> <img draggable="false" role="img" class="emoji" alt="❄" src="https://s.w.org/images/core/emoji/14.0.0/svg/2744.svg"></td>
<td> снежинка</td>
</tr>
<tr>
<td>&amp;#10053;</td>
<td> ❅</td>
<td> снежинка</td>
</tr>
<tr>
<td>&amp;#10054;</td>
<td> ❆</td>
<td> снежинка</td>
</tr>
<tr>
<td>&amp;#10057;</td>
<td> ❉</td>
<td> снежинка</td>
</tr>
<tr>
<td>&amp;#10059;</td>
<td> ❋</td>
<td> снежинка</td>
</tr>
<tr>
<td>&amp;#10034;</td>
<td> ✲</td>
<td> снежинка</td>
</tr>
<tr>
<td>&amp;#8258;</td>
<td> ⁂</td>
<td> три снежинки</td>
</tr>
</tbody></table>





## Знаки зодиака

<table style="width:100%;">
<tbody><tr>
<td>&amp;#9800;</td>
<td> <img draggable="false" role="img" class="emoji" alt="♈" src="https://s.w.org/images/core/emoji/14.0.0/svg/2648.svg"></td>
<td> овен</td>
</tr>
<tr>
<td>&amp;#9801;</td>
<td> <img draggable="false" role="img" class="emoji" alt="♉" src="https://s.w.org/images/core/emoji/14.0.0/svg/2649.svg"></td>
<td> телец</td>
</tr>
<tr>
<td>&amp;#9802;</td>
<td> <img draggable="false" role="img" class="emoji" alt="♊" src="https://s.w.org/images/core/emoji/14.0.0/svg/264a.svg"></td>
<td> близнецы</td>
</tr>
<tr>
<td>&amp;#9803;</td>
<td> <img draggable="false" role="img" class="emoji" alt="♋" src="https://s.w.org/images/core/emoji/14.0.0/svg/264b.svg"></td>
<td> рак</td>
</tr>
<tr>
<td>&amp;#9804;</td>
<td> <img draggable="false" role="img" class="emoji" alt="♌" src="https://s.w.org/images/core/emoji/14.0.0/svg/264c.svg"></td>
<td> лев</td>
</tr>
<tr>
<td>&amp;#9805;</td>
<td> <img draggable="false" role="img" class="emoji" alt="♍" src="https://s.w.org/images/core/emoji/14.0.0/svg/264d.svg"></td>
<td> дева</td>
</tr>
<tr>
<td>&amp;#9806;</td>
<td> <img draggable="false" role="img" class="emoji" alt="♎" src="https://s.w.org/images/core/emoji/14.0.0/svg/264e.svg"></td>
<td> весы</td>
</tr>
<tr>
<td>&amp;#9807;</td>
<td> <img draggable="false" role="img" class="emoji" alt="♏" src="https://s.w.org/images/core/emoji/14.0.0/svg/264f.svg"></td>
<td> скорпион</td>
</tr>
<tr>
<td>&amp;#9808;</td>
<td> <img draggable="false" role="img" class="emoji" alt="♐" src="https://s.w.org/images/core/emoji/14.0.0/svg/2650.svg"></td>
<td> стрелец</td>
</tr>
<tr>
<td>&amp;#9809;</td>
<td> <img draggable="false" role="img" class="emoji" alt="♑" src="https://s.w.org/images/core/emoji/14.0.0/svg/2651.svg"></td>
<td> козерог</td>
</tr>
<tr>
<td>&amp;#9810;</td>
<td> <img draggable="false" role="img" class="emoji" alt="♒" src="https://s.w.org/images/core/emoji/14.0.0/svg/2652.svg"></td>
<td> водолей</td>
</tr>
<tr>
<td>&amp;#9811;</td>
<td> <img draggable="false" role="img" class="emoji" alt="♓" src="https://s.w.org/images/core/emoji/14.0.0/svg/2653.svg"></td>
<td> рыбы</td>
</tr>
</tbody></table>





## Знаки карточные масти

<table style="width:100%;">
<tbody><tr>
<td>&amp;#9828;</td>
<td> ♤</td>
<td> знак масти пики</td>
</tr>
<tr>
<td>&amp;#9831;</td>
<td> ♧</td>
<td> знак масти трефы</td>
</tr>
<tr>
<td>&amp;#9825;</td>
<td> ♡</td>
<td> знак масти червы</td>
</tr>
<tr>
<td>&amp;#9826;</td>
<td> ♢</td>
<td> знак масти бубны</td>
</tr>
<tr>
<td>&amp;spades;</td>
<td> ♠</td>
<td> знак масти пики</td>
</tr>
<tr>
<td>&amp;clubs;</td>
<td> ♣</td>
<td> знак масти трефы</td>
</tr>
<tr>
<td>&amp;hearts;</td>
<td> ♥</td>
<td> знак масти червы</td>
</tr>
<tr>
<td>&amp;diams;</td>
<td> ♦</td>
<td> знак масти бубны</td>
</tr>
</tbody></table>





## Знаки греческого алфавита

<table style="width:100%;">
<tbody><tr>
<td>&amp;Alpha;</td>
<td> Α</td>
<td> греческая заглавная буква альфа</td>
</tr>
<tr>
<td>&amp;Beta;</td>
<td> Β</td>
<td> греческая заглавная буква бета</td>
</tr>
<tr>
<td>&amp;Gamma;</td>
<td> Γ</td>
<td> греческая заглавная буква гамма</td>
</tr>
<tr>
<td>&amp;Delta;</td>
<td> Δ</td>
<td> греческая заглавная буква дельта</td>
</tr>
<tr>
<td>&amp;Epsilon;</td>
<td> Ε</td>
<td> греческая заглавная буква эпсилон</td>
</tr>
<tr>
<td>&amp;Zeta;</td>
<td> Ζ</td>
<td> греческая заглавная буква дзета</td>
</tr>
<tr>
<td>&amp;Eta;</td>
<td> Η</td>
<td> греческая заглавная буква эта</td>
</tr>
<tr>
<td>&amp;Theta;</td>
<td> Θ</td>
<td> греческая заглавная буква тэта</td>
</tr>
<tr>
<td>&amp;Iota;</td>
<td> Ι</td>
<td> греческая заглавная буква йота</td>
</tr>
<tr>
<td>&amp;Kappa;</td>
<td> Κ</td>
<td> греческая заглавная буква каппа</td>
</tr>
<tr>
<td>&amp;Lambda;</td>
<td> Λ</td>
<td> греческая заглавная буква лямбда</td>
</tr>
<tr>
<td>&amp;Mu;</td>
<td> Μ</td>
<td> греческая заглавная буква мю</td>
</tr>
<tr>
<td>&amp;Nu;</td>
<td> Ν</td>
<td> греческая заглавная буква ню</td>
</tr>
<tr>
<td>&amp;Xi;</td>
<td> Ξ</td>
<td> греческая заглавная буква кси</td>
</tr>
<tr>
<td>&amp;Omicron;</td>
<td> Ο</td>
<td> греческая заглавная буква омикрон</td>
</tr>
<tr>
<td>&amp;Pi;</td>
<td> Π</td>
<td> греческая заглавная буква пи</td>
</tr>
<tr>
<td>&amp;Rho;</td>
<td> Ρ</td>
<td> греческая заглавная буква ро</td>
</tr>
<tr>
<td>&amp;Sigma;</td>
<td> Σ</td>
<td> греческая заглавная буква сигма</td>
</tr>
<tr>
<td>&amp;Tau;</td>
<td> Τ</td>
<td> греческая заглавная буква тау</td>
</tr>
<tr>
<td>&amp;Upsilon;</td>
<td> Υ</td>
<td> греческая заглавная буква ипсилон</td>
</tr>
<tr>
<td>&amp;Phi;</td>
<td> Φ</td>
<td> греческая заглавная буква фи</td>
</tr>
<tr>
<td>&amp;Chi;</td>
<td> Χ</td>
<td> греческая заглавная буква хи</td>
</tr>
<tr>
<td>&amp;Psi;</td>
<td> Ψ</td>
<td> греческая заглавная буква пси</td>
</tr>
<tr>
<td>&amp;Omega;</td>
<td> Ω</td>
<td> греческая заглавная буква омега</td>
</tr>
<tr>
<td>&amp;alpha;</td>
<td> α</td>
<td> греческая строчная буква альфа</td>
</tr>
<tr>
<td>&amp;beta;</td>
<td> β</td>
<td> греческая строчная буква бета</td>
</tr>
<tr>
<td>&amp;gamma;</td>
<td> γ</td>
<td> греческая строчная буква гамма</td>
</tr>
<tr>
<td>&amp;delta;</td>
<td> δ</td>
<td> греческая строчная буква дельта</td>
</tr>
<tr>
<td>&amp;epsilon;</td>
<td> ε</td>
<td> греческая строчная буква эпсилон</td>
</tr>
<tr>
<td>&amp;zeta;</td>
<td> ζ</td>
<td> греческая строчная буква дзета</td>
</tr>
<tr>
<td>&amp;eta;</td>
<td> η</td>
<td> греческая строчная буква эта</td>
</tr>
<tr>
<td>&amp;theta;</td>
<td> θ</td>
<td> греческая строчная буква тэта</td>
</tr>
<tr>
<td>&amp;iota;</td>
<td> ι</td>
<td> греческая строчная буква йота</td>
</tr>
<tr>
<td>&amp;kappa;</td>
<td> κ</td>
<td> греческая строчная буква каппа</td>
</tr>
<tr>
<td>&amp;lambda;</td>
<td> λ</td>
<td> греческая строчная буква лямбда</td>
</tr>
<tr>
<td>&amp;mu;</td>
<td> μ</td>
<td> греческая строчная буква мю</td>
</tr>
<tr>
<td>&amp;nu;</td>
<td> ν</td>
<td> греческая строчная буква ню</td>
</tr>
<tr>
<td>&amp;xi;</td>
<td> ξ</td>
<td> греческая строчная буква кси</td>
</tr>
<tr>
<td>&amp;omicron;</td>
<td> ο</td>
<td> греческая строчная буква омикрон</td>
</tr>
<tr>
<td>&amp;pi;</td>
<td> π</td>
<td> греческая строчная буква пи</td>
</tr>
<tr>
<td>&amp;rho;</td>
<td> ρ</td>
<td> греческая строчная буква ро</td>
</tr>
<tr>
<td>&amp;sigmaf;</td>
<td> ς</td>
<td> греческая строчная буква сигма</td>
</tr>
<tr>
<td>&amp;tau;</td>
<td> τ</td>
<td> греческая строчная буква тау</td>
</tr>
<tr>
<td>&amp;upsilon;</td>
<td> υ</td>
<td> греческая строчная буква ипсилон</td>
</tr>
<tr>
<td>&amp;phi;</td>
<td> φ</td>
<td> греческая строчная буква фи</td>
</tr>
<tr>
<td>&amp;chi;</td>
<td> χ</td>
<td> греческая строчная буква хи</td>
</tr>
<tr>
<td>&amp;psi;</td>
<td> ψ</td>
<td> греческая строчная буква пси</td>
</tr>
<tr>
<td>&amp;omega;</td>
<td> ω</td>
<td> греческая строчная буква омега</td>
</tr>
</tbody></table>
