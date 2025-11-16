<template>
    <UPageSection title="Terms of service">
        <UPageCard variant="subtle">
            <ContentRenderer :value="policy"/>
        </UPageCard>
    </UPageSection>
</template>

<script setup>
const { data: policy } = await useAsyncData(() => queryCollection('content').path('/terms').first())
</script>