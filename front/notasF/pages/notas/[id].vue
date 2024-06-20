<script setup lang="ts">
import { BACKEND_URL } from "~/models/app";
import { ref, computed } from "vue";
import { type InvoiceItem } from "~/models/invoiceItens";
const route = useRoute();
import { carrinho } from "~/stores/carrinho";
const { adicionarNoCarrinho, getCarrinho, estaNoCarrinho } = carrinho();
definePageMeta({
    middleware:'auth'})
const data = ref<{ results: InvoiceItem[] }>({ results: [] });
const ProcurarItem = async () => {
    try {
        const url = `${BACKEND_URL}/invoice-item?invoiceFK=${route.params.id}`;
        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },});
        if (!response.ok) {
            throw new Error('Erro ao buscar');}
        const resposta = await response.json();
        if (resposta.results) {
            data.value = resposta;
            console.log('item encontrado:', data.value.results);
        } else {
            throw new Error('Nenhum resultado encontrado');}
    } catch (error) {
        console.error('Erro ao buscar o item:', error);}};

const itens = computed(() => data.value.results);
const emit = defineEmits(['eventoAdicionado']); 
const adicionarItem = (item: InvoiceItem) => {
  adicionarNoCarrinho(item);
  emit('eventoAdicionado');
  console.log("CARRINHO ATUAL: ", getCarrinho());}
const produtoNoCarrinho = (item: InvoiceItem) => {
    return estaNoCarrinho(item);};
ProcurarItem();
</script>

<template>
    <main >
    <h1>Itens da Nota</h1>
    <div >
      <NuxtLink to="/carrinho">
        <Button icon="pi pi-shopping-cart" label="Carrinho"/>
      </NuxtLink> 
    </div>
    <div v-if="itens.length > 0">
      <div v-for="(item,index) in itens" :key="index">
        <section class="item">
          <div >      
            <Checkbox :modelValue="produtoNoCarrinho(item)" :binary="true" :readonly="true"/>
          </div>
          <div >
            <img :src="item.productFK.image" />
          </div>
          <div>
            <h4 >{{ item.productFK.name }}</h4>
          </div>
          <div class="ml-2">
            <span>Código de Barras: {{ item.productFK.barCode}} </span>
          <div>
          <div>
            <label>Peso: </label>
            <span>{{ item.productFK.weight}} kgs </span>
          </div>
            <label>Descrição: </label>
            <span>{{ item.productFK.description}} </span>
          </div>
          </div>
            <Button label="Adicionar Item ao Carrinho" @click="adicionarItem(item)"/>
        </section> <br>
      </div>  
    </div>
    </main>
</template>

<style scoped lang="scss">
</style>