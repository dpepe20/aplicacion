from django.db import models

    #Genero
class Genero(models.Model):
	nombre_genero = models.CharField(max_length=50)
	def __str__ (self):
		return self.nombre_genero

class Filtro(models.Model):
	tipo_genero		=models.CharField(max_length=40)
	tipo 			=models.CharField(max_length=30)
	fil_Fecha 		=models.DateField()
	def  __str__(self):
		return self.tipo_genero

    #Descarga

class Descarga(models.Model):
	des_Nombre		=models.CharField(max_length=300)
	link			=models.CharField(max_length=500)
	fotejes			=models.ImageField(upload_to='fotos',null = True, blank = True)
	descripcion 	=models.CharField(max_length=500)

	def  __str__(self):
		return self.des_Nombre

    #Extreno

class Extreno(models.Model):
	ext_Nombree		=models.CharField(max_length=110)
	ext_Idioma		=models.CharField(max_length=26)
	ext_descripcion	=models.CharField(max_length=500)
	fecha_estreno	=models.DateField()
	imagenes		=models.ImageField(upload_to='fotos',null = True, blank = True)

	def  __str__(self):
		return self.ext_Nombree

    #Pelicula

class Pelicula(models.Model):
	nombre 			=models.CharField(max_length=100)
	descripcion		=models.CharField(max_length=500)
	fecha 			=models.DateField()
	idioma 			=models.CharField(max_length=40)
	calidad			=models.CharField(max_length=40)
	generos			=models.ManyToManyField(Genero, null = True, blank = True)
	filtros			=models.ManyToManyField(Filtro, null = True, blank = True)
	descargas		=models.ManyToManyField(Descarga, null = True, blank = True)
	imagen			=models.ImageField(upload_to='fotos',null = True, blank = True)
	Ver_online		=models.CharField(max_length=400)
	

	def __str__(self):
		return self.nombre

    #Recomendacion
    
class Recomendacion(models.Model):
	#recomendaciones por parte de los usuarios
	rec_Nombre		=models.CharField(max_length=500)
	rec_idioma		=models.CharField(max_length=30)
	rec_calidad		=models.CharField(max_length=30)
	mensaje			=models.CharField(max_length=500)
	imga 			=models.ImageField(upload_to='fotos',null = True, blank = True)
	
	def  __str__(self):
		return self.rec_Nombre


