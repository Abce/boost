  {
    'targets': [
      {
        'target_name': 'boost',
        'type': '<(library)',
        
        'dependencies': [
        ],

        'defines': [
        ],
        
        'include_dirs': [
          '.',
        ],

        'sources': [
          'libs/system/src/error_code.cpp',
        ],

        'conditions': [
          ['OS=="ios"', {
            'include_dirs': [
            ],

            'sources': [
            ],

            'defines': [
            ],
          }],
          
          ['OS=="android"', {
            'defines': [              
            ]
          }],

          ['OS=="linux"', {
            'cflags':[
            ],
          }],
          
          ['OS=="winphone"', {
            'defines':['BOOST_ALL_NO_LIB',],
          }],

          ['OS=="win32"', {
            'defines':['BOOST_ALL_NO_LIB',],            
          }]
        ],
      },
    ],
  }