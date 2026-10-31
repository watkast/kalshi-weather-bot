# Range-Scalp Bot

*Updated Sat Oct 31 01:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41534 | 36248 | 5286 (54) | 2 | $-11611.13 | -4.4% |
| **+10¢** | 30956 | 24839 | 6117 (78) | 3 | $-10350.21 | -5.3% |
| **+15¢** | 25876 | 19283 | 6593 (106) | 3 | $-9416.48 | -5.8% |
| **+20¢** | 22970 | 16066 | 6904 (137) | 3 | $-8282.69 | -5.7% |
| **+10¢ (15¢ stop)** | 50616 | 50541 | 75 (41) | 0 | $-19116.83 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 01:13 | +10 stop | BTC | DOWN | 0.68 | 0.84 | 1.34 |
| 10-31 01:10 | +10 stop | BTC | DOWN | 0.71 | 0.85 | 1.16 |
| 10-31 01:08 | +10 stop | SOL | UP | 0.63 | 0.78 | 1.20 |
| 10-31 01:08 | +20 | SOL | UP | 0.63 | 0.92 | 2.66 |
| 10-31 01:08 | +15 | SOL | UP | 0.63 | 0.82 | 1.58 |
| 10-31 01:08 | +10 | SOL | UP | 0.63 | 0.78 | 1.16 |
| 10-31 01:08 | +5 | SOL | UP | 0.63 | 0.70 | 0.34 |
| 10-31 01:08 | +5 | XRP | DOWN | 0.68 | 0.73 | 0.20 |
| 10-31 01:08 | +10 stop | BNB | DOWN | 0.68 | 0.44 | -2.74 |
| 10-31 01:08 | +10 stop | HYPE | UP | 0.57 | 0.76 | 1.61 |
| 10-31 01:08 | +10 | HYPE | UP | 0.58 | 0.76 | 1.49 |
| 10-31 01:08 | +10 stop | DOGE | DOWN | 0.58 | 0.68 | 0.66 |
| 10-31 01:08 | +5 | BTC | UP | 0.54 | open |  |
| 10-31 01:08 | +5 | BNB | UP | 0.53 | open |  |
| 10-31 01:07 | +5 | HYPE | DOWN | 0.52 | 0.70 | 1.47 |
| 10-31 01:07 | +10 stop | ETH | DOWN | 0.67 | 0.82 | 1.23 |
| 10-31 01:07 | +10 | ETH | DOWN | 0.68 | 0.82 | 1.13 |
| 10-31 01:07 | +5 | ETH | DOWN | 0.68 | 0.76 | 0.51 |
| 10-31 01:07 | +5 | DOGE | DOWN | 0.67 | 0.77 | 0.71 |
| 10-31 01:07 | +10 stop | BTC | UP | 0.61 | 0.35 | -2.93 |
| 10-31 01:07 | +15 | BTC | UP | 0.61 | open |  |
| 10-31 01:07 | +10 | BTC | UP | 0.61 | open |  |
| 10-31 01:07 | +5 | BTC | UP | 0.61 | 0.69 | 0.48 |
| 10-31 01:07 | +10 | BNB | UP | 0.54 | open |  |
| 10-31 01:07 | +5 | BNB | UP | 0.54 | 0.62 | 0.45 |
| 10-31 01:07 | +10 stop | HYPE | UP | 0.51 | 0.64 | 0.91 |
| 10-31 01:07 | +20 | HYPE | UP | 0.51 | 0.76 | 2.15 |
| 10-31 01:07 | +15 | HYPE | UP | 0.51 | 0.76 | 2.15 |
| 10-31 01:07 | +10 | HYPE | UP | 0.51 | 0.64 | 0.91 |
| 10-31 01:07 | +5 | HYPE | UP | 0.51 | 0.60 | 0.51 |
| 10-31 01:07 | +10 stop | XRP | UP | 0.51 | 0.31 | -2.33 |
| 10-31 01:07 | +20 | XRP | UP | 0.50 | open |  |
| 10-31 01:07 | +15 | XRP | UP | 0.50 | open |  |
| 10-31 01:07 | +10 | XRP | UP | 0.50 | open |  |
| 10-31 01:07 | +5 | XRP | UP | 0.50 | 0.55 | 0.14 |
| 10-31 01:07 | +10 stop | DOGE | UP | 0.49 | 0.33 | -1.94 |
| 10-31 01:07 | +20 | DOGE | UP | 0.48 | no | -4.98 |
| 10-31 01:07 | +15 | DOGE | UP | 0.48 | no | -4.98 |
| 10-31 01:07 | +10 | DOGE | UP | 0.48 | no | -4.98 |
| 10-31 01:07 | +5 | DOGE | UP | 0.48 | 0.53 | 0.14 |
