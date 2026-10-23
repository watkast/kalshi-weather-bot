# Range-Scalp Bot

*Updated Fri Oct 23 22:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31036 | 27048 | 3988 (39) | 7 | $-8960.69 | -4.6% |
| **+10¢** | 23214 | 18606 | 4608 (57) | 7 | $-7966.31 | -5.5% |
| **+15¢** | 19418 | 14461 | 4957 (80) | 8 | $-7173.10 | -5.9% |
| **+20¢** | 17199 | 12008 | 5191 (103) | 8 | $-6404.89 | -5.9% |
| **+10¢ (15¢ stop)** | 38095 | 38036 | 59 (32) | 4 | $-14588.59 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 22:10 | +10 stop | NEAR | UP | 0.49 | 0.60 | 0.75 |
| 10-23 22:10 | +10 | NEAR | UP | 0.49 | 0.60 | 0.75 |
| 10-23 22:10 | +5 | NEAR | UP | 0.49 | 0.54 | 0.14 |
| 10-23 22:10 | +5 | BNB | DOWN | 0.63 | open |  |
| 10-23 22:10 | +10 stop | SOL | UP | 0.64 | open |  |
| 10-23 22:10 | +10 stop | NEAR | DOWN | 0.47 | 0.57 | 0.64 |
| 10-23 22:10 | +10 | NEAR | DOWN | 0.47 | 0.57 | 0.64 |
| 10-23 22:10 | +5 | NEAR | DOWN | 0.48 | 0.57 | 0.54 |
| 10-23 22:10 | +10 stop | BNB | DOWN | 0.57 | open |  |
| 10-23 22:10 | +10 | BNB | DOWN | 0.57 | open |  |
| 10-23 22:10 | +5 | BNB | DOWN | 0.57 | 0.66 | 0.56 |
| 10-23 22:09 | +10 stop | ZEC | DOWN | 0.71 | open |  |
| 10-23 22:09 | +10 stop | SOL | UP | 0.71 | 0.52 | -2.23 |
| 10-23 22:09 | +20 | SOL | UP | 0.71 | open |  |
| 10-23 22:09 | +15 | SOL | UP | 0.71 | open |  |
| 10-23 22:09 | +10 | SOL | UP | 0.71 | open |  |
| 10-23 22:09 | +5 | SOL | UP | 0.71 | open |  |
| 10-23 22:09 | +10 stop | NEAR | UP | 0.51 | 0.62 | 0.75 |
| 10-23 22:09 | +20 | NEAR | UP | 0.51 | open |  |
| 10-23 22:09 | +15 | NEAR | UP | 0.51 | open |  |
| 10-23 22:09 | +10 | NEAR | UP | 0.51 | 0.62 | 0.75 |
| 10-23 22:09 | +5 | NEAR | UP | 0.51 | 0.62 | 0.75 |
| 10-23 22:09 | +10 stop | DOGE | UP | 0.67 | open |  |
| 10-23 22:09 | +20 | DOGE | UP | 0.67 | open |  |
| 10-23 22:09 | +15 | DOGE | UP | 0.66 | open |  |
| 10-23 22:09 | +10 | DOGE | UP | 0.67 | open |  |
| 10-23 22:09 | +5 | DOGE | UP | 0.65 | open |  |
| 10-23 22:09 | +10 stop | BNB | UP | 0.47 | 0.61 | 1.05 |
| 10-23 22:09 | +15 | BNB | UP | 0.47 | open |  |
| 10-23 22:09 | +10 | BNB | UP | 0.47 | 0.61 | 1.05 |
| 10-23 22:09 | +5 | BNB | UP | 0.47 | 0.61 | 1.05 |
| 10-23 22:08 | +10 stop | BTC | DOWN | 0.60 | 0.79 | 1.61 |
| 10-23 22:08 | +10 stop | ZEC | UP | 0.56 | 0.39 | -2.05 |
| 10-23 22:08 | +20 | ZEC | UP | 0.56 | open |  |
| 10-23 22:08 | +15 | ZEC | UP | 0.56 | open |  |
| 10-23 22:08 | +10 | ZEC | UP | 0.56 | open |  |
| 10-23 22:08 | +5 | ZEC | UP | 0.56 | open |  |
| 10-23 22:08 | +10 stop | ETH | UP | 0.59 | 0.30 | -3.22 |
| 10-23 22:08 | +20 | ETH | UP | 0.60 | open |  |
| 10-23 22:08 | +15 | ETH | UP | 0.60 | open |  |
