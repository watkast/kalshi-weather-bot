# Range-Scalp Bot

*Updated Sun Nov 15 20:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61165 | 53372 | 7793 (114) | 0 | $-16467.20 | -4.3% |
| **+10¢** | 45686 | 36554 | 9132 (153) | 0 | $-15466.65 | -5.4% |
| **+15¢** | 38266 | 28418 | 9848 (191) | 0 | $-14107.53 | -5.9% |
| **+20¢** | 34105 | 23774 | 10331 (243) | 0 | $-12390.37 | -5.8% |
| **+10¢ (15¢ stop)** | 74437 | 74285 | 152 (90) | 0 | $-27397.31 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 19:58 | +10 stop | ETH | DOWN | 0.64 | 0.39 | -2.84 |
| 11-15 19:58 | +20 | ETH | DOWN | 0.62 | 0.98 | 3.39 |
| 11-15 19:58 | +15 | ETH | DOWN | 0.62 | 0.98 | 3.39 |
| 11-15 19:58 | +10 | ETH | DOWN | 0.62 | 0.98 | 3.39 |
| 11-15 19:58 | +5 | ETH | DOWN | 0.62 | 0.68 | 0.27 |
| 11-15 19:58 | +10 stop | HYPE | DOWN | 0.29 | 0.64 | 3.18 |
| 11-15 19:57 | +10 stop | BTC | DOWN | 0.65 | 0.22 | -4.59 |
| 11-15 19:55 | +5 | BTC | UP | 0.65 | 0.77 | 0.91 |
| 11-15 19:55 | +10 stop | HYPE | UP | 0.53 | 0.31 | -2.53 |
| 11-15 19:54 | +10 stop | BNB | DOWN | 0.62 | 0.87 | 2.25 |
| 11-15 19:54 | +10 stop | SOL | DOWN | 0.68 | 0.51 | -2.04 |
| 11-15 19:54 | +20 | SOL | DOWN | 0.67 | 0.89 | 1.93 |
| 11-15 19:54 | +15 | SOL | DOWN | 0.67 | 0.89 | 1.93 |
| 11-15 19:53 | +10 stop | BTC | UP | 0.63 | 0.37 | -2.94 |
| 11-15 19:53 | +10 stop | HYPE | UP | 0.70 | 0.53 | -2.03 |
| 11-15 19:53 | +10 stop | BNB | DOWN | 0.61 | 0.46 | -1.85 |
| 11-15 19:53 | +20 | BNB | DOWN | 0.61 | 0.87 | 2.35 |
| 11-15 19:53 | +15 | BNB | DOWN | 0.61 | 0.87 | 2.35 |
| 11-15 19:53 | +10 | BNB | DOWN | 0.61 | 0.87 | 2.35 |
| 11-15 19:53 | +5 | BNB | DOWN | 0.61 | 0.87 | 2.35 |
| 11-15 19:53 | +10 stop | ETH | DOWN | 0.59 | 0.80 | 1.81 |
| 11-15 19:53 | +15 | ETH | DOWN | 0.59 | 0.80 | 1.81 |
| 11-15 19:53 | +10 | ETH | DOWN | 0.59 | 0.80 | 1.81 |
| 11-15 19:53 | +5 | ETH | DOWN | 0.59 | 0.67 | 0.47 |
| 11-15 19:53 | +10 stop | DOGE | UP | 0.67 | 0.80 | 1.02 |
| 11-15 19:53 | +10 stop | BTC | DOWN | 0.67 | 0.39 | -3.13 |
| 11-15 19:53 | +10 stop | HYPE | DOWN | 0.61 | 0.36 | -2.84 |
| 11-15 19:53 | +10 stop | ZEC | UP | 0.64 | 0.79 | 1.21 |
| 11-15 19:52 | +10 stop | DOGE | UP | 0.66 | 0.49 | -2.04 |
| 11-15 19:52 | +5 | DOGE | UP | 0.66 | 0.74 | 0.50 |
| 11-15 19:52 | +10 stop | HYPE | UP | 0.60 | 0.33 | -3.07 |
| 11-15 19:52 | +20 | HYPE | UP | 0.60 | no | -6.21 |
| 11-15 19:52 | +15 | HYPE | UP | 0.60 | no | -6.21 |
| 11-15 19:52 | +10 | HYPE | UP | 0.60 | no | -6.21 |
| 11-15 19:52 | +5 | HYPE | UP | 0.60 | no | -6.21 |
| 11-15 19:51 | +10 stop | BTC | UP | 0.59 | 0.32 | -3.03 |
| 11-15 19:51 | +10 | BTC | UP | 0.59 | 0.77 | 1.50 |
| 11-15 19:51 | +5 | BTC | UP | 0.59 | 0.64 | 0.16 |
| 11-15 19:49 | +10 stop | SOL | UP | 0.65 | 0.48 | -2.04 |
| 11-15 19:49 | +10 | SOL | UP | 0.65 | no | -6.66 |
