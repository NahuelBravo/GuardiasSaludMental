Problema cuyo objetivo consiste en asignar 60 guardias de manera equitativa entre 10 agentes segun su disponibilidad.

Consideraciones:

- Las guardias cubren 30 días del mes a partir de una fecha ingresada por el usuario.
- Por fecha del mes existe una guardia turno DIA y una guardia turno NOCHE.
- Hay agentes que hacen guardias de 24 hs, empezando en el turno DIA y terminando en el turno NOCHE de la misma fecha.
- La distribución de guardias debe corresponderse con la disponibilidad de los agentes y atender las siguientes condiciones:
  * No se debe superar un máximo de 3 guardias de findeSemana por Agente por mes.
  * Cada agente tiene un crédito que se corresponde con la cantidad de guardias que quiere hacer. Las guardias asignadas a ese agente no puede superar ese límite.
  * No se debe asignar la guardia si el agente está de licencia ese día.
  * Las guardias deben asignarse al mismo agente con al menos dos días de separación entre una y otra.



Idea Original - Tomás Manoukian
LINK: https://github.com/tromenArarat/ITChangas/tree/main/GuardiasSaludMental

