module.exports = function (grunt) {
	grunt.initConfig({
		pkg: grunt.file.readJSON('package.json'),
		jshint: {
			files: ['Gruntfile.js']
		},
		jsonlint: {
			files: {
				src: ['emoji.json', 'emoji_strategy.json']
			}
		},
		// BUILD PNG SPRITES
		sprite: {
			pngsprites: {
				src: 'png/*.png',
				dest: 'sprites/sprites.png',
				destCss: 'sprites/sprites.css',
				cssTemplate: 'sprites/sprites.mustache',
				algorithm: 'binary-tree',
				cssVarMap: function (sprite) {
					sprite.name = 'e2-' + sprite.name;
				},
				padding: 1
			}
		},
		// OPTIMIZE SVG
		svgmin: {
			options: {
				pretty: true,
				plugins: [
					{
						removeViewBox: false
					}, {
						moveElemsAttrsToGroup: true
					}, {
						sortAttrs: true
					}, {
						collapseGroups: true
					}, {
						moveElemsAttrsToGroup: true
					}, {
						moveGroupAttrsToElems: false
					}, {
						removeUnusedNS: true
					}, {
						convertTransform: true
					}, {
						convertPathData: true
					}, {
						mergePaths: true
					}, {
						convertShapeToPath: false
					}, {
						removeRasterImages: true
					}, {
						removeUnknownsAndDefaults: true
					}, {
						cleanupIDs: false
					}, {
						removeComments: false
					}, {
						removeTitle: false
					}, {
						removeDesc: false
					}, {
						removeHiddenElems: false
					}, {
						minifyStyles: false
					}
				]
			},
			default: {
				pretty: true,
				files:  [{
					expand: true,
					cwd: 'svg',
					src: '*.svg',
					dest: 'svg'
				}]
			},
			sprite: {
				files: 'sprites/sprites.svg'
			}
		},
		// BUILD SVG SPRITES
		svgstore: {
			options: {
				prefix: 'emoji-', // symbol ID prefix
				svg: {
					viewBox: '0 0 64 64',
					xmlns: 'http://www.w3.org/2000/svg',
					"xmlns:xlink": "http://www.w3.org/1999/xlink",
					"xmlns:rdf": "http://www.w3.org/2000/01/rdf-schema#",
					"xmlns:cc": "http://creativecommons.org/ns#",
					"xmlns:dc": "http://purl.org/dc/elements/1.1/",
					"xmlns:inkscape": "http://www.inkscape.org/namespaces/inkscape",
					"xmlns:sodipodi": "http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
				}
			},
			default: {
				files: {
					'sprites/sprites.svg': ['svg/*.svg']
				}
			}
		},
		// GENERATE PNGs
		"convert-svg-to-png": {
			default: {
				options: {
					size: {
						w: 72,
						h: 72
					},
				},
				files: [{
						expand: true,
						cwd: "svg",
						src: "*.svg",
						dest: "png/",
						ext: ".png"
					}
				]
			} /*,
			text: {
				options: {
					size: {
						w: 16,
						h: 16
					},
				},
				files: [{
						expand: true,
						cwd: "svg",
						src: ["*.svg"],
						dest: "../png/16/"
					}
				]
			},
			largertext: {
				options: {
					size: {
						w: 18,
						h: 18
					},
				},
				files: [{
						expand: true,
						cwd: "svg",
						src: ["*.svg"],
						dest: "../png/18/"
					}
				]
			},
			enlarged: {
				options: {
					size: {
						w: 20,
						h: 20
					},
				},
				files: [{
						expand: true,
						cwd: "svg",
						src: ["*.svg"],
						dest: "../png/20/"
					}
				]
			},
			tiny: {
				options: {
					size: {
						w: 24,
						h: 24
					},
				},
				files: [{
						expand: true,
						cwd: "svg",
						src: ["*.svg"],
						dest: "../png/24/"
					}
				]
			},
			headline: {
				options: {
					size: {
						w: 28,
						h: 28
					},
				},
				files: [{
						expand: true,
						cwd: "svg",
						src: ["*.svg"],
						dest: "../png/28/"
					}
				]
			},
			title: {
				options: {
					size: {
						w: 30,
						h: 30
					},
				},
				files: [{
						expand: true,
						cwd: "svg",
						src: ["*.svg"],
						dest: "../png/30/"
					}
				]
			},
			small: {
				options: {
					size: {
						w: 32,
						h: 32
					},
				},
				files: [{
						expand: true,
						cwd: "svg",
						src: ["*.svg"],
						dest: "../png/32/"
					}
				]
			},
			icon: {
				options: {
					size: {
						w: 48,
						h: 48
					},
				},
				files: [{
						expand: true,
						cwd: "svg",
						src: ["*.svg"],
						dest: "../png/48/"
					}
				]
			},
			standard: {
				options: {
					size: {
						w: 64,
						h: 64
					},
				},
				files: [{
						expand: true,
						cwd: "svg",
						src: ["*.svg"],
						dest: "../png/64/"
					}
				]
			},
			medium: { // Instagram: 110x110
				options: {
					size: {
						w: 96,
						h: 96
					},
				},
				files: [{
						expand: true,
						cwd: "svg",
						src: ["*.svg"],
						dest: "../png/96/"
					}
				]
			},
			large: { // Tumblr
				options: {
					size: {
						w: 128,
						h: 128
					},
				},
				files: [{
						expand: true,
						cwd: "svg",
						src: ["*.svg"],
						dest: "../png/128/"
					}
				]
			},
			headshot: { // Pinterest: 165x165; Instagram thumbnail: 161x161; Pinterest board: 222x150
				options: {
					size: {
						w: 160,
						h: 160
					},
				},
				files: [{
						expand: true,
						cwd: "svg",
						src: ["*.svg"],
						dest: "../png/160/"
					}
				]
			},
			mugshot: { // Facebook
				options: {
					size: {
						w: 180,
						h: 180
					},
				},
				files: [{
						expand: true,
						cwd: "svg",
						src: ["*.svg"],
						dest: "../png/180/"
					}
				]
			},
			snapshot: { // Google+: 250x250; Pinterest pin: 238x...
				options: {
					size: {
						w: 300,
						h: 300
					},
				},
				files: [{
						expand: true,
						cwd: "svg",
						src: ["*.svg"],
						dest: "../png/300/"
					}
				]
			},
			profile: { // Twitter, Linked-in; Ello: 360x360
				options: {
					size: {
						w: 400,
						h: 400
					},
				},
				files: [{
						expand: true,
						cwd: "svg",
						src: ["*.svg"],
						dest: "../png/400/"
					}
				]
			},
			huge: {
				options: {
					size: {
						w: 512,
						h: 512
					},
				},
				files: [{
						expand: true,
						cwd: "svg",
						src: ["*.svg"],
						dest: "../png/512/"
					}
				]
			},
			hd: { // Instagram photo
				options: {
					size: {
						w: 1080,
						h: 1080
					},
				},
				files: [{
						expand: true,
						cwd: "svg",
						src: ["*.svg"],
						dest: "../png/1080/"
					}
				]
			}*/
		},
		// OPTIMIZE PNGs
		imageoptim: {
			options: {
				jpegMini: false,
				imageAlpha: false,
				quitAfter: false
			},
			pngs: {
				src: ['png', 'png/*']
			},
			sprite: {
				src: ['sprites']
			}
		},
		// Minify Project CSS
		cssmin: {
			target: {
				files: {
					'css/emojitwo.min.css': ['css/emojitwo.css'],
					'sprites/sprites.css': ['sprites/sprites.css']
				}
			}
		},
		watch: {
			files: ['<%= jshint.files %>'],
			tasks: ['jshint']
		}

	});
	grunt.loadNpmTasks('grunt-spritesmith');
	grunt.loadNpmTasks('grunt-svgstore');
	grunt.loadNpmTasks('grunt-svgmin');
	grunt.loadNpmTasks('grunt-contrib-jshint');
	grunt.loadNpmTasks('grunt-jsonlint');
	grunt.loadNpmTasks('grunt-contrib-watch');
	grunt.loadNpmTasks('grunt-contrib-cssmin');
	grunt.loadNpmTasks('grunt-imageoptim');
	grunt.loadNpmTasks('grunt-convert-svg-to-png');
	grunt.registerTask('bitmaps', ['convert-svg-to-png', 'sprite']);
	grunt.registerTask('minify', ['imageoptim', 'svgmin', 'cssmin']);
	grunt.registerTask('check', ['jshint', 'jsonlint']);
	grunt.registerTask('rebuild', ['jshint', 'jsonlint', 'convert-svg-to-png:default', 'sprite', 'svgstore', 'imageoptim', 'svgmin', 'cssmin']);
	grunt.registerTask('default', ['jshint', 'jsonlint', 'svgstore', 'svgmin:sprite', 'sprite', 'imageoptim:sprite']);
	grunt.registerTask('travis', []);
};
