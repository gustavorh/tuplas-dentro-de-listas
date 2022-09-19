# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 09:42:36 2021

Nombre: Gustavo Reyes Herrera
RUT: oculto

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""


def producto_mas_caro(lista_productos):
    valor_mayor = 0
    nombre_mayor = ""
    for i in lista_productos:
        # _ Ignorará dicho valor, en este caso: codigo, cantidad y mostrará solo el nombre y precio de la tupla
        _, nombre, precio, _ = i

        if precio > valor_mayor:
            valor_mayor = precio
            nombre_mayor = nombre

        return nombre_mayor


def valor_total_bodega(lista_productos):
    total = 0
    for i in lista_productos:
        _, _, precio, cantidad = i
        total += precio * cantidad
    return total


def ingreso_total_por_ventas(lista_productos, lista_items):
    ingreso_total = 0
    for i in lista_items:
        _, codigo_i, cantidad = i

        for j in lista_productos:
            codigo_j, _, precio, _ = j

            if codigo_i == codigo_j:
                ingreso_total += cantidad * precio
    return ingreso_total


# Más eficiente con diccionarios
def ingreso_total_por_ventas2(lista_productos, lista_items):
    precios = {}
    for i in lista_productos:
        codigo, _, precio, _ = i
        precios[codigo] = precio
    total = 0
    for j in lista_items:
        _, codigo_producto, cantidad = j
        total += precios[codigo_producto] * cantidad
    return total


def productos_con_mas_ingresos(lista_productos, lista_items):
    codigos = {}
    for i in lista_items:
        _, codigo, cantidad = i
        if codigo not in codigos:
            codigos[codigo] = cantidad
        else:
            codigos[codigo] += cantidad
    mas_ingresos = 0
    nombre_prod_mas_ingreso = ""
    for j in lista_productos:
        cod_prod, nombre_prod, precio_prod, _ = j
        if cod_prod in codigos:
            total = precio_prod * codigos[cod_prod]
            if total > mas_ingresos:
                mas_ingresos = total
                nombre_prod_mas_ingreso = nombre_prod
    return nombre_prod_mas_ingreso


def cliente_que_mas_pago(lista_productos, lista_clientes, lista_ventas, lista_items):
    precios = {}
    for producto in lista_productos:
        codigo, _, precio, _ = producto
        precios[codigo] = precio
    costo_cada_venta = {}
    for venta in lista_ventas:
        total_venta = 0
        cod_venta, _, _ = venta
        for item in lista_items:
            codigo_venta, codigo_producto, cantidad = item
            if codigo_venta == cod_venta:
                total_venta += precios[codigo_producto] * cantidad
        costo_cada_venta[codigo_venta] = total_venta

    mejor_cliente = 0
    nombre_mejor_cliente = ""
    for cliente in lista_clientes:
        total_cliente = 0
        rut, nombre = cliente
        for venta in lista_ventas:
            cod_venta, _, rut_cliente = venta
            if rut == rut_cliente:
                total_cliente += costo_cada_venta[codigo_venta]
        if total_cliente > mejor_cliente:
            mejor_cliente = total_cliente
            nombre_mejor_cliente = nombre
    return nombre_mejor_cliente, mejor_cliente


productos = [  # Código, Nombre, Precio, Cantidad
    (41419, "Fideos", 450, 38),
    (70717, "Salsa de Tomate", 580, 40),
    (78714, "Jabón", 730, 108),
    (30877, "Desodorante", 2190, 17),
    (47470, "Yoghurt", 99, 832),
    (50809, "Palta", 500, 23),
    (65466, "Galletas", 235, 0),
    (33692, "Bebida", 650, 25)
]

clientes = [  # Rut, Nombre
    ("24355132-7", "Pedro Díaz"),
    ("12345341-0", "Elena Martinez"),
    ("7765196-8", "Daniela Pérez")
]

ventas = [  # Venta N°, (Fecha), Rut
    (1, (2021, 7, 12), "24355132-7"),
    (2, (2021, 7, 19), "12345341-0"),
    (3, (2021, 7, 30), "7765196-8"),
    (4, (2021, 8, 1), "24355132-7"),
    (5, (2021, 8, 13), "7765196-8"),
    (6, (2021, 9, 11), "12345341-0")]

items = [  # Venta N°, Código de Item, Cantidad
    (1, 78714, 3),
    (2, 41419, 4),
    (2, 33692, 2),
    (2, 47470, 6),
    (3, 30877, 1),
    (3, 41419, 1),
    (4, 50809, 2),
    (5, 41419, 2),
    (5, 47470, 10),
    (6, 41419, 2)]

mas_caro = producto_mas_caro(productos)
total_bodega = valor_total_bodega(productos)
ingreso_total_ventas = ingreso_total_por_ventas(productos, items)
productos_mas_ingresos = productos_con_mas_ingresos(productos, items)
mejor_cliente = cliente_que_mas_pago(productos, items, ventas, clientes)

print(f"El producto más caro es: {mas_caro}, el valor total de la bodega es: {total_bodega}, el ingreso total por ventas es: {ingreso_total_ventas}, el producto con más ingresos fue: {productos_mas_ingresos}")
print(f"El mejor cliente fue: {mejor_cliente}")
