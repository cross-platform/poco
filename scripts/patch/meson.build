project('poco')

python = find_program('python', 'python3', required : true)

if host_machine.system() == 'windows'
  config_mt = 'release_mt'
  config_md = 'release_md'

  poco_dep = declare_dependency(
    compile_args: ['-DPOCO_NO_AUTOMATIC_LIBS', '-DPOCO_STATIC', '/wd4127', '/wd4244'],
    include_directories: 'win/include'
  )
else
  config_mt = 'release'
  config_md = 'release'

  poco_dep = declare_dependency(
    compile_args: ['-Wno-deprecated-declarations', '-Wno-sign-compare'],
    include_directories: 'mac/include'
  )
endif

libcrypto_lib = static_library( 'libcrypto',
  objects: run_command(python, 'globo', config_mt, 'libcrypto', check: true).stdout().strip().split('\n'),
)
libcrypto_lib_md = static_library( 'libcrypto_md',
  objects: run_command(python, 'globo', config_md, 'libcrypto', check: true).stdout().strip().split('\n'),
)

libssl_lib = static_library( 'libssl',
  objects: run_command(python, 'globo', config_mt, 'libssl', check: true).stdout().strip().split('\n'),
)
libssl_lib_md = static_library( 'libssl_md',
  objects: run_command(python, 'globo', config_md, 'libssl', check: true).stdout().strip().split('\n'),
)

activerecord_lib = static_library( 'activerecord',
  objects: run_command(python, 'globo', config_mt, 'Poco/ActiveRecord', check: true).stdout().strip().split('\n'),
)
activerecord_lib_md = static_library( 'activerecord_md',
  objects: run_command(python, 'globo', config_md, 'Poco/ActiveRecord', check: true).stdout().strip().split('\n'),
)

crypto_lib = static_library( 'crypto',
  objects: run_command(python, 'globo', config_mt, 'Poco/Crypto', check: true).stdout().strip().split('\n'),
)
crypto_lib_md = static_library( 'crypto_md',
  objects: run_command(python, 'globo', config_md, 'Poco/Crypto', check: true).stdout().strip().split('\n'),
)

data_lib = static_library( 'data',
  objects: run_command(python, 'globo', config_mt, 'Poco/Data', check: true).stdout().strip().split('\n'),
)
data_lib_md = static_library( 'data_md',
  objects: run_command(python, 'globo', config_md, 'Poco/Data', check: true).stdout().strip().split('\n'),
)

encodings_lib = static_library( 'encodings',
  objects: run_command(python, 'globo', config_mt, 'Poco/Encodings', check: true).stdout().strip().split('\n'),
)
encodings_lib_md = static_library( 'encodings_md',
  objects: run_command(python, 'globo', config_md, 'Poco/Encodings', check: true).stdout().strip().split('\n'),
)

foundation_lib = static_library( 'foundation',
  objects: run_command(python, 'globo', config_mt, 'Poco/Foundation', check: true).stdout().strip().split('\n'),
)
foundation_lib_md = static_library( 'foundation_md',
  objects: run_command(python, 'globo', config_md, 'Poco/Foundation', check: true).stdout().strip().split('\n'),
)

json_lib = static_library( 'json',
  objects: run_command(python, 'globo', config_mt, 'Poco/JSON', check: true).stdout().strip().split('\n'),
)
json_lib_md = static_library( 'json_md',
  objects: run_command(python, 'globo', config_md, 'Poco/JSON', check: true).stdout().strip().split('\n'),
)

jwt_lib = static_library( 'jwt',
  objects: run_command(python, 'globo', config_mt, 'Poco/JWT', check: true).stdout().strip().split('\n'),
)
jwt_lib_md = static_library( 'jwt_md',
  objects: run_command(python, 'globo', config_md, 'Poco/JWT', check: true).stdout().strip().split('\n'),
)

mongodb_lib = static_library( 'mongodb',
  objects: run_command(python, 'globo', config_mt, 'Poco/MongoDB', check: true).stdout().strip().split('\n'),
)
mongodb_lib_md = static_library( 'mongodb_md',
  objects: run_command(python, 'globo', config_md, 'Poco/MongoDB', check: true).stdout().strip().split('\n'),
)

net_lib = static_library( 'net',
  objects: run_command(python, 'globo', config_mt, 'Poco/Net', check: true).stdout().strip().split('\n'),
)
net_lib_md = static_library( 'net_md',
  objects: run_command(python, 'globo', config_md, 'Poco/Net', check: true).stdout().strip().split('\n'),
)

netssl_lib = static_library( 'netssl',
  objects: run_command(python, 'globo', config_mt, 'Poco/NetSSL', check: true).stdout().strip().split('\n'),
)
netssl_lib_md = static_library( 'netssl_md',
  objects: run_command(python, 'globo', config_md, 'Poco/NetSSL', check: true).stdout().strip().split('\n'),
)

pagecompiler_lib = static_library( 'pagecompiler',
  objects: run_command(python, 'globo', config_mt, 'Poco/PageCompiler', check: true).stdout().strip().split('\n'),
)
pagecompiler_lib_md = static_library( 'pagecompiler_md',
  objects: run_command(python, 'globo', config_md, 'Poco/PageCompiler', check: true).stdout().strip().split('\n'),
)

redis_lib = static_library( 'redis',
  objects: run_command(python, 'globo', config_mt, 'Poco/Redis', check: true).stdout().strip().split('\n'),
)
redis_lib_md = static_library( 'redis_md',
  objects: run_command(python, 'globo', config_md, 'Poco/Redis', check: true).stdout().strip().split('\n'),
)

util_lib = static_library( 'util',
  objects: run_command(python, 'globo', config_mt, 'Poco/Util', check: true).stdout().strip().split('\n'),
)
util_lib_md = static_library( 'util_md',
  objects: run_command(python, 'globo', config_md, 'Poco/Util', check: true).stdout().strip().split('\n'),
)

xml_lib = static_library( 'xml',
  objects: run_command(python, 'globo', config_mt, 'Poco/XML', check: true).stdout().strip().split('\n'),
)
xml_lib_md = static_library( 'xml_md',
  objects: run_command(python, 'globo', config_md, 'Poco/XML', check: true).stdout().strip().split('\n'),
)

zip_lib = static_library( 'zip',
  objects: run_command(python, 'globo', config_mt, 'Poco/Zip', check: true).stdout().strip().split('\n'),
)
zip_lib_md = static_library( 'zip_md',
  objects: run_command(python, 'globo', config_md, 'Poco/Zip', check: true).stdout().strip().split('\n'),
)
