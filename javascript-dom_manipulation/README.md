# 📜 JavaScript DOM Manipulation

This project focuses on manipulating the DOM (Document Object Model) using JavaScript. Below are the tasks and their descriptions:

---

## 0️⃣ Update Header Color

### 📝 Description:
Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`).

### 📌 Requirements:
- Use `document.querySelector` to select the `<header>` tag.

### 🧪 Test with:
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="0-script.js"></script>
  </body>
</html>
```

---

## 1️⃣ Click and Turn Red

### 📝 Description:
Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`) when the user clicks on the tag with `id="red_header"`.

### 🧪 Test with:
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="1-script.js"></script>
  </body>
</html>
```

---

## 2️⃣ Add `.red` Class

### 📝 Description:
Write a JavaScript script that adds the class `red` to the `<header>` element when the user clicks on the tag with `id="red_header"`.

### 🧪 Test with:
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <style>
      .red {
        color: #FF0000;
      }
    </style>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="2-script.js"></script>
  </body>
</html>
```

---

## 3️⃣ Toggle Classes

### 📝 Description:
Write a JavaScript script that toggles the class of the `<header>` element when the user clicks on the tag with `id="toggle_header"`. The `<header>` must always have one class: `red` or `green`.

### 🧪 Test with:
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <style>
      .red {
        color: #FF0000;
      }
      .green {
        color: #00FF00;
      }
    </style>
  </head>
  <body>
    <header class="green"> 
      First HTML page
    </header>
    <div id="toggle_header">Toggle header</div>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="3-script.js"></script>
  </body>
</html>
```

---

## 4️⃣ Add List Item

### 📝 Description:
Write a JavaScript script that adds a `<li>` element to a list when the user clicks on the element with `id="add_item"`. The new element must be `<li>Item</li>` and added to the `<ul>` with class `my_list`.

### 🧪 Test with:
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="4-script.js"></script>
  </body>
</html>
```

---

## 5️⃣ Update Header Text

### 📝 Description:
Write a JavaScript script that updates the text of the `<header>` element to `New Header!!!` when the user clicks on the element with `id="update_header"`.

### 🧪 Test with:
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="update_header">Update the header</div>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="5-script.js"></script>
  </body>
</html>
```

---

## 6️⃣ Star Wars Character

### 📝 Description:
Write a JavaScript script that fetches the character name from the URL: `https://swapi-api.hbtn.io/api/people/5/?format=json` and displays it in the HTML tag with `id="character"`.

### 🧪 Test with:
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      Star Wars character
    </header>
    <br />
    <div id="character"></div>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="6-script.js"></script>
  </body>
</html>
```

---

## 7️⃣ Star Wars Movies

### 📝 Description:
Write a JavaScript script that fetches and lists the titles of all movies from the URL: `https://swapi-api.hbtn.io/api/films/?format=json`. The titles must be listed in the `<ul>` with `id="list_movies"`.

### 🧪 Test with:
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      Star Wars movies
    </header>
    <br />
    <ul id="list_movies">
    </ul>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="7-script.js"></script>
  </body>
</html>
```

---

## 8️⃣ Say Hello!

### 📝 Description:
Write a JavaScript script that fetches from `https://hellosalut.stefanbohacek.dev/?lang=fr` and displays the value of `hello` in the HTML element with `id="hello"`.

### 🧪 Test with:
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script type="text/javascript" src="8-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello!
    </header>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
  </body>
</html>
```

--- 

🎉 **Happy Coding!**