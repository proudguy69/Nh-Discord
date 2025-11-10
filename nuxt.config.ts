// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  modules: ['@nuxt/ui', '@nuxtjs/robots', '@nuxtjs/sitemap'],
  css: ['~/assets/css/main.css'],
  app: {
    head: {
      title: 'NH Discord / New Hampshire Dating & Local Community',
      meta: [
        { name: 'description', content: 'Join NH Discord a local New Hampshire dating and social community where locals meet naturally. Free and real connections.' },
        { name: 'keywords', content: 'NH Discord, New Hampshire Dating, Live Free and Love, NH Community, Local Dating Discord' },
        { property: 'og:title', content: 'NH Discord Server' },
        { property: 'og:description', content: 'Safe space and communities for the likes of all people to join and interact with' },
        { property: 'og:type', content: 'website' },
        { property: 'og:url', content: 'https://nhdiscord.com' },
        { property: 'og:image', content: '' }
      ],
    }
  },
  site: {
    url: "https://nhdiscord.com",
    name: "New Hampshire Discord"
  },
  nitro: {
    devProxy: {
      '/api/': "https://api.nhdiscord.com"
    }
  }
})