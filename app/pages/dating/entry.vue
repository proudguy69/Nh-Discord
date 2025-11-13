<template>
    <UPageHero v-if="!user_info.id" title="Welcome to Live free or love!" description="Please log in with discord to continue">
        <UButton icon="logos:discord-icon" variant="subtle" color="secondary" :to="authentication_uri">Login</UButton>
    </UPageHero>
    <UPageHero v-if="user_info.id" title="Welcome to Live free or love!" description="Please watch the video">
        idk what goes here yet
    </UPageHero>
    this is still being worked on, join the main server and contact paul for updates
</template>

<script setup>

const authentication_uri = inject('authentication_uri')
const user_info = inject("user_info")

</script>