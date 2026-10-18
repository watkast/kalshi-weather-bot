# Range-Scalp Bot

*Updated Sun Oct 18 20:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 22916 | 19937 | 2979 (30) | 4 | $-6755.24 | -4.7% |
| **+10¢** | 17238 | 13799 | 3439 (44) | 5 | $-6035.11 | -5.6% |
| **+15¢** | 14444 | 10732 | 3712 (66) | 5 | $-5510.80 | -6.1% |
| **+20¢** | 12790 | 8908 | 3882 (84) | 5 | $-4886.30 | -6.1% |
| **+10¢ (15¢ stop)** | 28211 | 28160 | 51 (30) | 2 | $-10793.00 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 20:25 | +10 stop | BTC | UP | 0.61 | open |  |
| 10-18 20:25 | +10 stop | XRP | UP | 0.71 | open |  |
| 10-18 20:24 | +10 stop | XRP | DOWN | 0.50 | 0.60 | 0.65 |
| 10-18 20:23 | +10 stop | NEAR | UP | 0.62 | 0.77 | 1.20 |
| 10-18 20:23 | +10 stop | XRP | UP | 0.57 | 0.35 | -2.54 |
| 10-18 20:22 | +10 stop | DOGE | UP | 0.68 | 0.49 | -2.24 |
| 10-18 20:22 | +10 stop | NEAR | UP | 0.65 | 0.75 | 0.72 |
| 10-18 20:21 | +5 | BTC | DOWN | 0.70 | open |  |
| 10-18 20:21 | +10 stop | XRP | DOWN | 0.62 | 0.46 | -1.95 |
| 10-18 20:20 | +10 stop | DOGE | UP | 0.66 | 0.44 | -2.54 |
| 10-18 20:20 | +5 | BTC | DOWN | 0.64 | 0.69 | 0.18 |
| 10-18 20:19 | +10 stop | BNB | UP | 0.69 | 0.84 | 1.25 |
| 10-18 20:19 | +5 | BNB | UP | 0.60 | 0.67 | 0.37 |
| 10-18 20:19 | +10 stop | DOGE | UP | 0.57 | 0.68 | 0.76 |
| 10-18 20:18 | +10 stop | SOL | UP | 0.70 | 0.80 | 0.73 |
| 10-18 20:18 | +10 | SOL | UP | 0.70 | 0.80 | 0.73 |
| 10-18 20:18 | +10 stop | NEAR | UP | 0.65 | 0.78 | 1.01 |
| 10-18 20:18 | +5 | SOL | UP | 0.68 | 0.78 | 0.71 |
| 10-18 20:18 | +5 | BNB | UP | 0.55 | 0.60 | 0.15 |
| 10-18 20:18 | +5 | ZEC | DOWN | 0.48 | 0.54 | 0.24 |
| 10-18 20:18 | +10 stop | HYPE | DOWN | 0.34 | 0.61 | 2.33 |
| 10-18 20:18 | +20 | HYPE | DOWN | 0.36 | 0.61 | 2.12 |
| 10-18 20:18 | +15 | HYPE | DOWN | 0.37 | 0.61 | 2.06 |
| 10-18 20:18 | +10 | HYPE | DOWN | 0.37 | 0.61 | 2.06 |
| 10-18 20:18 | +5 | HYPE | DOWN | 0.37 | 0.61 | 2.06 |
| 10-18 20:18 | +10 stop | BNB | DOWN | 0.52 | 0.37 | -1.85 |
| 10-18 20:18 | +20 | BNB | DOWN | 0.52 | open |  |
| 10-18 20:18 | +15 | BNB | DOWN | 0.52 | open |  |
| 10-18 20:18 | +10 | BNB | DOWN | 0.52 | open |  |
| 10-18 20:18 | +5 | BNB | DOWN | 0.52 | 0.58 | 0.24 |
| 10-18 20:18 | +10 stop | DOGE | DOWN | 0.58 | 0.40 | -2.15 |
| 10-18 20:18 | +20 | DOGE | DOWN | 0.58 | open |  |
| 10-18 20:18 | +15 | DOGE | DOWN | 0.58 | open |  |
| 10-18 20:18 | +10 | DOGE | DOWN | 0.59 | open |  |
| 10-18 20:18 | +5 | DOGE | DOWN | 0.59 | open |  |
| 10-18 20:17 | +10 stop | ZEC | UP | 0.46 | 0.63 | 1.35 |
| 10-18 20:17 | +20 | ZEC | UP | 0.46 | 0.70 | 2.07 |
| 10-18 20:17 | +15 | ZEC | UP | 0.46 | 0.63 | 1.35 |
| 10-18 20:17 | +10 | ZEC | UP | 0.46 | 0.63 | 1.35 |
| 10-18 20:17 | +5 | ZEC | UP | 0.46 | 0.53 | 0.34 |
