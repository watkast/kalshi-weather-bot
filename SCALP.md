# Range-Scalp Bot

*Updated Wed Oct 28 23:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38603 | 33681 | 4922 (48) | 0 | $-10885.18 | -4.5% |
| **+10¢** | 28794 | 23109 | 5685 (70) | 0 | $-9664.35 | -5.3% |
| **+15¢** | 24087 | 17979 | 6108 (96) | 0 | $-8633.14 | -5.7% |
| **+20¢** | 21370 | 14973 | 6397 (124) | 0 | $-7546.44 | -5.6% |
| **+10¢ (15¢ stop)** | 47216 | 47149 | 67 (35) | 0 | $-17915.87 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 22:58 | +10 stop | SOL | DOWN | 0.50 | 0.65 | 1.16 |
| 10-28 22:58 | +10 stop | XRP | DOWN | 0.34 | 0.65 | 2.78 |
| 10-28 22:57 | +10 stop | SOL | DOWN | 0.52 | 0.63 | 0.71 |
| 10-28 22:56 | +10 stop | HYPE | DOWN | 0.65 | 0.82 | 1.41 |
| 10-28 22:56 | +10 stop | ETH | UP | 0.50 | 0.33 | -2.04 |
| 10-28 22:56 | +10 stop | XRP | UP | 0.63 | 0.43 | -2.35 |
| 10-28 22:56 | +5 | XRP | UP | 0.63 | 0.75 | 0.89 |
| 10-28 22:56 | +10 stop | SOL | UP | 0.57 | 0.41 | -1.95 |
| 10-28 22:56 | +10 stop | ETH | UP | 0.54 | 0.67 | 0.96 |
| 10-28 22:56 | +10 stop | DOGE | UP | 0.57 | 0.39 | -2.15 |
| 10-28 22:56 | +20 | DOGE | UP | 0.57 | no | -5.88 |
| 10-28 22:56 | +15 | DOGE | UP | 0.57 | no | -5.88 |
| 10-28 22:56 | +10 | DOGE | UP | 0.57 | no | -5.88 |
| 10-28 22:56 | +5 | DOGE | UP | 0.57 | no | -5.88 |
| 10-28 22:56 | +5 | SOL | UP | 0.59 | no | -6.07 |
| 10-28 22:56 | +10 stop | BTC | DOWN | 0.65 | 0.84 | 1.64 |
| 10-28 22:56 | +20 | BTC | DOWN | 0.65 | 0.94 | 2.68 |
| 10-28 22:56 | +15 | BTC | DOWN | 0.65 | 0.84 | 1.64 |
| 10-28 22:56 | +10 | BTC | DOWN | 0.65 | 0.84 | 1.64 |
| 10-28 22:56 | +5 | BTC | DOWN | 0.65 | 0.84 | 1.64 |
| 10-28 22:55 | +5 | SOL | DOWN | 0.38 | 0.59 | 1.76 |
| 10-28 22:55 | +10 stop | ETH | DOWN | 0.61 | 0.38 | -2.64 |
| 10-28 22:55 | +20 | ETH | DOWN | 0.60 | 0.85 | 2.24 |
| 10-28 22:55 | +15 | ETH | DOWN | 0.60 | 0.75 | 1.19 |
| 10-28 22:55 | +10 | ETH | DOWN | 0.60 | 0.70 | 0.68 |
| 10-28 22:55 | +5 | ETH | DOWN | 0.60 | 0.65 | 0.17 |
| 10-28 22:55 | +10 stop | XRP | DOWN | 0.61 | 0.39 | -2.54 |
| 10-28 22:55 | +20 | XRP | DOWN | 0.61 | 0.88 | 2.45 |
| 10-28 22:55 | +15 | XRP | DOWN | 0.61 | 0.76 | 1.20 |
| 10-28 22:55 | +10 | XRP | DOWN | 0.61 | 0.76 | 1.20 |
| 10-28 22:55 | +5 | XRP | DOWN | 0.61 | 0.67 | 0.27 |
| 10-28 22:54 | +10 stop | ZEC | UP | 0.63 | 0.48 | -1.85 |
| 10-28 22:54 | +20 | ZEC | UP | 0.64 | 0.86 | 1.94 |
| 10-28 22:54 | +15 | ZEC | UP | 0.62 | 0.83 | 1.83 |
| 10-28 22:54 | +10 | ZEC | UP | 0.62 | 0.83 | 1.83 |
| 10-28 22:54 | +5 | ZEC | UP | 0.61 | 0.83 | 1.93 |
| 10-28 22:54 | +10 stop | HYPE | UP | 0.69 | 0.40 | -3.22 |
| 10-28 22:54 | +20 | HYPE | UP | 0.68 | no | -6.96 |
| 10-28 22:54 | +15 | HYPE | UP | 0.68 | no | -6.96 |
| 10-28 22:54 | +10 | HYPE | UP | 0.69 | no | -7.05 |
