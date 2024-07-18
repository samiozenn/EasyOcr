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

This project is designed to recognize and extract text from images using EasyOCR. The project reads image files in a specified folder, applies OCR, and saves the text results as separate `.txt` files for each image.

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


