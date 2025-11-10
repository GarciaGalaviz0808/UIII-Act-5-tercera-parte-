from django.db import models

# ==========================================
# MODELO: VENDEDOR
# ==========================================
class Vendedor(models.Model):
    id_vendedor = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField(max_length=300, unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=300)
    ciudad = models.CharField(max_length=100)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# ==========================================
# MODELO: CATEGORIA (pendiente)
# ==========================================
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=50)
    fecha_creacion = models.DateField(auto_now_add=True)
    activa = models.BooleanField(default=True)
    img_url = models.URLField(max_length=254, blank=True, null=True)

    def __str__(self):
        return self.nombre

# ==========================================
# MODELO: PRODUCTO (pendiente)
# ==========================================
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True, unique=True)

    vendedor = models.ForeignKey(
        Vendedor, on_delete=models.CASCADE, related_name="productos"
    )

    categorias = models.ManyToManyField(
        Categoria, related_name="productos"
    )

    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    stock = models.IntegerField()
    fecha_publicacion = models.DateField(auto_now_add=True)
    descripcion = models.CharField(max_length=200)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
