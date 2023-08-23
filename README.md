FLASK İLE APİ YAZIP JAVASCRİPTLE YAZILAN TODO APP UYGULAMASINA API'YI BAĞLAMA

NASIL ÇALIŞIR?


1) -projeyi bilgisayarınıza kopyalayın 
-git clone https://github.com/kullanici_adi/my-flask-app.git
2) -cd my-flask-app (projenin içine girin)
3) -gerekli bağımlılıkları yükleyin (requirements.txt dosyasında yüklenecek paketler yer alıyor ordan bakabilirsiniz)
-pip install -r requirements.txt ile yükleyebilirsiniz
4) python app.py ile uygulamayı başlatın

- `GET /` : Ana sayfa, yapılacaklar listesini görüntüler
- `GET /todo/<int:todo_id>` : Belirli bir görevi JSON formatında görüntüler.
- `POST /todo` : Yeni bir görev ekler.
- `PUT /todo/<int:todo_id>` : Belirli bir görevi günceller.
- `DELETE /todo/<int:todo_id>` : Belirli bir görevi siler.

