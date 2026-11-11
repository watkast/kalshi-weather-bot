# Range-Scalp Bot

*Updated Wed Nov 11 00:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55100 | 48057 | 7043 (94) | 2 | $-15028.70 | -4.3% |
| **+10¢** | 41173 | 32961 | 8212 (124) | 2 | $-13911.07 | -5.4% |
| **+15¢** | 34518 | 25667 | 8851 (158) | 2 | $-12642.03 | -5.8% |
| **+20¢** | 30730 | 21444 | 9286 (207) | 2 | $-11050.05 | -5.7% |
| **+10¢ (15¢ stop)** | 67119 | 67001 | 118 (73) | 2 | $-24765.00 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 00:16 | +10 stop | ETH | DOWN | 0.54 | open |  |
| 11-11 00:16 | +20 | ETH | DOWN | 0.53 | open |  |
| 11-11 00:16 | +15 | ETH | DOWN | 0.53 | open |  |
| 11-11 00:16 | +10 | ETH | DOWN | 0.53 | open |  |
| 11-11 00:16 | +5 | ETH | DOWN | 0.53 | open |  |
| 11-11 00:16 | +10 stop | BNB | DOWN | 0.56 | open |  |
| 11-11 00:16 | +20 | BNB | DOWN | 0.56 | open |  |
| 11-11 00:16 | +15 | BNB | DOWN | 0.56 | open |  |
| 11-11 00:16 | +10 | BNB | DOWN | 0.57 | open |  |
| 11-11 00:16 | +5 | BNB | DOWN | 0.63 | open |  |
| 11-11 00:12 | +10 stop | XRP | DOWN | 0.28 | 0.57 | 2.57 |
| 11-11 00:12 | +20 | XRP | DOWN | 0.29 | 0.57 | 2.47 |
| 11-11 00:12 | +15 | XRP | DOWN | 0.29 | 0.57 | 2.47 |
| 11-11 00:12 | +10 | XRP | DOWN | 0.31 | 0.57 | 2.27 |
| 11-11 00:12 | +5 | XRP | DOWN | 0.31 | 0.57 | 2.27 |
| 11-11 00:12 | +10 stop | BNB | UP | 0.59 | 0.84 | 2.23 |
| 11-11 00:12 | +10 stop | XRP | UP | 0.33 | 0.63 | 2.67 |
| 11-11 00:12 | +20 | XRP | UP | 0.34 | 0.63 | 2.57 |
| 11-11 00:12 | +15 | XRP | UP | 0.32 | 0.63 | 2.77 |
| 11-11 00:12 | +10 | XRP | UP | 0.32 | 0.63 | 2.77 |
| 11-11 00:12 | +5 | XRP | UP | 0.32 | 0.63 | 2.77 |
| 11-11 00:11 | +10 stop | HYPE | DOWN | 0.50 | 0.32 | -2.14 |
| 11-11 00:10 | +10 stop | HYPE | UP | 0.61 | 0.42 | -2.28 |
| 11-11 00:10 | +5 | HYPE | UP | 0.61 | 0.79 | 1.48 |
| 11-11 00:10 | +10 stop | BNB | DOWN | 0.64 | 0.22 | -4.50 |
| 11-11 00:10 | +5 | BNB | DOWN | 0.69 | yes | -7.05 |
| 11-11 00:09 | +10 stop | BNB | DOWN | 0.59 | 0.69 | 0.69 |
| 11-11 00:09 | +20 | BNB | DOWN | 0.59 | yes | -6.06 |
| 11-11 00:09 | +15 | BNB | DOWN | 0.59 | yes | -6.06 |
| 11-11 00:09 | +10 | BNB | DOWN | 0.59 | yes | -6.09 |
| 11-11 00:09 | +5 | BNB | DOWN | 0.60 | 0.67 | 0.33 |
| 11-11 00:07 | +10 stop | ZEC | DOWN | 0.54 | 0.69 | 1.17 |
| 11-11 00:06 | +10 stop | ETH | DOWN | 0.67 | 0.77 | 0.71 |
| 11-11 00:06 | +5 | ETH | DOWN | 0.67 | 0.74 | 0.40 |
| 11-11 00:06 | +10 stop | HYPE | DOWN | 0.56 | 0.25 | -3.42 |
| 11-11 00:06 | +10 stop | HYPE | UP | 0.42 | 0.55 | 0.94 |
| 11-11 00:06 | +10 stop | NEAR | UP | 0.54 | 0.66 | 0.86 |
| 11-11 00:06 | +10 | NEAR | UP | 0.54 | 0.66 | 0.86 |
| 11-11 00:06 | +5 | NEAR | UP | 0.54 | 0.66 | 0.86 |
| 11-11 00:05 | +10 stop | ETH | UP | 0.57 | 0.31 | -2.93 |
