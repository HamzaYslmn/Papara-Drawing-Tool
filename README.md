# Papara-Drawing-Tool

![image](https://github.com/user-attachments/assets/341494f6-e34e-40a0-8957-0fd9a14f2cf7)



# Otomatik Çizim Aracı

Bu proje, belirli bir çizim alanına (örneğin Paint veya benzeri bir çizim programı) otomatik olarak resim çizimi gerçekleştiren bir Python betiğidir. Kod, ekran üzerinden kullanıcı etkileşimiyle çizim alanını belirler, `image.png` adlı görüntüyü orantılı olarak ölçeklendirir ve ardından pikselleri tarayarak çizim uygulamasında fare hareketleriyle resmi yeniden oluşturur.

## Özellikler

- **Ekran Üzerinden Alan Seçimi:**  
  Kullanıcı, çizim yapılacak alanın sağ üst ve sol alt köşelerini belirleyerek ekran koordinatlarını girer.

- **Görüntü Ölçeklendirme:**  
  Yüklenen resim, seçilen çizim alanına sığacak şekilde orantılı olarak yeniden boyutlandırılır ve ortalanır.

- **Otomatik Çizim:**  
  Resmin pikselleri taranır; eşik değerinin (30) altındaki renk değerlerine sahip pikseller, fare ile tıklama ve sürükleme hareketleri kullanılarak çizim programında işlenir. Böylece, ardışık koyu pikseller tek seferde çizgi olarak aktarılır.

- **İptal İşlevi:**  
  Çizim işlemi sırasında `ESC` tuşuna basılması durumunda işlem iptal edilebilir.

## Gereksinimler

- **Python 3.x**
- **[pyautogui](https://pypi.org/project/PyAutoGUI/):** Fare ve ekran otomasyonu için.
- **[keyboard](https://pypi.org/project/keyboard/):** Klavye girdilerini algılamak için.
- **[Pillow](https://pypi.org/project/Pillow/):** Görüntü işleme ve yeniden boyutlandırma işlemleri için.

Gereksinimleri yüklemek için terminal veya komut istemcisinde şu komutu çalıştırabilirsiniz:

```bash
pip install -r requirements.txt
```

## Kullanım

1. **Resmi Hazırlama:**  
   Proje dizinine `image.png` adında çizilmek istenen resmi ekleyin.

2. **Çizim Programını Açma:**  
   Çizim yapmak istediğiniz programı (örneğin, Paint) açın ve çizim alanının tamamen görünür olduğundan emin olun.

3. **Betiği Çalıştırma:**  
   Terminal veya komut istemcisinden betiği çalıştırın:
   ```bash
   python Papara.py
   ```

4. **Alan Seçimi:**  
   Betik çalışmaya başladığında ekranda talimatlar görünecektir. Aşağıdaki adımları izleyin:
   - **SAĞ ÜST Nokta:** Çizim alanının sağ üst köşesini belirlemek için farenizi istenen noktaya getirin ve terminale fare oynatmadan geri dönüp `Enter` tuşuna basın.
   - **SOL ALT Nokta:** Çizim alanının sol alt köşesini belirlemek için farenizi istenen noktaya getirin ve terminale fare oynatmadan geri dönüp `Enter` tuşuna basın.

5. **Çizimin Başlaması:**  
   Seçim işlemlerinden sonra betik, 5 saniyelik bir bekleme süresinden sonra otomatik olarak çizime başlayacaktır.

6. **İptal Etme:**  
   Eğer çizim sırasında işlemden çıkmak isterseniz, `ESC` tuşuna basabilirsiniz.

## Kodun Çalışma Mantığı

- **Ekran Koordinatları ile Çizim Alanı Belirleme:**  
  Kullanıcıdan alınan sağ üst ve sol alt noktalar kullanılarak, çizim alanının sol üst koordinatı, genişliği ve yüksekliği hesaplanır.

- **Görüntünün Ölçeklendirilmesi:**  
  `PIL` kütüphanesi ile açılan resim, çizim alanının genişlik ve yüksekliğine orantılı olarak yeniden boyutlandırılır. Böylece, resmin oranları korunur ve çizim alanına ortalanır.

- **Otomatik Çizim Döngüsü:**  
  Resmin her satırı taranır. Eşik değerinden (30) düşük renk değerlerine sahip (yani beyaza yakın olmayan) pikseller tespit edildiğinde, bu pikseller ardışık bir çizgi olarak kabul edilir.  
  `pyautogui` kullanılarak fare, başlangıç noktasından (ilk koyu piksel) tespit edilen son koyu piksel noktasına kadar hareket ettirilir; bu hareket sırasında fare tıklama basılı tutulur. Böylece, çizim programında bir çizgi çizilmiş olur.

- **İptal Kontrolü:**  
  Her satır ve piksel kontrolü sırasında `keyboard` kütüphanesi ile `ESC` tuşu kontrol edilerek, işlem iptal edilebilmektedir.

## Uyarılar

- **Güvenlik ve Kontrol:**  
  Otomatik fare hareketleri yapıldığından, çizim alanının doğru seçilmesi ve diğer uygulamaların etkilenmemesi için dikkatli olunmalıdır.
  
- **Doğru Koordinatlar:**  
  Çizim alanını doğru belirlemeniz, çizimin doğru ve istenilen şekilde aktarılması için kritik öneme sahiptir.

## Lisans

Bu proje Affero Lisansı altında lisanslanmıştır.

