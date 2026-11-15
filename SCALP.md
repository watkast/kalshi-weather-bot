# Range-Scalp Bot

*Updated Sun Nov 15 23:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61362 | 53542 | 7820 (115) | 1 | $-16523.82 | -4.3% |
| **+10¢** | 45827 | 36662 | 9165 (156) | 1 | $-15520.14 | -5.4% |
| **+15¢** | 38388 | 28502 | 9886 (195) | 2 | $-14168.17 | -5.9% |
| **+20¢** | 34217 | 23847 | 10370 (247) | 2 | $-12433.22 | -5.8% |
| **+10¢ (15¢ stop)** | 74673 | 74519 | 154 (90) | 1 | $-27467.84 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 23:22 | +10 stop | XRP | DOWN | 0.51 | 0.68 | 1.36 |
| 11-15 23:22 | +20 | XRP | DOWN | 0.51 | 0.77 | 2.29 |
| 11-15 23:22 | +15 | XRP | DOWN | 0.51 | 0.68 | 1.36 |
| 11-15 23:22 | +10 | XRP | DOWN | 0.51 | 0.68 | 1.36 |
| 11-15 23:22 | +5 | XRP | DOWN | 0.51 | 0.68 | 1.36 |
| 11-15 23:22 | +10 stop | BTC | DOWN | 0.58 | 0.71 | 0.97 |
| 11-15 23:22 | +20 | BTC | DOWN | 0.58 | open |  |
| 11-15 23:22 | +15 | BTC | DOWN | 0.58 | open |  |
| 11-15 23:22 | +10 | BTC | DOWN | 0.58 | 0.71 | 0.97 |
| 11-15 23:22 | +5 | BTC | DOWN | 0.58 | 0.64 | 0.25 |
| 11-15 23:22 | +10 stop | DOGE | UP | 0.70 | open |  |
| 11-15 23:22 | +20 | DOGE | UP | 0.68 | open |  |
| 11-15 23:22 | +15 | DOGE | UP | 0.68 | open |  |
| 11-15 23:22 | +10 | DOGE | UP | 0.66 | open |  |
| 11-15 23:22 | +5 | DOGE | UP | 0.66 | open |  |
| 11-15 23:17 | +10 stop | DOGE | DOWN | 0.71 | 0.84 | 1.05 |
| 11-15 23:17 | +15 | DOGE | DOWN | 0.71 | 0.88 | 1.47 |
| 11-15 23:17 | +10 | DOGE | DOWN | 0.71 | 0.84 | 1.05 |
| 11-15 23:17 | +5 | DOGE | DOWN | 0.66 | 0.71 | 0.19 |
| 11-15 23:16 | +10 stop | DOGE | DOWN | 0.56 | 0.68 | 0.89 |
| 11-15 23:16 | +20 | DOGE | DOWN | 0.52 | 0.84 | 2.92 |
| 11-15 23:16 | +15 | DOGE | DOWN | 0.52 | 0.68 | 1.26 |
| 11-15 23:16 | +10 | DOGE | DOWN | 0.52 | 0.68 | 1.26 |
| 11-15 23:16 | +5 | DOGE | DOWN | 0.52 | 0.57 | 0.14 |
| 11-15 23:16 | +10 stop | BTC | DOWN | 0.57 | 0.73 | 1.28 |
| 11-15 23:16 | +20 | BTC | DOWN | 0.57 | 0.78 | 1.79 |
| 11-15 23:16 | +15 | BTC | DOWN | 0.57 | 0.73 | 1.28 |
| 11-15 23:16 | +10 | BTC | DOWN | 0.57 | 0.73 | 1.28 |
| 11-15 23:16 | +5 | BTC | DOWN | 0.56 | 0.73 | 1.38 |
| 11-15 23:16 | +10 stop | HYPE | DOWN | 0.60 | 0.74 | 1.09 |
| 11-15 23:16 | +20 | HYPE | DOWN | 0.60 | 0.85 | 2.24 |
| 11-15 23:16 | +15 | HYPE | DOWN | 0.60 | 0.75 | 1.19 |
| 11-15 23:16 | +10 | HYPE | DOWN | 0.60 | 0.74 | 1.09 |
| 11-15 23:16 | +5 | HYPE | DOWN | 0.60 | 0.74 | 1.09 |
| 11-15 23:16 | +10 stop | ETH | DOWN | 0.61 | 0.76 | 1.20 |
| 11-15 23:16 | +20 | ETH | DOWN | 0.62 | 0.84 | 1.93 |
| 11-15 23:16 | +15 | ETH | DOWN | 0.62 | 0.77 | 1.20 |
| 11-15 23:16 | +10 | ETH | DOWN | 0.62 | 0.76 | 1.10 |
| 11-15 23:16 | +5 | ETH | DOWN | 0.62 | 0.76 | 1.10 |
| 11-15 23:16 | +10 stop | XRP | DOWN | 0.67 | 0.79 | 0.92 |
