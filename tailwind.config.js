/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",      // Specifically match index.html in the root directory
    "./src/**/*.{html,js}" // Match HTML and JS files in the src folder and its subfolders
  ],
  theme: {
   extend: {
      screens: {
        'c-md': '500px', // Custom breakpoint at 500px
      },
    },
  },
  plugins: [],
}

