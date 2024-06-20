import type { Invoice } from "./invoice";
import type { Product } from "./product";

export type InvoiceItem = {
    id: number;
    productFK: Product;
    invoiceFK: Invoice;
    price: number;
    quantity: number;}