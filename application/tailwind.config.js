/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
          './templates/**/*.html',
          './**/templates/**/*.html',
          './../**/templates/**/*.html',
          '!./node_modules',
          './**/*.js',
          './**/*.py'
    ],
    theme: {
        extend: {
          colors: {
            background: "var(--color-background)",
            text: "var(--color-text)",
            primary: "var(--color-primary)",
            secondary: "var(--color-secondary)",
            accent: "var(--color-accent)",
          },
          fontFamily: {
            mono: [
              "JetBrains Mono", "monospace",
            ],
          },
          boxShadow: {
            'retro': '5px 5px 0px var(--color-primary), 10px 10px 0px var(--color-accent)',
          },
        },
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}