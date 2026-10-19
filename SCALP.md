# Range-Scalp Bot

*Updated Mon Oct 19 23:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 24715 | 21516 | 3199 (31) | 3 | $-7226.66 | -4.6% |
| **+10¢** | 18582 | 14885 | 3697 (46) | 5 | $-6441.77 | -5.5% |
| **+15¢** | 15559 | 11579 | 3980 (70) | 5 | $-5788.14 | -5.9% |
| **+20¢** | 13757 | 9589 | 4168 (88) | 6 | $-5209.73 | -6.0% |
| **+10¢ (15¢ stop)** | 30353 | 30301 | 52 (30) | 1 | $-11408.30 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 23:06 | +10 stop | NEAR | DOWN | 0.64 | open |  |
| 10-19 23:05 | +10 stop | BTC | UP | 0.69 | 0.53 | -1.93 |
| 10-19 23:05 | +20 | BTC | UP | 0.69 | open |  |
| 10-19 23:05 | +15 | BTC | UP | 0.69 | open |  |
| 10-19 23:05 | +10 | BTC | UP | 0.69 | open |  |
| 10-19 23:05 | +5 | BTC | UP | 0.69 | open |  |
| 10-19 23:05 | +10 stop | XRP | UP | 0.64 | 0.47 | -2.05 |
| 10-19 23:05 | +5 | DOGE | UP | 0.62 | open |  |
| 10-19 23:05 | +15 | DOGE | UP | 0.62 | open |  |
| 10-19 23:04 | +10 stop | SOL | UP | 0.47 | 0.63 | 1.25 |
| 10-19 23:04 | +10 stop | DOGE | UP | 0.61 | 0.35 | -2.93 |
| 10-19 23:04 | +10 | DOGE | UP | 0.61 | open |  |
| 10-19 23:04 | +5 | DOGE | UP | 0.61 | 0.69 | 0.48 |
| 10-19 23:04 | +10 stop | ZEC | UP | 0.52 | 0.29 | -2.63 |
| 10-19 23:04 | +10 stop | HYPE | UP | 0.57 | 0.69 | 0.87 |
| 10-19 23:04 | +5 | SOL | UP | 0.52 | 0.63 | 0.75 |
| 10-19 23:04 | +5 | SOL | DOWN | 0.42 | 0.54 | 0.84 |
| 10-19 23:03 | +5 | NEAR | DOWN | 0.65 | 0.70 | 0.19 |
| 10-19 23:03 | +5 | SOL | DOWN | 0.54 | 0.59 | 0.15 |
| 10-19 23:03 | +10 stop | ZEC | DOWN | 0.56 | 0.39 | -2.05 |
| 10-19 23:03 | +5 | BTC | UP | 0.68 | 0.79 | 0.82 |
| 10-19 23:03 | +10 stop | XRP | UP | 0.42 | 0.61 | 1.55 |
| 10-19 23:03 | +10 stop | ETH | UP | 0.52 | 0.63 | 0.75 |
| 10-19 23:03 | +10 | ETH | UP | 0.52 | 0.63 | 0.75 |
| 10-19 23:03 | +5 | ETH | UP | 0.52 | 0.63 | 0.75 |
| 10-19 23:03 | +10 stop | ZEC | UP | 0.40 | 0.53 | 0.95 |
| 10-19 23:03 | +10 stop | BTC | UP | 0.55 | 0.65 | 0.66 |
| 10-19 23:03 | +20 | BTC | UP | 0.55 | 0.79 | 2.10 |
| 10-19 23:03 | +15 | BTC | UP | 0.55 | 0.70 | 1.17 |
| 10-19 23:03 | +10 | BTC | UP | 0.55 | 0.65 | 0.66 |
| 10-19 23:03 | +5 | BTC | UP | 0.55 | 0.62 | 0.35 |
| 10-19 23:02 | +10 stop | NEAR | DOWN | 0.62 | 0.37 | -2.84 |
| 10-19 23:02 | +20 | NEAR | DOWN | 0.62 | open |  |
| 10-19 23:02 | +15 | NEAR | DOWN | 0.62 | open |  |
| 10-19 23:02 | +10 | NEAR | DOWN | 0.62 | open |  |
| 10-19 23:02 | +5 | NEAR | DOWN | 0.62 | 0.70 | 0.48 |
| 10-19 23:02 | +10 stop | SOL | DOWN | 0.55 | 0.40 | -1.85 |
| 10-19 23:02 | +20 | SOL | DOWN | 0.55 | open |  |
| 10-19 23:02 | +15 | SOL | DOWN | 0.55 | 0.70 | 1.17 |
| 10-19 23:02 | +10 | SOL | DOWN | 0.55 | 0.70 | 1.17 |
