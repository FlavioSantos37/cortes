from moviepy.video.io.VideoFileClip import VideoFileClip

def cortar_video(video_path, inicio, fim, output_path):
    """
    Corta o vídeo no intervalo especificado e salva o clipe.

    :param video_path: Caminho para o vídeo de entrada.
    :param inicio: Tempo de início do corte (em segundos).
    :param fim: Tempo de fim do corte (em segundos).
    :param output_path: Caminho para salvar o vídeo cortado.
    """
    try:
        # Carrega o vídeo
        video = VideoFileClip(video_path)

        # Realiza o corte
        corte = video.subclip(inicio, fim)

        # Salva o vídeo cortado
        corte.write_videofile(output_path, codec="libx264")
        print(f"Vídeo cortado salvo em: {output_path}")

        # Fecha o vídeo
        video.close()
    except Exception as e:
        print(f"Erro ao cortar o vídeo: {e}")


if __name__ == "__main__":
    # Solicita as entradas do usuário
    video_path = input("Digite o caminho do vídeo: ")
    try:
        inicio = float(input("Digite o tempo de início do corte (em segundos): "))
        fim = float(input("Digite o tempo de fim do corte (em segundos): "))
        if inicio >= fim:
            raise ValueError("O tempo de início deve ser menor que o tempo de fim.")
    except ValueError as ve:
        print(f"Erro: {ve}")
        exit()

    output_path = input("Digite o caminho do arquivo de saída (exemplo: output.mp4): ")

    # Chama a função para cortar o vídeo
    cortar_video(video_path, inicio, fim, output_path)
