# Range-Scalp Bot

*Updated Tue Oct 20 16:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 25883 | 22542 | 3341 (31) | 7 | $-7561.02 | -4.6% |
| **+10¢** | 19486 | 15627 | 3859 (46) | 7 | $-6669.43 | -5.4% |
| **+15¢** | 16314 | 12161 | 4153 (70) | 8 | $-5947.47 | -5.8% |
| **+20¢** | 14429 | 10077 | 4352 (88) | 8 | $-5345.19 | -5.9% |
| **+10¢ (15¢ stop)** | 31742 | 31689 | 53 (30) | 0 | $-11674.06 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 16:23 | +10 stop | NEAR | DOWN | 0.66 | 0.77 | 0.81 |
| 10-20 16:22 | +10 stop | SOL | DOWN | 0.65 | 0.76 | 0.81 |
| 10-20 16:22 | +10 stop | DOGE | DOWN | 0.62 | 0.77 | 1.20 |
| 10-20 16:22 | +10 stop | ETH | DOWN | 0.66 | 0.84 | 1.54 |
| 10-20 16:22 | +10 stop | ZEC | DOWN | 0.61 | 0.73 | 0.89 |
| 10-20 16:17 | +10 stop | SOL | DOWN | 0.68 | 0.80 | 0.92 |
| 10-20 16:17 | +10 stop | NEAR | DOWN | 0.68 | 0.50 | -2.14 |
| 10-20 16:17 | +10 stop | ZEC | DOWN | 0.61 | 0.71 | 0.68 |
| 10-20 16:17 | +10 stop | DOGE | DOWN | 0.68 | 0.81 | 1.03 |
| 10-20 16:17 | +10 stop | XRP | DOWN | 0.70 | 0.82 | 0.94 |
| 10-20 16:17 | +10 stop | HYPE | DOWN | 0.71 | 0.81 | 0.74 |
| 10-20 16:17 | +10 | HYPE | DOWN | 0.70 | 0.81 | 0.84 |
| 10-20 16:17 | +5 | HYPE | DOWN | 0.70 | 0.78 | 0.52 |
| 10-20 16:17 | +10 stop | HYPE | UP | 0.45 | 0.55 | 0.64 |
| 10-20 16:17 | +20 | HYPE | UP | 0.45 | open |  |
| 10-20 16:17 | +15 | HYPE | UP | 0.45 | open |  |
| 10-20 16:17 | +10 | HYPE | UP | 0.45 | 0.55 | 0.64 |
| 10-20 16:17 | +5 | HYPE | UP | 0.45 | 0.55 | 0.64 |
| 10-20 16:16 | +10 stop | SOL | UP | 0.67 | 0.37 | -3.33 |
| 10-20 16:16 | +20 | SOL | UP | 0.67 | open |  |
| 10-20 16:16 | +15 | SOL | UP | 0.67 | open |  |
| 10-20 16:16 | +10 | SOL | UP | 0.67 | open |  |
| 10-20 16:16 | +5 | SOL | UP | 0.67 | open |  |
| 10-20 16:16 | +5 | XRP | UP | 0.71 | open |  |
| 10-20 16:16 | +10 stop | XRP | UP | 0.71 | 0.56 | -1.83 |
| 10-20 16:16 | +20 | XRP | UP | 0.71 | open |  |
| 10-20 16:16 | +15 | XRP | UP | 0.71 | open |  |
| 10-20 16:16 | +10 | XRP | UP | 0.71 | open |  |
| 10-20 16:16 | +10 stop | ZEC | UP | 0.66 | 0.49 | -2.04 |
| 10-20 16:16 | +20 | ZEC | UP | 0.66 | open |  |
| 10-20 16:16 | +15 | ZEC | UP | 0.66 | open |  |
| 10-20 16:16 | +10 | ZEC | UP | 0.66 | open |  |
| 10-20 16:16 | +5 | ZEC | UP | 0.66 | open |  |
| 10-20 16:16 | +10 stop | DOGE | UP | 0.67 | 0.51 | -1.94 |
| 10-20 16:16 | +20 | DOGE | UP | 0.67 | open |  |
| 10-20 16:16 | +15 | DOGE | UP | 0.67 | open |  |
| 10-20 16:16 | +10 | DOGE | UP | 0.67 | open |  |
| 10-20 16:16 | +5 | DOGE | UP | 0.67 | open |  |
| 10-20 16:16 | +10 stop | BTC | UP | 0.65 | 0.46 | -2.24 |
| 10-20 16:16 | +20 | BTC | UP | 0.65 | open |  |
