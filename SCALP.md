# Range-Scalp Bot

*Updated Mon Oct 26 06:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 34383 | 30010 | 4373 (43) | 5 | $-9572.15 | -4.4% |
| **+10¢** | 25740 | 20683 | 5057 (65) | 7 | $-8410.55 | -5.2% |
| **+15¢** | 21524 | 16082 | 5442 (89) | 8 | $-7522.91 | -5.6% |
| **+20¢** | 19073 | 13370 | 5703 (112) | 9 | $-6637.23 | -5.5% |
| **+10¢ (15¢ stop)** | 42134 | 42072 | 62 (33) | 0 | $-16063.61 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 06:24 | +10 | DOGE | DOWN | 0.71 | 0.82 | 0.84 |
| 10-26 06:24 | +5 | DOGE | DOWN | 0.71 | 0.82 | 0.84 |
| 10-26 06:24 | +10 stop | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 10-26 06:24 | +10 stop | XRP | DOWN | 0.61 | 0.80 | 1.61 |
| 10-26 06:24 | +10 stop | ZEC | DOWN | 0.60 | 0.82 | 1.92 |
| 10-26 06:24 | +10 | ZEC | DOWN | 0.60 | 0.82 | 1.92 |
| 10-26 06:24 | +5 | ZEC | DOWN | 0.60 | 0.82 | 1.92 |
| 10-26 06:24 | +10 stop | HYPE | DOWN | 0.67 | 0.77 | 0.71 |
| 10-26 06:24 | +10 | HYPE | DOWN | 0.67 | open |  |
| 10-26 06:24 | +5 | HYPE | DOWN | 0.67 | 0.74 | 0.40 |
| 10-26 06:23 | +10 stop | DOGE | UP | 0.46 | 0.61 | 1.15 |
| 10-26 06:23 | +15 | DOGE | UP | 0.46 | 0.61 | 1.15 |
| 10-26 06:23 | +10 | DOGE | UP | 0.46 | 0.61 | 1.15 |
| 10-26 06:23 | +5 | DOGE | UP | 0.46 | 0.61 | 1.15 |
| 10-26 06:23 | +10 stop | BTC | UP | 0.46 | 0.26 | -2.32 |
| 10-26 06:23 | +20 | BTC | UP | 0.46 | open |  |
| 10-26 06:23 | +15 | BTC | UP | 0.46 | open |  |
| 10-26 06:23 | +10 | BTC | UP | 0.46 | open |  |
| 10-26 06:23 | +5 | BTC | UP | 0.46 | 0.55 | 0.54 |
| 10-26 06:22 | +10 stop | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 10-26 06:22 | +10 stop | ETH | UP | 0.66 | 0.42 | -2.74 |
| 10-26 06:22 | +20 | ETH | UP | 0.66 | open |  |
| 10-26 06:22 | +10 | ETH | UP | 0.66 | open |  |
| 10-26 06:22 | +5 | ETH | UP | 0.66 | open |  |
| 10-26 06:22 | +10 stop | SOL | UP | 0.60 | 0.43 | -2.05 |
| 10-26 06:22 | +10 | SOL | UP | 0.60 | open |  |
| 10-26 06:22 | +5 | SOL | UP | 0.60 | open |  |
| 10-26 06:22 | +10 stop | XRP | UP | 0.71 | 0.39 | -3.52 |
| 10-26 06:22 | +15 | XRP | UP | 0.71 | open |  |
| 10-26 06:22 | +10 | XRP | UP | 0.71 | open |  |
| 10-26 06:22 | +5 | XRP | UP | 0.71 | open |  |
| 10-26 06:22 | +10 stop | NEAR | UP | 0.58 | 0.38 | -2.35 |
| 10-26 06:22 | +10 stop | BNB | UP | 0.47 | 0.58 | 0.74 |
| 10-26 06:21 | +10 stop | ETH | UP | 0.57 | 0.68 | 0.76 |
| 10-26 06:20 | +10 stop | DOGE | UP | 0.70 | 0.81 | 0.84 |
| 10-26 06:20 | +20 | DOGE | UP | 0.70 | open |  |
| 10-26 06:20 | +15 | DOGE | UP | 0.70 | 0.88 | 1.57 |
| 10-26 06:20 | +10 | DOGE | UP | 0.70 | 0.81 | 0.84 |
| 10-26 06:20 | +5 | DOGE | UP | 0.70 | 0.77 | 0.42 |
| 10-26 06:20 | +10 stop | XRP | UP | 0.71 | 0.84 | 1.05 |
