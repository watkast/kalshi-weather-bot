# Range-Scalp Bot

*Updated Sun Nov 01 22:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44025 | 38345 | 5680 (65) | 0 | $-12678.43 | -4.6% |
| **+10¢** | 32853 | 26292 | 6561 (86) | 1 | $-11411.91 | -5.5% |
| **+15¢** | 27492 | 20431 | 7061 (113) | 3 | $-10423.88 | -6.0% |
| **+20¢** | 24418 | 17024 | 7394 (147) | 5 | $-9189.07 | -6.0% |
| **+10¢ (15¢ stop)** | 53697 | 53611 | 86 (51) | 1 | $-20324.31 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 22:32 | +10 stop | BNB | UP | 0.61 | open |  |
| 11-01 22:32 | +20 | BNB | UP | 0.62 | open |  |
| 11-01 22:32 | +15 | BNB | UP | 0.62 | open |  |
| 11-01 22:32 | +10 | BNB | UP | 0.62 | open |  |
| 11-01 22:32 | +5 | BNB | UP | 0.62 | 0.67 | 0.17 |
| 11-01 22:31 | +10 stop | NEAR | UP | 0.71 | 0.81 | 0.74 |
| 11-01 22:31 | +20 | NEAR | UP | 0.71 | open |  |
| 11-01 22:31 | +15 | NEAR | UP | 0.71 | open |  |
| 11-01 22:31 | +10 | NEAR | UP | 0.71 | 0.81 | 0.74 |
| 11-01 22:31 | +5 | NEAR | UP | 0.71 | 0.77 | 0.32 |
| 11-01 22:31 | +10 stop | SOL | UP | 0.64 | 0.74 | 0.69 |
| 11-01 22:31 | +20 | SOL | UP | 0.63 | open |  |
| 11-01 22:31 | +15 | SOL | UP | 0.63 | 0.80 | 1.41 |
| 11-01 22:31 | +10 | SOL | UP | 0.64 | 0.74 | 0.69 |
| 11-01 22:31 | +5 | SOL | UP | 0.65 | 0.70 | 0.19 |
| 11-01 22:31 | +10 stop | DOGE | UP | 0.66 | 0.76 | 0.71 |
| 11-01 22:31 | +20 | DOGE | UP | 0.66 | open |  |
| 11-01 22:31 | +15 | DOGE | UP | 0.66 | open |  |
| 11-01 22:31 | +10 | DOGE | UP | 0.66 | 0.76 | 0.71 |
| 11-01 22:31 | +5 | DOGE | UP | 0.66 | 0.75 | 0.60 |
| 11-01 22:31 | +10 stop | HYPE | UP | 0.67 | 0.77 | 0.71 |
| 11-01 22:31 | +20 | HYPE | UP | 0.67 | open |  |
| 11-01 22:31 | +15 | HYPE | UP | 0.67 | 0.83 | 1.34 |
| 11-01 22:31 | +10 | HYPE | UP | 0.67 | 0.77 | 0.71 |
| 11-01 22:31 | +5 | HYPE | UP | 0.67 | 0.73 | 0.30 |
| 11-01 22:30 | +10 stop | XRP | UP | 0.62 | 0.75 | 0.94 |
| 11-01 22:30 | +20 | XRP | UP | 0.62 | 0.85 | 1.99 |
| 11-01 22:30 | +15 | XRP | UP | 0.62 | 0.80 | 1.46 |
| 11-01 22:30 | +10 | XRP | UP | 0.63 | 0.75 | 0.89 |
| 11-01 22:30 | +5 | XRP | UP | 0.63 | 0.71 | 0.48 |
| 11-01 22:16 | +10 stop | HYPE | DOWN | 0.71 | 0.82 | 0.84 |
| 11-01 22:16 | +20 | HYPE | DOWN | 0.71 | 0.92 | 1.90 |
| 11-01 22:16 | +15 | HYPE | DOWN | 0.71 | 0.92 | 1.90 |
| 11-01 22:16 | +10 | HYPE | DOWN | 0.71 | 0.82 | 0.84 |
| 11-01 22:16 | +5 | HYPE | DOWN | 0.71 | 0.79 | 0.53 |
| 11-01 22:04 | +10 stop | BTC | DOWN | 0.61 | 0.74 | 0.99 |
| 11-01 22:04 | +10 stop | SOL | UP | 0.54 | 0.36 | -2.15 |
| 11-01 22:04 | +10 stop | NEAR | DOWN | 0.67 | 0.85 | 1.55 |
| 11-01 22:03 | +5 | BNB | DOWN | 0.68 | 0.77 | 0.61 |
| 11-01 22:03 | +10 stop | ETH | DOWN | 0.68 | 0.81 | 1.03 |
