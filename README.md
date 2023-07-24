# PythonDeveloperTestProject

* Kitapsepeti sitesi selenium kullanarak gerekli elementleri kullandım.
* search input kısmını seçerek değer olarak python yazdırdım ve python kitap araması yaptım.
* Çıkan sonuçlar arasında satışta olan ürünler için filitreleme yapıp daha sonra bu ürünlerin title,publisher,author,price verilerini alarak array içerisine yerleştirdim.
* Oluşan arraylar içerisinde farklı veriler olduğunu fark ettim ve oluşan arrayleri düzenledim.
* Pandas kütüphanesi kullanarak bunları bir dataframe haline getirdim csv dosyasını aldım.
* Oluşan csv dosyasını dict çevirdim ve mongodb de oluşturdum veri tabanına bu verileri ekleyip kaydettim.
* mongodb docker hub üzerinden image olarak çekerek bir container oluşturan bir docker-compose.yml dosyası oluşturdum. Bu dosyayı çalıştırmak için: 
```
docker-compose up -d
``` 


<img src="Screenshot%20from%202023-07-24%2005-54-31.png"
     style="margin-left:20px" />