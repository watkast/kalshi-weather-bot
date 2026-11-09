# Range-Scalp Bot

*Updated Mon Nov 09 00:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53014 | 46228 | 6786 (85) | 1 | $-14627.66 | -4.4% |
| **+10¢** | 39573 | 31662 | 7911 (110) | 3 | $-13606.03 | -5.5% |
| **+15¢** | 33159 | 24635 | 8524 (141) | 2 | $-12416.37 | -6.0% |
| **+20¢** | 29491 | 20556 | 8935 (186) | 6 | $-10916.17 | -5.9% |
| **+10¢ (15¢ stop)** | 64547 | 64441 | 106 (63) | 0 | $-23900.19 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 00:11 | +5 | BTC | UP | 0.40 | 0.56 | 1.25 |
| 11-09 00:10 | +10 stop | BTC | UP | 0.60 | 0.22 | -4.10 |
| 11-09 00:10 | +10 | BTC | UP | 0.59 | open |  |
| 11-09 00:10 | +5 | BTC | UP | 0.60 | 0.65 | 0.17 |
| 11-09 00:09 | +10 stop | BTC | DOWN | 0.54 | 0.66 | 0.86 |
| 11-09 00:09 | +20 | BTC | DOWN | 0.54 | 0.77 | 1.99 |
| 11-09 00:09 | +15 | BTC | DOWN | 0.54 | 0.77 | 1.99 |
| 11-09 00:09 | +10 | BTC | DOWN | 0.54 | 0.66 | 0.86 |
| 11-09 00:09 | +5 | BTC | DOWN | 0.53 | 0.66 | 0.96 |
| 11-09 00:08 | +10 stop | ETH | UP | 0.69 | 0.84 | 1.25 |
| 11-09 00:08 | +15 | ETH | UP | 0.70 | 0.90 | 1.82 |
| 11-09 00:08 | +10 | ETH | UP | 0.71 | 0.84 | 1.05 |
| 11-09 00:08 | +5 | ETH | UP | 0.69 | 0.84 | 1.25 |
| 11-09 00:08 | +5 | NEAR | UP | 0.65 | 0.83 | 1.54 |
| 11-09 00:08 | +10 stop | BNB | UP | 0.65 | 0.85 | 1.75 |
| 11-09 00:08 | +15 | BNB | UP | 0.66 | 0.85 | 1.65 |
| 11-09 00:08 | +10 | BNB | UP | 0.66 | 0.85 | 1.65 |
| 11-09 00:08 | +5 | BNB | UP | 0.66 | 0.85 | 1.65 |
| 11-09 00:08 | +10 stop | DOGE | DOWN | 0.53 | 0.18 | -3.79 |
| 11-09 00:08 | +20 | DOGE | DOWN | 0.53 | open |  |
| 11-09 00:08 | +15 | DOGE | DOWN | 0.53 | open |  |
| 11-09 00:08 | +10 | DOGE | DOWN | 0.53 | open |  |
| 11-09 00:08 | +5 | DOGE | DOWN | 0.54 | open |  |
| 11-09 00:07 | +10 stop | NEAR | DOWN | 0.47 | 0.16 | -3.38 |
| 11-09 00:07 | +20 | NEAR | DOWN | 0.47 | open |  |
| 11-09 00:07 | +15 | NEAR | DOWN | 0.47 | open |  |
| 11-09 00:07 | +10 | NEAR | DOWN | 0.47 | open |  |
| 11-09 00:07 | +5 | NEAR | DOWN | 0.47 | 0.53 | 0.24 |
| 11-09 00:07 | +10 stop | HYPE | UP | 0.68 | 0.51 | -2.06 |
| 11-09 00:07 | +15 | HYPE | UP | 0.68 | 0.94 | 2.38 |
| 11-09 00:07 | +10 | HYPE | UP | 0.68 | 0.79 | 0.80 |
| 11-09 00:07 | +5 | HYPE | UP | 0.68 | 0.74 | 0.28 |
| 11-09 00:06 | +10 stop | ZEC | DOWN | 0.30 | 0.54 | 2.07 |
| 11-09 00:06 | +15 | ZEC | DOWN | 0.30 | 0.54 | 2.02 |
| 11-09 00:06 | +10 | ZEC | DOWN | 0.29 | 0.54 | 2.12 |
| 11-09 00:06 | +5 | ZEC | DOWN | 0.29 | 0.54 | 2.12 |
| 11-09 00:03 | +10 stop | HYPE | DOWN | 0.64 | 0.79 | 1.21 |
| 11-09 00:03 | +10 stop | ZEC | DOWN | 0.65 | 0.75 | 0.70 |
| 11-09 00:02 | +5 | BTC | DOWN | 0.70 | 0.75 | 0.21 |
| 11-09 00:02 | +5 | SOL | DOWN | 0.56 | 0.73 | 1.38 |
