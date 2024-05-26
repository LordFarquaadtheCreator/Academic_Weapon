/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'colorfulPink': '#F2055C',
        'colorfulDarkBlue': '#010326',
        'colorfulLightBlue': '#0798F2',
        'colorfulYellow': '#F2B33D',
        'colorfulOrange': '#D96523',
        'BrightBlack': '#0D0D0D',
        'mutedRed': '#730237',
        'mutedLightBlue': '#A7C8F2',
        'deepRed': '#8C1818',
        'deepWhite': '#F2F2F2',
        'darkBlue': '#03588C',
        'perfectGrey': '#615559',
      },
    },
  },
  plugins: [],
}

