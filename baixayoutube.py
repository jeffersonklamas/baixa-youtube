#-----------------------------------------------------------
# Baixar vídeos do youtube
#
# Programa copiado para teste, visto no Instagram: @pycodebr
#-----------------------------------------------------------
import os
from termcolor import colored
from pytube import YouTube

# Limpa tela ao iniciar // Clean screen on startup
os.system('clear') or None

# Informe o link do vídeo e o local onde deseja salvarprint
print(colored('1: Copie e cole o endereço do vídeo do Youtbe', 'red'))
print(colored('2: Informe o caminho correto da pasta onde o vídeo será baixado ou digite enter para baixar o vídeo na pasta atual\n', 'red'))
print(colored('3: O formato baixado é MP4\n', 'blue'))
link = input('Digite o link do vídeo que irá baixar: ')
path = input('Digite o diretório onde irá salvar o video OU pressione enter: ')
yt = YouTube(link)

# Detalhes do vídeos
print("Título: ", yt.title)
print('Número de views: ', yt.views)
print('Tamanho do Vídeo: ', yt.length)
print('Avaliação do vídeo: ', yt.rating)

# Usando a maior resolução
ys = yt.streams.get_highest_resolution()

# Inciando download
print('Baixando o vídeo na pasta informada......', path)
ys.download(path)
print(colored('Download finalizado...', 'green'))

