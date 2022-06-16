project('poco')

python = find_program('python', 'python3', required : true)

if host_machine.system() == 'windows'
    if get_option('mt').enabled()
		config = 'release_mt'
    else
		config = 'release_md'
    endif

	poco_dep = declare_dependency(
		compile_args: '-DPOCO_NO_AUTOMATIC_LIBS',
		include_directories: 'win/include'
	)
else
	config = 'release'
	poco_dep = declare_dependency(
		include_directories: 'mac/include'
	)
endif

foundation_lib = static_library( 'foundation',
  objects: run_command(python, 'globo', config, 'Foundation').stdout().strip().split('\n'),
)

json_lib = static_library( 'json',
  objects: run_command(python, 'globo', config, 'JSON').stdout().strip().split('\n'),
)
