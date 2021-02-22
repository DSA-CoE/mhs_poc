# Templates

Templates are organized according to [layouts](./layouts) and [pages](./pages).

[Layouts](./layouts) are HTML template structure that you want to share across different pages. This is useful when you want to share navbars and/or sidebars across many pages, or if you want to specify different layouts for login pages, dashboard pages etc.

```html
<!-- layouts/default.html -->
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Hellooo</title>
    ...
  </head>
  <body class="">
    {% block main_content %}
    <!-- Here is where your pages will be rendered. -->
    {% endblock %}
  </body>
</html>
```

[Pages](./pages) are templates that contain the main content of a page, and is what your view renders. Pages extend layouts like so:

```html
<!-- pages/home.html -->
<!-- Extend the layout that you want to use for this particular page -->
{% extends "../layouts/default.html" %}

<!-- Main content of the page goes inside the block tag -->
{% block main_content %}

<h1 class="text-4xl text-blue-600">Hello DSA!</h1>

{% endblock %}
```

The final rendered output will be like so:

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Hellooo</title>
    ...
  </head>
  <body class="">
    <h1 class="text-4xl text-blue-600">Hello DSA!</h1>
  </body>
</html>
```
