# Range-Scalp Bot

*Updated Sun Nov 01 20:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43919 | 38258 | 5661 (65) | 5 | $-12606.13 | -4.6% |
| **+10¢** | 32764 | 26224 | 6540 (86) | 6 | $-11351.78 | -5.5% |
| **+15¢** | 27417 | 20377 | 7040 (113) | 6 | $-10373.60 | -6.0% |
| **+20¢** | 24351 | 16977 | 7374 (147) | 6 | $-9164.45 | -6.0% |
| **+10¢ (15¢ stop)** | 53576 | 53490 | 86 (51) | 2 | $-20304.75 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 20:23 | +10 stop | DOGE | UP | 0.63 | open |  |
| 11-01 20:23 | +10 stop | ZEC | DOWN | 0.53 | open |  |
| 11-01 20:23 | +5 | ZEC | DOWN | 0.53 | open |  |
| 11-01 20:21 | +5 | NEAR | DOWN | 0.44 | 0.58 | 1.04 |
| 11-01 20:21 | +5 | SOL | DOWN | 0.62 | open |  |
| 11-01 20:21 | +5 | NEAR | DOWN | 0.57 | 0.62 | 0.15 |
| 11-01 20:19 | +10 stop | NEAR | DOWN | 0.68 | 0.43 | -2.84 |
| 11-01 20:19 | +15 | NEAR | DOWN | 0.68 | open |  |
| 11-01 20:19 | +10 | NEAR | DOWN | 0.68 | open |  |
| 11-01 20:19 | +5 | NEAR | DOWN | 0.64 | 0.71 | 0.38 |
| 11-01 20:19 | +5 | BNB | DOWN | 0.69 | 0.74 | 0.21 |
| 11-01 20:19 | +10 stop | ZEC | DOWN | 0.68 | 0.82 | 1.13 |
| 11-01 20:19 | +5 | ZEC | DOWN | 0.68 | 0.76 | 0.51 |
| 11-01 20:18 | +5 | NEAR | DOWN | 0.59 | 0.68 | 0.57 |
| 11-01 20:18 | +5 | BNB | DOWN | 0.54 | 0.61 | 0.35 |
| 11-01 20:18 | +10 stop | ZEC | DOWN | 0.49 | 0.60 | 0.75 |
| 11-01 20:18 | +5 | ZEC | DOWN | 0.54 | 0.60 | 0.25 |
| 11-01 20:17 | +10 stop | XRP | DOWN | 0.67 | 0.44 | -2.59 |
| 11-01 20:17 | +20 | XRP | DOWN | 0.67 | open |  |
| 11-01 20:17 | +15 | XRP | DOWN | 0.67 | open |  |
| 11-01 20:17 | +10 | XRP | DOWN | 0.67 | open |  |
| 11-01 20:17 | +5 | XRP | DOWN | 0.67 | open |  |
| 11-01 20:17 | +10 stop | NEAR | DOWN | 0.53 | 0.68 | 1.16 |
| 11-01 20:17 | +20 | NEAR | DOWN | 0.53 | open |  |
| 11-01 20:17 | +15 | NEAR | DOWN | 0.53 | 0.68 | 1.16 |
| 11-01 20:17 | +10 | NEAR | DOWN | 0.53 | 0.68 | 1.16 |
| 11-01 20:17 | +5 | NEAR | DOWN | 0.54 | 0.59 | 0.15 |
| 11-01 20:16 | +10 stop | DOGE | DOWN | 0.62 | 0.45 | -2.05 |
| 11-01 20:16 | +10 stop | SOL | DOWN | 0.69 | 0.47 | -2.53 |
| 11-01 20:16 | +20 | SOL | DOWN | 0.69 | open |  |
| 11-01 20:16 | +15 | SOL | DOWN | 0.69 | open |  |
| 11-01 20:16 | +10 | SOL | DOWN | 0.69 | open |  |
| 11-01 20:16 | +5 | SOL | DOWN | 0.69 | 0.74 | 0.21 |
| 11-01 20:16 | +10 stop | BNB | DOWN | 0.57 | 0.69 | 0.87 |
| 11-01 20:16 | +20 | BNB | DOWN | 0.57 | 0.79 | 1.90 |
| 11-01 20:16 | +15 | BNB | DOWN | 0.57 | 0.74 | 1.38 |
| 11-01 20:16 | +10 | BNB | DOWN | 0.57 | 0.69 | 0.87 |
| 11-01 20:16 | +5 | BNB | DOWN | 0.57 | 0.62 | 0.15 |
| 11-01 20:16 | +10 stop | ETH | DOWN | 0.66 | 0.77 | 0.81 |
| 11-01 20:16 | +20 | ETH | DOWN | 0.66 | 0.86 | 1.75 |
