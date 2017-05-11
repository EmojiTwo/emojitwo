SETLOCAL ENABLEEXTENSIONS
FOR /F "eol=; tokens=1-6* delims=," %%a IN (emoji-codes.csv) DO CALL :loopbody %%a %%c %%f %%e
@REM Don't "fall through" to :loopbody.
GOTO :EOF

:loopbody
	@ECHO mklink png\%%2.png png\%%1.png
	@ECHO mklink png\%%3.png png\%%1.png
	@ECHO mklink png_128x128\%%2.png png_128x128\%%1.png
	@ECHO mklink png_128x128\%%3.png png_128x128\%%1.png
	@ECHO mklink png_512x512\%%2.png png_512x512\%%1.png
	@ECHO mklink png_512x512\%%3.png png_512x512\%%1.png
	@ECHO mklink svg\%%2.svg svg\%%1.svg
	@ECHO mklink svg\%%3.svg svg\%%1.svg
	@ECHO mklink svg_bw\%%2.svg svg_bw\%%1.svg
	@ECHO mklink svg_bw\%%3.svg svg_bw\%%1.svg
GOTO :EOF

@REM	@ECHO mklink %%a %%e
ENDLOCAL
