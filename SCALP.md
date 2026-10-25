# Range-Scalp Bot

*Updated Sun Oct 25 10:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 33050 | 28840 | 4210 (42) | 1 | $-9246.24 | -4.4% |
| **+10¢** | 24731 | 19857 | 4874 (60) | 1 | $-8231.13 | -5.3% |
| **+15¢** | 20697 | 15451 | 5246 (83) | 2 | $-7392.81 | -5.7% |
| **+20¢** | 18334 | 12841 | 5493 (105) | 3 | $-6518.33 | -5.7% |
| **+10¢ (15¢ stop)** | 40548 | 40488 | 60 (32) | 0 | $-15443.48 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 10:57 | +10 stop | HYPE | UP | 0.56 | 0.40 | -1.95 |
| 10-25 10:55 | +10 stop | HYPE | DOWN | 0.61 | 0.43 | -2.15 |
| 10-25 10:55 | +15 | HYPE | DOWN | 0.61 | open |  |
| 10-25 10:55 | +10 | HYPE | DOWN | 0.61 | open |  |
| 10-25 10:55 | +5 | HYPE | DOWN | 0.61 | open |  |
| 10-25 10:55 | +10 stop | NEAR | DOWN | 0.64 | 0.76 | 0.90 |
| 10-25 10:55 | +10 | NEAR | DOWN | 0.64 | 0.76 | 0.90 |
| 10-25 10:55 | +5 | NEAR | DOWN | 0.64 | 0.70 | 0.28 |
| 10-25 10:53 | +5 | HYPE | DOWN | 0.58 | 0.66 | 0.46 |
| 10-25 10:53 | +10 stop | HYPE | DOWN | 0.58 | 0.70 | 0.87 |
| 10-25 10:53 | +10 stop | NEAR | DOWN | 0.64 | 0.74 | 0.69 |
| 10-25 10:52 | +5 | HYPE | DOWN | 0.54 | 0.61 | 0.35 |
| 10-25 10:52 | +5 | HYPE | DOWN | 0.54 | 0.67 | 0.96 |
| 10-25 10:51 | +10 stop | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-25 10:51 | +20 | ZEC | DOWN | 0.70 | open |  |
| 10-25 10:51 | +15 | ZEC | DOWN | 0.70 | 0.85 | 1.26 |
| 10-25 10:51 | +10 | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-25 10:51 | +5 | ZEC | DOWN | 0.70 | 0.77 | 0.42 |
| 10-25 10:51 | +10 stop | NEAR | DOWN | 0.69 | 0.52 | -2.03 |
| 10-25 10:51 | +20 | NEAR | DOWN | 0.69 | open |  |
| 10-25 10:51 | +15 | NEAR | DOWN | 0.69 | open |  |
| 10-25 10:51 | +10 | NEAR | DOWN | 0.69 | 0.79 | 0.73 |
| 10-25 10:51 | +5 | NEAR | DOWN | 0.69 | 0.74 | 0.21 |
| 10-25 10:50 | +10 stop | HYPE | DOWN | 0.64 | 0.45 | -2.25 |
| 10-25 10:50 | +10 | HYPE | DOWN | 0.65 | 0.77 | 0.91 |
| 10-25 10:50 | +5 | HYPE | DOWN | 0.66 | 0.73 | 0.40 |
| 10-25 10:47 | +10 stop | HYPE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-25 10:47 | +20 | HYPE | DOWN | 0.62 | open |  |
| 10-25 10:47 | +15 | HYPE | DOWN | 0.62 | 0.77 | 1.20 |
| 10-25 10:47 | +10 | HYPE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-25 10:47 | +5 | HYPE | DOWN | 0.62 | 0.69 | 0.38 |
| 10-25 10:41 | +10 stop | BNB | DOWN | 0.63 | 0.75 | 0.89 |
| 10-25 10:41 | +10 stop | BNB | DOWN | 0.71 | 0.51 | -2.33 |
| 10-25 10:39 | +10 stop | DOGE | UP | 0.55 | 0.35 | -2.34 |
| 10-25 10:39 | +20 | DOGE | UP | 0.55 | 0.77 | 1.89 |
| 10-25 10:39 | +15 | DOGE | UP | 0.55 | 0.77 | 1.89 |
| 10-25 10:39 | +5 | DOGE | UP | 0.55 | 0.69 | 1.07 |
| 10-25 10:39 | +5 | ETH | DOWN | 0.70 | 0.84 | 1.15 |
| 10-25 10:38 | +10 stop | ZEC | DOWN | 0.60 | 0.81 | 1.82 |
| 10-25 10:37 | +10 stop | BNB | DOWN | 0.64 | 0.47 | -2.05 |
