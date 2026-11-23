# Range-Scalp Bot

*Updated Mon Nov 23 02:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69424 | 60574 | 8850 (146) | 2 | $-18706.80 | -4.3% |
| **+10¢** | 51805 | 41466 | 10339 (189) | 2 | $-17404.70 | -5.3% |
| **+15¢** | 43414 | 32277 | 11137 (244) | 2 | $-15544.77 | -5.7% |
| **+20¢** | 38666 | 26958 | 11708 (306) | 2 | $-13835.23 | -5.7% |
| **+10¢ (15¢ stop)** | 84521 | 84331 | 190 (118) | 1 | $-31064.95 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 02:16 | +10 stop | NEAR | UP | 0.65 | open |  |
| 11-23 02:16 | +20 | NEAR | UP | 0.65 | open |  |
| 11-23 02:16 | +15 | NEAR | UP | 0.65 | open |  |
| 11-23 02:16 | +10 | NEAR | UP | 0.65 | open |  |
| 11-23 02:16 | +5 | NEAR | UP | 0.64 | open |  |
| 11-23 02:15 | +10 stop | BNB | DOWN | 0.55 | 0.40 | -1.86 |
| 11-23 02:15 | +20 | BNB | DOWN | 0.55 | open |  |
| 11-23 02:15 | +15 | BNB | DOWN | 0.55 | open |  |
| 11-23 02:15 | +10 | BNB | DOWN | 0.55 | open |  |
| 11-23 02:15 | +5 | BNB | DOWN | 0.55 | open |  |
| 11-23 02:12 | +10 stop | SOL | DOWN | 0.52 | 0.75 | 1.98 |
| 11-23 02:12 | +10 stop | DOGE | UP | 0.70 | 0.47 | -2.60 |
| 11-23 02:12 | +15 | XRP | UP | 0.70 | 0.94 | 2.24 |
| 11-23 02:11 | +10 | XRP | UP | 0.70 | 0.80 | 0.73 |
| 11-23 02:11 | +10 stop | XRP | UP | 0.68 | 0.80 | 0.92 |
| 11-23 02:11 | +5 | XRP | UP | 0.68 | 0.75 | 0.40 |
| 11-23 02:11 | +10 stop | DOGE | DOWN | 0.57 | 0.42 | -1.86 |
| 11-23 02:11 | +20 | DOGE | DOWN | 0.57 | yes | -5.88 |
| 11-23 02:11 | +15 | DOGE | DOWN | 0.57 | yes | -5.88 |
| 11-23 02:11 | +10 | DOGE | DOWN | 0.57 | yes | -5.88 |
| 11-23 02:11 | +5 | DOGE | DOWN | 0.56 | yes | -5.78 |
| 11-23 02:11 | +10 stop | XRP | DOWN | 0.36 | 0.64 | 2.46 |
| 11-23 02:11 | +5 | XRP | DOWN | 0.36 | 0.64 | 2.46 |
| 11-23 02:07 | +5 | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-23 02:06 | +10 | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-23 02:06 | +5 | XRP | DOWN | 0.64 | 0.72 | 0.48 |
| 11-23 02:05 | +5 | BTC | DOWN | 0.68 | 0.76 | 0.51 |
| 11-23 02:05 | +10 stop | HYPE | DOWN | 0.54 | 0.70 | 1.27 |
| 11-23 02:04 | +10 stop | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 11-23 02:04 | +10 stop | BNB | DOWN | 0.61 | 0.71 | 0.68 |
| 11-23 02:04 | +10 stop | XRP | DOWN | 0.68 | 0.79 | 0.82 |
| 11-23 02:04 | +10 stop | DOGE | DOWN | 0.63 | 0.74 | 0.79 |
| 11-23 02:04 | +5 | DOGE | DOWN | 0.63 | 0.68 | 0.17 |
| 11-23 02:04 | +10 stop | BTC | DOWN | 0.64 | 0.76 | 0.90 |
| 11-23 02:04 | +20 | BTC | DOWN | 0.64 | 0.85 | 1.84 |
| 11-23 02:04 | +15 | BTC | DOWN | 0.64 | 0.79 | 1.21 |
| 11-23 02:04 | +10 | BTC | DOWN | 0.64 | 0.76 | 0.90 |
| 11-23 02:04 | +5 | BTC | DOWN | 0.64 | 0.73 | 0.59 |
| 11-23 02:04 | +5 | XRP | DOWN | 0.62 | 0.70 | 0.48 |
| 11-23 02:03 | +10 stop | ETH | DOWN | 0.61 | 0.74 | 0.99 |
