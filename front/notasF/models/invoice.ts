export type Invoice = {
    id: number;
    code: string;
    customerName: string;
    customerCNPJ: string;
    sellerName: string;
    sellerCNPJ: string;
    totalValue: number;
    emissionDate: string;
    uploadDate: string;}