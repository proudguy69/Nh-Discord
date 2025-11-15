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
<<<<<<< HEAD
            v-if="false"
=======
>>>>>>> eddf04216a9f785a75ea9d080a04e7900ab38c32
            title="Still under development"
            description="This section is still under development, please be paitent while we work on this"
            icon="i-lucide-file"
            variant="subtle"
            />
<<<<<<< HEAD
            <UPageCard
            v-if="true"
            variant="subtle"
            >
            <UForm class="flex flex-col gap-1" @submit="submit">
                <UFormField label="Name">
                    <UFieldGroup orientation="vertical" class="w-full" >
                        <UInput placeholder="First"/>
                        <UInput placeholder="Last"/>
                    </UFieldGroup>
                </UFormField>

                <UFormField label="Date of birth" class="w-full">
                    <UFieldGroup>
                        <UInput class="w-11" placeholder="mm"/>
                        <UInput class="w-11" placeholder="dd"/>
                        <UInput class="w-13" placeholder="yyyy"/>
                    </UFieldGroup>
                </UFormField>

                <UFormField label="Residential Address" class="w-full">
                    <UFieldGroup orientation="vertical">
                        <UInput placeholder="308 Negra Arroyo Lane" />
                        <UInput placeholder="Albuquerque"/>
                        <UInput placeholder="NM"/>
                        <UInput placeholder="87104"/>
                    </UFieldGroup>
                </UFormField>

                <UFormField label="Upload a selfie" help="This is to verify authenticity, you will see this selfie when you enter the server and verify your identiy with the staff" class="w-full">
                    <UFileUpload variant="button" />
                </UFormField>
                
                <UButton class="w-full text-center" icon="i-lucide-arrow-right" variant="solid" label="Join" type="submit" :loading="load_join"/>
                
            </UForm>

            </UPageCard>
=======
>>>>>>> eddf04216a9f785a75ea9d080a04e7900ab38c32
        </UPageSection>
    </UPage>
    
    
</template>

<script setup>

const title = "New Hampshire's first real dating community. Built for authenticity, not algorithms."
const description = "Join early, help shape it, and be part of something that actually lasts."

const authentication_uri = inject('authentication_uri')
const user_info = inject("user_info")

<<<<<<< HEAD
const load_join = ref(false)

=======
>>>>>>> eddf04216a9f785a75ea9d080a04e7900ab38c32
const links = ref([
    {
        label: "Login with discord",
        icon: "logos:discord-icon",
        variant: "subtle",
        color: "secondary",
        to: authentication_uri

    }
])

<<<<<<< HEAD
function submit() {
    load_join.value = true
}

=======
>>>>>>> eddf04216a9f785a75ea9d080a04e7900ab38c32
</script>