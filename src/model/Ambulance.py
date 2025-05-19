from peewee import AutoField, CharField, IntegerField, Model

class Ambulance(Model):
    id              = AutoField()
    number_plate    = CharField(max_length=8, null=False)
    ambulance_model = CharField(max_length=35, null=False)
    year            = IntegerField(null=False)
    document_number = CharField(max_length=15, null=False)

    