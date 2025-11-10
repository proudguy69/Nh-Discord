<template>
  <UApp>
    <UHeader title="NH Discord">

      <template #right>
        <UNavigationMenu :items="items"/>
        <UColorModeButton />
      </template>
      

    </UHeader>
    <NuxtPage />
  </UApp>
</template>

<script setup>

const authentication_uri = "https://discord.com/oauth2/authorize?client_id=1304965391507914782&response_type=code&redirect_uri=https%3A%2F%2Fapi.nhdiscord.com%2Fauthorize&scope=identify+guilds.join+email"


const items = [
  {
    label: "Login",
    icon: "logos:discord-icon",
    to: authentication_uri
  }
]

fetch("https://api.nhdiscord.com/get/user")



</script>