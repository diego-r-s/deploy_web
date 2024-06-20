export type ProductCategory = {
    id: number;
    name: string;}
export type Product = {
    id: number;
    name: string;
    categoryFK: ProductCategory;
    weight: number;
    description: string;
    creationDate: string;
    barCode: string;
    image: string;}