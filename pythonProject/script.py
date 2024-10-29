import os
import subprocess

def get_user_input():
    """
    Obtém as entradas do usuário para os diretórios de entrada e saída.
    """
    input_folder = input("Digite o caminho para a pasta de entrada com arquivos TIFF: ")
    output_folder = input("Digite o caminho para a pasta de saída para os arquivos PDF: ")
    return input_folder, output_folder

def validate_paths(input_folder, output_folder):
    """
    Valida os caminhos fornecidos pelo usuário.
    """
    if not os.path.exists(input_folder):
        print(f"Erro: O caminho de entrada '{input_folder}' não existe.")
        return False
    if not os.path.isdir(input_folder):
        print(f"Erro: O caminho de entrada '{input_folder}' não é um diretório.")
        return False
    os.makedirs(output_folder, exist_ok=True)
    return True

def convert_tiff_to_pdf_with_ocr(input_folder, output_folder):
    """
    Converte arquivos TIFF para PDF com OCR usando o PDF24, mantendo a estrutura dos diretórios.
    """
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith(".tif"):
                # Caminho completo do arquivo de entrada
                input_file = os.path.join(root, file)

                # Diretório de saída correspondente ao diretório do arquivo TIFF
                relative_path = os.path.relpath(root, input_folder)
                output_dir = os.path.join(output_folder, relative_path)
                os.makedirs(output_dir, exist_ok=True)

                # Nome do arquivo de saída (com extensão .pdf)
                output_file = os.path.join(output_dir, f"{os.path.splitext(file)[0]}.pdf")

                # Comando para executar o PDF24 OCR com as configurações recomendadas
                pdf24_command = [
                    "C:\\Program Files\\PDF24\\pdf24-Ocr.exe",  # Substitua pelo caminho completo do executável
                    "-outputFile", output_file,
                    "-language", "por",
                    "-dpi", "300",
                    input_file
                ]

                try:
                    print(f"\nIniciando a conversão de '{input_file}' para '{output_file}' com OCR em português...")
                    subprocess.run(pdf24_command, check=True)
                    print(f"Conversão concluída: {output_file}")
                except subprocess.CalledProcessError as e:
                    print(f"Erro na conversão de '{input_file}': {e}")
                except FileNotFoundError:
                    print("Erro: Caminho para o executável PDF24 está incorreto. Verifique e tente novamente.")

if __name__ == "__main__":
    print("\nBem-vindo ao Conversor de TIFF para PDF com OCR (PDF24)\n")
    input_folder, output_folder = get_user_input()

    if validate_paths(input_folder, output_folder):
        convert_tiff_to_pdf_with_ocr(input_folder, output_folder)
    else:
        print("\nErro ao validar os caminhos fornecidos. Por favor, tente novamente.")

# Comando para converter o script em um executável usando pyinstaller
# No terminal, execute o seguinte comando:
# pyinstaller --onefile --name tiff_to_pdf_converter script.py
# O executável será criado no diretório "dist" dentro do diretório atual.
'''
Este script Python é um exemplo simples que solicita ao usuário os caminhos para a pasta de entrada e saída, valida esses caminhos e, em seguida, converte arquivos TIFF para PDF com OCR usando o PDF24. Ele mantém a estrutura dos diretórios de entrada ao salvar os arquivos PDF de saída.

Para executar o script, você precisa ter o Python instalado em seu sistema e o módulo `subprocess`. Você também precisa ter o PDF24 OCR instalado em seu sistema e configurar o caminho correto para o executável `pdf24-Ocr.exe` no script.

Você pode converter este script em um executável usando o PyInstaller para facilitar a execução em sistemas sem Python instalado. Basta seguir as instruções fornecidas no comentário no final do script.

Espero que este exemplo seja útil para você. Se precisar de mais ajuda ou esclarecimentos, sinta-se à vontade para perguntar. Boa sorte com o seu projeto'''