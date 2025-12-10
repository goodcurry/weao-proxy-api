# weao proxy api (python version)

### updates

- back up (12/10/25)
- added /api/versions/past (12/10/25)

### usage

to use the proxy server, send your requests to these endpoints:

- fetch current roblox versions: `http://farts.fadedis.xyz:25551/api/versions/current`
- fetch future roblox versions: `http://farts.fadedis.xyz:25551/api/versions/future`
- fetch all exploit statuses: `http://farts.fadedis.xyz:25551/api/status/exploits`
- fetch a specific exploit status: `http://farts.fadedis.xyz:25551/api/status/exploits/[exploit]` (replace `[exploit]` with the name of the executor. example: `solara`)

these endpoints will accept your requests to the [weao.xyz](https://weao.xyz/) api with the correct user-agent headers and return the response.
weao documentation: [WEAO Documentation](https://docs.weao.xyz/)
