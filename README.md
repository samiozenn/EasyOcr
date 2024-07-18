[TR]

# OCR Image Text Extraction

Bu kod, belirli bir klasördeki görüntü dosyalarını okuyarak bu görüntülerdeki metinleri tespit etmek ve her bir görüntü için OCR (Optik Karakter Tanıma) sonuçlarını ayrı bir metin dosyasına kaydetmek için kullanılır. Kısaca kullanım amacı şu şekildedir:

1. **Görüntü Dosyalarını Oku**: `input` klasöründe bulunan `.jpg`, `.jpeg`, veya `.png` dosyalarını okur.
2. **OCR İşlemi Uygula**: EasyOCR kütüphanesi kullanarak her bir görüntüdeki metinleri tespit eder.
3. **Sonuçları Kaydet**: Her bir görüntü için OCR sonuçlarını ayrı ayrı `.txt` dosyalarına kaydeder. Bu dosyalar `output` klasöründe saklanır.
4. **Metin Birleştirme**: Y ekseninde birbirine yakın olan metinleri birleştirerek daha anlamlı sonuçlar elde eder.
5. **Sonuçları Görselleştir**: İşlenmiş görüntüleri, üzerinde tespit edilen metin kutucuklarıyla birlikte görselleştirir ve gösterir.

## Gereksinimler

- Python 3.x
- EasyOCR
- OpenCV
- NumPy
- Matplotlib

## Kurulum

Aşağıdaki adımları takip ederek gerekli kütüphaneleri kurabilirsiniz:

```bash
pip install easyocr
pip install opencv-python-headless
pip install numpy
pip install matplotlib
```

[EN]

# OCR Image Text Extraction

This code is used to read image files from a specific folder, detect text within these images, and save the OCR (Optical Character Recognition) results into separate text files for each image. The main purpose of this code can be summarized as follows:

1. **Read Image Files**: It reads `.jpg`, `.jpeg`, or `.png` files located in the `input` folder.
2. **Apply OCR**: It uses the EasyOCR library to detect text within each image.
3. **Save Results**: It saves the OCR results for each image into separate `.txt` files, which are stored in the `output` folder.
4. **Combine Texts**: It combines texts that are close to each other on the y-axis to obtain more meaningful results.
5. **Visualize Results**: It visualizes the processed images with bounding boxes around the detected texts and displays them.

## Requirements

- Python 3.x
- EasyOCR
- OpenCV
- NumPy
- Matplotlib

## Installation

Follow the steps below to install the necessary libraries:

```bash
pip install easyocr
pip install opencv-python-headless
pip install numpy
pip install matplotlib


