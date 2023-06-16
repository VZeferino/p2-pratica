import cv2

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
                                      
# Abre o arquivo de video
video_capture = cv2.VideoCapture('../assets/arsene.mp4')
width  = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter('saida/output_video.mp4', fourcc, 20.0, (width, height))

# Checa se foi possivel abrir o arquivo
if not video_capture.isOpened():
    print("Error opening video file")
    exit(1)

# Loop de leitura frame por frame
while True:
    # Le um frame do video e, guarda o resultado da leitura
    # Se nao houver mais frames disponiveis, ret sera falso
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(gray, 1.7, 3 )

    for (x,y, w, h) in faces:
        cv2.rectangle(frame, pt1 = (x,y), pt2 = (x+w, y+h), color = (225,0,0),thickness =  3)
    
    output_video.write(frame)

    # Se nao conseguiu ler o frame, para o laco
    if not ret:
        break

    # Exibe o frame
    cv2.imshow('Video Playback', frame)

    # Se o usuario apertar q, encerra o playback
    # O valor utilizado no waiKey define o fps do playback
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
    
# Fecha tudo
video_capture.release()
output_video.release()
cv2.destroyAllWindows()