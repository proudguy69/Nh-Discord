<template>
    <UPageSection title="Privacy Policy">
        <UPageCard variant="subtle">
            <ContentRenderer :value="policy"/>
        </UPageCard>
    </UPageSection>
</template>

<script setup>
const { data: policy } = await useAsyncData(() => queryCollection('content').path('/privacy').first())
</script>