project('poco')

python = find_program('python', 'python3', required : true)

if host_machine.system() == 'windows'
	poco_dep = declare_dependency(
		compile_args: '-DPOCO_NO_AUTOMATIC_LIBS',
		include_directories: 'win/include'
	)
else
	poco_dep = declare_dependency(
		include_directories: 'mac/include'
	)
endif

foundation_lib = static_library( 'foundation',
  objects: run_command(python, 'globo', 'Foundation').stdout().strip().split('\n'),
)

json_lib = static_library( 'json',
  objects: run_command(python, 'globo', 'JSON').stdout().strip().split('\n'),
)
