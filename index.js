var fs = require('fs');

module.exports = JSON.parse(fs.readFileSync('emoji.json'));

/**
 * File conversions 
 */

var svg2png = require('svg-to-png'); // https://github.com/filamentgroup/svg-to-png

// var svgs-bw = "./svg_bw";
// var pngs-bw = "./png_bw"
// var fonts = "./fonts";
// var sprite-maps = "./sprites";

function updatePNGs(
	var vector-source = "./svg",
	var bitmap-targets = {
		16: "./png_16x16", // Text
	//	18: "./png_16x16", // Text
	//	20: "./png_16x16", // Text
		24: "./png_24x24", // Large Text
	//	28: "./png_16x16", // Text
	//	30: "./png_16x16", // Text
		32: "./png_32x32", // HiDPI Text
		48: "./png_48x48", // HiDPI Large Text
		64: "./png", // Traditional Default Size
		72: "./png_72x72", // Default Unicode Size
		128: "./png_128x128", // XL
		512: "./png_512x512" // XXXL
	},
	var optiPNG = 5 // compression level
	) {
	for (var resolution in bitmap-targets) {
		options = {defaultWidth: resolution, defaultHeight: resolution, compress: true, optimizationLevel: optiPNG};
		svg2png.convert(vector-source, bitmap-targets[resolution], options); // async, returns promise 
	} 
}
