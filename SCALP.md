# Range-Scalp Bot

*Updated Fri Nov 06 22:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50034 | 43619 | 6415 (76) | 7 | $-14025.05 | -4.5% |
| **+10¢** | 37341 | 29877 | 7464 (102) | 7 | $-12917.49 | -5.5% |
| **+15¢** | 31275 | 23230 | 8045 (131) | 7 | $-11831.19 | -6.0% |
| **+20¢** | 27804 | 19369 | 8435 (172) | 7 | $-10460.81 | -6.0% |
| **+10¢ (15¢ stop)** | 60937 | 60838 | 99 (58) | 6 | $-22571.22 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 22:06 | +10 stop | DOGE | UP | 0.57 | open |  |
| 11-06 22:06 | +10 stop | SOL | UP | 0.57 | open |  |
| 11-06 22:06 | +10 stop | ETH | UP | 0.67 | open |  |
| 11-06 22:06 | +20 | ETH | UP | 0.67 | open |  |
| 11-06 22:06 | +15 | ETH | UP | 0.67 | open |  |
| 11-06 22:06 | +10 | ETH | UP | 0.66 | open |  |
| 11-06 22:06 | +5 | ETH | UP | 0.66 | open |  |
| 11-06 22:05 | +10 stop | XRP | UP | 0.65 | open |  |
| 11-06 22:05 | +20 | XRP | UP | 0.65 | open |  |
| 11-06 22:05 | +15 | XRP | UP | 0.65 | open |  |
| 11-06 22:05 | +10 | XRP | UP | 0.65 | open |  |
| 11-06 22:05 | +5 | XRP | UP | 0.65 | open |  |
| 11-06 22:05 | +5 | NEAR | UP | 0.55 | open |  |
| 11-06 22:05 | +10 stop | ZEC | DOWN | 0.64 | open |  |
| 11-06 22:05 | +10 stop | HYPE | DOWN | 0.67 | open |  |
| 11-06 22:05 | +10 stop | NEAR | UP | 0.60 | 0.43 | -2.05 |
| 11-06 22:05 | +20 | NEAR | UP | 0.60 | open |  |
| 11-06 22:05 | +15 | NEAR | UP | 0.60 | open |  |
| 11-06 22:05 | +10 | NEAR | UP | 0.60 | open |  |
| 11-06 22:05 | +5 | NEAR | UP | 0.60 | 0.66 | 0.27 |
| 11-06 22:05 | +10 stop | DOGE | UP | 0.67 | 0.51 | -1.94 |
| 11-06 22:05 | +20 | DOGE | UP | 0.67 | open |  |
| 11-06 22:05 | +15 | DOGE | UP | 0.67 | open |  |
| 11-06 22:05 | +10 | DOGE | UP | 0.67 | open |  |
| 11-06 22:05 | +5 | DOGE | UP | 0.67 | open |  |
| 11-06 22:04 | +10 stop | SOL | UP | 0.69 | 0.53 | -1.93 |
| 11-06 22:04 | +20 | SOL | UP | 0.69 | open |  |
| 11-06 22:04 | +15 | SOL | UP | 0.69 | open |  |
| 11-06 22:04 | +10 | SOL | UP | 0.69 | open |  |
| 11-06 22:04 | +5 | SOL | UP | 0.69 | open |  |
| 11-06 22:04 | +10 stop | HYPE | UP | 0.59 | 0.42 | -2.05 |
| 11-06 22:04 | +20 | HYPE | UP | 0.60 | open |  |
| 11-06 22:04 | +15 | HYPE | UP | 0.60 | open |  |
| 11-06 22:04 | +10 | HYPE | UP | 0.59 | open |  |
| 11-06 22:04 | +5 | HYPE | UP | 0.60 | open |  |
| 11-06 22:03 | +10 stop | ZEC | UP | 0.59 | 0.44 | -1.85 |
| 11-06 22:03 | +20 | ZEC | UP | 0.61 | open |  |
| 11-06 22:03 | +15 | ZEC | UP | 0.61 | open |  |
| 11-06 22:03 | +10 | ZEC | UP | 0.61 | open |  |
| 11-06 22:03 | +5 | ZEC | UP | 0.61 | open |  |
