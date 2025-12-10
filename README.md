# weao proxy api (python version)

### updates

- back up (12/10/25)

### usage

to use the proxy server, send your requests to these endpoints:

- fetch current Roblox versions: `http://farts.fadedis.xyz:25551/api/versions/current`
- fetch future Roblox versions: `http://farts.fadedis.xyz:25551/api/versions/future`
- fetch all exploit statuses: `http://farts.fadedis.xyz:25551/api/status/exploits`
- fetch a specific exploit status: `http://farts.fadedis.xyz:25551/api/status/exploits/[exploit]` (replace `[exploit]` with the name of the executor. example: `solara`)

These endpoints will accept your requests to the [weao.xyz](https://weao.xyz/) API with the correct User-Agent headers and return the response.
WEAO Documentation: [WEAO Documentation](https://docs.weao.xyz/)
