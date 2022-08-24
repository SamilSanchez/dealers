from django.db import models

class Dealer(models.Model):

    rnc = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    direction = models.TextField()
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)

    def __str__(self) -> str:
        return f"RNC: {self.rnc} Nombre: {self.name}"


class Official(models.Model):

    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"Código: {self.code} Nombre: {self.name}"


STATUS_DEALER = [
    ("accept", 'Aprobar'),
    ("reject", 'Rechazar'),
]

class AcceptDealer(models.Model):

    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    official = models.ForeignKey(Official, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=11,
        choices=STATUS_DEALER,
    )

    def __str__(self) -> str:
        return f"Dealer: {self.dealer} Oficial: {self.official} Estado: {self.status}"

