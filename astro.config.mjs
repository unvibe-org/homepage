import { defineConfig } from "astro/config";

export default defineConfig({
    site: "https://unvibe.org",
    output: "static",
    trailingSlash: "always",
    build: {
        format: "directory",
    },
});
