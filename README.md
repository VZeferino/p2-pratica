# Explicação da implementação

Nesse repositório está um código Python que serve para detectar rostos em vídeo usando a biblioteca OpenCV (cv2). 
Este código importa a biblioteca cv2 para trabalhar com vídeo. Em seguida, um objeto 'CascadeClassifier' é criado para detectar a face. O arquivo XML "haarcascade_frontalface_default.xml" é usado como um modelo pré-treinado para detecção facial. Este arquivo contém informações sobre características faciais que o algoritmo usará para identificar o rosto. O código usa `VideoCapture` para abrir um arquivo de vídeo chamado "arsene.mp4". Um objeto "VideoWriter" é criado para gravar o vídeo de saída. O código verifica se o arquivo de vídeo pode ser aberto. Caso contrário, exibe uma mensagem de erro e fecha o programa. O código entra em um loop que lê cada quadro do vídeo, é o que "read()" faz. 

A detecção de faces é feita chamando o método 'detectMultiScale()' do objeto face_detector que nos retorna uma lista de retângulos representando a face especificada. O loop "for" é usado para percorrer cada retângulo definido. Os quadros processados ​​são gravados no vídeo de saída usando o objeto `output_video.write()`. Utilizando a função "imshow()" é mostrado o vídeo para nós. Quando o usuário pressiona a tecla 'q', o loop sai. Após o loop, todas as janelas se fecham com 'destroyAllWindows()'.

# Vídeo da implementação

[video-prova.webm](https://github.com/VZeferino/p2-pratica/assets/99190423/8918cd8e-b074-44f7-ac51-963505d02559)
