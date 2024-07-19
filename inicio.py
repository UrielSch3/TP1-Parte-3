import pandas as pd

customers_df = pd.read_csv('ecommerce_customers_dataset.csv')
orders_df = pd.read_csv('ecommerce_orders_dataset.csv')
order_items_df = pd.read_csv('ecommerce_order_items_dataset.csv')
products_df = pd.read_csv('ecommerce_products_dataset.csv')
order_payments_df = pd.read_csv('ecommerce_order_payments_dataset.csv')

customers_df.set_index('customer_id', inplace=True)
orders_df.set_index('order_id', inplace=True)
order_items_df.set_index('order_item_id', inplace=True)
products_df.set_index('product_id', inplace=True)
order_payments_df.set_index('order_id', inplace=True)

total_unique_customers = customers_df.index.nunique()
print(f"Total de clientes únicos: {total_unique_customers}")

avg_payment_per_order = order_payments_df.groupby('order_id')['payment_value'].mean().mean()
print(f"Promedio de valor de pago por pedido: {avg_payment_per_order:.2f}")

# Supongo que hay una columna `product_category` en `products_df`
merged_items_products = order_items_df.merge(products_df, on='product_id')
most_sold_category = merged_items_products['product_category_name'].value_counts().idxmax()
print(f"Categoría de producto más vendida: {most_sold_category}")

total_orders = orders_df.index.nunique()
print(f"Número total de pedidos realizados: {total_orders}")
