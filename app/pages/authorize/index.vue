<template>
    if you see thus page please wait while you are being redirected
    <br>
    data = {{ data }}
</template>

<script setup>

const route = useRoute()
const router = useRouter()

const user_info = inject("user_info")

let data = ref({})

const uris = {
    dev: "http://127.0.0.1:5000",
    prod: "https://api.nhdiscord.com"
}

<<<<<<< HEAD
const current_uri = uris.dev
=======
const current_uri = uris.prod
>>>>>>> eddf04216a9f785a75ea9d080a04e7900ab38c32

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
            return
        }
        user_info.value = data.value.user_info

        localStorage.setItem("token", data.value.token)
        localStorage.setItem("avatar", data.value.user_info.avatar)
        localStorage.setItem("user_id", data.value.user_info.id)
<<<<<<< HEAD

=======
        
>>>>>>> eddf04216a9f785a75ea9d080a04e7900ab38c32
        router.push('/')
    }
})



</script>