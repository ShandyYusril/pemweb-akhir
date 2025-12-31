from django.db import models

class Berita(models.Model):
    judul = models.CharField(max_length=200)
    isi = models.TextField()
    gambar = models.ImageField(upload_to='berita/')
    tanggal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul

    class Meta:
        verbose_name_plural = "Berita"

class Dosen(models.Model):
    nama = models.CharField(max_length=100)
    nidn = models.CharField(max_length=20, null=True, blank=True) 
    jabatan = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='dosen/')
    
    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = "Dosen"

class PhotoCollage(models.Model):
    nama = models.CharField(max_length=100, default="Foto Galeri")
    gambar = models.ImageField(upload_to='asset/')
    urutan = models.IntegerField(default=0, help_text="Urutan tampil di galeri")
    
    def __str__(self):
        return f"{self.nama} ({self.id})"
    
    class Meta:
        verbose_name_plural = "Photo Collage"
        ordering = ['urutan']
    
    