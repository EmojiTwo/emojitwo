@echo off

if "%1" == "" (
	echo No file specified
	echo.
	echo.Usage: %0% file [option]
	echo file:   lowercase hexadecimal Unicode code point
	echo option: [ skin / sex / gender ]
	echo         'skin'   = U+1F3FB..F suffix
	echo         'sex'    = U+1F468/9 prefix plus 'skin'
	echo         'gender' = U+2640/2 suffix plus 'skin'
	goto :end
)

for %%i in (%~1) do (
	echo. * [U+%%i ![^&#x%%i;][%%i.png]][%%i.svg] ![][%%i.e1] >> changes.md
	echo.[%%i.e1]: https://rawgit.com/emojione/emojione/2.2.7/assets/png/%%i.png >> changes.md
	echo.[%%i.png]: https://rawgit.com/emojitwo/emojitwo/master/png/%%i.png >> changes.md
	echo.[%%i.svg]: https://github.com/EmojiTwo/emojitwo/blob/master/svg/%%i.svg >> changes.md
	if "%2" == "skin" (
		echo Converting svg\%%~ni.svg and its skin tone variants to optimized PNGs ...
		call :sizes %%~ni
		call :sizes %%~ni-1f3fb
		call :sizes %%~ni-1f3fc
		call :sizes %%~ni-1f3fd
		call :sizes %%~ni-1f3fe
		call :sizes %%~ni-1f3ff
		goto :end
	)
	if "%2" == "sex" (
		echo Converting svg\%%~ni.svg and its sex and skin tone variants to optimized PNGs ...
		call :sizes 1f468-%%~ni
		call :sizes 1f468-1f3fb-%%~ni
		call :sizes 1f468-1f3fc-%%~ni
		call :sizes 1f468-1f3fd-%%~ni
		call :sizes 1f468-1f3fe-%%~ni
		call :sizes 1f468-1f3ff-%%~ni
		call :sizes 1f469-%%~ni
		call :sizes 1f469-1f3fb-%%~ni
		call :sizes 1f469-1f3fc-%%~ni
		call :sizes 1f469-1f3fd-%%~ni
		call :sizes 1f469-1f3fe-%%~ni
		call :sizes 1f469-1f3ff-%%~ni
		goto :end
	)
	if "%2" == "gender" (
		echo Converting svg\%%~ni.svg and its gender and skin tone variants to optimized PNGs ...
		call :sizes %%~ni
		call :sizes %%~ni-2640
		call :sizes %%~ni-1f3fb-2640
		call :sizes %%~ni-1f3fc-2640
		call :sizes %%~ni-1f3fd-2640
		call :sizes %%~ni-1f3fe-2640
		call :sizes %%~ni-1f3ff-2640
		call :sizes %%~ni-2642
		call :sizes %%~ni-1f3fb-2642
		call :sizes %%~ni-1f3fc-2642
		call :sizes %%~ni-1f3fd-2642
		call :sizes %%~ni-1f3fe-2642
		call :sizes %%~ni-1f3ff-2642
		goto :end
	)
	call :sizes %%~ni
	goto :end
)

:sizes
	call :convert %%~n1 16
	call :convert %%~n1 32
	call :convert %%~n1 48
	call :convert %%~n1 64
	call :convert %%~n1 72
	call :convert %%~n1 96
	call :convert %%~n1 128
	call :convert %%~n1 512
goto :eof

:convert
	echo U+%1 SVG to %2 x %2 PNG
	if "%2" == "72" (
		@inkscape --without-gui --file=svg\%1.svg --export-png=png\%1.png --export-width=%2 --export-height=%2
		@optipng -o7 -clobber -preserve -quiet png\%1.png
	) else (
		@inkscape --without-gui --file=svg\%1.svg --export-png=png\%2\%1.png --export-width=%2 --export-height=%2
		@optipng -o5 -clobber -preserve -quiet png\%2\%1.png
	)
	echo.
goto :eof

:end
:: exit
