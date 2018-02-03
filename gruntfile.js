module.exports = function(grunt) {

  const autoprefixer = require('autoprefixer')({
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

  const algoliasearch = require('algoliasearch');

  grunt.initConfig({

    sass: {
      options: {
        sourceMap: true,
        outputStyle: 'compressed'
      },
      default: {
        files: {
          'src/assets/css/theDocs.min.css': 'src/assets/css/theDocs.scss'
        }
      }
    },

    uglify: {
      options: {
        mangle: true,
      },
      default: {
        files: {
          'src/assets/js/theDocs.min.js': ['src/assets/js/theDocs.js']
        }
      }
    },

    concat: {
      vendorCss: {
        files: {
          'src/assets/css/vendor.min.css': [
            'node_modules/bootstrap/dist/css/bootstrap.min.css',
            'node_modules/font-awesome/css/font-awesome.min.css',
            'node_modules/perfect-scrollbar/css/perfect-scrollbar.min.css',
          ]
        }
      },
      vendorJs: {
        files: {
          'src/assets/js/vendor.min.js': [
            'node_modules/jquery/dist/jquery.min.js',
            'node_modules/bootstrap/dist/js/bootstrap.min.js',
            'node_modules/perfect-scrollbar/dist/js/perfect-scrollbar.jquery.min.js',
            'node_modules/jquery-match-height/dist/jquery.matchHeight-min.js',
            'node_modules/algoliasearch/dist/algoliasearchLite.min.js',
            'node_modules/algoliasearch-helper/dist/algoliasearch.helper.min.js',
            'node_modules/mousetrap/mousetrap.min.js',
            'src/assets/js/prism.min.js'
          ]
        }
      }
    },

    copy: {
      cssmaps: {
        files: [
          {
            expand: true,
            cwd: 'node_modules/bootstrap/dist/css',
            src: ['bootstrap.min.css.map'],
            dest: 'src/assets/css/'
          }
        ]
      },

      fonts: {
        files: [
          {
            expand: true,
            cwd: 'node_modules/bootstrap/dist/fonts',
            src: ['**'],
            dest: 'src/assets/fonts/'
          },
          {
            expand: true,
            cwd: 'node_modules/font-awesome/fonts',
            src: ['**'],
            dest: 'src/assets/fonts/'
          }
        ]
      }
    },

    postcss: {
      options: {
        map: {
          inline: false
        },
        processors: [
          autoprefixer,
        ]
      },
      files: {
        src: [
          'src/assets/css/theDocs.min.css',
          'src/assets/css/vendor.min.css'
        ]
      }
    },

    clean: {
      options: {
        force: true
      },
      css: ['src/assets/css/*.css', 'src/assets/css/*.css.map'],
      js: [
        'src/assets/js/theDocs.min.js',
        'src/assets/js/vendor.min.js'
      ],
      fonts: ['src/assets/fonts'],
      site: ['site']
    },

    watch: {
      scss: {
        files: ['src/assets/css/**/*.scss'],
        tasks: ['sass']
      },
      js: {
        files: ['src/assets/js/theDocs.js'],
        tasks: ['uglify'],
      }
    },

    exec: {
      site: 'PYTHONPATH=. mkdocs build',
      serve: 'PYTHONPATH=. mkdocs serve'
    }
  });

  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-postcss');
  grunt.loadNpmTasks('grunt-sass');
  grunt.loadNpmTasks('grunt-exec');

  grunt.registerTask(
    'build', [
      'sass',
      'uglify',
      'concat',
      'copy',
      'postcss',
      'exec:site'
    ]
  );

  grunt.registerTask(
    'serve', [
      'build',
      'exec:serve'
    ]
  );

  var index = function() {
    const done = this.async();

    const client = algoliasearch(
      'I1IYALZNSK',
      'c80940c47c99d45b08a80a592345c43c');
    const index = client.initIndex('guild.ai');

    const initIndex = function() {
      const settings = {
        searchableAttributes: ['title', 'text'],
        attributesToHighlight: [],
        attributesToSnippet: ['title:10', 'text:25'],
        attributesToRetrieve: ['location']
      };
      return index.setSettings(settings);
    };

    const clearIndex = function() {
      return index.clearIndex();
    };

    const addObjects = function() {

      // mkdocs generates search_index.json with both the full page
      // content and also each section as docs. We don't want to
      // present users both the full page and separate sections as
      // they appear identical apart from their link. We address this
      // by only indexing sections and not the entire document. We
      // also change the location of the top section document to the
      // page location to avoid using a hash location for the top of
      // the page. We can safely do this because all of our pages have
      // a single top-level h1 element that precedes page content.

      const data = grunt.file.readJSON('./site/search/search_index.json');
      const objects = [];
      var promoteSectionLocation = null;
      data.docs.forEach(function(doc) {
        if (!doc.location.includes('#')) {
          promoteSectionLocation = doc.location;
        } else {
          if (promoteSectionLocation) {
            doc.location = promoteSectionLocation;
          }
          objects.push(doc);
          promoteSectionLocation = null;
        }
      });
      grunt.file.write("/tmp/obj.json", JSON.stringify(objects));
      return index.addObjects(objects);
    };

    initIndex()
      .then(clearIndex)
      .then(addObjects)
      .then(done);
  };

  grunt.registerTask('index', index);

  grunt.registerTask('build-and-index', ['build', 'index']);
};
