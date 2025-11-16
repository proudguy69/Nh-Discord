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

    <!--If user IS logged in-->
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
            v-if="false"
            title="Still under development"
            description="This section is still under development, please be paitent while we work on this"
            icon="i-lucide-file"
            variant="subtle"
            />
            <UPageCard
            v-if="true"
            variant="subtle"
            >
            <UForm
            class="flex flex-col gap-1"
            @submit="submit"
            :validate="validate"
            :state="form_state"
            >
                <UFormField label="Name" name="name" required>
                    <UFieldGroup orientation="vertical" class="w-full" >
                        <UInput placeholder="First" v-model="form_state.first"/>
                        <UInput placeholder="Last" v-model="form_state.last"/>
                    </UFieldGroup>
                </UFormField>

                <UFormField label="Date of birth" name="birth" class="w-full" required>
                    <UFieldGroup>
                        <UInput class="w-11" placeholder="mm" v-model="form_state.month"/>
                        <UInput class="w-11" placeholder="dd" v-model="form_state.day"/>
                        <UInput class="w-13" placeholder="yyyy" v-model="form_state.year"/>
                    </UFieldGroup>
                </UFormField>

                <UFormField label="Residential Address" name="address" class="w-full" required>
                    <UFieldGroup orientation="vertical">
                        <UInput placeholder="308 Negra Arroyo Lane" v-model="form_state.street"/>
                        <UInput placeholder="Albuquerque" v-model="form_state.city"/>
                        <UInput placeholder="NM" v-model="form_state.state"/>
                        <UInput placeholder="87104" v-model="form_state.zip"/>
                    </UFieldGroup>
                </UFormField>

                <UFormField
                label="Upload a selfie"
                help="This is to verify authenticity, you will see this selfie when you enter the server and verify your identiy with the staff"
                class="w-full"
                >
                    <UFileUpload variant="button" />
                </UFormField>

                <UFormField label="To continue you must agree to" name="policy">
                    <UCheckbox required v-model="form_state.terms">
                        <template #label>
                            <ULink
                            to="/policy/terms"
                            >
                            Terms of service
                        </ULink>
                        </template>
                    </UCheckbox>
                    <UCheckbox required v-model="form_state.privacy">
                        <template #label>
                            <ULink
                            to="/policy/privacy"
                            >
                            Privacy Policy
                        </ULink>
                        </template>
                    </UCheckbox>
                </UFormField>
                
                <UButton class="w-full text-center" icon="i-lucide-arrow-right" variant="solid" label="Join" type="submit" :loading="load_join"/>
                
            </UForm>

            </UPageCard>
        </UPageSection>
    </UPage>
    
    
</template>

<script setup>

const title = "New Hampshire's first real dating community. Built for authenticity, not algorithms."
const description = "Join early, help shape it, and be part of something that actually lasts."

const authentication_uri = inject('authentication_uri')
const current_uri = inject('api_uri')

const user_info = inject("user_info")
const load_join = ref(false)

const links = ref([
    {
        label: "Login with discord",
        icon: "logos:discord-icon",
        variant: "subtle",
        color: "secondary",
        to: authentication_uri

    }
])

const toast = useToast()

const form_state = reactive({
    first: undefined,
    last: undefined,
    month: undefined,
    day: undefined,
    year: undefined,
    street: undefined,
    city: undefined,
    state: undefined,
    zip: undefined,
    terms: undefined,
    privacy: undefined
})

function validate(state) {
    const errors = []
    if (!form_state.first || !form_state.last) {
        errors.push({name: 'name', message: 'First and Last name required'})
    }
    // Month Validation
    if (!form_state.month) {
        errors.push({name: 'birth', message: 'Month is a required feild'})
    } else if (form_state.month.length != 2) {
        errors.push({name: 'birth', message: 'Month must be 2 digits'})
    } else if (!Number(form_state.month)) {
        errors.push({name: 'birth', message: 'Month must be a number'})
    } else if (Number(form_state.month) > 12 || Number(form_state.month) < 1) {
        errors.push({name: 'birth', message: 'Month must be between 1-12'})
    }
    // Day Validation
    if (!form_state.day) {
        errors.push({name: 'birth', message: 'Day is a required feild'})
    } else if (form_state.day.length != 2) {
        errors.push({name: 'birth', message: 'Day must be 2 digits'})
    } else if (!Number(form_state.day)) {
        errors.push({name: 'birth', message: 'Day must be a number'})
    } else if (Number(form_state.day) > 31 || Number(form_state.day) < 1) {
        errors.push({name: 'birth', message: 'Day must be between 1-31'})
    }
    // Year Validation
    if (!form_state.year) {
        errors.push({name: 'birth', message: 'Year is a required feild'})
    } else if (form_state.year.length != 4) {
        errors.push({name: 'birth', message: 'Year must be 4 digits'})
    } else if (!Number(form_state.year)) {
        errors.push({name: 'birth', message: 'Year must be a number'})
    } else if (Number(form_state.year) > 2025 || Number(form_state.year) < 1925) {
        errors.push({name: 'birth', message: 'Year must be between 1925 -> 2025'})
    }


    if(!form_state.street | !form_state.city || !form_state.state || !form_state.zip) {
        errors.push({name: 'address', message: 'Please provide a full address (this will be verified with your ID upon entry)'})
    }

    return errors
}

async function submit() {
    load_join.value = true
    const response = await fetch(`${current_uri}/dating/entry/form`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(form_state)
    })
    const json_data = await response.json()
    if (json_data.success) {
        
        toast.add({
            title: 'Form submitted successfully!',
            description: "Your form was submitted, you will be added to the server automatically when it opens"
        })
    }
    load_join.value = false
}

</script>