from django.contrib import admin


from .models import Article,Comment # .models ile aynı klasörün altındaki models.py dosyasına gittik ve Article class'ı dahil ettik.
# Register your models here.
admin.site.register(Comment)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title","author","created_date"] # Bu şekilde kullanarak başlığı kullanıcı adını ve oluşturulma tarihini de eklemiş olduk.
    list_display_links = ["title","created_date"] # Bu şekilde kullanarak link vermiş olduk. 'author'da link verilmedi.
    search_fields = ["title"]  # Arama çubuğu ekliyor.Title'a göre arıyor.
    list_filter = ["author","created_date"] # Yan tarafa filtreleme eklendi. Şu anda yazar'a göre ama her şekilde  değiştirilebilir.
    class Meta:
        model = Article
