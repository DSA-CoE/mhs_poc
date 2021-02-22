# Styles

Contains the configuration and scaffolding of [TailwindCSS](https://tailwindcss.com/docs) for this project.

**Important**: For development purposes, you don't need to run or install anything since everything is ready to go. However, if:

- you want to install latest versions of TailwindCSS from scratch
- or, you want to build for production,

here's how you would do it:

## To install from scratch

1. Make sure you have [Node.js](https://nodejs.org/en/download/) installed.
2. Go to the `/static_src` directory, and install all dependencies:

   ```bash
   npm install
   ```

3. Build your CSS:

   ```bash
   npm run dev
   ```

4. Include the following in your HTML:

   ```html
   {% load static %}
   <!DOCTYPE html>
   <html>
     <head>
       <meta charset="UTF-8" />
       <meta name="viewport" content="width=device-width, initial-scale=1.0" />
       <title>....</title>
       <link rel="stylesheet" href="{% static 'css/tailwind.min.css' %}" />
       ....
     </head>
     <body>
       ...
     </body>
   </html>
   ```

5. You're good to go! The CSS output will be in [\<appname\>/styles/static/css/tailwind.min.css](./../static/css/tailwind.min.css).

## To install for production

1. Purge unused CSS and minify CSS (using [PurgeCSS](https://github.com/FullHuman/purgecss) and [CSSO](https://github.com/css/csso)):

   ```bash
   npm run build
   ```

2. You're good to go! The purged CSS output will be in [\<appname\>/styles/static/css/tailwind.min.css](./../static/css/tailwind.min.css). Notice how small the file size is!

## Optimizing for production

(taken from the [TailwindCSS docs](https://tailwindcss.com/docs/optimizing-for-production))

In order to allow PurgeCSS work properly, **avoid dynamically creating class strings in your templates with string concatenation**, otherwise PurgeCSS won't know to preserve those classes.

❌ Don't use string concatenation to create class names:

```html
<div class="text-{{ error ? 'red' : 'green' }}-600"></div>
```

✅ Do dynamically select a complete class name:

```html
<div class="{{ error ? 'text-red-600' : 'text-green-600' }}"></div>
```

As long as a class name appears in your template in its entirety, PurgeCSS will not remove it.

For more information, refer to the [TailwindCSS docs](https://tailwindcss.com/docs/optimizing-for-production).
