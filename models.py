__author__ = "Jeremy Nelson"
import redis
import rom

CONNECTION = None
def ala_get_connection():
    global CONNECTION
    if not CONNECTION:
        CONNECTION = redis.Redis(host='0.0.0.0', port=6342)
    return CONNECTION

rom.util.get_connection = ala_get_connection

class Variant(rom.Model):
    name = rom.String(required=True)
    description = rom.String()

class Interaction(rom.Model):
    comment = rom.Text(index=True)
    element = rom.ManyToOne('Variant')
    rating = rom.Integer()
    timestamp = rom.String()
    
    
    
