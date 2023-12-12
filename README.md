# MachineLearningFor-Images

## Proje Bileşenleri:

### Devre Elemanı Çizimleri: 
Elimizde 7 farklı devre elemanının el ile çizimleri bulunmaktadır. Amaç daha sonra çizilecek olan bu devre elemanlarının makine öğrenmesi modeliyle tespit edilip sınıflandırılmasıdır.
Görseller bu repo içerisine eklenmiştir. 

### Model Seçimi ve Eğitimi: [ModelSelection.ipynb](https://www.google.com](https://github.com/hamza37yavuz/MachineLearningFor-Images/blob/main/ModelSelection.ipynb)https://github.com/hamza37yavuz/MachineLearningFor-Images/blob/main/ModelSelection.ipynb) 
datanın incelendiği ve skor karşılaştırılmasının yapıldığı dosyadır.

[circuit_components_ml.py](https://github.com/hamza37yavuz/MachineLearningFor-Images/blob/main/circuit_components_ml.py) seçilen modelin pkl dosyası bu dosya yardımıyla üretilebilir.

### API Servisi:
Sonrasında bu sınıflandırmanın yapılmasının kolaylaştırılması için [API.py](https://github.com/hamza37yavuz/MachineLearningFor-Images/blob/main/API.py) isimli kod hazırlanmıştır. FastAPI kullanılmıştır. Servisi aşağıdaki şekilde başlatabilirsiniz:

`uvicorn API.py:app --reload`

### Servis Testi:
[req.py](https://github.com/hamza37yavuz/MachineLearningFor-Images/blob/main/req.py) ile servisi test edebilirsiniz. Gerekli düzenlemeleri yapabilirsiniz.



### Gereksinimlerin Kurulumu:
`pip install -r requirements.txt`

## Lisans
Bu proje MIT Lisansı altında lisanslanmıştır. Detaylı bilgi için lisans dosyasını kontrol edin.
