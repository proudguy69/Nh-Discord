<template>
    <UPageHero title="You are being redirected" description="Do not leave this page, let it leave for you"/>
</template>

<script setup>

const route = useRoute()
const router = useRouter()

const user_info = inject("user_info")

let data = ref({})

const current_uri = inject('api_uri')

onMounted(async () => {
    const code = route.query.code
    if (!code) {
        router.push('/')
    } else {
        const response = await fetch(`${current_uri}/authorize?code=${code}`, {
            method: "POST",
            headers: {"Content-Type": "application/json"}
        })
        data.value = await response.json()
        if (!data.value.success) {
            console.log("Failed!")
            router.push('/')
            return
        }
        user_info.value = data.value.user_info

        localStorage.setItem("token", data.value.token)
        localStorage.setItem("avatar", data.value.user_info.avatar)
        localStorage.setItem("user_id", data.value.user_info.id)
        router.push('/')
    }
})



</script>