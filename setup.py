from distutils.core import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'DadosAbertosBrasil',
  packages = ['DadosAbertosBrasil'],
  version = '0.1',
  license='MIT',
  description = 'Pacote Python para acesso a dados abertos e APIs do governo brasileiro.',
  long_description=long_description,
  long_description_content_type='text/markdown'  
  author = 'Gustavo Furtado',
  author_email = 'gustavofurtado2@gmail.com',
  url = 'https://github.com/GusFurtado/DadosAbertosBrasil',
  download_url = 'https://github.com/GusFurtado/DadosAbertosBrasil/archive/0.1.tar.gz',
  keywords = ['pandas', 'api', 'brasil', 'ibge', 'ipea', 'camara', 'requests', 'dados_abertos', 'dadosgovbr'],
  install_requires=[
          'pandas',
          'requests',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Financial and Insurance Industry',
    'Intended Audience :: Science/Research',
    'Topic :: Scientific/Engineering',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: Portuguese (Brazilian)',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)