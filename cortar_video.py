import json
from moviepy.video.io.VideoFileClip import VideoFileClip

def cortar_video(video_path, cortes, output_folder):
    """
    Corta o vídeo em intervalos especificados e salva os clipes.

    :param video_path: Caminho para o vídeo de entrada.
    :param cortes: Lista de intervalos [(inicio, fim), ...].
    :param output_folder: Pasta onde os cortes serão salvos.
    """
    try:
        # Carrega o vídeo
        video = VideoFileClip(video_path)

        for i, (inicio, fim) in enumerate(cortes):
            # Define o nome do arquivo de saída
            output_path = f"{output_folder}/corte_{i+1}.mp4"

            # Realiza o corte
            corte = video.subclip(inicio, fim)
            
            # Salva o clipe
            corte.write_videofile(output_path, codec="libx264")
            print(f"Corte {i+1} salvo em: {output_path}")

        video.close()
        print("Todos os cortes foram realizados com sucesso!")

    except Exception as e:
        print(f"Erro ao processar o vídeo: {e}")

if __name__ == "__main__":
    # Caminho do vídeo e arquivo JSON de configuração
    video_path = input("Digite o caminho do vídeo: ")
    json_path = input("Digite o caminho do arquivo JSON com os intervalos: ")
    output_folder = input("Digite a pasta de saída para os cortes: ")

    try:
        # Carrega os intervalos do arquivo JSON
        with open(json_path, "r") as file:
            cortes = json.load(file)

        # Verifica se o formato dos intervalos está correto
        if not all(isinstance(corte, list) and len(corte) == 2 for corte in cortes):
            raise ValueError("O arquivo JSON deve conter uma lista de intervalos [inicio, fim].")

        # Realiza os cortes
        cortar_video(video_path, cortes, output_folder)

    except FileNotFoundError:
        print("Arquivo de vídeo ou JSON não encontrado.")
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo JSON. Certifique-se de que está no formato correto.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
