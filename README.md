FLASK İLE APİ YAZIP JAVASCRİPTLE YAZILAN TODO APP UYGULAMASINA API'YI BAĞLAMA
NASIL ÇALIŞIR?
-projeyi bilgisayarınıza kopyalayın 
-git clone https://github.com/kullanici_adi/my-flask-app.git
-cd todo-app
-gerekli bağımlılıkları yükleyin (pyproject.toml dosyasında yüklenecek paketler yer alıyor ordan bakabilirsiniz)
-



- `GET /` : Ana sayfa, yapılacaklar listesini görüntüler
- `GET /todo/<int:todo_id>` : Belirli bir görevi JSON formatında görüntüler.
- `POST /todo` : Yeni bir görev ekler.
- `PUT /todo/<int:todo_id>` : Belirli bir görevi günceller.
- `DELETE /todo/<int:todo_id>` : Belirli bir görevi siler.

