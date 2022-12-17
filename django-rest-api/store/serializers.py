from rest_framework import serializers


class ProdcutSerializers(serializers.Serializer):
    """
    serializer me models ki sarri field ho esa zaruri nhi hota. because of data base me kuch private data bhi hota hai or wo show nhi karna hota hai
    """

    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2)
