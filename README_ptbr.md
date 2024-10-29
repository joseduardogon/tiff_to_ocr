# Conversor de Arquivos TIFF para PDF com OCR

Este repositório contém um script que realiza a conversão de arquivos TIFF para PDF, aplicando OCR (Reconhecimento Óptico de Caracteres) usando a ferramenta PDF24. O script é ideal para quem possui grandes quantidades de arquivos TIFF e precisa convertê-los para PDF mantendo a estrutura de pastas dos arquivos originais e adicionando texto pesquisável ao documento final.

## Funcionalidades

- Converte arquivos TIFF para PDF.
- Aplica OCR aos arquivos, permitindo a pesquisa de texto nos PDFs resultantes.
- Mantém a estrutura de diretórios dos arquivos TIFF originais.
- Possibilidade de escolha do idioma do OCR (atualmente configurado para português).

## Pré-requisitos

1. **Python 3.x**: O script foi escrito em Python e requer uma versão recente do Python instalada em seu sistema.
2. **PDF24 OCR**: O PDF24 é usado para realizar o OCR. Certifique-se de que o PDF24 Creator está instalado e disponível no caminho especificado no script.
3. **PyInstaller (opcional)**: Caso deseje transformar o script em um executável (.exe), é necessário ter o PyInstaller instalado.

Para instalar o PyInstaller, use o comando:
```sh
pip install pyinstaller
```

## Como Utilizar

### Passo 1: Clone o Repositório

Clone este repositório para o seu ambiente local usando o seguinte comando:
```sh
git clone https://github.com/joseduardogon/tiff-to-pdf-ocr.git
```

### Passo 2: Configure o Caminho do PDF24

No script, você precisará ajustar o caminho para o executável do PDF24 OCR. Substitua `C:\Caminho\para\pdf24-Ocr.exe` pelo caminho completo do executável do PDF24 em seu sistema.

### Passo 3: Execute o Script

Para executar o script, siga os passos abaixo:

1. Abra um terminal e navegue até o diretório do script.
2. Execute o script usando o comando:
   ```sh
   python tiff_to_pdf_ocr_conversion.py
   ```
3. Você será solicitado a informar o caminho da pasta de entrada (onde estão os arquivos TIFF) e da pasta de saída (onde serão salvos os arquivos PDF).

### Passo 4: Converter para Executável (Opcional)

Caso deseje gerar um executável para facilitar a execução do script, utilize o PyInstaller com o comando abaixo:
```sh
pyinstaller --onefile --name tiff_to_pdf_converter tiff_to_pdf_ocr_conversion.py
```
Isso criará um executável na pasta `dist` que poderá ser utilizado sem a necessidade de instalar o Python em outros computadores.

## Estrutura do Código

O script está dividido nas seguintes funções principais:

1. **get_user_input()**: Solicita ao usuário os caminhos de entrada e saída.
2. **validate_paths(input_folder, output_folder)**: Verifica se os caminhos fornecidos são válidos e cria a pasta de saída, se necessário.
3. **convert_tiff_to_pdf_with_ocr(input_folder, output_folder)**: Percorre os diretórios de entrada, convertendo cada arquivo TIFF em PDF com OCR e mantendo a estrutura dos diretórios.

### Tratamento de Erros

- O script valida os caminhos fornecidos e informa ao usuário caso o caminho de entrada não exista ou não seja um diretório.
- Caso o caminho para o PDF24 esteja incorreto, uma mensagem de erro será exibida solicitando a correção.
- Em caso de falha durante a conversão, o script informará qual arquivo não pôde ser processado.

## Exemplo de Uso

1. Execute o script no terminal.
2. Informe o caminho para a pasta contendo os arquivos TIFF.
3. Informe o caminho para a pasta onde deseja salvar os arquivos PDF.
4. O script começará a conversão e informará o progresso de cada arquivo.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias ou correções.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

