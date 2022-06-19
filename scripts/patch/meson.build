project('poco')

python = find_program('python', 'python3', required : true)

if host_machine.system() == 'windows'
    if get_option('default_library') == 'static'
		config = 'release_mt'
    else
		config = 'release_md'
    endif

	poco_dep = declare_dependency(
		compile_args: ['-DPOCO_NO_AUTOMATIC_LIBS', '-DPOCO_STATIC', '/wd4127', '/wd4244'],
		include_directories: 'win/include'
	)
else
	config = 'release'
	poco_dep = declare_dependency(
    compile_args: ['-Wno-deprecated-declarations', '-Wno-sign-compare'],
		include_directories: 'mac/include'
	)
endif

libcrypto_lib = static_library( 'libcrypto',
  objects: run_command(python, 'globo', config, 'libcrypto', check: true).stdout().strip().split('\n'),
)

libssl_lib = static_library( 'libssl',
  objects: run_command(python, 'globo', config, 'libssl', check: true).stdout().strip().split('\n'),
)

activerecord_lib = static_library( 'activerecord',
  objects: run_command(python, 'globo', config, 'Poco/ActiveRecord', check: true).stdout().strip().split('\n'),
)

crypto_lib = static_library( 'crypto',
  objects: run_command(python, 'globo', config, 'Poco/Crypto', check: true).stdout().strip().split('\n'),
)

data_lib = static_library( 'data',
  objects: run_command(python, 'globo', config, 'Poco/Data', check: true).stdout().strip().split('\n'),
)

encodings_lib = static_library( 'encodings',
  objects: run_command(python, 'globo', config, 'Poco/Encodings', check: true).stdout().strip().split('\n'),
)

foundation_lib = static_library( 'foundation',
  objects: run_command(python, 'globo', config, 'Poco/Foundation', check: true).stdout().strip().split('\n'),
)

json_lib = static_library( 'json',
  objects: run_command(python, 'globo', config, 'Poco/JSON', check: true).stdout().strip().split('\n'),
)

jwt_lib = static_library( 'jwt',
  objects: run_command(python, 'globo', config, 'Poco/JWT', check: true).stdout().strip().split('\n'),
)

mongodb_lib = static_library( 'mongodb',
  objects: run_command(python, 'globo', config, 'Poco/MongoDB', check: true).stdout().strip().split('\n'),
)

net_lib = static_library( 'net',
  objects: run_command(python, 'globo', config, 'Poco/Net', check: true).stdout().strip().split('\n'),
)

netssl_lib = static_library( 'netssl',
  objects: run_command(python, 'globo', config, 'Poco/NetSSL', check: true).stdout().strip().split('\n'),
)

pagecompiler_lib = static_library( 'pagecompiler',
  objects: run_command(python, 'globo', config, 'Poco/PageCompiler', check: true).stdout().strip().split('\n'),
)

redis_lib = static_library( 'redis',
  objects: run_command(python, 'globo', config, 'Poco/Redis', check: true).stdout().strip().split('\n'),
)

util_lib = static_library( 'util',
  objects: run_command(python, 'globo', config, 'Poco/Util', check: true).stdout().strip().split('\n'),
)

xml_lib = static_library( 'xml',
  objects: run_command(python, 'globo', config, 'Poco/XML', check: true).stdout().strip().split('\n'),
)

zip_lib = static_library( 'zip',
  objects: run_command(python, 'globo', config, 'Poco/Zip', check: true).stdout().strip().split('\n'),
)
