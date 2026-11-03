# Range-Scalp Bot

*Updated Tue Nov 03 15:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46136 | 40170 | 5966 (70) | 6 | $-13314.62 | -4.6% |
| **+10¢** | 34435 | 27523 | 6912 (92) | 7 | $-12192.41 | -5.6% |
| **+15¢** | 28823 | 21393 | 7430 (120) | 7 | $-11116.86 | -6.1% |
| **+20¢** | 25603 | 17817 | 7786 (157) | 7 | $-9867.95 | -6.1% |
| **+10¢ (15¢ stop)** | 56288 | 56199 | 89 (53) | 5 | $-21135.74 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 15:32 | +10 stop | XRP | UP | 0.69 | open |  |
| 11-03 15:32 | +20 | XRP | UP | 0.68 | open |  |
| 11-03 15:32 | +15 | XRP | UP | 0.68 | open |  |
| 11-03 15:32 | +10 | XRP | UP | 0.68 | open |  |
| 11-03 15:32 | +5 | XRP | UP | 0.68 | open |  |
| 11-03 15:31 | +10 | BNB | UP | 0.67 | open |  |
| 11-03 15:31 | +5 | BNB | UP | 0.67 | 0.72 | 0.19 |
| 11-03 15:31 | +10 stop | DOGE | UP | 0.71 | open |  |
| 11-03 15:31 | +20 | DOGE | UP | 0.71 | open |  |
| 11-03 15:31 | +15 | DOGE | UP | 0.71 | open |  |
| 11-03 15:31 | +10 | DOGE | UP | 0.70 | open |  |
| 11-03 15:31 | +5 | DOGE | UP | 0.70 | open |  |
| 11-03 15:31 | +10 stop | ETH | UP | 0.68 | open |  |
| 11-03 15:31 | +20 | ETH | UP | 0.68 | open |  |
| 11-03 15:31 | +15 | ETH | UP | 0.68 | open |  |
| 11-03 15:31 | +10 | ETH | UP | 0.68 | open |  |
| 11-03 15:31 | +5 | ETH | UP | 0.68 | open |  |
| 11-03 15:31 | +10 stop | BNB | UP | 0.71 | open |  |
| 11-03 15:31 | +20 | BNB | UP | 0.71 | open |  |
| 11-03 15:31 | +15 | BNB | UP | 0.71 | open |  |
| 11-03 15:31 | +10 stop | BTC | UP | 0.63 | open |  |
| 11-03 15:31 | +20 | BTC | UP | 0.63 | open |  |
| 11-03 15:31 | +15 | BTC | UP | 0.63 | open |  |
| 11-03 15:31 | +10 | BTC | UP | 0.63 | open |  |
| 11-03 15:31 | +5 | BTC | UP | 0.63 | open |  |
| 11-03 15:31 | +10 stop | HYPE | UP | 0.65 | 0.46 | -2.24 |
| 11-03 15:31 | +20 | HYPE | UP | 0.65 | open |  |
| 11-03 15:31 | +15 | HYPE | UP | 0.65 | open |  |
| 11-03 15:31 | +10 | HYPE | UP | 0.65 | open |  |
| 11-03 15:31 | +5 | HYPE | UP | 0.65 | open |  |
| 11-03 15:31 | +10 stop | ZEC | UP | 0.71 | 0.53 | -2.13 |
| 11-03 15:31 | +20 | ZEC | UP | 0.71 | open |  |
| 11-03 15:31 | +15 | ZEC | UP | 0.71 | open |  |
| 11-03 15:31 | +10 | ZEC | UP | 0.71 | open |  |
| 11-03 15:31 | +5 | ZEC | UP | 0.71 | open |  |
| 11-03 15:23 | +10 stop | BTC | DOWN | 0.71 | 0.83 | 0.95 |
| 11-03 15:22 | +10 stop | BNB | DOWN | 0.70 | 0.84 | 1.15 |
| 11-03 15:22 | +5 | ZEC | DOWN | 0.69 | 0.77 | 0.52 |
| 11-03 15:22 | +10 stop | ETH | DOWN | 0.71 | 0.83 | 0.95 |
| 11-03 15:22 | +20 | ETH | DOWN | 0.71 | 0.92 | 1.84 |
