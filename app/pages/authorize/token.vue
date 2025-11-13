<template>
    data = {{ data }}
</template>

<script setup>

const data = useRoute().query.token
</script>