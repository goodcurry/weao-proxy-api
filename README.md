# weao proxy api (python version)

## purpose (this is yellowgregs yap)

When I was developing a simple template website using the Whatexpsare.online API, I encountered an issue with the requests being blocked due to CORS restrictions. After discussing this with the API owner, we couldn't find a solution immediately, though he did mention he would fix the CORS issue. Therefore, with his permission, I created this open-source proxy server to make the API accessible to everyone without restrictions.

### usage

To use the proxy server, send your requests to these endpoints:

- Fetch current Roblox versions: `http://farts.fadedis.xyz:25551/api/versions/current`
- Fetch future Roblox versions: `http://farts.fadedis.xyz:25551/api/versions/future`
- Fetch all exploit statuses: `http://farts.fadedis.xyz:25551/api/status/exploits`
- Fetch a specific exploit status: `http://farts.fadedis.xyz:25551/api/status/exploits/[exploit]` (Replace `[exploit]` with the name of the executor. Example: `solara`)

These endpoints will accept your requests to the [weao.xyz](https://weao.xyz/) API with the correct User-Agent headers and return the response.
WEAO Documentation: [WEAO Documentation](https://docs.weao.xyz/)
