@echo off
setlocal enabledelayedexpansion

rem Solicitar o diretório das fotos ao usuário
set /p input_directory=Digite o caminho completo para o diretório das fotos (ex: C:\caminho\para\fotos): 
set /p output_directory=Digite o caminho completo para salvar as fotos (ex: C:\caminho\para\fotos): 

rem Verificar se o diretório de entrada existe
if not exist "%input_directory%" (
    echo Diretório não encontrado.
    pause
    exit /b
)

rem Solicitar o diretório de saída ao usuário
set /p output_directory=Digite o caminho completo para o diretório de saída (ex: C:\caminho\para\saida): 

rem Verificar se o diretório de saída existe; caso contrário, criá-lo
if not exist "%output_directory%" (
    mkdir "%output_directory%"
)

rem Loop através de todos os arquivos PNG no diretório de entrada
for %%f in ("%input_directory%\*.png") do (
    rem Obter o nome do arquivo e a extensão
    set "filename=%%~nf"
    set "extension=%%~xf"

    rem Usar o ImageMagick para redimensionar a imagem para uma altura de 1080 pixels, preservando a transparência
    magick "%%f" -resize x1080 -background none -gravity center -extent x1080 "%output_directory%\!filename!!extension!"
)

echo Conversão concluída.
pause
