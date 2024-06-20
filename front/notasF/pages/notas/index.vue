<script setup lang="ts">
import { BACKEND_URL_invoces } from "~/models/app";
import { type Ref, ref, computed } from 'vue';
import { type Invoice } from '~/models/invoice';
import { getItem } from "~/services/itens";

definePageMeta({
    middleware: 'auth'});
const code:Ref<string> = ref('');
const dataNota:Ref<string> = ref('');
const data = ref<{ results: Invoice[] }>({ results: [] });
const ProcurarNota = async () => {
    try {
        let url = `${BACKEND_URL_invoces}?code=${code.value}`;
        if(dataNota.value != ''){
            url += `&emissionDate_after=${dataNota.value}`;}
        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Token cf44981f5d7290d1207594282ee3655d5e6d7a94'},});
        if (!response.ok) {
            throw new Error('Erro ao buscar nota');}
        const resposta = await response.json();
        if (resposta.results) {
            data.value = resposta;
            console.log('Notas fiscais encontradas:', data.value.results[0]);
        } else {
            throw new Error('Nenhum resultado foi encontrado');}
    } catch (error) {
        console.error('Erro ao buscar a nota:', error);}};

const notas = computed(() => data.value.results);
console.log(notas);
</script>

<template>
    <main>
        <h1>Buscar Notas</h1>
        <section>
            <div>
                <FloatLabel>
                    <InputText v-model="code" />
                    <label>Número da nota</label>
                </FloatLabel>
                <br>
            </div>
            <div>
                <FloatLabel>
                    <InputText v-model="dataNota" />
                    <label>Data</label>
                </FloatLabel>
                <br>
            </div>
            <div>
                <Button @click="ProcurarNota()" label="Buscar"></Button>
            </div>
            <div v-if="notas.length > 0 && code !== '' && dataNota !== ''">
                <h3>Nota Encontrada:</h3>
                <span>Numero da nota: {{ notas[0].code }}</span>
                <br><br>
                <span>Data de emissão: {{ notas[0].emissionDate }}</span>
                <br><br>
                <span>Nome do cliente: {{ notas[0].customerName }}</span>
                <br><br>
                <span>CNPJ do cliente: {{ notas[0].customerCNPJ }}</span>
                <br><br>
                <span>Nome do vendedor: {{ notas[0].sellerName }}</span>
                <br><br>
                <span>CNPJ do vendedor: {{ notas[0].sellerCNPJ }}</span>
                <br><br>
                <span>Valor da nota: {{ notas[0].totalValue }}</span>
                <br><br>
                <div v-if="notas.length > 0 && code !== '' && dataNota !== ''" class="botao-item">
                    <NuxtLink :to="`/notas/${notas[0].id}`">
                        <Button label="itens da nota" id="botão"></Button>
                    </NuxtLink>
                </div>
            </div>
        </section>
    </main>
</template>

<style scoped lang="scss">
</style>
