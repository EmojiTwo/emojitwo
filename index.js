var fs = require('fs');

module.exports = JSON.parse(fs.readFileSync('emoji.json'));

/**
 * File conversions 
 */

var svg2png = require('svg-to-png'); // https://github.com/filamentgroup/svg-to-png

// var svgs-bw = "svg_bw";
// var pngs-bw = "png_bw"
// var fonts = "fonts";
// var sprite-maps = "sprites";

// TODO: optionally only generate files that do not exist yet

function updatePNGs(
	 vectorSource = "svg",
	 bitmapTargets = {
		16: "png_16x16", // Text
	//	18: "png_18x18", // Text
	//	20: "png_20x20", // Text
		24: "png_24x24", // Large Text
	//	28: "png_28x28", // Text
	//	30: "png_30x30", // Text
		32: "png_32x32", // HiDPI Text
		48: "png_48x48", // HiDPI Large Text
		64: "png", // Traditional Default Size
		72: "png_72x72", // Default Unicode Size
	//	96: "png_96x96", // Text
		128: "png_128x128", // XL
		512: "png_512x512" // XXXL
	},
	 optiPNG = 5 // compression level
	) {
	for (var resolution in bitmapTargets) {
		options = {defaultWidth: resolution, defaultHeight: resolution, compress: true, optimizationLevel: optiPNG};
		svg2png.convert(vectorSource, bitmapTargets[resolution], options); // async, returns promise 
		console.log(vectorSource + " -> " + bitmapTargets[resolution] + " @ " + options.defaultWidth + "x" + options.defaultHeight + " " + options.optimizationLevel);
	} 
}

updatePNGs();

svg2png.convert("svg", "png");
