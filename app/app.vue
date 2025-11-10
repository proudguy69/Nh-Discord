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

const authentication_uri = "https://discord.com/oauth2/authorize?client_id=1304965391507914782&response_type=code&redirect_uri=http%3A%2F%2Fapi.nhdiscord.com%2Fauthorize&scope=identify+email+guilds.join"

const items = [
  {
    label: "Login",
    icon: "logos:discord-icon",
    to: authentication_uri
  }
]

fetch("/api/get/user")

</script>