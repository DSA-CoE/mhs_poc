// This is a minimal TailwindCSS config.
// Docs: https://tailwindcss.com/docs/configuration
module.exports = {
  purge: [
    "../../**/templates/*.html",
    "../../**/templates/**/*.html",
    // Add path to templates in other apps below.
    // '../../templates/**/*.html',
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
