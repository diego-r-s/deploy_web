<script setup lang="ts">
import { ref, computed, type Ref } from "vue";
import { carrinho, type CarrinhoItem } from "~/stores/carrinho";
const { getCarrinho, removerDoCarrinho, getValorTotalDoCarrinho, getPesoTotalDoCarrinho, esvaziarCarrinho } = carrinho();

definePageMeta({
  middleware: "auth",});
const itensNoCarrinho = computed<Array<CarrinhoItem>>(() => getCarrinho());
const valorTotal = computed(() => getValorTotalDoCarrinho().toFixed(2));
const pesoTotal = computed(() => getPesoTotalDoCarrinho().toFixed(2));
const carregando = ref(false);
const salvo: Ref<boolean | null> = ref(null);
console.log("carrinho itens:", itensNoCarrinho);
const deletarDoCarrinho = async (itemParaRemover: CarrinhoItem) => {
  carregando.value = true;
  try {
    await removerDoCarrinho({
      item: itemParaRemover.item,
      quantidade: 0,
    });
  } catch (error) {
    console.error("falha", error);
  } finally {
    carregando.value = false;}};
const salvarPedido = async () => {
  carregando.value = true;
  try {
    salvo.value = true;
  } catch (error) {
    salvo.value = false;
    console.error("O pedido não pode ser salvo", error);
  } finally {
    carregando.value = false;}};
</script>

<template>
  <main class="container flex flex-column align-items-center">
    <h2 class="mt-4 mb-4">Seu Carrinho</h2>
    <div class="card flex justify-content-center" v-if="carregando">
      <ProgressSpinner />
    </div>
    <table v-if="!carregando">
      <thead>
        <tr class="text-center">
          <td>Item</td>
          <td>Produto</td>
          <td>Descrição</td>
          <td>Categoria</td>
          <td>Peso</td>
          <td>Preço Unitário</td>
          <td>Quantidade</td>
          <td>Peso Nota</td>
          <td>Subtotal</td>
          <td>Ações</td>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(itemCarrinho, index) in itensNoCarrinho" :key="index" class="text-center">
          <td>{{ index + 1 }}</td>
          <td><img class="fotoProduto" :src="itemCarrinho.item.productFK.image" alt="foto produto" /></td>
          <td>{{ itemCarrinho.item.productFK.name }}</td>
          <td>{{ itemCarrinho.item.productFK.categoryFK.name }}</td>
          <td>{{ itemCarrinho.item.productFK.weight }}</td>
          <td>R$ {{ itemCarrinho.item.price.toFixed(2) }}</td>
          <td>{{ itemCarrinho.quantidade }}</td>
          <td>{{ (itemCarrinho.quantidade * itemCarrinho.item.productFK.weight).toFixed(2) }}</td>
          <td>R$ {{ (itemCarrinho.quantidade * itemCarrinho.item.price).toFixed(2) }}</td>
          <td>
            <Button @click="deletarDoCarrinho(itemCarrinho)" label=""><i class="pi pi-trash"></i></Button>
          </td>
        </tr>
      </tbody>
      <tfoot>
        <tr class="text-center">
          <th colspan="6"></th>
          <th>Peso total:</th>
          <th>{{ pesoTotal }} kgs</th>
          <th>Valor Total:</th>
          <th>R$ {{ valorTotal }}</th>
        </tr>
      </tfoot>
    </table>
    <Button v-if="Number(pesoTotal) < 15" @click="salvarPedido" class="mt-2 botao bg-primary" label="Fechar pedido" />
    <h2 v-else>O peso maxímo é de 15kgs</h2>
    <Message v-if="salvo === true" severity="success">
      <p>Pedido realizado</p>
    </Message>
    <Message v-if="salvo === false" severity="error">
      <p>Não foi possível salvar o pedido</p>
    </Message>
  </main>
</template>

<style scoped lang="scss">
$largura-tabela: 90vw;
.container {
  margin: 0;
  width: 100vw;
  min-height: calc(100vh - 80px);
  background-image: url("background.jpg");
  background-repeat: repeat;
  background-size: cover;}

table {
  width: $largura-tabela;
  background-color: rgb(179, 179, 179);
  border-radius: 1rem;
  margin-bottom: 2rem;}

thead {
  font-weight: bold;
  tr {
    border-bottom: 2px solid rgb(8, 8, 8);}}

td {
  padding: 1rem;}

.fotoProduto {
  width: 50px;
  height: 50px;}

button {
  background-color: rgb(236, 234, 234);
  color: rgb(180, 5, 5);
  border: none;}

.valor-total {
  font-weight: bold;
  width: 900px;}

.botao {
  width: $largura-tabela;
  height: 40px;
  transition: transform 0.3s;
  &:hover {
    transform: scale(1.05);}}
</style>
