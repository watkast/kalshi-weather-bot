# Range-Scalp Bot

*Updated Mon Oct 26 20:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 35361 | 30868 | 4493 (43) | 5 | $-9852.29 | -4.4% |
| **+10¢** | 26444 | 21248 | 5196 (65) | 8 | $-8671.14 | -5.2% |
| **+15¢** | 22128 | 16535 | 5593 (89) | 9 | $-7767.83 | -5.6% |
| **+20¢** | 19624 | 13763 | 5861 (112) | 9 | $-6808.64 | -5.5% |
| **+10¢ (15¢ stop)** | 43359 | 43297 | 62 (33) | 1 | $-16503.93 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 20:22 | +10 stop | NEAR | UP | 0.36 | 0.54 | 1.45 |
| 10-26 20:22 | +10 stop | ZEC | UP | 0.56 | open |  |
| 10-26 20:21 | +10 stop | ETH | DOWN | 0.51 | 0.70 | 1.57 |
| 10-26 20:21 | +10 | ETH | DOWN | 0.50 | 0.70 | 1.67 |
| 10-26 20:21 | +5 | ETH | DOWN | 0.50 | 0.59 | 0.55 |
| 10-26 20:21 | +10 stop | BNB | DOWN | 0.55 | 0.77 | 1.89 |
| 10-26 20:21 | +5 | BNB | DOWN | 0.55 | 0.63 | 0.45 |
| 10-26 20:21 | +5 | DOGE | DOWN | 0.65 | open |  |
| 10-26 20:20 | +5 | BNB | DOWN | 0.67 | 0.75 | 0.50 |
| 10-26 20:19 | +10 stop | XRP | DOWN | 0.63 | 0.40 | -2.64 |
| 10-26 20:19 | +10 stop | ETH | DOWN | 0.63 | 0.74 | 0.79 |
| 10-26 20:19 | +15 | ETH | DOWN | 0.63 | open |  |
| 10-26 20:19 | +10 | ETH | DOWN | 0.63 | 0.74 | 0.79 |
| 10-26 20:19 | +5 | ETH | DOWN | 0.63 | 0.74 | 0.79 |
| 10-26 20:19 | +10 stop | ZEC | DOWN | 0.67 | 0.49 | -2.14 |
| 10-26 20:19 | +10 stop | BTC | DOWN | 0.67 | 0.78 | 0.81 |
| 10-26 20:19 | +10 stop | SOL | DOWN | 0.68 | 0.79 | 0.82 |
| 10-26 20:19 | +10 stop | DOGE | DOWN | 0.67 | 0.41 | -2.93 |
| 10-26 20:19 | +10 stop | NEAR | DOWN | 0.61 | 0.46 | -1.85 |
| 10-26 20:19 | +10 stop | BNB | DOWN | 0.59 | 0.71 | 0.92 |
| 10-26 20:19 | +5 | BTC | DOWN | 0.67 | 0.75 | 0.50 |
| 10-26 20:19 | +5 | DOGE | DOWN | 0.66 | 0.74 | 0.50 |
| 10-26 20:19 | +5 | BNB | DOWN | 0.59 | 0.66 | 0.41 |
| 10-26 20:19 | +10 stop | HYPE | DOWN | 0.71 | 0.81 | 0.74 |
| 10-26 20:18 | +5 | BNB | UP | 0.51 | 0.62 | 0.75 |
| 10-26 20:18 | +5 | BTC | UP | 0.47 | 0.55 | 0.44 |
| 10-26 20:18 | +5 | DOGE | UP | 0.56 | 0.64 | 0.45 |
| 10-26 20:18 | +5 | ZEC | UP | 0.65 | open |  |
| 10-26 20:17 | +10 stop | BNB | UP | 0.65 | 0.45 | -2.34 |
| 10-26 20:17 | +20 | BNB | UP | 0.65 | open |  |
| 10-26 20:17 | +15 | BNB | UP | 0.65 | open |  |
| 10-26 20:17 | +10 | BNB | UP | 0.65 | open |  |
| 10-26 20:17 | +5 | BNB | UP | 0.65 | 0.72 | 0.39 |
| 10-26 20:17 | +5 | ETH | UP | 0.66 | 0.74 | 0.50 |
| 10-26 20:17 | +10 stop | BTC | UP | 0.57 | 0.37 | -2.35 |
| 10-26 20:17 | +20 | BTC | UP | 0.57 | open |  |
| 10-26 20:17 | +15 | BTC | UP | 0.57 | open |  |
| 10-26 20:17 | +10 | BTC | UP | 0.57 | open |  |
| 10-26 20:17 | +5 | BTC | UP | 0.57 | 0.62 | 0.15 |
| 10-26 20:17 | +10 stop | ZEC | UP | 0.54 | 0.38 | -1.95 |
