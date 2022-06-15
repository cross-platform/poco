project('openssl', 'c',
   default_options: [
        'warning_level=0',
        'werror=false'
    ]
)

if host_machine.system() == 'windows'
    if get_option('mt').enabled()
        add_global_arguments('/MT', language: 'c')
    else
        add_global_arguments('/MD', language: 'c')
    endif
else
    add_global_arguments('-mmacosx-version-min=10.15', language: 'c')
endif

openssl = subproject('openssl', default_options: ['default_library=static'])
