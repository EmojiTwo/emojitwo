module.exports = function(grunt) {
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
        sprite:{
            pngsprites: {
                src: 'png/*.png',
                dest: 'sprites/sprites.png',
                destCss: 'sprites/sprites.css',
                'cssTemplate': 'sprites/sprites.mustache',
                'algorithm': 'binary-tree',
                'cssVarMap': function (sprite) {
                    sprite.name = 'e2-' + sprite.name;
                },
                padding: 1
            }

        },
       // BUILD SVG SPRITES
       svgstore: {
          options: {
            prefix: 'emoji-', // symbol ID prefix
            svg: {
              viewBox : '0 0 64 64',
              xmlns: 'http://www.w3.org/2000/svg',
              "xmlns:xlink": "http://www.w3.org/1999/xlink"
            }
          },
          default: {
            files: {
              'sprites/sprites.svg': ['svg/*.svg']
            }
          }
        },
        // OPTIMIZE PNGs
        imageoptim: {
            pngs: {
                src: ['png', 'png']
            },
            sprite: {
                src: ['sprites', 'sprites']
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
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-svgstore');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-jshint');
    grunt.loadNpmTasks('grunt-jsonlint');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.loadNpmTasks('grunt-imageoptim');
    //grunt.registerTask('default', ['jshint','jsonlint', 'sprite:pngsprites', 'sass', 'svgstore', 'uglify', 'cssmin', 'imageoptim']);
    grunt.registerTask('default', ['jshint','jsonlint', 'sass', 'svgstore', 'cssmin']);
    grunt.registerTask('travis', []);
};
