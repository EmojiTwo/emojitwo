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
	var bitmap-targets = {72: "./png", 128: "./png_128x128", 512: "./png_512x512"},
	var optiPNG = 5 // compression level
	) {
	for (var resolution in bitmap-targets) {
		options = {defaultWidth: resolution, defaultHeight: resolution, compress: true, optimizationLevel: optiPNG};
		svg2png.convert(vector-source, bitmap-targets[resolution], options); // async, returns promise 
	} 
}
