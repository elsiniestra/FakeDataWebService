/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

let COLOR_WHITE = {DEFAULT: "#FFFFFF"};
let COLOR_BLACK = {DEFAULT: "#373A3C"};
let COLOR_BLUE = {DEFAULT: "#0275D8"};
let COLOR_RED = {DEFAULT: "#D9534F"};
let COLOR_GREEN = {DEFAULT: "#5CB85C"};
let COLOR_GRAY = {
	lightest: "#E5E5E5",
	light: "#CCCCCC",
	DEFAULT: "#C9C9CA",
	dark: "#F7F7F9",
	darkest: "#999999",
};
let COLOR_PRIMARY = COLOR_WHITE;
let COLOR_SECONDARY = COLOR_BLACK;
let COLOR_BORDER = {DEFAULT: COLOR_GRAY.light};

module.exports = {
	mode: "jit",
	purge: [
		/**
		 * HTML. Paths to Django template files that will contain Tailwind CSS classes.
		 */

		/*
		 * Main templates directory of the project (BASE_DIR/templates).
		 * Adjust the following line to match your project structure.
		 */
		'../../../../../**/templates/**/*.html',
		'../../../../**/*.py'
	],
	darkMode: false, // or 'media' or 'class'
	theme: {
		fontFamily: {
			'sans': ["Helvetica Neue"],
		},
		extend: {
			colors: {
				white: COLOR_WHITE,
				black: COLOR_BLACK,
				blue: COLOR_BLUE,
				red: COLOR_RED,
				green: COLOR_GREEN,
				gray: COLOR_GRAY,
				primary: COLOR_PRIMARY,
				secondary: COLOR_SECONDARY,
				border: COLOR_BORDER,
			},
		},
	},
	variants: {
		extend: {},
	},
	plugins: [
		require("@tailwindcss/forms"),
		require("@tailwindcss/typography"),
		require("@tailwindcss/line-clamp"),
		require("@tailwindcss/aspect-ratio"),
	],
}
