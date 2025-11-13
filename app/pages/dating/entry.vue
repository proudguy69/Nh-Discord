<template>
    <UPageHero v-if="!user_info.id" title="Welcome to Live free or love!" description="Please log in with discord to continue">
        <UButton icon="logos:discord-icon" variant="subtle" color="secondary" :to="authentication_uri">Login</UButton>
    </UPageHero>
    <UPageHero
    v-if="user_info.id"
    :title="title"
    :description="description"
    orientation="horizontal"
    headline="Experimental"
    >
        <video src="~/assets/videos/sample_video.mp4" controls>
            <source src="~/assets/videos/sample_video.mp4" type="video/mp4">
        </video>

        <h2>
            this is still being worked on, join the main server and contact paul for updates
        </h2>
    </UPageHero>
    
</template>

<script setup>

const title = "New Hampshire's first real dating community. Built for authenticity, not algorithms."
const description = "Join early, help shape it, and be part of something that actually lasts."

const authentication_uri = inject('authentication_uri')
const user_info = inject("user_info")

</script>