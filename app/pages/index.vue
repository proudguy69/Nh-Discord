<template>
    <UPageHero title="Live Free New Hampshire" description="Join a welcoming New Hampshire community where locals meet new friends, share events, and talk about life in the Granite State. Whether you’re here for gaming, dating, or casual chat, there’s always someone nearby to connect with" />
    <UPageSection title="Our Servers">
        <UPricingPlans :plans="servers"/>
    </UPageSection>
    
</template>

<script setup>
    
const servers = ref([
    {
        title: "Live Free New Hampshire",
        description: "The main general community for all New Hampshire related things",
        features: [
            "600+ Members",
            "Active community",
            "Weekly events",
            "News"
        ],
        button: {
            label: "Join",
            to: "https://discord.gg/PFM7gQJa2H"
        },
    },
    {
        title: "Live Free And Love",
        description: "Experimental dating community free for all",
        features: [
            "Enforced 1:1 Male to female ratio",
            "Delgated categories for differing sexualities",
            "Id verified users",
            "Enforced activity"
        ],
        button: {
            label: "Join",
            to: "https://discord.gg/tM6xn3XWkN"
        }
    }
])

</script>