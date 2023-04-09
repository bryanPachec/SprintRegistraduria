from Modelos.Candidato import Candidato
from Repositorios.RepositorioCandidato import RepositorioCandidato


class ControladorCandidato():
   """
   constructor que permite llevar a cabo la creacion de instancias del controlador.
   """
   def __init__(self) -> object:
       self.repositorioCandidato = RepositorioCandidato()
       print("Creando Controlador Candidato")


   def index(self):
       print("Listar todos los Candidatos")
       return self.repositorioCandidato.findAll()

   def create(self, elCandidato):
       print("Crear un Candidato")
       nuevoCandidato = Candidato(elCandidato)
       return self.repositorioEstudiante.save(nuevoCandidato)

   def show(self, id):
       print("Mostrando un Candidato con id ", id)
       elCandidato = Candidato(self.repositorioCandidato.findById(id))
       return elCandidato.__dict__

   def update(self, id, elCandidato):
       print("Actualizando Candidato con id ", id)
       CandidatoActual = Candidato(self.repositorioCandidato.findById(id))
       CandidatoActual.cedula = elCandidato["cedula"]
       CandidatoActual.no_resolucion = elCandidato["no_resolucion"]
       CandidatoActual.nombre = elCandidato["nombre"]
       CandidatoActual.apellido = elCandidato["apellido"]
       return self.repositorioCandidato.save(CandidatoActual)

   def delete(self, id):
       print("Elimiando Candidato con id ", id)
       return self.repositorioCandidato.delete(id)
