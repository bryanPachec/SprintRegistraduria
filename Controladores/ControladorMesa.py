from Modelos.Mesa import Mesa
from Repositorios.RepositorioMesa import RepositorioMesa

class ControladorMesa():
   """
   constructor que permite llevar a cabo la creacion de instancias del controlador.
   """
   def __init__(self) -> object:
       self.repositorioMesa = RepositorioMesa()
       print("Creando Controlador Mesa")


   def index(self):
       print("Listar todas las mesas de Votacion")
       return self.repositorioMesa.findAll()

   def create(self, laMesa):
       print("Crear una Mesa de votacion")
       nuevaMesa = Mesa(laMesa)
       return self.repositorioMesa.save(nuevaMesa)

   def show(self, id):
       print("Mostrando mesa de votacion con id ", id)
       laMesa = Mesa(self.repositorioMesa.findById(id))
       return laMesa.__dict__

   def update(self, id, laMesa):
       print("Actualizando Mesa con id ", id)
       MesaActual = Mesa(self.repositorioMesa.findById(id))
       MesaActual.numero = laMesa["numero"]
       MesaActual.cantidad_inscritos = laMesa["cantidad_inscritos"]
       return self.repositorioMesa.save(MesaActual)

   def delete(self, id):
       print("Elimiando Mesa con id ", id)
       return self.repositorioMesa.delete(id)