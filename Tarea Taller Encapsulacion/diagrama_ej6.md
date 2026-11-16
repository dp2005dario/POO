# Ejercicio 6 · Diagrama de referencias

## 1. Justo antes de `del libro`
```mermaid
flowchart LR
    libro --> L["Libro L14 Atlas"]
    mostrador --> L
    inv["inventario[0]"] --> L
```

## 2. Justo después de `del libro`
```mermaid
flowchart LR
    mostrador --> L["Libro L14 Atlas"]
    inv["inventario[0]"] --> L
```

## 3. Después de `del mostrador`
```mermaid
flowchart LR
    inv["inventario[0]"] --> L["Libro L14 Atlas"]
```

## 4. Después de `inventario.clear()`
```mermaid
flowchart LR
    L["Libro L14 Atlas (sin referencias)"]
```

Solo hay un objeto. Los nombres son flechas hacia él: `del` quita una flecha,
no borra el objeto. Cuando no queda ninguna flecha, Python puede liberarlo.

#PARA PROBAR COMO SE VE VISULAMENTE USA CRTL + SHIFT + V