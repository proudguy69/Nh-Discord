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

onMounted(async () => {
    const code = route.query.code
    if (!code) {
        router.push('/')
    } else {
        const response = await fetch(`https://api.nhdiscord.com/authorize?code=${code}`)
        data.value = await response.json()
        
        console.log(user_info)
        user_info.value = data.value.data
        router.push('/')
    }
})



</script>