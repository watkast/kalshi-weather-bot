# Range-Scalp Bot

*Updated Sat Oct 03 10:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 643 | 555 | 88 (1) | 5 | $-221.86 | -5.4% |
| **+10¢** | 488 | 389 | 99 (2) | 5 | $-182.89 | -5.9% |
| **+15¢** | 416 | 310 | 106 (3) | 5 | $-163.76 | -6.3% |
| **+20¢** | 362 | 253 | 109 (3) | 5 | $-150.39 | -6.6% |
| **+10¢ (15¢ stop)** | 843 | 842 | 1 (1) | 0 | $-462.79 | -8.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 10:56 | +10 stop | XRP | UP | 0.68 | 0.84 | 1.34 |
| 10-03 10:56 | +15 | XRP | UP | 0.68 | 0.84 | 1.34 |
| 10-03 10:56 | +10 | XRP | UP | 0.68 | 0.84 | 1.34 |
| 10-03 10:56 | +5 | XRP | UP | 0.68 | 0.73 | 0.20 |
| 10-03 10:55 | +10 stop | XRP | UP | 0.59 | 0.77 | 1.50 |
| 10-03 10:55 | +20 | XRP | UP | 0.59 | 0.84 | 2.23 |
| 10-03 10:55 | +15 | XRP | UP | 0.59 | 0.77 | 1.50 |
| 10-03 10:55 | +10 | XRP | UP | 0.59 | 0.77 | 1.50 |
| 10-03 10:55 | +5 | XRP | UP | 0.59 | 0.64 | 0.16 |
| 10-03 10:54 | +10 stop | ZEC | UP | 0.62 | 0.45 | -2.05 |
| 10-03 10:53 | +10 stop | DOGE | UP | 0.60 | 0.74 | 1.09 |
| 10-03 10:53 | +10 stop | ETH | UP | 0.65 | 0.81 | 1.35 |
| 10-03 10:53 | +20 | ETH | UP | 0.60 | 0.81 | 1.82 |
| 10-03 10:53 | +15 | ETH | UP | 0.60 | 0.81 | 1.82 |
| 10-03 10:53 | +10 | ETH | UP | 0.60 | 0.81 | 1.82 |
| 10-03 10:53 | +5 | ETH | UP | 0.60 | 0.65 | 0.17 |
| 10-03 10:52 | +10 stop | ZEC | UP | 0.59 | 0.71 | 0.88 |
| 10-03 10:51 | +10 stop | DOGE | DOWN | 0.69 | 0.51 | -2.13 |
| 10-03 10:51 | +20 | DOGE | DOWN | 0.69 | open |  |
| 10-03 10:51 | +15 | DOGE | DOWN | 0.69 | open |  |
| 10-03 10:51 | +10 | DOGE | DOWN | 0.69 | open |  |
| 10-03 10:51 | +5 | DOGE | DOWN | 0.69 | open |  |
| 10-03 10:50 | +10 stop | XRP | UP | 0.52 | 0.63 | 0.75 |
| 10-03 10:50 | +10 stop | NEAR | DOWN | 0.64 | 0.41 | -2.64 |
| 10-03 10:50 | +10 stop | SOL | DOWN | 0.59 | 0.23 | -3.90 |
| 10-03 10:50 | +10 stop | BNB | DOWN | 0.62 | 0.21 | -4.39 |
| 10-03 10:50 | +20 | BNB | DOWN | 0.63 | open |  |
| 10-03 10:50 | +15 | BNB | DOWN | 0.63 | open |  |
| 10-03 10:50 | +10 | BNB | DOWN | 0.63 | open |  |
| 10-03 10:50 | +5 | BNB | DOWN | 0.63 | open |  |
| 10-03 10:49 | +10 stop | XRP | DOWN | 0.61 | 0.43 | -2.15 |
| 10-03 10:49 | +5 | BTC | UP | 0.69 | 0.76 | 0.42 |
| 10-03 10:49 | +5 | DOGE | DOWN | 0.69 | 0.74 | 0.21 |
| 10-03 10:48 | +5 | ZEC | DOWN | 0.65 | open |  |
| 10-03 10:48 | +10 stop | DOGE | DOWN | 0.56 | 0.68 | 0.86 |
| 10-03 10:48 | +20 | DOGE | DOWN | 0.56 | 0.76 | 1.69 |
| 10-03 10:48 | +15 | DOGE | DOWN | 0.56 | 0.74 | 1.48 |
| 10-03 10:48 | +10 | DOGE | DOWN | 0.56 | 0.68 | 0.86 |
| 10-03 10:48 | +5 | DOGE | DOWN | 0.56 | 0.64 | 0.45 |
| 10-03 10:48 | +10 stop | ETH | DOWN | 0.56 | 0.71 | 1.17 |
