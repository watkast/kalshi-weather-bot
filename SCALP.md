# Range-Scalp Bot

*Updated Wed Oct 28 21:47 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38581 | 33663 | 4918 (48) | 0 | $-10873.67 | -4.5% |
| **+10¢** | 28775 | 23093 | 5682 (70) | 0 | $-9664.60 | -5.3% |
| **+15¢** | 24070 | 17966 | 6104 (95) | 0 | $-8637.24 | -5.7% |
| **+20¢** | 21353 | 14963 | 6390 (120) | 0 | $-7562.80 | -5.6% |
| **+10¢ (15¢ stop)** | 47189 | 47122 | 67 (35) | 0 | $-17912.49 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 21:42 | +5 | DOGE | UP | 0.69 | 0.77 | 0.52 |
| 10-28 21:42 | +10 stop | ZEC | UP | 0.59 | 0.40 | -2.24 |
| 10-28 21:42 | +10 stop | HYPE | UP | 0.56 | 0.75 | 1.58 |
| 10-28 21:42 | +10 stop | DOGE | UP | 0.67 | 0.77 | 0.71 |
| 10-28 21:41 | +10 stop | BTC | DOWN | 0.55 | 0.65 | 0.66 |
| 10-28 21:41 | +15 | BTC | DOWN | 0.55 | yes | -5.68 |
| 10-28 21:41 | +10 | BTC | DOWN | 0.56 | yes | -5.78 |
| 10-28 21:41 | +5 | BTC | DOWN | 0.54 | 0.65 | 0.76 |
| 10-28 21:40 | +10 stop | ETH | UP | 0.47 | 0.68 | 1.76 |
| 10-28 21:40 | +10 | ETH | UP | 0.47 | 0.68 | 1.76 |
| 10-28 21:40 | +5 | ETH | UP | 0.47 | 0.68 | 1.76 |
| 10-28 21:40 | +10 stop | BNB | UP | 0.68 | 0.51 | -2.01 |
| 10-28 21:40 | +10 stop | DOGE | UP | 0.60 | 0.44 | -1.95 |
| 10-28 21:40 | +10 | DOGE | UP | 0.60 | 0.77 | 1.40 |
| 10-28 21:40 | +5 | DOGE | UP | 0.60 | 0.65 | 0.17 |
| 10-28 21:40 | +10 stop | BTC | DOWN | 0.46 | 0.64 | 1.45 |
| 10-28 21:40 | +15 | BTC | DOWN | 0.46 | 0.64 | 1.45 |
| 10-28 21:40 | +10 | BTC | DOWN | 0.46 | 0.64 | 1.45 |
| 10-28 21:40 | +5 | BTC | DOWN | 0.50 | 0.55 | 0.14 |
| 10-28 21:40 | +10 stop | HYPE | DOWN | 0.63 | 0.48 | -1.85 |
| 10-28 21:40 | +10 | HYPE | DOWN | 0.63 | yes | -6.47 |
| 10-28 21:40 | +5 | HYPE | DOWN | 0.63 | yes | -6.47 |
| 10-28 21:40 | +10 stop | ETH | DOWN | 0.42 | 0.55 | 0.94 |
| 10-28 21:40 | +10 | ETH | DOWN | 0.42 | 0.55 | 0.94 |
| 10-28 21:40 | +5 | ETH | DOWN | 0.42 | 0.55 | 0.94 |
| 10-28 21:39 | +10 stop | XRP | DOWN | 0.47 | 0.61 | 1.05 |
| 10-28 21:39 | +5 | XRP | DOWN | 0.47 | 0.61 | 1.05 |
| 10-28 21:39 | +5 | BNB | DOWN | 0.58 | yes | -5.95 |
| 10-28 21:39 | +10 stop | ZEC | DOWN | 0.63 | 0.43 | -2.35 |
| 10-28 21:39 | +5 | ZEC | DOWN | 0.63 | 0.73 | 0.69 |
| 10-28 21:39 | +5 | NEAR | DOWN | 0.47 | 0.56 | 0.54 |
| 10-28 21:38 | +10 stop | NEAR | DOWN | 0.68 | 0.45 | -2.64 |
| 10-28 21:38 | +10 stop | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-28 21:38 | +10 stop | XRP | DOWN | 0.62 | 0.75 | 0.99 |
| 10-28 21:38 | +10 stop | BNB | DOWN | 0.64 | 0.45 | -2.25 |
| 10-28 21:37 | +10 stop | ZEC | DOWN | 0.52 | 0.64 | 0.85 |
| 10-28 21:37 | +10 stop | HYPE | DOWN | 0.64 | 0.77 | 0.96 |
| 10-28 21:37 | +20 | HYPE | DOWN | 0.64 | yes | -6.61 |
| 10-28 21:37 | +15 | HYPE | DOWN | 0.64 | yes | -6.61 |
| 10-28 21:37 | +10 | HYPE | DOWN | 0.66 | 0.77 | 0.81 |
