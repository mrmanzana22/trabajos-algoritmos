# Contexto del Curso - Algoritmos II

## Información General
- **Universidad:** Universidad de la Costa (CUC)
- **Materia:** Algoritmos II
- **Profesor:** Ing. Oscar Javier Ramírez Vargas
- **Carrera:** Ingeniería de Sistemas
- **Estudiante:** Sebastian Lizarazo
- **Fecha inicio:** Sábado 21 de febrero de 2026

---

## Unidad 1: Estructuras Dinámicas de Datos

### Objetivo
Que el estudiante comprenda conceptualmente qué son las estructuras dinámicas de datos y modele, implemente y manipule una lista enlazada simple, entendiendo por qué y cuándo se usa frente a estructuras estáticas.

### Conceptos Clave

#### Estructuras Estáticas vs Dinámicas
| Criterio | Estáticas | Dinámicas |
|----------|-----------|------------|
| Tamaño | Fijo, definido antes de ejecución | Variable, cambia en ejecución |
| Memoria | Se asigna una vez, continua | Se asigna dinámicamente, no continua |
| Flexibilidad | Baja | Alta |
| Inserción/Eliminación | Costosa (mover elementos) | Eficiente (ajustar enlaces) |
| Acceso | Directo O(1) | Secuencial O(n) |
| Ejemplos | Arrays, matrices | Listas enlazadas, pilas, colas, árboles |

#### Ejemplo cotidiano
- **Estática:** Casilleros numerados en un colegio (cantidad fija)
- **Dinámica:** Fila de personas que puede crecer o disminuir

---

## Listas Enlazadas Simples

### Estructura
Cada nodo contiene:
- **dato:** valor almacenado
- **siguiente:** puntero al siguiente nodo (o NULL si es el último)

### Terminología
- **Cabeza/Cabecera:** primer nodo de la lista
- **Último nodo:** tiene puntero NULL (fin de lista)

### Representación Visual
```
cabeza -> [Dato A | *B] -> [Dato B | *C] -> [Dato C | NULL]
```

---

## Pseudocódigo del Profesor

### 1. Definición del Nodo
```
Estructura Nodo
    dato
    siguiente
FinEstructura
```

### 2. Definición de la Lista
```
Estructura ListaEnlazada
    cabeza
FinEstructura
```

### 3. Crear un Nodo
```
Función crearNodo(valor)
    nuevoNodo ← Nuevo Nodo
    nuevoNodo.dato ← valor
    nuevoNodo.siguiente ← NULO
    Retornar nuevoNodo
FinFunción
```

### 4. Verificar si está vacía
```
Función estaVacia(lista)
    Si lista.cabeza = NULO Entonces
        Retornar VERDADERO
    Sino
        Retornar FALSO
FinFunción
```

### 5. Insertar al inicio
```
Procedimiento insertarInicio(lista, valor)
    nuevo ← crearNodo(valor)
    nuevo.siguiente ← lista.cabeza
    lista.cabeza ← nuevo
FinProcedimiento
```

### 6. Insertar al final
```
Procedimiento insertarFinal(lista, valor)
    nuevo ← crearNodo(valor)
    Si estaVacia(lista) Entonces
        lista.cabeza ← nuevo
    Sino
        actual ← lista.cabeza
        Mientras actual.siguiente ≠ NULO Hacer
            actual ← actual.siguiente
        FinMientras
        actual.siguiente ← nuevo
    FinSi
FinProcedimiento
```

### 7. Recorrer y mostrar
```
Procedimiento mostrarLista(lista)
    actual ← lista.cabeza
    Mientras actual ≠ NULO Hacer
        Escribir actual.dato
        actual ← actual.siguiente
    FinMientras
FinProcedimiento
```

### 8. Buscar elemento
```
Función buscar(lista, valor)
    actual ← lista.cabeza
    posición ← 0
    Mientras actual ≠ NULO Hacer
        Si actual.dato = valor Entonces
            Retornar posición
        FinSi
        actual ← actual.siguiente
        posición ← posición + 1
    FinMientras
    Retornar -1
FinFunción
```

### 9. Eliminar elemento
```
Procedimiento eliminar(lista, valor)
    Si estaVacia(lista) Entonces
        Escribir "Lista vacía"
        Retornar
    FinSi
    
    Si lista.cabeza.dato = valor Entonces
        lista.cabeza ← lista.cabeza.siguiente
        Retornar
    FinSi
    
    anterior ← lista.cabeza
    actual ← lista.cabeza.siguiente
    
    Mientras actual ≠ NULO Hacer
        Si actual.dato = valor Entonces
            anterior.siguiente ← actual.siguiente
            Retornar
        FinSi
        anterior ← actual
        actual ← actual.siguiente
    FinMientras
    
    Escribir "Elemento no encontrado"
FinProcedimiento
```

---

## Trabajo Práctico: Sistema de Turnos

### Enunciado
**Gestión de turnos en una ventanilla de atención al cliente**

En una empresa de servicios públicos existe una ventanilla de atención al cliente donde las personas llegan durante el día para realizar distintos trámites (pagos, reclamos, solicitudes, etc.).

### Requisitos del Sistema
1. **Agregar cliente al final de la fila** (cada cliente se identifica por turno + nombre)
2. **Eliminar cliente de la fila** (cuando se retira voluntariamente) - por número de turno
3. **Buscar cliente en la fila** - por número de turno
4. **Mostrar fila completa** en orden de llegada
5. **Menú interactivo** para seleccionar operaciones

### Justificación de Lista Enlazada
Se usa lista enlazada simple porque:
- No se conoce previamente cuántos clientes llegarán
- La fila puede crecer o disminuir dinámicamente
- Inserción al final y eliminación son eficientes

### Solución Implementada
- Cada nodo tiene: `turno` (único, autoincremental) + `nombre` + `siguiente`
- Operaciones por número de turno para evitar problemas con nombres duplicados
- El contador de turnos nunca se reinicia (como en un banco real)

---

## Tipos de Listas Enlazadas

| Tipo | Descripción | Ejemplo |
|------|-------------|----------|
| Simple | Cada nodo apunta al siguiente | Fila de banco |
| Doblemente enlazada | Cada nodo apunta al siguiente y anterior | Lista de reproducción |
| Circular | El último apunta al primero | Turnos rotativos |

---

## Características de Estructuras Dinámicas
1. **Tamaño variable:** crecen/reducen según necesidad
2. **Asignación dinámica de memoria:** en tiempo de ejecución
3. **Flexibilidad:** se adaptan a cambios en cantidad de datos
4. **Mayor complejidad:** requieren manejo de punteros/referencias

---

## Notas Importantes
- El profesor usa pseudocódigo con sintaxis específica (FinSi, FinMientras, etc.)
- Los trabajos deben usar lista enlazada simple (no listas de Python)
- Implementar clases separadas para Nodo y Lista
- Incluir menú interactivo con while
- Código debe ser simple y explicable en clase
