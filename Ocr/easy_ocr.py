

import easyocr as ocr
import cv2
import numpy as np
import matplotlib.pyplot as plt

# OCR okuyucuyu oluştur
ocr_engine = ocr.Reader(['en', 'tr'])

# Görüntüyü dosyadan oku
image_path = 'ERYHnPhWoAA_4gD.jpg'
resim_cv2 = cv2.imread(image_path)

# OCR işlemi yap
yazilar = ocr_engine.readtext(image_path)

# OCR sonucunu yazdır ve metin dosyasına kaydet
with open('ocr_sonuclari.txt', 'w', encoding='utf-8') as file:
    previous_text = ''
    previous_y = None
    threshold = 10  # Metinleri birleştirmek için kullanılacak y koordinatı farkı

    for yazi in yazilar:
        text = yazi[1].strip()  # Tespit edilen metni al ve kenar boşluklarını kaldır
        y_coord = yazi[0][0][1]  # Metnin y koordinatı (üst sol köşe)

        if previous_text:
            if abs(y_coord - previous_y) < threshold:
                # Eğer y koordinatları birbirine yakınsa, metinleri birleştir
                previous_text += f" {text}"
            else:
                # Değilse, önceki metni yaz ve yeni metni sakla
                file.write(f"{previous_text}\n")
                previous_text = text
        else:
            previous_text = text

        previous_y = y_coord

        cv2.rectangle(resim_cv2, (int(yazi[0][0][0]), int(yazi[0][0][1])), (int(yazi[0][2][0]), int(yazi[0][2][1])),
                      (0, 0, 255), 2)

    # Eğer önceki metin hala varsa, onu da yaz
    if previous_text:
        file.write(f"{previous_text}\n")

# Görüntüyü göster
plt.imshow(cv2.cvtColor(resim_cv2, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
