# Range-Scalp Bot

*Updated Fri Nov 20 05:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65922 | 57529 | 8393 (124) | 0 | $-17773.56 | -4.3% |
| **+10¢** | 49236 | 39421 | 9815 (165) | 0 | $-16572.71 | -5.4% |
| **+15¢** | 41296 | 30711 | 10585 (211) | 0 | $-14930.99 | -5.8% |
| **+20¢** | 36765 | 25649 | 11116 (267) | 0 | $-13217.56 | -5.7% |
| **+10¢ (15¢ stop)** | 80278 | 80114 | 164 (98) | 0 | $-29597.88 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 05:46 | +10 stop | HYPE | UP | 0.68 | 0.83 | 1.27 |
| 11-20 05:46 | +20 | HYPE | UP | 0.68 | 0.88 | 1.79 |
| 11-20 05:46 | +15 | HYPE | UP | 0.68 | 0.83 | 1.27 |
| 11-20 05:46 | +10 | HYPE | UP | 0.68 | 0.83 | 1.27 |
| 11-20 05:46 | +5 | HYPE | UP | 0.68 | 0.83 | 1.27 |
| 11-20 05:43 | +10 stop | BNB | UP | 0.66 | 0.48 | -2.14 |
| 11-20 05:43 | +5 | BTC | DOWN | 0.66 | 0.76 | 0.71 |
| 11-20 05:42 | +5 | BTC | DOWN | 0.63 | 0.68 | 0.17 |
| 11-20 05:42 | +10 stop | XRP | DOWN | 0.54 | 0.68 | 1.06 |
| 11-20 05:42 | +15 | XRP | DOWN | 0.52 | 0.68 | 1.26 |
| 11-20 05:42 | +10 | XRP | DOWN | 0.57 | 0.68 | 0.76 |
| 11-20 05:42 | +5 | XRP | DOWN | 0.56 | 0.68 | 0.86 |
| 11-20 05:42 | +5 | ETH | DOWN | 0.62 | 0.67 | 0.17 |
| 11-20 05:42 | +5 | ETH | DOWN | 0.49 | 0.61 | 0.85 |
| 11-20 05:42 | +5 | BTC | DOWN | 0.54 | 0.64 | 0.65 |
| 11-20 05:41 | +20 | DOGE | UP | 0.70 | 0.91 | 1.89 |
| 11-20 05:41 | +15 | DOGE | UP | 0.70 | 0.88 | 1.57 |
| 11-20 05:41 | +10 | DOGE | UP | 0.70 | 0.88 | 1.57 |
| 11-20 05:41 | +5 | DOGE | UP | 0.69 | 0.76 | 0.42 |
| 11-20 05:41 | +10 stop | DOGE | UP | 0.71 | 0.54 | -2.03 |
| 11-20 05:41 | +5 | BTC | DOWN | 0.68 | 0.74 | 0.30 |
| 11-20 05:40 | +10 stop | XRP | DOWN | 0.61 | 0.71 | 0.68 |
| 11-20 05:40 | +20 | XRP | DOWN | 0.61 | 0.81 | 1.72 |
| 11-20 05:40 | +15 | XRP | DOWN | 0.62 | 0.77 | 1.20 |
| 11-20 05:40 | +10 | XRP | DOWN | 0.61 | 0.71 | 0.68 |
| 11-20 05:40 | +5 | XRP | DOWN | 0.61 | 0.71 | 0.68 |
| 11-20 05:40 | +10 stop | ETH | DOWN | 0.67 | 0.48 | -2.24 |
| 11-20 05:40 | +20 | ETH | DOWN | 0.67 | 0.93 | 2.42 |
| 11-20 05:40 | +15 | ETH | DOWN | 0.67 | 0.82 | 1.23 |
| 11-20 05:40 | +10 | ETH | DOWN | 0.67 | 0.81 | 1.13 |
| 11-20 05:40 | +5 | ETH | DOWN | 0.67 | 0.76 | 0.61 |
| 11-20 05:39 | +10 stop | BTC | DOWN | 0.67 | 0.46 | -2.44 |
| 11-20 05:39 | +15 | BTC | DOWN | 0.65 | 0.99 | 3.23 |
| 11-20 05:39 | +10 | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 11-20 05:39 | +5 | BTC | DOWN | 0.65 | 0.71 | 0.29 |
| 11-20 05:39 | +10 stop | BNB | UP | 0.70 | 0.52 | -2.15 |
| 11-20 05:37 | +10 stop | HYPE | DOWN | 0.57 | 0.38 | -2.25 |
| 11-20 05:37 | +15 | HYPE | DOWN | 0.57 | yes | -5.88 |
| 11-20 05:37 | +10 | HYPE | DOWN | 0.57 | yes | -5.88 |
| 11-20 05:37 | +10 stop | NEAR | UP | 0.57 | 0.72 | 1.17 |
