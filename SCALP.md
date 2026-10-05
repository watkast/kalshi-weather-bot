# Range-Scalp Bot

*Updated Mon Oct 05 23:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4301 | 3704 | 597 (6) | 3 | $-1485.75 | -5.5% |
| **+10¢** | 3317 | 2625 | 692 (9) | 4 | $-1361.17 | -6.5% |
| **+15¢** | 2781 | 2051 | 730 (12) | 5 | $-1179.83 | -6.8% |
| **+20¢** | 2486 | 1725 | 761 (17) | 6 | $-1011.81 | -6.5% |
| **+10¢ (15¢ stop)** | 5286 | 5275 | 11 (6) | 2 | $-1897.78 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 23:03 | +10 stop | SOL | DOWN | 0.50 | open |  |
| 10-05 23:03 | +20 | SOL | DOWN | 0.50 | open |  |
| 10-05 23:03 | +15 | SOL | DOWN | 0.50 | open |  |
| 10-05 23:03 | +10 | SOL | DOWN | 0.50 | open |  |
| 10-05 23:03 | +5 | SOL | DOWN | 0.50 | open |  |
| 10-05 23:03 | +10 stop | ZEC | DOWN | 0.55 | 0.31 | -2.73 |
| 10-05 23:03 | +5 | ZEC | DOWN | 0.55 | open |  |
| 10-05 23:03 | +10 stop | DOGE | UP | 0.66 | 0.78 | 0.87 |
| 10-05 23:03 | +20 | DOGE | UP | 0.66 | open |  |
| 10-05 23:03 | +15 | DOGE | UP | 0.66 | open |  |
| 10-05 23:03 | +10 | DOGE | UP | 0.66 | 0.78 | 0.87 |
| 10-05 23:03 | +5 | DOGE | UP | 0.66 | 0.72 | 0.25 |
| 10-05 23:03 | +10 stop | HYPE | DOWN | 0.55 | open |  |
| 10-05 23:03 | +10 | HYPE | DOWN | 0.55 | open |  |
| 10-05 23:03 | +5 | HYPE | DOWN | 0.55 | 0.61 | 0.27 |
| 10-05 23:03 | +10 stop | XRP | UP | 0.64 | 0.77 | 1.00 |
| 10-05 23:03 | +15 | XRP | UP | 0.64 | 0.86 | 1.94 |
| 10-05 23:03 | +10 | XRP | UP | 0.64 | 0.77 | 1.00 |
| 10-05 23:03 | +5 | XRP | UP | 0.64 | 0.69 | 0.18 |
| 10-05 23:03 | +5 | BNB | UP | 0.64 | 0.72 | 0.48 |
| 10-05 23:02 | +10 stop | HYPE | UP | 0.44 | 0.55 | 0.74 |
| 10-05 23:02 | +20 | HYPE | UP | 0.44 | open |  |
| 10-05 23:02 | +15 | HYPE | UP | 0.44 | open |  |
| 10-05 23:02 | +10 | HYPE | UP | 0.44 | 0.55 | 0.74 |
| 10-05 23:02 | +5 | HYPE | UP | 0.44 | 0.55 | 0.74 |
| 10-05 23:01 | +20 | ZEC | UP | 0.71 | open |  |
| 10-05 23:01 | +15 | ZEC | UP | 0.71 | open |  |
| 10-05 23:01 | +10 | ZEC | UP | 0.71 | open |  |
| 10-05 23:01 | +5 | ZEC | UP | 0.71 | 0.76 | 0.22 |
| 10-05 23:01 | +10 stop | BNB | UP | 0.64 | 0.76 | 0.90 |
| 10-05 23:01 | +20 | BNB | UP | 0.64 | 0.87 | 2.05 |
| 10-05 23:01 | +15 | BNB | UP | 0.64 | 0.80 | 1.31 |
| 10-05 23:01 | +10 | BNB | UP | 0.64 | 0.76 | 0.90 |
| 10-05 23:01 | +5 | BNB | UP | 0.64 | 0.71 | 0.38 |
| 10-05 23:01 | +10 stop | NEAR | UP | 0.61 | 0.46 | -1.89 |
| 10-05 23:01 | +20 | NEAR | UP | 0.61 | open |  |
| 10-05 23:01 | +15 | NEAR | UP | 0.61 | open |  |
| 10-05 23:01 | +10 | NEAR | UP | 0.61 | open |  |
| 10-05 23:01 | +5 | NEAR | UP | 0.61 | open |  |
| 10-05 23:01 | +10 stop | DOGE | UP | 0.62 | 0.73 | 0.79 |
