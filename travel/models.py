from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from py2neo import Graph,authenticate


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return self.title

'''
    Only called when Post Save method executes based on the @receiver signal
'''
@receiver(post_save, sender=Todo)
def create_todo_node(sender, instance, **kwargs):
    """
    Creates the todo node on the graph database.
    """
    
    if instance is not None:
        #graph = Graph('http://localhost:7474/db/data')
        #graph = Graph("http://neo4j:password@localhost:7474")
        authenticate("hobby-hnhnphgpkdehgbkecgpgnpal.dbs.graphenedb.com:24786", "traveldiaries", "b.5yAEyKlxfCO5.VNM1FNl0f9b0BjaP")
        graph = Graph("bolt://hobby-hnhnphgpkdehgbkecgpgnpal.dbs.graphenedb.com:24786", user="traveldiaries", password="b.5yAEyKlxfCO5.VNM1FNl0f9b0BjaP", bolt=True, secure = True, http_port = 24789, https_port = 24780)
        #graph = Graph("https://traveldiaries:b.5yAEyKlxfCO5.VNM1FNl0f9b0BjaP@hobby-hnhnphgpkdehgbkecgpgnpal.dbs.graphenedb.com:24786")
        query = '''
        CREATE (n:Todo { title : {title}, description : {description}})
        '''
    
        ## now execute the query
        graph.run(query, title=instance.title,
                description=instance.description
        )
          

