
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
def poster_path(instance, filename):
    return "alba/images/" + str(instance.nazev) + "/poster/" + filename

class Vydavatelstvi(models.Model):
    nazev = models.CharField(max_length=50, unique=True, verbose_name='Název vydavatelství', help_text='Zadejte název vydavatelství')

    class Meta:
        ordering = ['nazev']

    def __str__(self):
        return self.nazev

class Certifikace(models.Model):
    oceneni = models.CharField (max_length=20, unique=True, verbose_name='Název ocenění', help_text='Zadejte název ocenění')

    class Meta:
        ordering = ['oceneni']

    def __str__(self):
        return self.oceneni


class Zanr(models.Model):
    zanr = models.CharField (max_length=20, unique=True, verbose_name='Název žánru', help_text='Zadejte název žánru')

    class Meta:
        ordering = ['zanr']

    def __str__(self):
        return self.zanr


class Interpret(models.Model):
    POHLAVI = [
        ('Muž','Muž'),
        ('Žena', 'Žena')
    ]

    jmeno = models.CharField (max_length=50, verbose_name='Jméno umělce', help_text='Zadejte jméno umělce')
    prijmeni = models.CharField(max_length=50, verbose_name='Příjmení umělce', help_text='Zadejte příjmení umělce')
    narodnost = models.CharField(max_length=50, verbose_name='Národnost umělce', help_text='Zadejte národnost umělce')
    pohlavi = models.CharField(max_length=5, choices=POHLAVI, verbose_name='Pohlaví umělce', help_text='Vyberte pohlaví umělce')
    datumN = models.DateField(verbose_name='Datum narození', help_text='Vyberte datum narození')
    datumU = models.DateField(blank=True, null=True, verbose_name='Datum umrtí', help_text='Vyberte datum umrtí')

    class Meta:
        ordering = ['prijmeni']

    def __str__(self):
        return f'{self.jmeno} {self.prijmeni}'


class Album(models.Model):
    FORM = [
        ('LP', 'LP'),
        ('EP', 'EP'),
        ('Single', 'Single')
    ]
    nazev = models.CharField(max_length=100, verbose_name='Název alba', help_text='Zvolte název alba')
    hodnoceni = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], verbose_name='Hodnocení', help_text='Ohodnoťte album')
    forma = models.CharField(max_length=10, choices=FORM, verbose_name='Forma alba', help_text='Zvolte formu alba')
    datumV = models.DateField(verbose_name='Datum vydání', help_text='Zvolte datum vydání')
    certifikace = models.ForeignKey(Certifikace, on_delete=models.CASCADE)
    vydavatelstvi = models.ForeignKey(Vydavatelstvi, on_delete=models.CASCADE)
    zanr = models.ManyToManyField(Zanr, help_text='Zvolte žánry')
    interpret = models.ManyToManyField(Interpret, help_text='Zvolte interpreta')
    image = models.ImageField(upload_to=poster_path, blank=True, null=True, verbose_name="Náhledový obrázek")
    runtime = models.IntegerField(null=True, verbose_name="Délka alba")

    class META:
        ordering = ['nazev']

    def __str__(self):
        return self.nazev


class Pisen(models.Model):
    nazev = models.CharField(max_length=100, verbose_name='Název skladby', help_text='Zadejte název skladby')
    delka = models.TimeField(verbose_name='Délka stopy', help_text='Zadejte délku stopy')
    poradi = models.IntegerField(verbose_name='Pořadí stopy', help_text='Zadejte pořadí stopy')
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    class META:
        ordering = ['nazev']

    def __str__(self):
        return self.nazev