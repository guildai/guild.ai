module.exports = function(grunt) {

  var autoprefixer = require('autoprefixer')({
    browsers: [
      'Chrome >= 35',
      'Firefox >= 31',
      'Edge >= 12',
      'Explorer >= 10',
      'iOS >= 8',
      'Safari >= 8',
      'Android 2.3',
      'Android >= 4',
      'Opera >= 12'
    ]
  });

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    banner: '/*!\n' +
            ' * TheDocs v<%= pkg.version %> (<%= pkg.homepage %>)\n' +
            ' * Copyright <%= grunt.template.today("yyyy") %> <%= pkg.author %>\n' +
            ' * Licensed under the Themeforest Standard Licenses\n' +
            ' */\n',

    sass: {
      dist: {
        options: {
          sourceMap: false,
          outputStyle: 'compressed'
        },
        files: {
          'src/assets/css/<%= pkg.name %>.min.css': 'src/assets/css/<%= pkg.name %>.scss'
        }
      },

      dev: {
        options: {
          sourceMap: true,
          outputStyle: 'expanded'
        },
        files: {
          'src/assets/css/<%= pkg.name %>.css': 'src/assets/css/<%= pkg.name %>.scss'
        }
      }
    },

    watch: {
      sass: {
        files: ['src/assets/css/**/*.scss'],
        tasks: ['sass:dev'],
      }
    },

    browserSync: {
      dev: {
        bsFiles: {
          src : [
            'src/assets/css/*.css',
            'src/*.html'
          ]
        },
        options: {
          watchTask: true,
          server: 'src'
        }
      }
    },

    clean: {
      options: {
        force: true
      },
      before_copy: ['dist'],
      after_copy: {
        src: [
          "dist/**/theDocs.js",
          "dist/**/theDocs.min.js",
          "dist/**/theDocs.css",
          "dist/**/theDocs.min.css",
          "dist/**/*.css.map",
          "dist/**/theDocs.scss",
          "dist/**/css/theDocs",
          "dist/**/vendors",
          "dist/assets/css/custom.css",
          "dist/assets/js/custom.js",
          "dist/assets/img/*",
          "!dist/assets/img/favicon*",
          "!dist/assets/img/logo*",
        ],
      }
    },

    replace: {
      dist: {
        src: ['dist/*.html'],
        overwrite: true,
        replacements: [{
          from: /    <link href="assets\/css\/theDocs\.css" rel="stylesheet">\n/g,
          to: ""
        },
        {
          from: /    <script src="assets\/js\/theDocs\.js"><\/script>\n/g,
          to: ""
        }]
      }
    },

    copy: {
      dist: {
        files: [
          {expand: true, cwd: 'src/', src: ['**'], dest: 'dist'},

        ],
      },

      dev: {
        files: [
          {expand: true, cwd: 'src/assets/vendors/bootstrap/fonts', src: ['**'], dest: 'src/assets/fonts/'},
          {expand: true, cwd: 'src/assets/vendors/font-awesome/fonts', src: ['**'], dest: 'src/assets/fonts/'}
        ]
      }
    },

    concat: {
      dist: {
        files: {
          'dist/assets/js/theDocs.all.js': [
            'src/assets/js/theDocs.all.min.js',
            'src/assets/js/theDocs.js'
          ],

          'dist/assets/js/theDocs.all.min.js': [
            'src/assets/js/theDocs.all.min.js',
            'src/assets/js/theDocs.min.js'
          ],

          'dist/assets/css/theDocs.all.css': [
            'src/assets/css/theDocs.all.min.css',
            'src/assets/css/theDocs.css'
          ],

          'dist/assets/css/theDocs.all.min.css': [
            'src/assets/css/theDocs.all.min.css',
            'src/assets/css/theDocs.min.css'
          ]
        },
      },

      dev: {
        files: {
          'src/assets/js/theDocs.all.min.js': [
            'src/assets/vendors/jquery/jquery.min.js',
            'src/assets/vendors/bootstrap/js/bootstrap.min.js',
            'src/assets/vendors/prism/prism.js',
            'src/assets/vendors/perfect-scrollbar/js/perfect-scrollbar.jquery.min.js',
            'src/assets/vendors/clipboard.js/clipboard.min.js',
            'src/assets/vendors/lity/lity.min.js',
            'src/assets/vendors/fitvids/jquery.fitvids.js',
            'src/assets/vendors/matchHeight.min.js'
          ],

          'src/assets/css/theDocs.all.min.css': [
            'src/assets/vendors/bootstrap/css/bootstrap.min.css',
            'src/assets/vendors/font-awesome/css/font-awesome.min.css',
            'src/assets/vendors/prism/prism.css',
            'src/assets/vendors/perfect-scrollbar/css/perfect-scrollbar.min.css',
            'src/assets/vendors/lity/lity.min.css'
          ]
        },
      },
    },

    uglify: {
      options: {
        mangle: true,
        //preserveComments: 'some',
        banner: '<%= banner %>'
      },
      dist: {
        files: {
          //'dist/assets/js/<%= pkg.name %>.js': ['dist/assets/js/<%= pkg.name %>.js']
        }
      },
      dev: {
        files: {
          'src/assets/js/theDocs.min.js': ['src/assets/js/theDocs.js']
        }
      }
    },

    postcss: {
      options: {
        processors: [
          autoprefixer, // add vendor prefixes
          //require('cssnano')({zindex: false}) // minify the result
        ]
      },
      dist: {
        //src: 'dist/*/assets/css/*.css'
      },
      dev: {
        src: ['src/assets/css/theDocs.css', 'src/assets/css/theDocs.min.css']
      }
    },

    "file-creator": {
      build: {
        "dist/assets/js/custom.js": function(fs, fd, done) {
          fs.writeSync(fd, '$(function() {\n\n\n\n})(jQuery);');
          done();
        },

        "dist/assets/css/custom.css": function(fs, fd, done) {
          fs.writeSync(fd, '');
          done();
        }
      }
    },
  });

  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-file-creator');
  grunt.loadNpmTasks('grunt-text-replace');
  grunt.loadNpmTasks('grunt-postcss');
  grunt.loadNpmTasks('grunt-sass');
  grunt.loadNpmTasks('grunt-browser-sync');

  grunt.registerTask('default', ['browserSync', 'watch']);

  grunt.registerTask('dist',
    [
      'dev',
      'sass:dist',
      'clean:before_copy',
      'copy:dist',
      'concat:dist',
      'replace:dist',
      'uglify:dist',
      'postcss:dist',
      'clean:after_copy',
      'file-creator'
    ]
  );

  grunt.registerTask('dev',
    [
      'sass',
      'concat:dev',
      'uglify:dev',
      'postcss:dev',
      'copy:dev',
      //'watch'
    ]
  );
};
