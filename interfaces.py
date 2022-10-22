from abc import ABC, abstractmethod

class IUsuario(ABC):

    @abstractmethod
    def crear_usuario():
        pass

    @abstractmethod
    def iniciar_sesion():
        pass

    @abstractmethod
    def mostrar_datos(self):
        pass

    @abstractmethod
    def actualizar_datos_usuario(self):
        pass

    @abstractmethod
    def cerrar_sesion(self):
        pass



class IAplicacion(ABC):

    @abstractmethod
    def hacer_transferencia(self):
        pass

    @abstractmethod
    def cargar_dinero(self):
        pass

    @abstractmethod
    def pagar(self):
        pass
