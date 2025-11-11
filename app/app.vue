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

const authentication_uri = uris.prod
const user_info = ref({})

provide("user_info", user_info)

function logout() {
  user_info.value = {}
}

const items = [
  {
    label: "about",
    to: '/about'
  }
]

fetch("/api/get/user")

</script>