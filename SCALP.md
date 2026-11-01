# Range-Scalp Bot

*Updated Sun Nov 01 05:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43234 | 37688 | 5546 (62) | 4 | $-12277.92 | -4.5% |
| **+10¢** | 32242 | 25833 | 6409 (84) | 4 | $-10995.55 | -5.4% |
| **+15¢** | 26977 | 20070 | 6907 (112) | 4 | $-10057.15 | -5.9% |
| **+20¢** | 23957 | 16720 | 7237 (146) | 6 | $-8886.59 | -5.9% |
| **+10¢ (15¢ stop)** | 52706 | 52623 | 83 (48) | 4 | $-19909.12 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 05:04 | +10 stop | HYPE | UP | 0.70 | open |  |
| 11-01 05:04 | +5 | HYPE | UP | 0.70 | open |  |
| 11-01 05:04 | +10 stop | ZEC | UP | 0.55 | open |  |
| 11-01 05:03 | +5 | BNB | UP | 0.64 | open |  |
| 11-01 05:03 | +5 | BNB | UP | 0.50 | 0.55 | 0.14 |
| 11-01 05:02 | +5 | HYPE | UP | 0.60 | 0.67 | 0.37 |
| 11-01 05:02 | +10 stop | NEAR | UP | 0.69 | open |  |
| 11-01 05:02 | +20 | NEAR | UP | 0.70 | open |  |
| 11-01 05:02 | +15 | NEAR | UP | 0.71 | open |  |
| 11-01 05:02 | +10 | NEAR | UP | 0.69 | open |  |
| 11-01 05:02 | +5 | NEAR | UP | 0.69 | open |  |
| 11-01 05:02 | +10 stop | HYPE | DOWN | 0.47 | 0.31 | -1.93 |
| 11-01 05:02 | +20 | HYPE | DOWN | 0.47 | open |  |
| 11-01 05:02 | +15 | HYPE | DOWN | 0.47 | open |  |
| 11-01 05:02 | +10 | HYPE | DOWN | 0.47 | open |  |
| 11-01 05:02 | +5 | HYPE | DOWN | 0.47 | 0.55 | 0.44 |
| 11-01 05:02 | +10 stop | ZEC | UP | 0.67 | 0.46 | -2.44 |
| 11-01 05:02 | +20 | ZEC | UP | 0.67 | open |  |
| 11-01 05:02 | +15 | ZEC | UP | 0.67 | open |  |
| 11-01 05:02 | +10 | ZEC | UP | 0.68 | open |  |
| 11-01 05:02 | +5 | ZEC | UP | 0.68 | open |  |
| 11-01 05:01 | +10 stop | SOL | UP | 0.60 | 0.74 | 1.09 |
| 11-01 05:01 | +20 | SOL | UP | 0.60 | 0.80 | 1.71 |
| 11-01 05:01 | +15 | SOL | UP | 0.60 | 0.80 | 1.71 |
| 11-01 05:01 | +10 | SOL | UP | 0.60 | 0.74 | 1.09 |
| 11-01 05:01 | +5 | SOL | UP | 0.60 | 0.66 | 0.27 |
| 11-01 05:01 | +10 stop | BNB | UP | 0.57 | open |  |
| 11-01 05:01 | +20 | BNB | UP | 0.57 | open |  |
| 11-01 05:01 | +15 | BNB | UP | 0.57 | open |  |
| 11-01 05:01 | +10 | BNB | UP | 0.57 | open |  |
| 11-01 05:01 | +5 | BNB | UP | 0.57 | 0.63 | 0.27 |
| 11-01 05:01 | +10 stop | XRP | UP | 0.68 | 0.82 | 1.13 |
| 11-01 05:01 | +20 | XRP | UP | 0.67 | open |  |
| 11-01 05:01 | +15 | XRP | UP | 0.68 | 0.84 | 1.34 |
| 11-01 05:01 | +10 | XRP | UP | 0.68 | 0.82 | 1.13 |
| 11-01 05:01 | +5 | XRP | UP | 0.68 | 0.82 | 1.13 |
| 11-01 05:01 | +10 stop | BTC | UP | 0.68 | 0.80 | 0.92 |
| 11-01 05:01 | +20 | BTC | UP | 0.68 | open |  |
| 11-01 05:01 | +15 | BTC | UP | 0.68 | 0.84 | 1.34 |
| 11-01 05:01 | +10 | BTC | UP | 0.68 | 0.80 | 0.92 |
