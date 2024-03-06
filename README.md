# Simple Cloudflare DDNS Utility
This is a very handy Python script that handles updating your DNS record when your IP address changes. There is no need to set up your subdomains beforehand. The utility only requires a domain you own (managed by Cloudflare) and an API token.
## Dependencies
Python
## Usage
First create an API token with *DNS edit* permission on either a specific zone or all zones ([reference](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/)).

Then edit `config.json` to include the token and the ID of the zone you want to edit. Finally include the domains you wish to set up in the `domains` section of `config.json`, and execute `./run.sh`.

## 使用说明
（需要Python）无需手动创建 DNS 记录，只需要你的域名和 API 令牌就可以自动管理你的动态 DNS。

首先为你的 Cloudflare 账户设置一个 API 令牌，并赋予它 DNS 编辑权限。

然后在 `config.json` 中加入你创建的令牌和目标域名的区域 ID。最后把需要管理的域名添加到 `config.json` 的 `domains` 部分，然后执行 `./run.sh`。
