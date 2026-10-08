# Range-Scalp Bot

*Updated Thu Oct 08 03:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 7207 | 6253 | 954 (13) | 5 | $-2181.18 | -4.8% |
| **+10¢** | 5461 | 4339 | 1122 (20) | 7 | $-2117.35 | -6.2% |
| **+15¢** | 4580 | 3396 | 1184 (28) | 7 | $-1755.69 | -6.1% |
| **+20¢** | 4090 | 2860 | 1230 (35) | 7 | $-1385.77 | -5.4% |
| **+10¢ (15¢ stop)** | 8731 | 8709 | 22 (14) | 0 | $-3143.63 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 03:04 | +10 stop | XRP | DOWN | 0.62 | 0.78 | 1.30 |
| 10-08 03:03 | +10 stop | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 10-08 03:03 | +10 stop | BNB | DOWN | 0.63 | 0.73 | 0.69 |
| 10-08 03:03 | +5 | DOGE | DOWN | 0.61 | 0.69 | 0.48 |
| 10-08 03:03 | +5 | NEAR | DOWN | 0.71 | 0.86 | 1.26 |
| 10-08 03:02 | +10 stop | ZEC | DOWN | 0.61 | 0.71 | 0.68 |
| 10-08 03:02 | +10 stop | BTC | DOWN | 0.55 | 0.71 | 1.27 |
| 10-08 03:02 | +10 stop | HYPE | DOWN | 0.68 | 0.79 | 0.82 |
| 10-08 03:02 | +10 stop | SOL | DOWN | 0.63 | 0.76 | 1.00 |
| 10-08 03:02 | +10 stop | XRP | UP | 0.66 | 0.47 | -2.24 |
| 10-08 03:02 | +20 | XRP | UP | 0.66 | open |  |
| 10-08 03:02 | +15 | XRP | UP | 0.66 | open |  |
| 10-08 03:02 | +10 | XRP | UP | 0.66 | open |  |
| 10-08 03:02 | +5 | XRP | UP | 0.66 | open |  |
| 10-08 03:02 | +10 stop | DOGE | UP | 0.54 | 0.39 | -1.85 |
| 10-08 03:02 | +20 | DOGE | UP | 0.54 | open |  |
| 10-08 03:02 | +15 | DOGE | UP | 0.54 | open |  |
| 10-08 03:02 | +10 | DOGE | UP | 0.54 | open |  |
| 10-08 03:02 | +5 | DOGE | UP | 0.55 | 0.60 | 0.15 |
| 10-08 03:02 | +5 | BTC | DOWN | 0.62 | 0.71 | 0.58 |
| 10-08 03:02 | +10 stop | NEAR | DOWN | 0.59 | 0.73 | 1.09 |
| 10-08 03:02 | +20 | NEAR | DOWN | 0.59 | 0.86 | 2.44 |
| 10-08 03:02 | +15 | NEAR | DOWN | 0.59 | 0.86 | 2.44 |
| 10-08 03:02 | +10 | NEAR | DOWN | 0.59 | 0.73 | 1.09 |
| 10-08 03:02 | +5 | NEAR | DOWN | 0.59 | 0.64 | 0.16 |
| 10-08 03:01 | +10 stop | ETH | DOWN | 0.67 | 0.77 | 0.71 |
| 10-08 03:01 | +20 | ETH | DOWN | 0.67 | 0.87 | 1.76 |
| 10-08 03:01 | +15 | ETH | DOWN | 0.67 | 0.82 | 1.23 |
| 10-08 03:01 | +10 | ETH | DOWN | 0.67 | 0.77 | 0.71 |
| 10-08 03:01 | +5 | ETH | DOWN | 0.67 | 0.73 | 0.30 |
| 10-08 03:01 | +10 stop | BNB | UP | 0.60 | 0.41 | -2.24 |
| 10-08 03:01 | +20 | BNB | UP | 0.60 | open |  |
| 10-08 03:01 | +15 | BNB | UP | 0.60 | open |  |
| 10-08 03:01 | +10 | BNB | UP | 0.60 | open |  |
| 10-08 03:01 | +5 | BNB | UP | 0.60 | open |  |
| 10-08 03:01 | +10 stop | ZEC | UP | 0.61 | 0.43 | -2.15 |
| 10-08 03:01 | +20 | ZEC | UP | 0.61 | open |  |
| 10-08 03:01 | +15 | ZEC | UP | 0.61 | open |  |
| 10-08 03:01 | +10 | ZEC | UP | 0.61 | open |  |
| 10-08 03:01 | +5 | ZEC | UP | 0.61 | open |  |
