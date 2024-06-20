import { type InvoiceItem } from "~/models/invoiceItens";

export type CarrinhoItem = {
    item: InvoiceItem;
    quantidade: number;}
export type Carrinho = {
    itens: Array<CarrinhoItem>;}
export const carrinho = defineStore('carrinhoStore', {
    state: (): Carrinho => ({
        itens: []}),
    actions: {
      adicionarNoCarrinho(novoItem: InvoiceItem){
            const ItemJaExiste = this.getItemDoCarrinho(novoItem);
            if(ItemJaExiste){
                ItemJaExiste.quantidade += 1;
                this.itens = [
                    ...this.itens.filter(produto=>produto.item.productFK.id !== ItemJaExiste.item.productFK.id),
                    ItemJaExiste];}
            else{
                this.itens.push({
                    quantidade: 1,
                    item: novoItem});}},
      removerDoCarrinho(carrinhoItem: CarrinhoItem){
        const posicaoNoCarrinho = this.getItemDoCarrinhoIndex(carrinhoItem.item);
        this.itens.splice(posicaoNoCarrinho,1);
        if(carrinhoItem.quantidade){
            this.itens = [
                ...this.itens,
                carrinhoItem];}},
      esvaziarCarrinho(){
        this.itens = [];}},
    getters: {
        estaNoCarrinho: (carrinho:Carrinho) => (itemParaEncontrar: InvoiceItem): boolean =>{
            return carrinho.itens.findIndex(produto=>produto.item.productFK.id === itemParaEncontrar.productFK.id) !== -1;},
        getItemDoCarrinho: (carrinho:Carrinho) => (itemParaEncontrar: InvoiceItem)=>{
            return carrinho.itens.find(produto=>produto.item.productFK.id === itemParaEncontrar.productFK.id);},
        getItemDoCarrinhoIndex: (carrinho:Carrinho) => (itemParaEncontrar: InvoiceItem)=>{
            return carrinho.itens.findIndex(produto=>produto.item.productFK.id === itemParaEncontrar.productFK.id);},
        getCarrinho: (carrinho: Carrinho) => () : Array<CarrinhoItem> => {
            return carrinho.itens;},
        getValorTotalDoCarrinho: (carrinho: Carrinho) => () : Number => {
            let soma = 0;
            carrinho.itens.forEach(produto=>{
                soma += (produto.item.price * produto.quantidade)})
            return soma;},
        getPesoTotalDoCarrinho: (carrinho: Carrinho) => () : Number => {
            let peso = 0;
            carrinho.itens.forEach(produto=>{
                peso += (produto.item.productFK.weight * produto.quantidade)})
            return peso;}}})