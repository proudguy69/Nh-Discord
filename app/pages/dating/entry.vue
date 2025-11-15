<template>
    <!--If the user is NOT logged in-->
    <UBanner
    title="This page is still under development, please check back again later"
    icon="i-lucide-info"
    />

    <UPage v-if="!user_info.id">
        <UPageHero
        title="Welcome to Live free or love!"
        description="Please log in with discord to continue"
        :links="links"
        />

    </UPage>


    <UPage v-if="user_info.id">
        
        <UPageHero
        :title="title"
        :description="description"
        orientation="horizontal"
        headline="Experimental"
        >
            <video src="~/assets/videos/sample_video.mp4" controls>
                <source src="~/assets/videos/sample_video.mp4" type="video/mp4">
            </video>

            
        </UPageHero>

        <UPageSection
        title="Entry Form"
        description="Fill out the form below to enter the server"
        headline="Start here"
        >
            <UEmpty
            title="Still under development"
            description="This section is still under development, please be paitent while we work on this"
            icon="i-lucide-file"
            variant="subtle"
            />
        </UPageSection>
    </UPage>
    
    
</template>

<script setup>

const title = "New Hampshire's first real dating community. Built for authenticity, not algorithms."
const description = "Join early, help shape it, and be part of something that actually lasts."

const authentication_uri = inject('authentication_uri')
const user_info = inject("user_info")

const links = ref([
    {
        label: "Login with discord",
        icon: "logos:discord-icon",
        variant: "subtle",
        color: "secondary",
        to: authentication_uri

    }
])

</script>