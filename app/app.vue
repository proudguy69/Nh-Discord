<template>
  <UApp>
    <UHeader title="NH Discord">

      <template #right>
        <UNavigationMenu :items="items"/>
        <UButton v-if="!user_info.id" icon="logos:discord-icon" variant="subtle" color="secondary" :to="authentication_uri">Login</UButton>
        <UButton v-if="user_info.id" variant="subtle" color="secondary" :avatar="{src: `https://cdn.discordapp.com/avatars/${user_info.id}/${user_info.avatar}.png`}" @click="logout">Account</UButton>
        <UColorModeButton />
      </template>
      

    </UHeader>
    <NuxtPage />
  </UApp>
</template>

<script setup>

const uris = {
  dev: "https://discord.com/oauth2/authorize?client_id=1304965391507914782&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A3000%2Fauthorize&scope=identify+guilds.join+email",
  prod: "https://discord.com/oauth2/authorize?client_id=1304965391507914782&response_type=code&redirect_uri=https%3A%2F%2Fnhdiscord.com%2Fauthorize&scope=identify+guilds.join+email"
}
// dont forget to set it in authorize/index.vue
// dont forget to set it in main.py aswell
const authentication_uri = uris.dev
provide("authentication_uri", authentication_uri)
const user_info = ref({
})

provide("user_info", user_info)

function logout() {
  user_info.value = {}
  localStorage.clear()
}

const items = [
  {
    label: "about",
    to: '/about'
  }
]

onMounted(async () => {
  // verify user is authenticated
  const avatar = localStorage.getItem("avatar")
  if (avatar) {
    user_info.value.avatar = avatar
    user_info.value.id = localStorage.getItem("user_id")
    return
  }
  // get from token if token is set
  const token = localStorage.getItem("token")
  // make api call
  
})


</script>