# Range-Scalp Bot

*Updated Mon Oct 19 10:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 23863 | 20747 | 3116 (31) | 0 | $-7124.66 | -4.7% |
| **+10¢** | 17952 | 14361 | 3591 (45) | 2 | $-6357.02 | -5.6% |
| **+15¢** | 15037 | 11170 | 3867 (68) | 3 | $-5752.57 | -6.1% |
| **+20¢** | 13313 | 9269 | 4044 (86) | 3 | $-5110.54 | -6.1% |
| **+10¢ (15¢ stop)** | 29373 | 29322 | 51 (30) | 2 | $-11100.65 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 10:30 | +10 stop | XRP | DOWN | 0.68 | 0.79 | 0.82 |
| 10-19 10:30 | +20 | XRP | DOWN | 0.68 | open |  |
| 10-19 10:30 | +15 | XRP | DOWN | 0.69 | open |  |
| 10-19 10:30 | +10 | XRP | DOWN | 0.69 | 0.79 | 0.73 |
| 10-19 10:30 | +5 | XRP | DOWN | 0.71 | 0.76 | 0.22 |
| 10-19 10:30 | +10 stop | SOL | DOWN | 0.69 | open |  |
| 10-19 10:30 | +20 | SOL | DOWN | 0.69 | open |  |
| 10-19 10:30 | +15 | SOL | DOWN | 0.69 | open |  |
| 10-19 10:30 | +10 | SOL | DOWN | 0.69 | open |  |
| 10-19 10:30 | +5 | SOL | DOWN | 0.69 | 0.75 | 0.35 |
| 10-19 10:30 | +10 stop | BNB | DOWN | 0.69 | open |  |
| 10-19 10:30 | +20 | BNB | DOWN | 0.69 | open |  |
| 10-19 10:30 | +15 | BNB | DOWN | 0.69 | open |  |
| 10-19 10:30 | +10 | BNB | DOWN | 0.69 | open |  |
| 10-19 10:30 | +5 | BNB | DOWN | 0.69 | 0.77 | 0.52 |
| 10-19 10:24 | +10 stop | NEAR | DOWN | 0.68 | 0.78 | 0.71 |
| 10-19 10:21 | +10 stop | BNB | DOWN | 0.71 | 0.85 | 1.16 |
| 10-19 10:21 | +5 | BNB | DOWN | 0.71 | 0.78 | 0.42 |
| 10-19 10:19 | +10 stop | BNB | UP | 0.52 | 0.33 | -2.25 |
| 10-19 10:19 | +5 | BNB | DOWN | 0.56 | 0.65 | 0.56 |
| 10-19 10:18 | +10 stop | ZEC | DOWN | 0.67 | 0.81 | 1.13 |
| 10-19 10:18 | +10 stop | NEAR | UP | 0.63 | 0.47 | -1.95 |
| 10-19 10:17 | +10 stop | ETH | DOWN | 0.69 | 0.85 | 1.36 |
| 10-19 10:17 | +10 stop | BNB | DOWN | 0.63 | 0.44 | -2.25 |
| 10-19 10:17 | +20 | BNB | DOWN | 0.63 | 0.85 | 1.94 |
| 10-19 10:17 | +15 | BNB | DOWN | 0.63 | 0.78 | 1.20 |
| 10-19 10:17 | +10 | BNB | DOWN | 0.63 | 0.78 | 1.20 |
| 10-19 10:17 | +5 | BNB | DOWN | 0.63 | 0.69 | 0.28 |
| 10-19 10:16 | +10 stop | ZEC | UP | 0.54 | 0.29 | -2.83 |
| 10-19 10:16 | +20 | ZEC | UP | 0.54 | no | -5.58 |
| 10-19 10:16 | +15 | ZEC | UP | 0.54 | no | -5.58 |
| 10-19 10:16 | +10 | ZEC | UP | 0.54 | no | -5.58 |
| 10-19 10:16 | +5 | ZEC | UP | 0.54 | no | -5.58 |
| 10-19 10:16 | +10 stop | SOL | UP | 0.58 | 0.33 | -2.84 |
| 10-19 10:16 | +20 | SOL | UP | 0.58 | no | -5.98 |
| 10-19 10:16 | +15 | SOL | UP | 0.57 | no | -5.88 |
| 10-19 10:16 | +10 | SOL | UP | 0.57 | no | -5.88 |
| 10-19 10:16 | +5 | SOL | UP | 0.57 | no | -5.88 |
| 10-19 10:16 | +10 stop | NEAR | UP | 0.68 | 0.47 | -2.44 |
| 10-19 10:16 | +20 | NEAR | UP | 0.68 | no | -6.96 |
