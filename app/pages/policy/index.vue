<template>
    <UPageHero
    title="Policy Pages"
    description="Please review our policies below"
    :links="links"
    />
</template>

<script setup>

const links = ref([
    {
        label: "Terms of Service",
        to: "/policy/terms",
        color: "secondary"
    },
    {
        label: "Privacy Policy",
        to: "/policy/privacy",
        color: "secondary"
    },
])

</script>